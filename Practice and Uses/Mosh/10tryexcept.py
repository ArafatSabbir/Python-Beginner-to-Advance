try:
    age = int(input('>>'))
    print(f'Age is {age}')
except ValueError:
    print('invalid number')