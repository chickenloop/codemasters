def comp(array1, array2):
    sqlist = []
    final = []
    mysum = 0
    print(array1)
    print(array2)

    if array1 and array2 != None:
        if len(array1)==0 and len(array2)==0:
            return True
        else:
            if (len(array1) != len(array2)):
                return False
            else:
                for x in array1:
                    if x*x in array2:
                        final.append("True")
                    else:
                        final.append("False")
                if "False" in final:
                    return False
                else:
                    for x in array1:
                        mysum = mysum + x * x
                    if mysum != sum(array2):
                        return False
                    else:
                        return True
    else:
        return False