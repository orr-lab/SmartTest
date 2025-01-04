from typing import List

from chatgpt.chatgpt_api import chatgpt_request
from dataclasses import dataclass

class LlmBadResponse(Exception):
    pass

@dataclass
class LlmTestResponse:
    code: str
    code_language: str

def debug_log(tag: str, message: str):
    print(f"----------------{tag}")
    print(message)
    print("----------------")


def format_llm_message(input_files: List) -> str:
    output = ""

    output += """Write a unit test for this code: \n\n"""

    for file in input_files:
        filename = file["name"]
        file_content = file["content"]

        output += f"""
file: {filename}
```
{file_content}
```
"""

    output += "Output only code, without any explanation. Add comments explaining the code"
    return output

def process_llm_response(llm_response: str) -> LlmTestResponse:
    # Remove redundant newlines
    llm_response = llm_response.strip()
    if not llm_response.startswith("```") or not llm_response.endswith("```"):
        raise LlmBadResponse("Chatgpt returned invalid code")
    first_line, code = llm_response.split("\n", 1)
    # remove ` specifying code end
    code = code.rstrip("` ")
    language = first_line.strip("` ")
    return LlmTestResponse(code, language)



def generate_test(input_files: List) -> str:
    llm_message = format_llm_message(input_files)
    debug_log("llm_message", llm_message)

    llm_response = chatgpt_request(llm_message)
    debug_log("llm_response", llm_response)
    llm_result = process_llm_response(llm_response)
    debug_log("llm_result", llm_result.code)
    return llm_result.code
