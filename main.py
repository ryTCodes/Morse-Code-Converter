import sys
from dict import dict_list


def main() -> None:
    while True:
        encryption_type: str = input("To encode type 'encode', to decode type 'decode': ").strip().lower()
        morse(encryption_type)
        if not should_continue():
            break


def should_continue() -> bool:
    continue_encryption: str = input("Continue the encryption?\nType 'y' to continue, type 'n' to stop: ").strip().lower()
    return continue_encryption == 'y'


def morse(encryption_type: str) -> None:
    user_input: str = input("Enter the text:\n").upper()
    result_text: str = ""

    if encryption_type == 'encode':
        for char in user_input:
            if char == " ":
                result_text += ' /'
            else:
                for dict in dict_list:
                    if char in dict:
                        result_text += f" {dict[char]}"

    elif encryption_type == 'decode':
        code_list: list = user_input.split(' ')
        for char in code_list:
            if char == '/':
                result_text += ' '
            else:
                for dict in dict_list:
                    for (key, value) in dict.items():
                        if value == char:
                            result_text += key
    else:
        sys.exit()

    result_text = result_text.capitalize().strip() if encryption_type == 'decode' else result_text.strip()
    print(f"Result Text:\n{result_text}\n")


if __name__ == "__main__":
    main()
