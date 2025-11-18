def main():
    conAmount = int(input("How much money would you like to convert? £"))
    conCurrency = input("What currency would you like to convert too?\nUSD\nEUR\nBRL\nJPY\nTRY\n")
    staff = input("Are you a staff memeber [Yes/No]? ")
    staff = staff.lower()
    conCurrency = conCurrency.lower()

    if(staff == "yes"):
        isStaff = True
    else:
        isStaff = False

    if(conCurrency == "usd"):
        currency = 1.40
    elif(conCurrency == "eur"):
        currency = 1.14
    elif(conCurrency == "brl"):
        currency = 4.77
    elif(conCurrency == "jpy"):
        currency = 151.05
    else:
        currency = 5.68


    return conAmount, currency, isStaff

def convert():
    conAmount, currency, isStaff = main()
    fee = 0

    if(conAmount > 2500):
        print("The value you have entered is too much. Maximum conversion is £2500")
        return
    
    if(conAmount >= 300):
        fee = conAmount * 0.035
    elif(conAmount >= 750):
        fee = conAmount * 0.03
    elif(conAmount >= 1000):
        fee = conAmount * 0.025
    elif(conAmount >= 2000):
        fee = conAmount * 0.02
    else:
        fee = conAmount * 0.015

    transaction = conAmount * currency

    discount = "0%"
    fee = conAmount + fee
    if(isStaff):
        discountFee = fee*0.05
        fee = fee - discountFee
        discount = "5%"
    
    print("You are converting £" + str(format(conAmount, '.2f')), "to", format(transaction, '.2f'), "of your selected currency for £" + str(format(fee, '.2f')), "with a discount of", discount, "\n")

while(True):
    convert()