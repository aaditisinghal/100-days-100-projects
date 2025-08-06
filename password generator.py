print("welcome to password generator")
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=["!","@","#","$","%","^","&","*","+"]
maletters=int(input("how many letters?"))
masymbols=int(input("how many symbols?"))
manumbers=int(input("how many numbers?"))
import random
  let= random.choice(letters)
  sym= random.choice(symbols)
  numb= random.choice(numbers)
  print(f"your password is:{let+sym+numb}")

