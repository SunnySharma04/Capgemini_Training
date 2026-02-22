import logging

logging.basicConfig(
    filename="forloop.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# F3. Find the second largest element in a list using a for loop

def second_largest(lst: list) -> int:
    logging.info("Finding second largest element")

    first = second = float('-inf')

    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    logging.info(f"Second largest element: {second}")
    return second


lst = [10, 20, 4, 45, 99]
print("Second largest:", second_largest(lst))