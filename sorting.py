#define a function
def list_sort(lista):

    even = []
    odd = []
    characters = []
    mydict = dict()
    #conditional statements
    if not isinstance(lista, list):
        return 'Invalid Input'

    if not lista:
        mydict['evens'] = even
        mydict['odds'] = odd
        mydict['chars'] = characters
        return mydict

    for i in lista:

        if isinstance(i, int):
            if i % 2 == 0:
                even.append(i)

            else:
                #odd number
                odd.append(i)
        #characters
        elif isinstance(i, str):
            characters.append(i)

    mydict['evens'] = sorted(even)
    mydict['odds'] = sorted(odd)
    mydict['chars'] = sorted(characters)
    return mydict


print(list_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b']))
  
