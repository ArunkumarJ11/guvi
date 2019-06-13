a= int(input())
if a > 1:
    for k in range(2, a):
        if (a % k) == 0:
            print("yes")
            break
    else:
        print("no")
