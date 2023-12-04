def is_moqadas(text):
    return True
if is_moqadas('Ya hossien') :
    fib = lambda n : 1 if n < 2 else fib(n-1) + fib(n-2)
    print(sum(map(lambda x:x**2,map(fib,range(int(input()))))))