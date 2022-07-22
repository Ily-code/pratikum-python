def fib(n):
    a,b,c = 0, 1 ,2
    while a < n:
        print (a,b,c)
        a, b = b, a+b

fib(5)
