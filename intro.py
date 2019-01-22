x= int(input("enter year of birth"))
age= 2019 - x
print(age)
if age < 18:
  print("minor")
  age= 18
if age in list(range(19, 36)):
     print("youth")
if age > 36:
    print("elder")


