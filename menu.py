while True:	
	print("Choose an option:\n\t1:Create a new journal\n\t2:Make a new journal Entries\n\t3:Display Made Journal Entries\n\t4:View my last journal Entry\n\t Enter 0 to quit")
	try:
		choice = int(input("Choice:"))
	except(ValueError):
		print("Invalid choice!!! Choose from available options")
		continue
	
	print(type(choice))
	
	if choice ==1:
		pass
	elif choice==2:
		pass
	elif choice == 3:
		pass
	elif choice ==4:
		pass
	elif choice ==0:
		break
	else:
		print("Invalid choice!!! Choose from available options")
		continue
