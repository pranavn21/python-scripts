def getMaxInteger(n: int) -> str:
    return int("".join(sorted(str(n), reverse=True)))

def getMinInteger(n: int) -> str:
    return "".join(sorted(str(n)))


print("-------------------------------")
x = input("Enter integer: ")
count = 0
print("-------------------------------" + "\n")
while(x != 6174):
    print("n = " + str(count) + ": " + str(x))
    max = getMaxInteger(x)
    min = getMinInteger(x)
    diff = max - int(min)
    print(str(max) + " - " + str(min) + " = " + str(diff))
    print("\n" + "-------------------------------" + "\n")
    x = diff
    count+=1

