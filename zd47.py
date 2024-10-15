a = 239
Del = []
count = 0
Max = 0

for i in range(1,a + 1):
    if a % i == 0:
        Del.append(str(i))

for i in range(len(Del)):
    for j in range(len(Del[i])):
        count += int(j)
    if count > Max:
        Max = Del[i]
        count = 0

print(Max)