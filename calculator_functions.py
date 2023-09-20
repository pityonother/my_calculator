
def Add(value1,value2):
    return value1+value2

def Substract(value1,value2):
    return value1-value2

def Times(value1,value2):
    return value1*value2

def Divide(value1,value2):
    if value2==0:
        return '除数不能为0'
    return value1/value2

def IsOperator(value):
    if value == '+' or value == '-' or value == '*' or value=='/':
        return True
    else:
        return False
def CalculatorPath(value1,value2,operator):
    if operator=='+':
        result=Add(value1,value2)
        return result
    elif operator=='-':
        result=Substract(value1,value2)
        return result
    elif operator=='*':
        result=Times(value1,value2)
        return result
    elif operator=='-':
        result=Divide(value1,value2)
        return result
def CreateOSList(message):
    Operatorlist =[]
    SeparateValueList =[]
    for value in process_message:
        if IsOperator(value):
            Operatorlist.append(value)
            SeparateValueList.append('/')
        else:
            SeparateValueList.append(value)
    return Operatorlist,SeparateValueList


def GenerateLastValue(TempValueList):
    TempValueList.append(SeparateValue)
    TempValue = TempValueList[0]
    for SigelValue in TempValueList[1:]:
        TempValue = TempValue + SigelValue
        TempValueList.clear()
    FinalList.append(TempValue)
    return FinalList

def ValueMoreThanOne(TempValueList,OperatorListIndex):
        TempValue = TempValueList[0]
        for SigelValue in TempValueList[1:]:
            TempValue = TempValue + SigelValue
        TempValueList.clear()
        FinalList.append(TempValue)
        FinalList.append(Operatorlist[OperatorlistIndex])
def ValueEqualsToOne(TempValueList):
    TempValue = TempValueList[0]
    TempValueList.clear()
    FinalList.append(TempValue)
    FinalList.append(Operatorlist[OperatorlistIndex])

message = input()
process_message = list(message)
Operatorlist, SeparateValueList = CreateOSList(message)
TempValueList = []
OperatorlistIndex = 0
SeparateValueListindex = 0
FinalList = []
for SeparateValue in SeparateValueList:
    if SeparateValueListindex==len(SeparateValueList)-1:
        GenerateLastValue(TempValueList)
    else:
        if SeparateValue=='/':
            if len(TempValueList) > 1:
                ValueMoreThanOne(TempValueList,OperatorlistIndex)
                OperatorlistIndex+=1
                SeparateValueListindex+=1
            elif len(TempValueList)==1:
                ValueEqualsToOne(TempValueList)
                OperatorlistIndex+=1
                SeparateValueListindex+=1
        else:
            TempValueList.append(SeparateValue)
            SeparateValueListindex+=1
print(FinalList)



















