import math


class FinancialCalculator:
    beam_tax = 0.19

    def __init__(self):
        pass

    @staticmethod
    def apply_beam_tax(value):
        return value - value*FinancialCalculator.beam_tax

    @staticmethod
    def calculate_consistent_savings(deposit, months, rate, include_beam_tax):
        sum = 0
        monthly = [0]
        for x in range(months):
            sum += deposit
            interest = sum*(rate/12)
            #interest = (round(interest*100))/100
            if include_beam_tax:
                interest = FinancialCalculator.apply_beam_tax(interest)
                #interest = (math.ceil(interest * 100))/100
            sum += interest
            monthly.append(sum)
        return monthly


if __name__ == "__main__":
    deposit = input("Tell me your monthly deposit : ")
    months = input("Tell me how long you want to save in years : ")
    rate = input("Tell me the rate of return ( 1% = 0.01 ) : ")
    deposit = int(deposit)
    months = int(months)*12
    rate = float(rate)
    beam_tax = False

    result = FinancialCalculator.calculate_consistent_savings(
        deposit, months, rate, beam_tax)
    rounded_result = []
    for value in result:
        rounded_result.append(round(value, 2))

    for x in range(months):
        result[x-1] = (round(result[x-1]*100))/100
#    print("After " + str(months/12) + " years you will have " +      str(result[months]) + " zl ( excluding beam_tax's tax )")
    #print(f'After {months/12} years you will have {rounded_result[months]} zł (excluding beam tax)')
    print(rounded_result)
    rounded_result = []
    beam_tax = True
    result = FinancialCalculator.calculate_consistent_savings(
        deposit, months, rate, beam_tax)
    for value in result:
        rounded_result.append(round(value, 2))
    print(rounded_result)
    #print("After " + str(months/12) + " years you will have " +      str(result[months]) + " zl ( including beam_tax's tax )")
    #print(f'After {months/12} years you will have {rounded_result[months]} zł (including beam tax)')
