#input the year of birth
x= int(input("enter year of birth"))
age= 2019 - x
print(age)
#below 18 years
if age < 18:
  print("minor")
  age= 18
  #between 18 to 36
if age in list(range(19, 36)):
     print("youth")
     #above  36 years
if age > 36:
    print("elder")


