# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    if n == 0:
        return 0
    elif n == 1:
        return 1

    i = 1
    t1 = res = 0
    t2 = 1
    while i < n:
        res = (t1 + t2) % 10
        t1 = t2
        t2 = res
        i += 1
    return res



if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
