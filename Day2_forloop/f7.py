import logging

logging.basicConfig(
    filename="forloop.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# F7. Find the missing number in a list containing numbers from 1 to N

def find_missing_number(lst: list, n: int) -> int:
    logging.info("Finding missing number")

    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i

    actual_sum = 0
    for num in lst:
        actual_sum += num

    missing = total_sum - actual_sum

    logging.info(f"Missing number: {missing}")
    return missing


lst = [1, 2, 4, 5]
n = 5
print("Missing number:", find_missing_number(lst, n))