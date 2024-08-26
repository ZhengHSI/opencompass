python3 run.py --models minicpm_api --datasets gsm8k_gen_1d7fe4 -w outputs/minicpm_api+gsm8k --dump-eval-details
python3 run.py --models minicpm_api --datasets math_0shot_gen_393424 -w outputs/minicpm_api+math --dump-eval-details
python3 run.py --models minicpm_api --datasets bbh_gen_5b92b0 -w outputs/minicpm_api+bbh --dump-eval-details
python3 run.py --models minicpm_api --datasets ARC_c_gen_1e0de5 -w outputs/minicpm_api+arc_c --dump-eval-details
python3 run.py --models minicpm_api --datasets ARC_e_gen_1e0de5 -w outputs/minicpm_api+arc_e --dump-eval-details
python3 run.py --models minicpm_api --datasets hellaswag_10shot_gen_e42710 -w outputs/minicpm_api+hellaswag --dump-eval-details
python3 run.py --models minicpm_api --datasets mmlu_gen_4d595a -w outputs/minicpm_api+mmlu --dump-eval-details
python3 run.py --models minicpm_api --datasets cmmlu_gen_c13365 -w outputs/minicpm_api+cmmlu --dump-eval-details
python3 run.py --models minicpm_api --datasets ceval_gen_2daf24 -w outputs/minicpm_api+ceval --dump-eval-details

#以下是附加数据集
# python3 run.py --models minicpm_api --datasets GaokaoBench_no_subjective_gen_4c31db -w outputs/minicpm_api+GaokaoBench_no_subjective
# python3 run.py --models minicpm_api --datasets triviaqa_wiki_1shot_gen_eaf81e -w outputs/minicpm_api+triviaqa_wiki
# python3 run.py --models minicpm_api --datasets nq_open_1shot_gen_01cf41 -w outputs/minicpm_api+nq_open
# python3 run.py --models minicpm_api --datasets race_gen_69ee4f -w outputs/minicpm_api+race
# python3 run.py --models minicpm_api --datasets winogrande_5shot_gen_b36770 -w outputs/minicpm_api+winogrande
# python3 run.py --models minicpm_api --datasets TheoremQA_5shot_gen_6f0af8 -w outputs/minicpm_api+TheoremQA
# python3 run.py --models minicpm_api --datasets lcbench_gen_5ff288 -w outputs/minicpm_api+lcbench
# python3 run.py --models minicpm_api --datasets gpqa_gen_4baadb -w outputs/minicpm_api+gpqa
# python3 run.py --models minicpm_api --datasets IFEval_gen_3321a3 -w outputs/minicpm_api+IFEval
# python3 run.py --models minicpm_api --datasets humaneval_gen_8e312c -w outputs/minicpm_api+humaneval
# python3 run.py --models minicpm_api --datasets sanitized_mbpp_mdblock_gen_a447ff -w outputs/minicpm_api+mbpp