def is_prime(num):
    if num < 2 :
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def generate_primes_grid(width, height, start):
    result = ""
    num = start + 1
    for _ in range(height):
        row = ""
        for _ in range(width):
            while not is_prime(num):
                  num += 1
            row += f"{num:2} "
            num += 1
        result += row.strip()+"\n"
    return result

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """