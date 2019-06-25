def find_combinations(target):
	p2 = p3 = p5 = 0
	while target != 1:
		if target % 2 == 0:
			target = target/2
			p2 += 1
		elif target % 3 == 0:
			target = target/3
			p3 += 1
		elif target % 5 == 0:
			target = target/5
			p5 += 1
		else:
			# print(target)
			return None
	return {"2": p2, "3": p3, "5": p5}


result = find_combinations(1845281250)
output = []

if result is None:
	print("None")
else:
	for i in result:
		output += list(i) * result[i]
	print(tuple(map(int, output)))
