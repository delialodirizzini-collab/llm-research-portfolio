
# Pun Detection — LLM Evaluation Study 

## Research Question 
Do LLMs detect puns through genuine linguistic understanding, or do they default to over-detection once prompted to identify puns, regardless of semantic context? 

Three LLMs were evaluated across four pathways of increasing 
granularity:
- **Pathway 1** — Sentence-level detection (no ambiguous cases)
- **Pathway 2** — Sentence-level detection (dataset including accidental puns)
- **Pathway 3** — Word-level detection (identifying the pun word)
- **Pathway 4** — Semantic prediction (identifying the word that the pun word replaces)
  
   - Models compared: GPT-4o mini, Gemini 2.5 Flash, Meta-Llama 3.1

     Evaluation metrics: Sensitivity (#TP / #TP + #FN) and Specificity (#TN / #TN + #FP) per model per pathway.

     ## Data

A dataset of 30 sentences was encoded in a tabular node, split equally between true puns (label: P) and non-puns (label: N). Each pun entry included three metadata 

fields: the sentence, the pun word (pun_word), and the word it replaces (word_replaced). A second dataset of 20 additional ambiguous sentences containing accidental puns (non-intentional puns) was added for Pathway 2 to test models under higher ambiguity.

Key Findings 
| Model | Pathway 1 Sensitivity | Pathway 1 Specificity | |---|---|---| | GPT-4o mini | 80% | 86% | | Gemini 2.5 Flash | 100% | 100% | | Meta-Llama 3.1 | 86% | 13% | -

All three models showed a systematic bias toward over-detection (higher sensitivity than specificity). This suggests a default tendency to classify sentences as puns - Gemini 2.5 Flash was the only model achieving 100% on both metrics in the clean dataset - The introduction of accidental puns caused significant False Positive increase in GPT-4o mini and Meta-Llama 3.1, while Gemini retained 86% specificity - Gemini's superiority extended to word-level (15/15) and semantic prediction (14/15), indicating disparity in the models' results and a deeper linguistic understanding by Gemini rather than surface pattern matching - Meta-Llama 3.1 scored only 3/15 on semantic prediction, confirming that high sensitivity without specificity reflects shallow detection (probably conditioned by the prompt) rather than comprehension 
## Interpretation 
Specificity emerged as the more diagnostic metric for genuine pun understanding over sensibility. Gemini 2.5 Flash's consistent performance across all four pathways suggests a mechanism closer to semantic reasoning than the other two models. 

## Tools 
ChainForge (multi-model prompt evaluation platform), GPT-4o mini, Gemini 2.5 Flash, Meta-Llama 3.1 
