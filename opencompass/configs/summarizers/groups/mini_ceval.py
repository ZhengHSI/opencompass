mini_ceval_summary_groups = []

_ceval_stem = ['computer_network', 'operating_system', 'college_programming', 'college_physics', 'probability_and_statistics', 'discrete_mathematics', 'electrical_engineer', 'high_school_mathematics', 'high_school_physics', 'middle_school_biology', 'veterinary_medicine']
_ceval_stem = ['mini_ceval-' + s for s in _ceval_stem]
mini_ceval_summary_groups.append({'name': 'mini_ceval-stem', 'subsets': _ceval_stem})

_ceval_social_science = ['college_economics', 'business_administration', 'marxism', 'education_science', 'teacher_qualification', 'high_school_politics', 'middle_school_politics', 'middle_school_geography']
_ceval_social_science = ['mini_ceval-' + s for s in _ceval_social_science]
mini_ceval_summary_groups.append({'name': 'mini_ceval-social-science', 'subsets': _ceval_social_science})

_ceval_humanities = ['modern_chinese_history', 'ideological_and_moral_cultivation', 'logic', 'law', 'chinese_language_and_literature', 'art_studies', 'professional_tour_guide', 'legal_professional', 'high_school_chinese', 'high_school_history', 'middle_school_history']
_ceval_humanities = ['mini_ceval-' + s for s in _ceval_humanities]
mini_ceval_summary_groups.append({'name': 'mini_ceval-humanities', 'subsets': _ceval_humanities})

_ceval_other = ['civil_servant', 'plant_protection', 'basic_medicine', 'urban_and_rural_planner', 'accountant', 'fire_engineer', 'environmental_impact_assessment_engineer', 'tax_accountant', 'physician']
_ceval_other = ['mini_ceval-' + s for s in _ceval_other]
mini_ceval_summary_groups.append({'name': 'mini_ceval-other', 'subsets': _ceval_other})

_ceval_hard = ['discrete_mathematics', 'probability_and_statistics', 'college_physics', 'high_school_mathematics', 'high_school_physics']
_ceval_hard = ['mini_ceval-' + s for s in _ceval_hard]
mini_ceval_summary_groups.append({'name': 'mini_ceval-hard', 'subsets': _ceval_hard})

_ceval_all = _ceval_stem + _ceval_social_science + _ceval_humanities + _ceval_other
mini_ceval_summary_groups.append({'name': 'mini_ceval', 'subsets': _ceval_all})

_ceval_stem = ['computer_network', 'operating_system', 'college_programming', 'college_physics', 'probability_and_statistics', 'discrete_mathematics', 'electrical_engineer', 'high_school_mathematics', 'high_school_physics', 'middle_school_biology', 'veterinary_medicine']
_ceval_stem = ['mini_ceval-test-' + s for s in _ceval_stem]
mini_ceval_summary_groups.append({'name': 'mini_ceval-test-stem', 'subsets': _ceval_stem})

_ceval_social_science = ['college_economics', 'business_administration', 'marxism', 'education_science', 'teacher_qualification', 'high_school_politics', 'middle_school_politics', 'middle_school_geography']
_ceval_social_science = ['mini_ceval-test-' + s for s in _ceval_social_science]
mini_ceval_summary_groups.append({'name': 'mini_ceval-test-social-science', 'subsets': _ceval_social_science})

_ceval_humanities = ['modern_chinese_history', 'ideological_and_moral_cultivation', 'logic', 'law', 'chinese_language_and_literature', 'art_studies', 'professional_tour_guide', 'legal_professional', 'high_school_chinese', 'high_school_history', 'middle_school_history']
_ceval_humanities = ['mini_ceval-test-' + s for s in _ceval_humanities]
mini_ceval_summary_groups.append({'name': 'mini_ceval-test-humanities', 'subsets': _ceval_humanities})

_ceval_other = ['civil_servant', 'plant_protection', 'basic_medicine', 'urban_and_rural_planner', 'accountant', 'fire_engineer', 'environmental_impact_assessment_engineer', 'tax_accountant', 'physician']
_ceval_other = ['mini_ceval-test-' + s for s in _ceval_other]
mini_ceval_summary_groups.append({'name': 'mini_ceval-test-other', 'subsets': _ceval_other})

_ceval_hard = ['discrete_mathematics', 'probability_and_statistics', 'college_physics', 'high_school_mathematics', 'high_school_physics']
_ceval_hard = ['mini_ceval-test-' + s for s in _ceval_hard]
mini_ceval_summary_groups.append({'name': 'mini_ceval-test-hard', 'subsets': _ceval_hard})

_ceval_all = _ceval_stem + _ceval_social_science + _ceval_humanities + _ceval_other
mini_ceval_summary_groups.append({'name': 'mini_ceval-test', 'subsets': _ceval_all})
