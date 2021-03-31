class FinancialCalculator: 
    def __init__(self):
        pass

    @staticmethod
    def calculate_consistent_savings_no_belko_tax(deposit, years, rate, beam_tax=False):
        sum = 0
        for x in range (0, years):
            sum += deposit
            sum *= (1+rate/12)
        return sum


if __name__ == "__main__":
    deposit=input("Tell me your monthly deposit : ")
    years=input("Tell me how long you want to save in years : ")
    rate=input("Tell me the rate of return ( 1% = 0.01 ) : ")
    deposit = int(deposit)
    years=int(years)*12
    rate=float(rate)
    result =FinancialCalculator.calculate_consistent_savings_no_belko_tax(deposit, years, rate)*100
    result =(round(result))/100
    print("After " + str(years/12) + " years you will have "+ str(result) + " zl ( excluding Belko's tax )")
