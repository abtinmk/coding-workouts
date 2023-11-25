
N, A, B = map(int ,input().split())


if (N%(A*B)==0):
    print("FizzBuzz")
elif (N%A == 0):
    print("Fizz")
elif (N%B == 0):
    print("Buzz")
elif ((N%B and N%A != 0)):
    print(N)
