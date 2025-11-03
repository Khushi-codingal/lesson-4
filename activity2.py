#taking amount from the user
amount = int(input(" enter amount:"))

#calculating the number of notes
note1 = amount//100
note2 = (amount %100)//50
note3 = ((amount %100)%50)//10

print("notes of 100 rupess:", note1)
print("notes of 50 rupess:", note2)
print("notes of 10 rupess:", note3)