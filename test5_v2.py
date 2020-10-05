def comp(array1, array2):
    sqlist = []
    final = []
    mysum = 0

    if array1 and array2 != None:
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
                for z in array1:
                    mysum = mysum + z * z
                if mysum != sum(array2):
                    return False
                else:
                    return True
    else:
        if array1==[] and array2==[]:
            return True
        else:
            return False

a=[]
b=[]
print(comp(a,b))