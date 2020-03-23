def sophie(x):
    if prime(x) and prime(2*x+1):
        return True
    else:
        return False

def harshad(x):
    xStr = str(x)
    sum = 0
    for i in range(len(xStr)):
        sum = sum + int(xStr[i])
    if x%sum == 0:
        return True
    return False
    
def prime(x):
    for i in range(2, x, 1):
        if x%i == 0:
            return False
    return True

password = 0
for i in range(1000, 100, -1):
    if sophie(i):
        password = i + password
        print(i)
        break

for i in range(1000, 10000, 1):
    if harshad(i):
        password = i + password
        print(i)
        break

print(password)