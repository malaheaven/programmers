def solution(num):
    answer = 0

    while True:
        if num == 1:
            break

        if answer > 500:
            answer = -1
            break

        if num % 2 == 0:
            num = num / 2
            answer += 1

        else:
            num = (num * 3) + 1
            answer += 1

    return answer


if __name__ == '__main__':
    n = 6
    print(solution(n))
