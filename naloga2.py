seznam=[1,2,3,4]

def povecaj(seznam):
	return [3*i if i%2==0 else i
		for i in seznam
	]

print(seznam)
print(povecaj(seznam))
print(seznam)
