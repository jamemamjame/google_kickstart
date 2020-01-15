'''
Practice Round 2019 - Kick Start 2019
'''


def readline_int():
    return int(input())


def readline_mul_int():
    return [int(x) for x in input().split()]


def guess(a, b):
    return int((a + b) / 2) + ((a + b) % 2)


T = readline_int()  # read the number of test cases

for _ in range(T):
    A, B = readline_mul_int()
    N = readline_int()
    is_correct = False

    for n in range(N):
        guess_number = guess(A, B)
        print(guess_number)

        res = str(input())
        if res == 'TOO_BIG':
            B = guess_number - 1
        elif res == 'TOO_SMALL':
            A = guess_number + 1
        elif res == 'CORRECT':
            is_correct = True
            break
        elif res == 'WRONG_ANSWER':
            break
    if not is_correct:
        break
