item1 = ['推荐排序','价格升序','价格降序','好评优先']
item2 = ['不限','二星及以下','两种星级','3种星级星',]
item3 = ['不限','酒店','两种类型','3中类型','4种类型','5种类型']
item4 = ['不限','silom','2个地址','3个地址']
cases = []
count=0
combinations = []
ifmove = True 
x,y,z,w = '','','',''

if item1 != []:
    for each in item1:
        x = each
        for each in item2:
            y = each
            if item3 == []:
                case = count,x,y
                cases.append(case)
                count += 1
                continue
            else:
                for each in item3:
                    z  = each
                    if item4 == []:
                        case = count,x,y,z
                        cases.append(case)
                        count += 1
                        continue
                    else:
                        for each in item4:
                            case = count,x,y,z,w
                            cases.append(case)
                            count += 1 
print(cases)
print(len(cases))

combinationnumber = 0
while combinationnumber < (count-1):
    ifmove = True
    for i in range(1,len(cases[1])):
        j = i+1
        while j<len(cases[1]):
            #print(cases[combinationnumber][i]+cases[combinationnumber][j])
            if (cases[combinationnumber][i]+cases[combinationnumber][j]) in combinations:
                break
            else:
                ifmove = False
                for x in range(1,len(cases[1])):
                    y = x+1     
                    while y<len(cases[1]):
                        combinations.append(cases[combinationnumber][x]+cases[combinationnumber][y])
                        y += 1
                           
            j += 1
    if ifmove == True:
        cases.remove(cases[combinationnumber])
        combinationnumber -= 1
        count -= 1
        
    combinationnumber += 1
print(cases)
print(len(cases))


        
