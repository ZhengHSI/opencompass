subcategories = {
    'agronomy': ['other'],
    'anatomy': ['biology'],
    'ancient_chinese': ['linguistics','china specific'],
    'arts': ['arts'],
    'astronomy': ['physics'],
    'business_ethics': ['business'],
    'chinese_civil_service_exam': ['politics','china specific'],
    'chinese_driving_rule': ['other','china specific'],
    'chinese_food_culture': ['culture','china specific'],
    'chinese_foreign_policy': ['politics','china specific'],
    'chinese_history':['history','china specific'],
    # 'chinese_literature': ['literature','china specific'],
    # 'chinese_teacher_qualification': ['education','china specific'],
    # 'college_actuarial_science':['math'],
    'college_education':['education'],
    'college_engineering_hydrology': ['engineering'],
    'college_law': ['law'],
    'college_mathematics': ['math'],
    # 'college_medical_statistics':['statistics'],
    'clinical_knowledge': ['other'],
    'college_medicine': ['other'],
    'computer_science': ['computer science'],
    'computer_security': ['other'],
    'conceptual_physics': ['physics'],
    # 'construction_project_management': ['other','china specific'],
    'economics': ['economics'],
    'education': ['education'],
    'elementary_chinese':['linguistics','china specific'],
    'elementary_commonsense':['other','china specific'],
    # 'elementary_information_and_technology': ['other'],
    'electrical_engineering': ['engineering'],
    'elementary_mathematics': ['math'],
    'ethnology': ['culture','china specific'],
    'food_science': ['other'],
    'genetics': ['biology'],
    'global_facts': ['global'],
    'high_school_biology': ['biology'],
    'high_school_chemistry': ['chemistry'],
    'high_school_geography': ['geography'],
    'high_school_mathematics': ['math'],
    # 'high_school_physics': ['physics'],
    'high_school_politics': ['politics','china specific'],
    # 'human_sexuality': ['other'],
    'international_law': ['law'],
    # 'journalism': ['sociology'],
    'jurisprudence': ['law'],
    'legal_and_moral_basis': ['other'],
    # 'logical': ['philosophy'],
    'machine_learning': ['computer science'],
    'management': ['business'],
    'marketing': ['business'],
    'marxist_theory': ['philosophy'],
    'modern_chinese': ['linguistics','china specific'],
    'nutrition': ['other'],
    # 'philosophy': ['philosophy'],
    'professional_accounting': ['business'],
    'professional_law': ['law'],
    'professional_medicine': ['other'],
    'professional_psychology': ['psychology'],
    # 'public_relations': ['politics'],
    'security_study': ['politics'],
    'sociology': ['culture'],
    'sports_science': ['other'],
    'traditional_chinese_medicine': ['other','china specific'],
    'virology': ['biology'],
    'world_history':['history'],
    'world_religions': ['global'],
}

categories = {
    'STEM': ['physics', 'chemistry', 'biology', 'computer science', 'math', 'engineering', 'statistics'],
    'Humanities': ['history', 'philosophy', 'law', 'arts', 'literature', 'global'],
    'Social Science': ['linguistics','business', 'politics', 'culture', 'economics', 'geography', 'psychology', 'education', 'sociology'],
    'Other':['other'],
    'China specific': ['china specific'],
}

category2subject = {}
for k, v in categories.items():
    for subject, subcat in subcategories.items():
        for c in subcat:
            if c in v:
                category2subject.setdefault(k, []).append(subject)

mini_cmmlu_summary_groups = []

_cmmlu_humanities = ['mini_cmmlu-' + s for s in category2subject['Humanities']]
mini_cmmlu_summary_groups.append({'name': 'mini_cmmlu-humanities', 'subsets': _cmmlu_humanities})

_cmmlu_stem = ['mini_cmmlu-' + s for s in category2subject['STEM']]
mini_cmmlu_summary_groups.append({'name': 'mini_cmmlu-stem', 'subsets': _cmmlu_stem})

_cmmlu_social_science = ['mini_cmmlu-' + s for s in category2subject['Social Science']]
mini_cmmlu_summary_groups.append({'name': 'mini_cmmlu-social-science', 'subsets': _cmmlu_social_science})

_cmmlu_other = ['mini_cmmlu-' + s for s in category2subject['Other']]
mini_cmmlu_summary_groups.append({'name': 'mini_cmmlu-other', 'subsets': _cmmlu_other})

_cmmlu_china_specific = ['mini_cmmlu-' + s for s in category2subject['China specific']]
mini_cmmlu_summary_groups.append({'name': 'mini_cmmlu-china-specific', 'subsets': _cmmlu_china_specific})

_cmmlu_all = ['mini_cmmlu-' + s for s in subcategories.keys()]
mini_cmmlu_summary_groups.append({'name': 'mini_cmmlu', 'subsets': _cmmlu_all})
