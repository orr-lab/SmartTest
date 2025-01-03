import os

def _chatgpt_api_key():
    return os.environ["ChatGPTprivateKey"]

def format_llm_message(input_code: str):
    return f"""
Write a unit test for this code: 
```
{input_code}
```
"""

def generate_test(input_code: str) -> str:
    # Mock response
    return "run_test()"

