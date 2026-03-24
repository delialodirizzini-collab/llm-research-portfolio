ef evaluate(response):
    import json

    solution = {
        "1": {"color": "yellow", "nationality": "norwegian", "drink": "water", "cigarette": "kools", "pet": "fox"},
        "2": {"color": "blue", "nationality": "ukrainian", "drink": "tea", "cigarette": "chesterfields", "pet": "horse"},
        "3": {"color": "red", "nationality": "englishman", "drink": "milk", "cigarette": "old gold", "pet": "snails"},
        "4": {"color": "ivory", "nationality": "spaniard", "drink": "orange juice", "cigarette": "lucky strike", "pet": "dog"},
        "5": {"color": "green", "nationality": "japanese", "drink": "coffee", "cigarette": "parliaments", "pet": "zebra"}
    }

    try:
        clean = response.text.replace("```json", "").replace("```", "").strip()
        parsed = json.loads(clean)
    except:
        return 0

    score = 0
    for pos in ["1","2","3","4","5"]:
        if pos not in parsed:
            continue
        for attr in ["color","nationality","drink","cigarette","pet"]:
            if attr in parsed[pos] and parsed[pos][attr].lower().strip() == solution[pos][attr]:
                score += 1

    return score / 25 
