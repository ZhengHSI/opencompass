import time
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Optional, Union

from opencompass.utils.prompt import PromptList
import requests

from .base_api import BaseAPIModel

PromptType = Union[PromptList, str]


class minicpm(BaseAPIModel):
    def __init__(self,
                 path: str,
                 key: str,
                 query_per_second: int = 1,
                 max_seq_len: int = 2048,
                 meta_template: Optional[Dict] = None,
                 retry: int = 5,
                 generation_kwargs: Dict = {},
                 ):
        super().__init__(path=path,
                         max_seq_len=max_seq_len,
                         query_per_second=query_per_second,
                         meta_template=meta_template,
                         retry=retry,
                         generation_kwargs=generation_kwargs,)

    def generate(
        self,
        inputs: List[PromptType],
        max_out_len: int = 512,
    ) -> List[str]:
        """Generate results given a list of inputs.

        Args:
            inputs (List[PromptType]): A list of strings or PromptDicts.
                The PromptDict should be organized in OpenCompass'
                API format.
            max_out_len (int): The maximum length of the output.

        Returns:
            List[str]: A list of generated strings.
        """
        with ThreadPoolExecutor() as executor:
            results = list(
                executor.map(self._generate, inputs,
                             [max_out_len] * len(inputs)))
        self.flush()
        return results

    def _generate(
            self,
            input: PromptType,
            max_out_len: int = 512,
        ) -> str:
            """Generate results given an input.

            Args:
                inputs (PromptType): A string or PromptDict.
                    The PromptDict should be organized in Test'
                    API format.
                max_out_len (int): The maximum length of the output.

            Returns:
                str: The generated string.
            """
            # print(input)
            assert isinstance(input, (str, PromptList))
            if isinstance(input, str):
                messages = [{
                    'content': input
                }]
            else:
                messages = []
                for item in input:
                    msg = {'content': item['prompt']}
                    messages.append(msg)
            data = {
                'messages':
                messages,
                "max_out_len":
                max_out_len
            }
            max_num_retries = 0
            while max_num_retries < self.retry:
                self.acquire()
                try:
                    raw_response = requests.request('POST',self.path,json=data)
                    response = raw_response.json()
                except Exception as err:
                    print('Request Error:{}'.format(err))
                    time.sleep(3)
                    continue
                self.release()

                if response is None:
                    print('Connection error, reconnect.')
                    # if connect error, frequent requests will casuse
                    # continuous unstable network, therefore wait here
                    # to slow down the request
                    self.wait()
                    continue
                if raw_response.status_code == 200:
                    # msg = json.load(response.text)
                    # response
                    msg = response["messages"][0]['content']
                    print(msg)
                    # msg = response['choices']['messages']['text']
                    return msg
                # sensitive content, prompt overlength, network error
                # or illegal prompt
                if (response.status_code == 1000 or response.status_code == 1001
                        or response.status_code == 1002
                        or response.status_code == 1004
                        or response.status_code == 1008
                        or response.status_code == 1013
                        or response.status_code == 1027
                        or response.status_code == 1039
                        or response.status_code == 2013):
                    print(response.text)
                    time.sleep(1)
                    continue
                print(response)
                max_num_retries += 1

            raise RuntimeError(response.text)
