BASE_PATH = ""
DATA_PATH = {
    "Colon_Kvasir": f"{BASE_PATH}./data/Colon/Kvasir",
}


CLASS_NAMES = {
    "Colon_Kvasir": ["Kvasir"],
}

DOMAINS = {
    "Colon_Kvasir": "Medical",
}
REAL_NAMES = {
    "Colon_Kvasir": {"Kvasir": "colon endoscopy image"},
}
PROMPTS = {
    "prompt_normal": ["{}", "a {}", "the {}"],
    "prompt_abnormal": [
        "a damaged {}",
        "a broken {}",
        "a {} with flaw",
        "a {} with defect",
        "a {} with damage",
    ],
    "prompt_templates": [
        "{}.",
        "a photo of {}.",
    ],
}