def fib(seq):
    prev = 0
    current = 1
    result = 0
    if seq == 0:
        return prev
    elif seq == 1:
        return current
    else:
        for x in range(0, seq - 1):
            result = prev + current
            prev = current
            current = result
        return result


def test_fibonacci():
    assert fib(8) == 21


def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)




