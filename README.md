# llm-research-portfolio
Empirical analysis evaluating LLM reasoning, evaluation and profile alignment.




### 1. Reasoning vs Memorisation — Zebra Puzzle ('Einstein's Ridlle'- that wasn't Einstein's)
Does model size predict reasoning ability, or do larger models simply recall from a larger training data?

GPT-3.5, GPT-4o mini, and GPT-5 were tested across three puzzle variants using an automated Python scoring pipeline. GPT-5 was found to perform perfect scores on the original riddle, the rearranged riddle and a novel variant of it, suggesting it can grasp the underlying logic rather than merely recalling. Smaller versions of the model collapsed, as they replicated memorised solutions.

→ [View study](zebra-puzzle/)

---

### 2. Pun Detection — Four-Pathway Evaluation
Do LLMs detect puns through genuine linguistic understanding or surface pattern matching?

Three models evaluated across varying levels of granularity : sentence, word, and semantic levels, using sensitivity and specificity metrics.
Specificity emerged as the more diagnostic metric for genuine pun comprehension. Gemini 2.5 Flash was the only 
model that maintained a high performance across all four pathways, 
suggesting a reasoning mechanism closer to semantic understanding vis à vis other models.
→ [View study](pun-detection/)
→ [View ChainForge workflow](https://chainforge.ai/play/?f=3mt83u00npwko)

---

### 3. LLM Alignment Profiles — Moral Dilemma Study
Do LLMs from different organisations exhibit measurably and qualitatively different alignment profiles on symmetrical moral dilemmas?

A 6×6 factorial prompt design generated 36 variants per model 
across three LLMs (GPT-5, Gemini 2.5 Flash, Meta-Llama 3.1). 
Responses were classified by a GPT-5 scorer node across four 
dimensions: stance, hedging level, justification type, and 
deference type across 108 total responses.

Three distinct alignment profiles emerged. GPT-5 displayed a
legalist and ecologically sensitivity, Gemini was more force-tolerant and 
morally grounded, Meta-Llama displayed more consequentialist compass and strong 
hedging. Consequentialism was the dominant justification type 
across all models combined. 


## Tools
- Python — automated scoring and evaluation pipelines
- ChainForge — multi-model prompt evaluation platform
- Models — GPT-3.5, GPT-4o mini, GPT-5, Gemini 2.5 Flash, 
Meta-Llama 3.1 Instruct Turbo
- Methods — sensitivity/specificity analysis, factorial 
experimental design, and LLM-as-scorer methodology. 
