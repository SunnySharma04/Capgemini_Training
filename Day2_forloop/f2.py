import logging

logging.basicConfig(
    filename="forloop.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# F2. Print the frequency of each character in a string

def char_frequency(s: str) -> dict:
    logging.info("Calculating character frequency")

    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    logging.info(f"Character frequency: {freq}")
    return freq


s = "hello"
print("Character frequency:", char_frequency(s))