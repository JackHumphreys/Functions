

def currency_from():
    currency_from = str(input("Please enter your currency you would like to convert from. Enter either GBP, USD or EUR: "))
    return currency_from

def currency_to():
    currency_to = str(input("Please enter your currency you would like to convert to. Enter either GBP, USD or EUR: "))
    return currency_to

def amount(currencyfrom):
    amount = int(input("Please enter your amount in {0}: ".format(currencyfrom)))
    return amount

def multiplier(currencyto,currencyfrom):
    if currencyfrom == "GBP" and currencyto == "USD":
        multiplier = 1.601
    elif currencyfrom == "GBP" and currencyto == "EUR":
        multiplier = 1.229
    elif currencyfrom == "EUR" and currencyto == "GBP":
        multiplier = 0.814
    elif currencyfrom == "EUR" and currencyto == "USD":
        multiplier = 1.302
    elif currencyfrom == "USD" and currencyto == "GBP":
        multiplier = 0.625
    else:
        multiplier = 0.768
    return multiplier


def conversion(total,mp):
    conversion = total*mp
    return conversion

def display(total,currencyfrom,convert,currencyto):
    print("{0} {1} = {2} {3}".format(total,currencyfrom,convert,currencyto))


def convert_currency():
    currencyfrom = currency_from()
    currencyto = currency_to()
    total = amount(currencyfrom)
    mp = multiplier(currencyto,currencyfrom)
    convert = conversion(total,mp)
    display(total,currencyfrom,convert,currencyto)


convert_currency()
