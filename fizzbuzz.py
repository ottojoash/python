def fizzbuzz(list1, list2):
   add = len(list(list1)) + len(list(list2))
   print(int(add))
    #logical statments
   if add % 3 == 0 and add % 5 != 0:
      print("fizz")
   if add % 5 == 0 and add % 3 != 0:
      print("buzz")
   if add % 3 == 0 and add % 5 == 0:
      print("fizzbuzz")

fizzbuzz([1,2,3,4,5,6,],[3,4,5,3,5])   