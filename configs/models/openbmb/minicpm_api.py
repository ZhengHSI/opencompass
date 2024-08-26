from opencompass.models import minicpm

models = [
    dict(
        type=minicpm,                             # 使用
        path='http://192.168.10.92:8000',         # 本地暴露的模型api路径
        key='',                  
        max_seq_len=2048,                        # 最大输入长度
        abbr='minicpm',                          # 模型简称
        run_cfg=dict(num_gpus=0),                # 资源需求（不需要 GPU）
        max_out_len=2048,                        # 最长生成长度
        batch_size=1,                            # 批次大小
    ),
]