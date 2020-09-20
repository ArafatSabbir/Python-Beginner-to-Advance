if __name__ == '__main__':
    n = int(input())
    li = list()
    for i in range(n):
        li.append(i+1)

    st = ''.join(str(e) for e in li)
    print(st)
