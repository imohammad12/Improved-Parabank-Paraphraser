Original Version : https://github.com/decompositional-semantics-initiative/improved-ParaBank-rewriter

## Install the conda env:
> conda env create -f IPP.yml

Download params.best from [here](https://github.com/decompositional-semantics-initiative/improved-ParaBank-rewriter/releases/tag/v0.1) and put it in the root of project.

## Usage in python:
```
from constrained_paraphrasing import paraphrase

sent = "the great dark spot is thought to represent a hole in the methane cloud deck of neptune."
paraphrase(sent, ['great', 'dark'], ['enormous'])
# first list contains the negative constraints, and the second list contains positive constraints

# output :
# 'An enormous black spot is thought to represent a hole in the methane cloud deck of neptune.\n'
```

For not giving negative/positive constraints give empty list to the paraphrase function


