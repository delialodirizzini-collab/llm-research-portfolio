Zebra Puzzle — LLM Reasoning vs Memorisation Study

## Research Question
Does model size predict performance on logical reasoning tasks, and do LLMs reason to solve puzzles or recall memorised solutions?

## Design
Three conditions were used to distinguish memorisation from reasoning:

Original puzzle : The classic Zebra puzzle ('Einstein Riddle') as widely available online, likely in training data
Rearranged puzzle : Same clues, different solution grid. Requires reasoning, not recall 
Shawshank : Novel clues (prison setting) but preserved logical structure, requiring further reasoning.

LLM Models tested: GPT-3.5 (small), GPT-4o-mini (medium), GPT-5 (large)
## Prompt
Each model received the full puzzle clues and was instructed to return a solution as JSON object only. Keys "1" through "5" represented house positions, 
each containing color, nationality, drink, cigarette, and pet values.

## Scoring
Each correct attribute out of 25 total contributed 4% to the final score.
Responses were  evaluated against a hardcoded solution dictionary, adapted to each puzzle's solution grid.
Cf evaluator_original.py, evaluator_rearranged.py, evaluator_shawshank.py.

## Results

| Model | Original | Rearranged | Shawshank |
|---|---|---|---|
| GPT-3.5 | 100% | 12% | 8% |
| GPT-4o-mini | 52% | 0% | 8% |
| GPT-5 | 100% | 100% | 100% |

## Findings
Model size was not predictive for the original puzzle — GPT-3.5 matched GPT-5 at 100%, while GPT-4o-mini scored only 52% due to hallucination. 
All models scored highest on this widely available version of the riddle.
On the rearranged and novel variants, only GPT-5 retained perfect performance, confirming its ability to reason over problems rather than purely recalling memorised solutions. 
Smaller models replicated original puzzle answers into the rearranged version, revealing memorisation as their primary strategy.





## Note
The full methodology and report are available upon request.
