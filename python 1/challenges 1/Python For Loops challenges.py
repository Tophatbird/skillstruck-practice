# Automatic Numbers
var1 = int(input("enter a number"))
var2 = int(input("enter a number"))

while var1 <=var2:
    print(var1)
    var1  += 1


# Add the Numbers
start = int(input("enter a number"))
end = int(input("enter a number"))
num = 0
for i in range(start,end):
    num = num + i
print(num)