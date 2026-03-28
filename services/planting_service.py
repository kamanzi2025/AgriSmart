from datetime import datetime

PLANTING_WINDOWS = {
    "Kigali":        {"A": "March 1–15",     "B": "Aug 20–Sep 5"},
    "Huye":          {"A": "March 5–20",     "B": "Aug 25–Sep 10"},
    "Musanze":       {"A": "Feb 20–Mar 5",   "B": "Aug 10–25"},
    "Rubavu":        {"A": "March 1–15",     "B": "Aug 20–Sep 5"},
    "Nairobi":       {"A": "March 10–25",    "B": "Sep 1–15"},
    "Kampala":       {"A": "March 5–20",     "B": "Aug 25–Sep 10"},
    "Dar es Salaam": {"A": "March 15–Apr 1", "B": "Sep 10–25"},
}

VARIETIES = {
    "Kigali":        "RWR 2245 (Angular Leaf Spot resistant)",
    "Huye":          "MAC 44 (high-altitude climbing bean)",
    "Musanze":       "KAB 94 (fast-maturing bush bean)",
    "Rubavu":        "RWR 2064 (rust tolerant)",
    "Nairobi":       "GLP 2 (drought tolerant)",
    "Kampala":       "NABE 26 (high-yield)",
    "Dar es Salaam": "Lari 1 (wet-season adapted)",
}

def generate(region: str) -> dict:
    window  = PLANTING_WINDOWS.get(region, PLANTING_WINDOWS["Kigali"])
    variety = VARIETIES.get(region, "Certified local variety")
    month   = datetime.now().month
    season  = "Season A (Long Rains)" if month <= 6 else "Season B (Short Rains)"
    key     = "A" if month <= 6 else "B"
    return {
        "region":              region,
        "season":              season,
        "planting_window":     window.get(key),
        "recommended_variety": variety,
        "generated_at":        datetime.now().isoformat(),
    }
        