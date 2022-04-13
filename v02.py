good = []
with open ('1.txt', 'r') as f:
	good = [num.strip() for num in f if "1" in num]
print(good)