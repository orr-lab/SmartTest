from chatgpt import chatgpt

def file_to_string(file):
    content = file.read().decode("utf-8")
    result = chatgpt.generate_test(content)
    return result