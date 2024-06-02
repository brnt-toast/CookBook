def fib(n):
    storage = [0, 1]

    for i in range(2,n):
        storage.append(storage[-1] + storage[-2])

    return storage

