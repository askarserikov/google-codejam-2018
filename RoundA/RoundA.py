import random


a = [random.randint(0, 10000000000000000) for _ in range(100)]


def extract_digits(n):
    extracted = []
    while n >= 10:
        extracted.append(n % 10)
        n = n // 10
    extracted.append(n)
    extracted.reverse()
    return extracted


def has_odd_digits(n):
    b = extract_digits(n)
    for i in range(0, len(b)):
        if b[i] % 2 != 0:
            return True
    return False


def count_moves(n, case):
    b = extract_digits(n)
    result = 0
    for i in range(0, len(b)):
        if b[i] % 2 == 0:
            pass
        else:
            # if it's the last digit - just increment it
            if i + 1 >= len(b):
                result = 1
                break
            remainder = 0
            # get a number that starts with the leftmost odd digit
            for j in range(i, len(b)):
                remainder += b[j] * 10 ** (len(b) - j - 1)
            medium = b[i] * 10 ** (len(b) - i - 1)
            for j in range(i + 1, len(b)):
                medium += 4 * 10 ** (len(b) - j - 1)
            if remainder >= medium and not has_odd_digits(1+b[i]):
                result = (1 + b[i]) * 10 ** (len(b) - i - 1) - remainder
                break
            else:
                num = (b[i] - 1) * 10 ** (len(b) - i - 1)
                for j in range(i + 1, len(b)):
                    num += 8 * 10 ** (len(b) - j - 1)
                result = remainder - num
                break
    print("Case #{}: {}".format(case + 1, result))