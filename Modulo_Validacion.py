#Validacion del tipo entero
def valInt(*argu):
    if len(argu) == 1:
        if type(argu[0]) == int:
            result = True
        else:
            result= False
    
    if len(argu) == 2:
        if type(argu[1]) != list and type(argu[1]) != tuple:
            raise TypeError
        elif (argu[1][0]>argu[1][1] or (len(argu[1])>2 or len(argu[1])==0)):
            raise ValueError 
        elif type(argu[0]) == int and (type(argu[1]) == list and argu[0]>=argu[1][0] and argu[0]<=argu[1][1] or type(argu[1]) == tuple and argu[0]>argu[1][0] and argu[0]<argu[1][1]):
            result = True
        else:
            result = False
    else:
        raise ValueError
    return result
         


#Validacion de tipo flotantes.
def valFloat(*argu):    
    if len(argu) == 1:
        if type(argu[0]) == float:
            result = True
        else:
            result = False

    if len(argu) == 2:
        if type(argu[1]) != list and type(argu[1]) != tuple:
            raise TypeError
        elif (argu[1][0]>argu[1][1] or (len(argu[1])>2 or len(argu[1])==0)):
            raise ValueError
        elif type(argu[0]) == float and (type(argu[1]) == list and argu[0]>=argu[1][0] and argu[0]<=argu[1][1] or type(argu[1]) == tuple and argu[0]>argu[1][0] and argu[0]<argu[1][1]):
            result = True
        else:
            result = False
    return result

#Validacion de tiplo complejos.
def valComplex(*argu):
    if len(argu) == 1:
        if type(argu[0]) == complex:
            result = True
        else:
            result = False
    elif len(argu) == 2:
        if type(argu[1]) != list and type(argu[1]) != tuple:
            raise TypeError
        elif (argu[1][0]>argu[1][1] or (len(argu[1])>2 or len(argu[1])==0)):
            raise ValueError
        elif type(argu[0]) == complex and (type(argu[1]) == list and abs(argu[0])>=argu[1][0] and abs(argu[0])<=argu[1][1] or type(argu[1]) == tuple and abs(argu[0])>argu[1][0] and argu[0]<argu[1][1]):
            result = True
        else:
            result = False
    return result
 


#Validacion de datos tipo lista.
def valList(*argu):
    if len(argu) == 1:
        if type(argu[0]) == list:
            result = True
        else:
            result = False
    if len(argu) == 3:
        if argu[2] == "value":
            if type(argu[0]) == list and type(argu[1]) == list and argu[0] == argu[1]:
                result = True
            else:
                result = False
        if argu[2] == "len":
            if type(argu[0]) == list and type(argu[1]) == int and len(argu[0]) == argu[1]:
                result = True
            else:
                result = False
        elif (type(argu[1]) != type(6) and type(argu[2]) != type("x")) or (type(argu[1]) != type([7,2]) and type(argu[2]) != type("u")):
            raise TypeError
        elif argu[2]!= ("value" and list):
            raise ValueError
    return result

