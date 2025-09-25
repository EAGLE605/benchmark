import time

PRODUCTS = ['A', 'B', 'C']


def run():
    results = {}
    for p in PRODUCTS:
        start = time.time()
        s = 0
        for i in range(1000):
            # simulate some work
            s += i * i
        end = time.time()
        results[p] = end - start
    print(results)


if __name__ == '__main__':
    run()
