import logging

logging.basicConfig(
    filename="Q2_frequency.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def freq(str) -> list:
    logging.info("counting the freq of the charcater")
    dic={}
    for ch in str:
        if ch in dic:
            dic[ch]+=1
        else:
            dic[ch]=1
    logging.info(f"Frequency count calculated: {dic}")
    return dic
print(freq("aeioua"))