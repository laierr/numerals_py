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
	array = list(str(numeral))
	array = map(lambda x: int(x), array)

	if len(array) == 1:
		return units[numeral]
	elif len(array) == 2:
		return tens_to_txt(array[0], array[1])
	elif len(array) == 3:
		return hundreds_to_txt(array[0],array[1],array[2])

def tens_to_txt(ten, unit):
	if unit == 0:
		return tens[ten]
	elif ten == 1:
		return units[unit] + "esre"

	return tens[ten] + " ve" + units[unit]


def hundreds_to_txt(hundred, ten, unit):
	if ten == 0 and unit == 0:
		return hundreds[hundred]
	elif ten == 0:
		return hundreds[hundred] + " ve"+ units[unit]
	elif ten == 1:
		return hundreds[hundred] + " ve"+ units[unit] + "esre"
	return hundreds[hundred] + " " + tens_to_txt(ten, unit)