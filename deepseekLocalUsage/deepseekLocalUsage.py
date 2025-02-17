import os
from transformers.utils import logging
from transformers import AutoModelForCausalLM

logging.set_verbosity_info()

os.environ["TRANSFORMERS_VERBOSITY"] = "info"
os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"

#tokenizer = AutoTokenizer.from_pretrained("DeepPavlov/rubert-base-cased-conversational", 
#                                          force_download=True, resume_download=True)
model = AutoModelForCausalLM.from_pretrained("unsloth/DeepSeek-R1-GGUF", trust_remote_code=True)  

print("succes!")
