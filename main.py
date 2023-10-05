

def generateRatio(list1, list2):
    ratioList = []
    for i in range(len(list1)):
        ratioList.append(list2[i] / list1[i])
    return ratioList


def sortDict(keyList, valueList):
    for i in range(len(keyList)):
        for j in range(0, len(keyList)-i-1):
            if valueList[j] < valueList[j+1]:
                valueList[j], valueList[j+1] = valueList[j+1], valueList[j]
                keyList[j], keyList[j+1] = keyList[j+1], keyList[j]
                
    sortedDict = {}
    for i in range(len(keyList)):
        sortedDict.update({keyList[i] : valueList[i]})
    return sortedDict


def generateDict(priceList, ratioList):
    priceDict = {}
    for i in range(len(priceList)):
        priceDict.update({priceList[i] : ratioList[i]})
    
    return priceDict
    





# def stockPicker(budget, ratioList, stockPrices):
#     for i in range(len(ratioList)):
#         if (budget - st)
#     return 0






companies  = ["GOOGL", "MSFT", "IBM", "HPQ", "ORCL", "META", "TSLA"]
stockPrice = [134.98, 323.23, 150.03, 27.22, 113.38, 300.65, 265.51]
projection = [5.18, 0.45, 5.43, -13.06, -2.68, 3.75, 14.62]

price2projection = generateRatio(stockPrice, projection)
pdict = generateDict(stockPrice,price2projection)

values = pdict.values()

print(values[0])


# print(pdict)
# print(" ")

# print(pdict.values())
# print(sortDict(pdict.keys(), pdict.values()))