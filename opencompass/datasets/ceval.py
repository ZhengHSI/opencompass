import csv
import json
import os.path as osp
from os import environ
# import random
from datasets import Dataset, DatasetDict

from opencompass.registry import LOAD_DATASET
from opencompass.utils import get_data_path

from .base import BaseDataset


@LOAD_DATASET.register_module()
class CEvalDataset(BaseDataset):

    @staticmethod
    def load(path: str, name: str, local_mode: bool = False, limit=5):
        path = get_data_path(path, local_mode=local_mode)
        dataset = {}
        if environ.get('DATASET_SOURCE') == 'ModelScope':
            from modelscope import MsDataset
            dataset = MsDataset.load(dataset_name=path, subset_name=name)
        else:
            for split in ['dev', 'val', 'test']:
                raw_data = []
                filename = osp.join(path, split, f'{name}_{split}.csv')
                with open(filename, encoding='utf-8') as f:
                    reader = csv.reader(f)
                    header = next(reader)  # 读取表头
                    
                    for row in reader:
                        item = dict(zip(header, row))
                        item.setdefault('explanation', '')
                        item.setdefault('answer', '')
                        raw_data.append(item)
                
                # 随机打乱数据顺序
                # random.shuffle(raw_data)
                if limit is not None:
                    raw_data = raw_data[:limit]  # 仅加载随机采样的 limit 条数据
                dataset[split] = raw_data
            # 将数据转换为 Hugging Face 的 DatasetDict 格式
            dataset = DatasetDict({split: Dataset.from_list(data) for split, data in dataset.items()})
        
        return dataset


class CEvalDatasetClean(BaseDataset):

    @staticmethod
    def load_contamination_annotations(path, split='val'):
        import requests

        assert split == 'val', 'Now we only have annotations for val set'
        if environ.get('DATASET_SOURCE') == 'ModelScope':
            from modelscope.utils.config_ds import MS_DATASETS_CACHE
            annotation_cache_path = osp.join(
                MS_DATASETS_CACHE, 'ceval_contamination_annotations.json')
            link_of_annotations = 'https://modelscope.cn/datasets/opencompass/Contamination_Detector/resolve/master/ceval_annotations.json'  # noqa
        else:
            annotation_cache_path = osp.join(
                path, split, 'ceval_contamination_annotations.json')
            link_of_annotations = 'https://github.com/liyucheng09/Contamination_Detector/releases/download/v0.1.1rc/ceval_annotations.json'  # noqa

        if osp.exists(annotation_cache_path):
            with open(annotation_cache_path, 'r') as f:
                annotations = json.load(f)
            return annotations
        annotations = json.loads(requests.get(link_of_annotations).text)
        with open(annotation_cache_path, 'w') as f:
            json.dump(annotations, f)
        return annotations

    @staticmethod
    def load(path: str, name: str, limit=5):  # 添加 limit 参数
        path = get_data_path(path)
        dataset = {}
        if environ.get('DATASET_SOURCE') == 'ModelScope':
            from modelscope import MsDataset
            dataset = MsDataset.load(dataset_name=path, subset_name=name)
            annotations = CEvalDatasetClean.load_contamination_annotations(
                path, 'val')
            val = dataset['val']
            val_data = []
            for index in range(min(val.num_rows, limit)):  # 限制加载的数据条数
                row = val[index]
                row_id = f'{name}-{index}'
                row.update({
                    'is_clean':
                    annotations[row_id][0]
                    if row_id in annotations else 'not labeled'
                })
                val_data.append(row)
            dataset['val'] = Dataset.from_list(val_data)
        else:
            for split in ['dev', 'val', 'test']:
                if split == 'val':
                    annotations = CEvalDatasetClean.load_contamination_annotations(
                        path, split)
                filename = osp.join(path, split, f'{name}_{split}.csv')
                with open(filename, encoding='utf-8') as f:
                    reader = csv.reader(f)
                    header = next(reader)
                    for i, row in enumerate(reader):
                        if i >= limit:  # 仅加载前 limit 条数据
                            break
                        item = dict(zip(header, row))
                        item.setdefault('explanation', '')
                        item.setdefault('answer', '')
                        if split == 'val':
                            row_id = f'{name}-{i}'
                            if row_id in annotations:
                                item['is_clean'] = annotations[row_id][0]
                            else:
                                item['is_clean'] = 'not labeled'
                        dataset.setdefault(split, []).append(item)
            dataset = DatasetDict(
                {i: Dataset.from_list(dataset[i])
                 for i in dataset})
        return dataset
