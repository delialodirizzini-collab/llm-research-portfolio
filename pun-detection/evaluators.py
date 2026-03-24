# Pun Detection — LLM Evaluation 
# Four evaluators testing LLMs' pun understanding, at varying levels of granularity.
# 1. Sentence-level detection (binary yes/no)
# 2. Sentence-level detection with accidental puns (sentences that seem like puns but are non-intentional)
# 3. Word-level detection (identify the pun word)
# 4. Semantic prediction (identify the word that the pun replaces)


# Pathway 1 & 2 — Sentence-level pun detection
# Classifies model responses as True Positive (TP), False Negative (FN), False Positive (FP), or True Negative (TN)
# against ground truth labels (P = pun, N = non-pun)
def evaluate_sentence_level(response):
    answer = response.text.strip().lower()
    is_actual_pun = response.meta['label'] == 'P'
    said_yes = answer.startswith("yes")

    if is_actual_pun and said_yes:
        return "TP"
    elif is_actual_pun and not said_yes:
        return "FN"
    elif not is_actual_pun and said_yes:
        return "FP"
    else:
        return "TN"


# Pathway 3 — Word-level pun detection
# Checks whether the model correctly identifies the specific word carrying the pun

def evaluate_word_level(response):
    predicted = response.text.strip().lower()
    correct = response.meta['pun_word'].strip().lower()

    if predicted == correct:
        return "correct"
    else:
        return "incorrect"


# Pathway 4 — Semantic prediction
# Checks whether the model can identify the word replaced by the pun word 
def evaluate_semantic_prediction(response):
    predicted = response.text.strip().lower()
    correct = response.meta['word_replaced'].strip().lower()

    return "correct" if predicted == correct else "incorrect"

