def process_log_file(input_file="keylog.txt"):
    with open(input_file, "r") as f:
        lines = f.readlines()

    typed_chars = []

    for line in lines:
        if ": " not in line:
            continue
        key = line.split(": ", 1)[1].strip()

        if key == 'Key.space':
            typed_chars.append(" ")
        elif key == 'Key.backspace':
            if typed_chars:
                typed_chars.pop()
        elif key.startswith("Key."):
            continue
        else:
            typed_chars.append(key)

    return "".join(typed_chars)

if __name__ == "__main__":
    result = process_log_file()
    print("🧠 Reconstructed Typed Text:\n", result)

    with open("cleaned_output.txt", "w") as f:
        f.write(result)
