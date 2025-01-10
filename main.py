def word_count(string: str) -> int:
    words = string.split()
    return len(words)


def char_counts(string: str) -> dict[str, int]:
    counts = {}
    normalized_string = string.lower()

    for c in normalized_string:
        if c.isalpha():
            if c in counts:
                counts[c] += 1
            else:

                counts[c] = 1
    return dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))


def generate_report(string: str) -> str:
    report = "--- Begin report of books/frankenstein.txt ---\n"

    words = word_count(string)
    report += f"{words} words found in the document\n\n"

    chars_count = char_counts(string)
    for k, v in chars_count.items():
        report += f"The '{k}' character was found {v} times\n"

    report += "--- End report ---\n"

    return report


def main() -> None:
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    report = generate_report(file_contents)
    print(report)


if __name__ == "__main__":
    main()
