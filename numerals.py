units = {
	0: "efes",
	1: "ehad",
	2: "shtaim",
	3: "shelosh",
	4: "arba",
	5: "hamesh",
	6: "shesh",
	7: "sheva",
	8: "shmone",
	9: "teisha"
}

tens = {
	1: "eser",
	2: "esrim",
	3: "shloshim",
	4: "arbaim",
	5: "hameshim",
	6: "shishim",
	7: "shevim",
	8: "shmonim",
	9: "teshim"
}

hundreds = {
	1: "mea",
	2: "mataim",
	3: "shlosh meot",
	4: "arba meot",
	5: "hamesh meot",
	6: "shesh meot",
	7: "shva meot",
	8: "shmona meot",
	9: "tsha meot"
}

def number_to_txt (numeral):
	# convert incoming number to array of digits:
	array = map(int, list(str(numeral)))	# *numeral* >> to string >> split to array >> map as integers

	if len(array) == 1:		# 0 - 9
		return units[numeral]
	elif len(array) == 2:	# 10 - 99
		return tens_to_txt(*array)
	elif len(array) == 3:	# 100 - 999
		return hundreds_to_txt(*array)

def tens_to_txt(ten, unit):
	if unit == 0:						# 10, 20, 30, etc.
		return tens[ten]
	elif ten == 1:						# 11-19
		return units[unit] + "esre"	

	return tens[ten] + " ve" + units[unit] # everything else

def hundreds_to_txt(hundred, ten, unit):
	if ten == 0 and unit == 0:			# 100, 200, 300, etc.
		return hundreds[hundred]
	elif ten == 0:						# 101, 202, 403, 804, etc.
		return hundreds[hundred] + " ve" + units[unit]	
	elif ten == 1:						# x11-x19 
		return hundreds[hundred] + " ve" + units[unit] + "esre" 

	return hundreds[hundred] + " " + tens_to_txt(ten, unit)	#everything else
