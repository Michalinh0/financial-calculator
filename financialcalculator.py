import math

class FinancialCalculator: 
    def __init__(self):
        pass

    @staticmethod
    def calculate_consistent_savings(deposit, years, rate, belko):
        sum = 0
        monthly = [0]
        for x in range (years):
            sum += deposit
            interest = sum*(rate/12)
            #interest = (round(interest*100))/100
            if belko == True : 
                interest *= 0.81
                #interest = (math.ceil(interest * 100))/100
            sum += interest
            monthly.append(sum)
        return monthly


if __name__ == "__main__":
    deposit=input("Tell me your monthly deposit : ")
    years=input("Tell me how long you want to save in years : ")
    rate=input("Tell me the rate of return ( 1% = 0.01 ) : ")
    deposit = int(deposit)
    years=int(years)*12
    rate=float(rate)
    belko = False
    result =FinancialCalculator.calculate_consistent_savings(deposit, years, rate, belko)
    for x in range (years):
        result[x-1]=(round(result[x-1]*100))/100 
    print("After " + str(years/12) + " years you will have "+ str(result[years]) + " zl ( excluding Belko's tax )")
    belko = True
    result = FinancialCalculator.calculate_consistent_savings(deposit, years, rate, belko)
    for x in range (years):
        result[x-1]=(round(result[x-1]*100))/100 
    print("After " + str(years/12) + " years you will have "+ str(result[years]) + " zl ( including Belko's tax )")


