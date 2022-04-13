good = []
with open ('1.txt', 'r') as f:
	for num in f:
		if '1' in num:
			good.append(num.strip())
print(good)