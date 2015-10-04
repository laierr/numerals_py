from random import randint
import numerals

rnd = randint(0,999)
print numerals.number_to_txt(rnd)

done = False

while not done:
	raw_answer = raw_input('Your answer: ')
	if raw_answer.isdigit():
		answer = int(raw_answer)
		if answer == rnd:
			print 'CORRECT!'
			done = True
		else:
			print 'No luck, try again!'
	else:
		print 'INTEGER, pleese!'
