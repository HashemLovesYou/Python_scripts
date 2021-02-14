def fib_func(c):
    a = 0
    b = 1
    counter = 1

    print("\n\n")

    while counter < c:
        print(f"{counter} : {a}")
        counter += 1
        a +=b
        print(f"{counter} : {b}")
        counter += 1
        b +=a

print("\n______________________________________________________\n")

n = input("How many numbers?")

fib_func(int(n))
