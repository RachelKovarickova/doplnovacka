# doplnovacka
"""
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
"""

import re
import string


file_text = input('Vlož text nebo soubor s textem i s příponou: ')

text_erase = int(input('Kolikáte slovo smažeme? '))


def nahrazeni():

	roster = []
	output = []
	roster = text.split(' ')
	
	for i in range(0, len(roster)):
		word = roster[i]
		changed_word = ''

		if ((i + 1) % text_erase == 0):
			for letter in word:
				if letter in string.ascii_letters:
					changed_word += '*'
				else:
					changed_word += letter
			output.append(changed_word)
		else:
			output.append(word)

	s = ' '.join(output)
	print(s)


if re.fullmatch('.+\.txt$', file_text):
	with open(file_text) as f:
		text = f.read()
	f.closed
	nahrazeni()
else:
	text = file_text
	nahrazeni()
	


