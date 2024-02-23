def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def primeX(x):
    list_prime =[]
    num = 2
    while len(list_prime) < x:
        if is_prime(num):
            list_prime.append(num)
        num += 1
    return list_prime[-1]

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29