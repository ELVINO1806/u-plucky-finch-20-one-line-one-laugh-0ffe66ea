
"""Write the competition entry to /output/entry.txt."""

import os

ENTRY = "My plants have a group chat now. They voted me out for underwatering and elected the cactus as president."


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
