import torch
import os
import sys
# from transformers import pipeline

device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Using device: {device}")


print(sys.version)

model_id = "meta-llama/Llama-3.2-1B"

# pipe = pipeline(
#     "text-generation", 
#     model=model_id, 
#     torch_dtype=torch.bfloat16, 
#     device_map="auto"
# )

# pipe("The key to life is")
