import logging

logging.basicConfig(
    filename="Q2.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def secondLargest(lst) -> int:
    logging.info("Searching second largest number in a list")
    second_largest = 0

    logging.info(f"Second largest number: {second_largest}")
    return second_largest
print(secondLargest(1,2,3,4,5))