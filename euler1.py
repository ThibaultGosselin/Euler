# Euler
10/09
somme = 0


for n in range(0,1000):

	if n%3==0:
		somme = n+somme
	elif n%5==0:
		somme = n+somme
	
print somme
