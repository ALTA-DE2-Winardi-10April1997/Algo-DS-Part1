def start_fibonacci(num):
    if num == 0 or num == 1:
        return True
    return False
    
    
def fibonacci(number):
    list_fibonacci = []
    num = 0
    for i in range(number+1):
        if start_fibonacci(num) and (not list_fibonacci or list_fibonacci[-1] != 1):
            list_fibonacci.append(num)
            num += 1
        else:
            x = list_fibonacci[-1] + list_fibonacci[-2]
            list_fibonacci.append(x)
    return list_fibonacci[-1]

if __name__ == "__main__":
    print(fibonacci(0))  # 0
    print(fibonacci(2))  # 1
    print(fibonacci(9))  # 34
    print(fibonacci(10)) # 55
    print(fibonacci(12)) # 144