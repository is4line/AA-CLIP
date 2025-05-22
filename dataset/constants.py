BASE_PATH = ""
DATA_PATH = {
    "Colon_clinicDB": f"{BASE_PATH}/data/Colon/CVC-ClinicDB",
    "Colon_colonDB": f"{BASE_PATH}/data/Colon/CVC-ColonDB",
    "Colon_cvc300": f"{BASE_PATH}/data/Colon/CVC-300",
    "Colon_Kvasir": f"{BASE_PATH}/data/Colon/Kvasir",
}


CLASS_NAMES = {
    "Colon_clinicDB": ["Colon_clinicDB"],
    "Colon_colonDB": ["Colon_colonDB"],
    "Colon_Kvasir": ["Kvasir"],
    "Colon_cvc300": ["CVC-300"],
}

DOMAINS = {
    "Colon_clinicDB": "Medical",
    "Colon_colonDB": "Medical",
    "Colon_Kvasir": "Medical",
    "Colon_cvc300": "Medical",
}
REAL_NAMES = {
    "Colon_clinicDB": {
        "Colon_clinicDB": "colon endoscopy image",
    },
    "Colon_colonDB": {
        "Colon_colonDB": "colon endoscopy image",
    },
    "Colon_cvc300": {"CVC-300": "colon endoscopy image"},
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