input_data = open('input.txt', 'r')
a = int(input_data.read())


Del = []
count = 0
Max = 0
max_ch = 0

for i in range(1,a + 1):
    if a % i == 0:
        Del.append(str(i))

for i in range(len(Del)):
    for j in range(len(Del[i])):
        count += int((Del[i])[j])
    if count > max_ch:
        Max = Del[i]
        max_ch = count
        count = 0
        

output_data = open('output.txt', 'w')
output_data.write(str(Max))
#запись

input_data.close()
output_data.close()
#ОБЯЗАТЕЛЬНО не забывать