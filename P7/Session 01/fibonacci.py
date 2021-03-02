x = 0
y = 1

numbers = int(11)
#number = 5 range(0,6) -> 0,1,2,3,4,5 | range(0,5) -> 0,1,2,3,4
if numbers == 1:
    print(x)
elif numbers == 2:
    print(x)
    print(y)
else:
    print(x)
    print(y)
    for n in range(0, numbers - 2):
        fn = x + y
        print(fn)
        x = y
        y = fn