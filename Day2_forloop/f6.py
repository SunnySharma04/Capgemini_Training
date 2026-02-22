import logging

logging.basicConfig(
    filename="forloop.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# F6. Remove duplicate elements from a list while preserving order

def remove_duplicates(lst: list) -> list:
    logging.info("Removing duplicates from list")

    result = []

    for item in lst:
        if item not in result:
            result.append(item)

    logging.info(f"List after removing duplicates: {result}")
    return result


lst = [1, 2, 2, 3, 4, 3, 5]
print("After removing duplicates:", remove_duplicates(lst))