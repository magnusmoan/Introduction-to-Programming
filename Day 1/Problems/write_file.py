def a(x):
    return x+1


result = []
for i in range(10):
    result.append(a(i))

with open("./Resources/fibonacci.txt", "w") as f:
    for l in result:
        f.write(l)

