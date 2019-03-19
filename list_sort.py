def list_sort(listX):
    
    odd = []
    even = []
    characters = []
    mydict = dict()

    
    if not listX:
        mydict['evens'] = even
        mydict['odds'] = odd
        mydict['chars'] = characters
        return mydict

    if not isinstance(listX, list):
        return 'Invalid Input'

    for P in listX:

        if isinstance(P, int):
            if P % 2 == 0:
                even.append(P)

            else:
                odd.append(P)

        elif isinstance(P, str):
            characters.append(P)

    mydict['evens'] = sorted(even)
    mydict['odds'] = sorted(odd)
    mydict['chars'] = sorted(characters)
    return mydict


print(list_sort([4, 5,'a', 7, 8,'d', 9, 11, 12, 'x', 'z', 'y'])) 