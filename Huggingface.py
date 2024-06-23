import transformers
import torch
from transformers import pipeline
from huggingface_hub import HfFolder

# Save the HF token using HfFolder
HfFolder.save_token('your_api_key')

# Define the model ID (use a known model for demonstration)
model_id = "facebook/opt-125m"

# Initialize the pipeline
pipe = pipeline("text-generation", model=model_id)

# Define the prompt
prompt = "Once upon a time"

# Generate text using the pipeline
output = pipe(prompt, max_length=50)

# Print the generated text
print(output)
