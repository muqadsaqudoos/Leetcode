
def calPoints(operations):
    record = []
    for i in range(len(operations)):
       
        if operations[i] == "+":
            record.append(record[-1]+record[-2])
        elif operations[i] == "D":
            record.append(record[-1]*2)
        elif operations[i] == "C":
            record.pop()
        else:
            record.append(int (operations[i]))
    output = 0
    for i in range(len(record)):
        output += record[i]
    return output

ops = ["5","2","C","D","+"]
print(calPoints(ops))
