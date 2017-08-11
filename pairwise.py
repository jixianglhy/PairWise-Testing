item1 = ['value1','value2','value3']
item2 = ['shu1','shu2','shu3']
item3 = ['ka1','ka2','ka3']
item4 = ['ma1','ma2','ma3','ma4']
cases = []
count=1


for each in item1:
    x = each
    for each in item2:
        y = each
        for each in item3:
            z = each
            for each in item4:
                case = count,x,y,each
                cases.append(case)
                count += 1
            
print(cases)
