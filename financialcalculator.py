import math


class FinancialCalculator:
    beam_tax = 0.19

    def __init__(self):
        pass

    @staticmethod
    def apply_beam_tax(value):
        return value - value*FinancialCalculator.beam_tax

    @staticmethod
    def calculate_savings(deposit, years, rate, include_beam_tax):
        sum = 0
        monthly = [0]
        for x in range(years):
            sum += deposit
            interest = sum*(rate/12)
            #interest = (round(interest*100))/100
            if include_beam_tax:
                interest = FinancialCalculator.apply_beam_tax(interest)
                #interest = (math.ceil(interest * 100))/100
            sum += interest
            monthly.append(sum)
        return monthly

    @staticmethod
    def calculate_investement(money, duration, rate):
        interest = money * (duration*rate/12)
        return {
            "interest": interest,
            "interest_with_beam_tax": FinancialCalculator.apply_beam_tax(interest)
        }

    @staticmethod
    def calculate_interest_saving_time(expected, initial, savings, rate):
        saving_months = 0
        sum = initial
        if initial >= expected:
            not_found = False
        else:
            not_found = True
        while not_found:
            saving_months += 1
            interests = sum*(rate/12)
            interests = FinancialCalculator.apply_beam_tax(interests)
            sum += interests
            if sum >= expected:
                not_found = False
            elif sum+savings >= expected:
                not_found = False
                saving_months += 1
            else:
                sum += savings
        return saving_months

    @staticmethod
    def calculate_installment(loan, duration, rate):
        sum = 0
        factor = 1+(rate/12)
        for x in range(1, duration+1):
            sum += factor**-x
        installment = loan/sum
        return installment


if __name__ == "__main__":
    deposit = input("Tell me your monthly deposit : ")
    years = input("Tell me how long you want to save in years : ")
    rate = input("Tell me the rate of return ( 1% = 0.01 ) : ")
    deposit = int(deposit)
    years = int(years)*12
    rate = float(rate)
    beam_tax = False
    result = FinancialCalculator.calculate_savings(
        deposit, years, rate, beam_tax)
    for x in range(years):
        result[x-1] = (round(result[x-1]*100))/100
    print("After " + str(years/12) + " years you will have " +
          str(result[years]) + " zl ( excluding beam_tax's tax )")
    beam_tax = True
    result = FinancialCalculator.calculate_savings(
        deposit, months, rate, beam_tax)
    for value in result:
        rounded_result.append(round(value, 2))
    print(rounded_result)
    #print("After " + str(months/12) + " years you will have " +      str(result[months]) + " zl ( including beam_tax's tax )")
    #print(f'After {months/12} years you will have {rounded_result[months]} zł (including beam tax)')

    money = input("Tell me how much money you can deposit : ")
    duration = input("Tell me how long the deposit will be ( in months ): ")
    returnrate = input("Tell me the yearly rate of return ( 1% = 0.01 ): ")
    money = int(money)
    duration = int(duration)
    returnrate = float(returnrate)
    interest = round(FinancialCalculator.calculate_investement(
        money, duration, returnrate), 2)
    print(f'Interest after substracting beam tax will be {interest} zl')

    expected = input("Tell me how much you want to have : ")
    initial = input("Tell me how much you can invest initially : ")
    savings = input("Tell me how much you can save every month : ")
    rate_of_return = input("Tell me yearly rate of return ( 1% = 0.01 ) : ")
    expected = int(expected)
    initial = int(initial)
    savings = int(savings)
    rate_of_return = float(rate_of_return)
    saving_duration = FinancialCalculator.calculate_interest(
        expected, initial, savings, rate_of_return)
    if saving_duration == 0:
        print("You already have expected amount of money")
    else:
        print(f'You will need to save for {saving_duration} months')
    loan = input("Tell me how much you want to loan : ")
    duration = input("Tell me how long ( in months ) loan will be : ")
    rate = input("Tell me rate of loan ( 1% = 0.01 ) : ")
    loan = int(loan)
    duration = int(duration)
    rate = float(rate)
    installment = FinancialCalculator.calculate_installment(
        loan, duration, rate)
    installment = round(installment, 2)
    print(f'Monthly installment will be {installment} zl')
    '''
    amount = input("Tell me how many loans you want to connect : ")
    amount  = int(amount)
    suma = 0
    kredyt = 0 
    for x in range (amount):
        loan = input("Tell me how much you want to loan : ")
        duration = input("Tell me how long ( in months ) loan will be : ")
        rate = input("Tell me rate of loan ( 1% = 0.01 ) : ")
        loan = int(loan)
        kredyt += loan
        duration = int(duration)
        rate = float(rate)
        suma += FinancialCalculator.calculate_installment(loan , duration, rate)
        suma = round(suma,2)
    duration = input("Tell me how long ( in months ) consolidation loan will be : ")
    rate = input("Tell me rate of consolidation loan ( 1% = 0.01 ) : ")
    duration = int(duration)
    rate = float(rate)
    #suma = suma/duration
    #suma = round(suma,2)
    result = FinancialCalculator.calculate_installment(kredyt, duration, rate)
    result = round(result,2)
    print (f'Monthly installment of consolidation loan will be {result} zl')
    suma -= result
    suma = round(suma,2)
    print (f'Monthly installment will be lower by {suma} zl')
    '''
