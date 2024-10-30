mini_mmlu_summary_groups = []

_mini_mmlu_humanities = ['high_school_european_history', 'high_school_us_history', 'high_school_world_history', 'jurisprudence', 'logical_fallacies', 'moral_disputes', 'moral_scenarios', 'philosophy', 'prehistory', 'professional_law', 'world_religions']
_mini_mmlu_humanities = ['mini_lukaemon_mmlu_' + s for s in _mini_mmlu_humanities]
mini_mmlu_summary_groups.append({'name': 'mini_mmlu-humanities', 'subsets': _mini_mmlu_humanities})

_mini_mmlu_stem = ['anatomy', 'astronomy', 'college_physics', 'conceptual_physics', 'electrical_engineering', 'elementary_mathematics', 'high_school_biology', 'high_school_chemistry', 'high_school_computer_science', 'high_school_mathematics', 'high_school_physics', 'high_school_statistics']
_mini_mmlu_stem = ['mini_lukaemon_mmlu_' + s for s in _mini_mmlu_stem]
mini_mmlu_summary_groups.append({'name': 'mini_mmlu-stem', 'subsets': _mini_mmlu_stem})

_mini_mmlu_social_science = ['econometrics', 'high_school_government_and_politics', 'high_school_macroeconomics', 'high_school_microeconomics', 'high_school_psychology', 'professional_psychology', 'sociology', 'us_foreign_policy']
_mini_mmlu_social_science = ['mini_lukaemon_mmlu_' + s for s in _mini_mmlu_social_science]
mini_mmlu_summary_groups.append({'name': 'mini_mmlu-social-science', 'subsets': _mini_mmlu_social_science})

_mini_mmlu_other = ['business_ethics', 'clinical_knowledge', 'college_medicine', 'human_aging', 'marketing', 'miscellaneous', 'nutrition', 'professional_accounting', 'professional_medicine', 'virology']
_mini_mmlu_other = ['mini_lukaemon_mmlu_' + s for s in _mini_mmlu_other]
mini_mmlu_summary_groups.append({'name': 'mini_mmlu-other', 'subsets': _mini_mmlu_other})

_mmlu_all = _mini_mmlu_humanities + _mini_mmlu_stem + _mini_mmlu_social_science + _mini_mmlu_other
# _mmlu_weights = {'college_biology': 144,'college_chemistry': 100,'college_computer_science': 100,'college_mathematics': 100,'college_physics': 102,'electrical_engineering': 145,'astronomy': 152,'anatomy': 135,'abstract_algebra': 100,'machine_learning': 112,'clinical_knowledge': 265,'global_facts': 100,'management': 103,'nutrition': 306,'marketing': 234,'professional_accounting': 282,'high_school_geography': 198,'international_law': 121,'moral_scenarios': 895,'computer_security': 100,'high_school_microeconomics': 238,'professional_law': 1534,'medical_genetics': 100,'professional_psychology': 612,'jurisprudence': 108,'world_religions': 171,'philosophy': 311,'virology': 166,'high_school_chemistry': 203,'public_relations': 110,'high_school_macroeconomics': 390,'human_sexuality': 131,'elementary_mathematics': 378,'high_school_physics': 151,'high_school_computer_science': 100,'high_school_european_history': 165,'business_ethics': 100,'moral_disputes': 346,'high_school_statistics': 216,'miscellaneous': 783,'formal_logic': 126,'high_school_government_and_politics': 193,'prehistory': 324,'security_studies': 245,'high_school_biology': 310,'logical_fallacies': 163,'high_school_world_history': 237,'professional_medicine': 272,'high_school_mathematics': 270,'college_medicine': 173,'high_school_us_history': 204,'sociology': 201,'econometrics': 114,'high_school_psychology': 545,'human_aging': 223,'us_foreign_policy': 100,'conceptual_physics': 235}
# _mmlu_weights = {'mini_lukaemon_mmlu_' + k : v for k,v in _mmlu_weights.items()}
mini_mmlu_summary_groups.append({'name': 'mini_mmlu', 'subsets': _mmlu_all})
# mini_mmlu_summary_groups.append({'name': 'mmlu-weighted', 'subsets': _mmlu_all, 'weights': _mmlu_weights})
