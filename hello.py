# cos = ["ryuk" + " rajk"]
# cos.append("text") 
# range(1,10)

# def petla(liczba):
# 	for x in cos:
# 		for y in range (1,liczba):
# 			print(str(y) + str(x) +" huhu" )
# 	pass
# 	passlog



lista = []
for x in range(1,101):
	lista.append(x)
	pass
print(lista)

# lista2 = []
# for element in lista:
# 	lista2.append(element*5)
# print(lista2)

# lista3 = [] 
# for cos in lista2:
# 	lista3.append(cos/4)
# print(lista3)

# lista4 = [] 
# for cos in lista3:
# 	lista4.append(cos*5)
# print(lista4)


# [
# import random 
# random.seed()

# liczba = random.randint(1,100)

# print("Zgadnij moją liczbe (1-100)")
# sam = int(input())
# if sam == liczba:
# 	print("zgadłeś")
# if sam > liczba:
# 	print("za dużo")
# if sam <liczba:
# 	print("za mało")
# ]


# import random 
# random.seed()
# pczlon = ["Społeczeństwo obywatelskie", "Edukacja", "Służba zdrowia","Nasza partia", "Partia rządząca", "Wojsko", "Unia Europejska", "Opozycja"]
# dczlon = ["utrudnia", "ułatwia", "umożliwia", "uniemożliwia"]
# tczlon = ["przeprowadzenie reform.", "budowę nowych dróg", "rozwój gospodarki", "wprowadzenie Euro", "budowę elektrowni atomowej", "sprzedaż uranu Czeczenom"]
# pindex = random.randint(0,len(pczlon)-1)
# dindex = random.randint(0, len(dczlon)-1)
# tindex = random.randint(0, len(tczlon)-1)
# print(pczlon[pindex], dczlon[dindex], tczlon[tindex])

# for i in range(1253544,1253548):
# 	print("Obecna liczba to:", i)
# 	print("Jej potęga to:", i*i)



# import random
# random.seed()
# score = 0 
# panstwa = ['Niemcy ', 'Białorus ', 'Litwa ', 'Estonia ', 'USA ', 'Chiny ', 'Australia ','Hiszpania ', 'Portugalia ', 'Austria ']
# stolice = ['Berlin', 'Minsk', 'Wilno', 'Tallinn', 'Waszyngton ', 'Pekin', 'Canberra', 'Madryt', 'Lizbona', 'Wieden']
# for x in range(1,6):
# 	print("Numer pytania:", x)
# 	index = random.randint(0, len(panstwa)-1)
# 	for y in range(1,4):
# 		guess = input("podaj stolice panstwa: " + panstwa[index])
# 		if guess == stolice[index]:
# 			print("Zgadles")
# 			score = score + 4 - y
# 			break
# 		else:
# 			if (score !=0 ):
# 				score = score - 1
# 			print("jeszcze raz")
# 			if y == 3:
# 				print("prawidłową odpowiedzią jest:", stolice[index] )
# print(" Ilość uzbieranych punktów", score)