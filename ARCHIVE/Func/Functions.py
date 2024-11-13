#IMPORTS CURRENCY CONVERTER
from currency_converter import CurrencyConverter
c = CurrencyConverter()

def CurrencyRequest(input):
    # RETURN DICT
    returnValue = {
        "CURR": [],
        "AMOUNT": [],
        "SORT": input['SORT'],
        "REQ_CURR": input['NOW_CURR'],
        "REQ_AMOUNT": input['AMOUNT'],
        "ADDR": ''
    }
    #TRY TO CONVERT:
    try:

        # PERFORM CALCULATIONS:
        tempDict = {};
        for x in input['REQ_CURR']:
            tempDict.update( {x :c.convert(returnValue['REQ_AMOUNT'], returnValue['REQ_CURR'], x)});

        #SORT DICTIONARY
        #SORT BASED ON CURRENCY
        if(input['SORT'] == 'CURR'):
            keys = list(tempDict.keys())
            keys.sort()
            sortedDict = {i:tempDict[i] for i in keys}

        #SORT BASED ON VALUES:
        elif (input['SORT'] == 'VALUE'):
            sortedDict = {k: v for k, v in sorted(tempDict.items(), key=lambda item: item[1])}

        #NO SORT
        else:
            sortedDict = tempDict

        #FILL IN RETURN DICT WITH SORTED VALUES:
        returnValue['AMOUNT'] = list(sortedDict.values())
        returnValue['CURR'] = list(sortedDict.keys())


    #ERROR HANDLING IF IT CAN'T FIGURE IT OUT JUST RETURN EMPTY:
    except:
        returnValue = {
            "CURR": [],
            "AMOUNT": [],
            "SORT": input['SORT'],
            "REQ_CURR": input['NOW_CURR'],
            "REQ_AMOUNT": input['AMOUNT'],
            "ADDR": ''
        }
    #RETURN THE CALCULATION
    return returnValue