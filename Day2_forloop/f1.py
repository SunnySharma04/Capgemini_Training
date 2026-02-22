import logging

logging.basicConfig(
    filename="forloop.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# F1. Count how many vowels are present in a string

def count_vowels(s: str) -> int:
    logging.info("Counting vowels in string")

    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1

    logging.info(f"Vowel count: {count}")
    return count


s = "programming"
print("Vowel count:", count_vowels(s))