def evaluate(response):

    """ Scores LLM responses against similar but rearranged Zebra puzzle solutions. 
    Returns a float between 0 and 1 representing the proportion of correct answers. 
    Handles malformed or non-JSON responses . """
    

    import json

    solution = {
        "1": {"color": "blue", "nationality": "spaniard", "drink": "water", "cigarette": "parliaments", "pet": "zebra"},
        "2": {"color": "ivory", "nationality": "norwegian", "drink": "milk", "cigarette": "chesterfields", "pet": "dog"},
        "3": {"color": "yellow", "nationality": "japanese", "drink": "orange juice", "cigarette": "lucky strike", "pet": "horse"},
        "4": {"color": "green", "nationality": "ukrainian", "drink": "tea", "cigarette": "kools", "pet": "snails"},
        "5": {"color": "red", "nationality": "englishman", "drink": "coffee", "cigarette": "old gold", "pet": "fox"}
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
