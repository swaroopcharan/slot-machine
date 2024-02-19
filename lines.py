MAX_LINES = 3

def get_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print("Enter Valid Number of Lines")
        else:
            print("Enter a Valid Number")
    return lines