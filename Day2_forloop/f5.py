import logging

logging.basicConfig(
    filename="forloop.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# F5. Reverse a string using a for loop (no slicing)

def reverse_string(s: str) -> str:
    logging.info("Reversing string")

    reversed_str = ""

    for ch in s:
        reversed_str = ch + reversed_str

    logging.info(f"Reversed string: {reversed_str}")
    return reversed_str


s = "Sunny"
print("Reversed string:", reverse_string(s))