from transformers import pipeline

unmasker = pipeline('fill-mask', model='bert-base-multilingual-cased')
unmasker("Москва - [MASK] Российской Федерации.")
