#!/bin/bash

MODEL_PATH=$(dirname $0)
echo $MODEL_PATH
BPE_CODES="$MODEL_PATH/bpe.codes"
BPE_VOCAB="$MODEL_PATH/bpe.vocab"

python3 $MODEL_PATH/custom_constraints.py \
    --BPE-codes $BPE_CODES \
    --BPE-vocab $BPE_VOCAB \
    --compute-factor \