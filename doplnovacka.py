# doplnovacka

with open ("lorem.txt") as f:
	text = f.read()
f.closed

text = text.replace("\n", "# ")

seznam = []
seznam = text.split(" ") # rozdelime string na seznam, na jednotlive prvky, slova
vysledek = []
interpunkce = ".,?!-;\""

# print(seznam)

for i in range (0, len(seznam)):
	slovo = seznam[i]		# prvek seznamu ulozim do slovo
	slovoUpraveno = ""
	if ((i + 1) % 5 == 0):		
		for pismeno in slovo:
			if pismeno not in interpunkce:
				slovoUpraveno += "*"
			else:
				slovoUpraveno += pismeno
		vysledek.append(slovoUpraveno)
	else:
		vysledek.append(slovo)

s = " ".join(vysledek) # vsechny prvky vysledku spoj pomoci mezery
s = s.replace("#", "\n")
print(s)
