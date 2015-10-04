from random import randint
import numerals

rnd = randint(0,999)
print numerals.number_to_txt(rnd)

def jumpstart():
	raw_answer = raw_input('Your answer: ')
	if raw_answer.isdigit():
		answer = int(raw_answer)
		if answer == rnd:
			print 'CORRECT!'
		else:
			print 'No luck, try again!'
			jumpstart()
	else:
		print 'INTEGER, please!'
		jumpstart()

if __name__ == '__main__':
	jumpstart()
