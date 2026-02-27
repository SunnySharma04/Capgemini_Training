try:
    a = 10000000
    for i in range(1, a):
        print(i, end=' ')
except Exception as e:
    print("Exception is handled, ERROR: ", e)