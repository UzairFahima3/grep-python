import sys
import re
# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
      return pattern in input_line
    elif pattern == "\\d":
      return any(c.isdigit() for c in input_line)
    elif pattern == "\\w":
      return any(c.isalnum() or c == '_' for c in input_line)
    elif re.match(r"\[.*\]", pattern):
      neg_char = pattern[1]
      chars_to_match = pattern[1:-1]
      if neg_char == '^':
        return any(c not in chars_to_match for c in input_line)
      else:
        return any(c in chars_to_match for c in input_line)
    elif re.search(r"\\d", pattern) or re.search(r"\\w", pattern):
        # Handle cases like '\d apple' or '\d\d\d apple'
        regex_pattern = pattern.replace("\\d", r"\d").replace("\\w", r"\w")
        return re.search(regex_pattern, input_line) is not None
    elif pattern[0] == "^":
      if pattern[1:] == input_line:
        return True
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
