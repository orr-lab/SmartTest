import sys

from chatgpt.chatgpt import generate_test


def run_test(filename: str):
    with open(filename, "rt") as file:
        file_content = file.read()

    response = generate_test([{
        "name": filename,
        "content": file_content
    }])
    print("Response: ")
    print(response)


def main(args):
    if len(args) != 2:
        print(f"Usage: python {args[0]} [file_name]")
        return 1
    filename = args[1]
    run_test(filename)

if __name__ == "__main__":
    sys.exit(main(sys.argv))