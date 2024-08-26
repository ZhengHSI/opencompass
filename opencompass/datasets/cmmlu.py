import csv
import os.path as osp
from os import environ
# import random
from datasets import Dataset, DatasetDict

from opencompass.registry import LOAD_DATASET
from opencompass.utils import get_data_path

from .base import BaseDataset


@LOAD_DATASET.register_module()
class CMMLUDataset(BaseDataset):

    @staticmethod
    def load(path: str, name: str, limit=5):
        path = get_data_path(path)        
        if environ.get('DATASET_SOURCE') == 'ModelScope':
            from modelscope import MsDataset
            dataset = MsDataset.load(path, subset_name=name)
            modified_dataset = DatasetDict()
            for split in dataset.keys():
                raw_data = []
                for data in dataset[split]:
                    raw_data.append({
                        'question': data['Question'],
                        'A': data['A'],
                        'B': data['B'],
                        'C': data['C'],
                        'D': data['D'],
                        'answer': data['Answer']
                    })
                # 随机打乱数据顺序
                # random.shuffle(raw_data)
                if limit is not None:
                    raw_data = raw_data[:limit]
                modified_dataset[split] = Dataset.from_list(raw_data)
            dataset = modified_dataset       
        else:
            dataset = DatasetDict()
            for split in ['dev', 'test']:
                raw_data = []
                filename = osp.join(path, split, f'{name}.csv')
                with open(filename, encoding='utf-8') as f:
                    reader = csv.reader(f)
                    _ = next(reader)  # 跳过表头
                    for row in reader:
                        assert len(row) == 7
                        raw_data.append({
                            'question': row[1],
                            'A': row[2],
                            'B': row[3],
                            'C': row[4],
                            'D': row[5],
                            'answer': row[6],
                        })
                # 随机打乱数据顺序
                # random.shuffle(raw_data)
                if limit is not None:
                    raw_data = raw_data[:limit]
                dataset[split] = Dataset.from_list(raw_data)
        return dataset