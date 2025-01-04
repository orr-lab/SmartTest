from chatgpt import chatgpt

class FileProcessingException(Exception):
    pass

SUPPORTED_FILE_EXTENSIONS = [".txt", ".py"]

def is_file_supported(file_name):
    """Check if a file has a supported extension."""
    return any(file_name.endswith(ext) for ext in SUPPORTED_FILE_EXTENSIONS)

def file_to_array(files):
    """
    Reads the uploaded files, validates them, and delegates content
    to the chatbot processing logic.
    """
    file_data = []

    for file in files:
        if not is_file_supported(file.filename):
            continue




        # Read file content and prepare for processing
        content = file.read().decode('utf-8')  # Assuming UTF-8 encoding
        file_data.append({"name": file.filename, "content": content})


    # Pass the array of file data to the chatbot for processing
    print(len(file_data))
    return chatgpt.generate_test(file_data)
