# Ideal NPK ranges for some crops (approximate values)
ideal_npk = {
    "rice": {"N": (80, 120), "P": (40, 60), "K": (40, 60)},
    "maize": {"N": (70, 110), "P": (35, 60), "K": (30, 50)},
    "chickpea": {"N": (20, 60), "P": (40, 70), "K": (20, 40)},
    "kidneybeans": {"N": (20, 60), "P": (40, 70), "K": (20, 40)},
    "pigeonpeas": {"N": (20, 60), "P": (40, 70), "K": (20, 40)},
    "mothbeans": {"N": (20, 50), "P": (30, 60), "K": (20, 40)},
    "mungbean": {"N": (20, 50), "P": (30, 60), "K": (20, 40)},
    "blackgram": {"N": (20, 50), "P": (30, 60), "K": (20, 40)},
    "lentil": {"N": (20, 50), "P": (30, 60), "K": (20, 40)},
    "pomegranate": {"N": (50, 100), "P": (25, 50), "K": (50, 100)},
    "banana": {"N": (100, 150), "P": (50, 80), "K": (80, 120)},
    "mango": {"N": (50, 100), "P": (25, 50), "K": (50, 100)},
    "grapes": {"N": (60, 120), "P": (40, 80), "K": (60, 120)},
    "watermelon": {"N": (60, 120), "P": (40, 80), "K": (60, 120)},
    "muskmelon": {"N": (60, 120), "P": (40, 80), "K": (60, 120)},
    "apple": {"N": (60, 120), "P": (40, 80), "K": (60, 120)},
    "orange": {"N": (60, 120), "P": (40, 80), "K": (60, 120)},
    "papaya": {"N": (60, 120), "P": (40, 80), "K": (60, 120)},
    "coconut": {"N": (80, 150), "P": (40, 80), "K": (80, 150)},
    "cotton": {"N": (80, 120), "P": (40, 60), "K": (40, 60)},
    "jute": {"N": (60, 100), "P": (30, 50), "K": (30, 50)},
    "coffee": {"N": (80, 120), "P": (40, 60), "K": (40, 60)},
}

def diagnose_soil(crop, N, P, K):

    if crop not in ideal_npk:
        return "No soil data available for this crop."

    ideal = ideal_npk[crop]

    report = []

    # Nitrogen check
    if N < ideal["N"][0]:
        report.append("Nitrogen deficiency → add Urea fertilizer")
    elif N > ideal["N"][1]:
        report.append("Nitrogen excess → reduce nitrogen fertilizer")

    # Phosphorus check
    if P < ideal["P"][0]:
        report.append("Phosphorus deficiency → add DAP fertilizer")
    elif P > ideal["P"][1]:
        report.append("Phosphorus excess → reduce phosphorus fertilizer")

    # Potassium check
    if K < ideal["K"][0]:
        report.append("Potassium deficiency → add Potash fertilizer")
    elif K > ideal["K"][1]:
        report.append("Potassium excess → reduce potassium fertilizer")

    if not report:
        return "Soil nutrients are optimal for this crop."

    return report