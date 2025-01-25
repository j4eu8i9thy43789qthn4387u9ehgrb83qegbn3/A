def kalkulator():
	print ("Prosty kalkulator")
	print ("1. Dodaj")
	print ("2. Odejmij")
	print ("3. Pomnóż")
	print ("4. Podziel")
	wybor = input("Wybierz operacje 1/2/3/4")
	a = float(input("Podaj wartość a: "))
	b = float(input("Podaj wartość b: "))

	if wybor == "1":
		print (f"Wynik: {a + b}")
	elif wybor == "2":
		print (f"Wynik: {a - b}")
	elif wybor == "3":
		print (f"Wynik: {a * b}")
	elif wybor == "4":
		if b == 0:
			print ("Nie można dzielić przez 0.")
			return
		print (f"Wynik: {a / b}")
	else:
		print ("Błędny wybór")

kalkulator()
