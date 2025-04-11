def digit_root(num):
    answer = 0
    if isinstance(num, int) and num <= 10000000:
        answer = (num-1)%9+1
        print(answer)
    else:
        print('wrong input')