"""
このファイルに解答コードを書いてください
"""

dic = {}
input_num = 0
########

for line in open("./input.txt"):
    value = line.split(":")
    if(len(value) == 2):
        dic[int(value[0])] = value[1].replace("\n","")
    else:
        input_num = int(value[0])
        break
    

output_index = []
output_value = ""

for value in dic:
    if(input_num % value == 0):
        output_index.append(value)

output_index.sort()
for value in output_index:
    output_value += dic[value]

if output_value:
    print(output_value)
else:
    print(input_num)