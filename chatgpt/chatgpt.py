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

def generate_test(input_code: list) -> str:
    # Mock response
    return str(input_code)

