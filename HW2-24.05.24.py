def odd(a, b):
    l = [i for i in range(a, b+1) if i%2==0]
    print(*l, sep='\n')

a = int(input('a'))
b = int(input('b'))
odd(a, b)