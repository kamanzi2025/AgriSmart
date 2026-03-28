KNOWLEDGE_BASE = [
  {
    "name":       "Bean Stem Maggot (Ophiomyia spp.)",
    "symptoms":   "Yellowing of lower leaves; wilting despite adequate moisture; small exit holes at stem base.",
    "treatment":  "Apply Imidacloprid seed dressing before planting. For infestations use Dimethoate 40 EC soil drench.",
    "prevention": "Use certified dressed seed. Rotate crops.",
  },
  {
    "name":       "Bean Anthracnose (Colletotrichum lindemuthianum)",
    "symptoms":   "Dark sunken lesions on pods, stems and leaves.",
    "treatment":  "Copper Oxychloride fungicide every 7–10 days.",
    "prevention": "Disease-free seed. Avoid overhead irrigation.",
  },
  {
    "name":       "Angular Leaf Spot (Phaeoisariopsis griseola)",
    "symptoms":   "Angular brown spots bounded by leaf veins.",
    "treatment":  "Mancozeb or Chlorothalonil every 7–14 days.",
    "prevention": "Plant RWR 2245. 3-year crop rotation.",
  },
  # Additional entries such as Bean Mosaic Virus, Aphids, Root Rot can be added here.
]

def diagnose(keyword: str):
    """Case-insensitive match on name or symptoms."""
    kw = keyword.lower().strip()
    for entry in KNOWLEDGE_BASE:
        if (kw in entry["name"].lower() or
            kw in entry["symptoms"].lower()):
            return entry
    return None

def get_all_pest_names() -> list[str]:
    return [e["name"] for e in KNOWLEDGE_BASE]