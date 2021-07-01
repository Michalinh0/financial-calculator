import math


class FinancialCalculator:
    beam_tax = 0.19

    def __init__(self):
        pass

    @staticmethod
    def apply_beam_tax(value):
        return value - value*FinancialCalculator.beam_tax

    @staticmethod
    def calculate_savings(deposit, months, rate, include_beam_tax):
        """Calculate how much you save after given time in months, annual interest rate"""
        sum = 0
        monthly = [0]
        for x in range(months):
            sum += deposit
            interest = sum*(rate*0.01/12)
            #interest = (round(interest*100))/100
            if include_beam_tax:
                interest = FinancialCalculator.apply_beam_tax(interest)
                #interest = (math.ceil(interest * 100))/100
            sum += interest
            monthly.append(sum)
        return monthly

    @staticmethod
    def calculate_investement(money, duration, rate):
        sum = money
        for x in range(duration):
            interest = sum*(rate/12*0.01)
            sum += interest
        sum -=money
        return {
            "interest": sum,
            "interest_with_beam_tax": FinancialCalculator.apply_beam_tax(sum)
        }

    @staticmethod
    def calculate_interest_saving_time(expected, initial, savings, rate):
        """Calculate the number of months needed to save given amount of money."""
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
        """Calculate an installment for a given loan."""
        sum = 0
        factor = 1+(rate/12)
        for x in range(1, duration+1):
            sum += factor**-x
        installment = loan/sum
        return installment
