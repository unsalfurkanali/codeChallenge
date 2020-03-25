def prime(x):
    for i in range(2, x, 1):
        if not x%i:
            return False
    return True

def palandoken(x):
    strX = str(x)
    for i in range(0, len(strX), 1):
        if not prime(int(strX[0 : i : ] + strX[i + 1 : :])):
            return False
    return True

sum = 0
for i in range(10, 50000, 1):
    if prime(i):
        if palandoken(i):
            sum = sum + i
            print(i)
print("Total = {}".format(sum))