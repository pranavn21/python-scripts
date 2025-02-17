def getMaxInteger(n: int) -> str:
    return int("".join(sorted(str(n), reverse=True)))

def getMinInteger(n: int) -> str:
    return "".join(sorted(str(n)))


print("-------------------------------")
x = int(input("Enter integer: "))
count = 0
print("-------------------------------" + "\n")
while(x >= 100 and x <= 99999):
    oldNum = x
    max = getMaxInteger(x)
    min = getMinInteger(x)
    diff = max - int(min)

    if(diff == oldNum):
        break

    print("n = " + str(count) + ": " + str(x))
    print(str(max) + " - " + str(min) + " = " + str(diff))
    print("\n" + "-------------------------------" + "\n")
    x = diff

    count+=1

