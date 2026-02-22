import logging

logging.basicConfig(
    filename="forloop.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# F4. Check whether a list is sorted in ascending order

def is_sorted(lst: list) -> bool:
    logging.info("Checking if list is sorted")

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            logging.info("List is NOT sorted")
            return False

    logging.info("List is sorted")
    return True


lst = [1, 2, 3, 4]
print("Is sorted:", is_sorted(lst))