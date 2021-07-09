from flask import Flask, render_template, redirect, request
from financialcalculator import FinancialCalculator as FC
app = Flask(__name__)
app.config.update(
    TEMPLATES_AUTO_RELOAD=True,
    debug4=True
)


@app.route('/')
def display_main_page():
    return redirect('/savings')


@app.route('/investement', methods=['GET', 'POST'])
def display_investement_calculator():
    if request.method == "POST":
        try:
            loan = float(request.form['loan'])
            duration = int(request.form['duration'])
            rate = float(request.form['rate'])
            response = FC.calculate_investement(loan, duration, rate)
            return render_template('investement.html', response=response)
        except:
            return render_template('investement.html', error="Nieprawidłowe dane.")

    return render_template('investement.html')


@app.route('/savings', methods=['GET', 'POST'])
def display_savings_calculator():
    if request.method == "POST":
        try:
            deposit = float(request.form['deposit'])
            period = int(request.form['period'])
            rate = float(request.form['rate'])
            response = FC.calculate_savings(deposit, period, rate, include_beam_tax=True)
            return render_template('savings.html', response=response)
        except:
            return render_template('savings.html', error="Nieprawidłowe dane.")
    return render_template('savings.html')


@app.route('/interest', methods=['GET', 'POST'])
def display_interest_calculator():
    if request.method == "POST":
        try:
            expected = float(request.form['expected'])
            initial = float(request.form['initial'])
            savings = float(request.form['savings'])
            rate = float(request.form['rate'])
            response = FC.calculate_interest_saving_time(expected, initial, savings, rate)
            return render_template('interest.html', response=response)
        except:    
            return render_template('interest.html', error="Nieprawidłowe dane.")
        
    return render_template('interest.html')


@app.route('/credit', methods=['GET', 'POST'])
def display_credit_calculator():
    if request.method == "POST":
        try:
            loan = float(request.form['loan'])
            duration = int(request.form['duration'])
            rate = float(request.form['rate'])
            response = FC.calculate_installment(loan, duration, rate)
            return render_template('credit.html', response=response)
        except:    
            return render_template('credit.html', error="Nieprawidłowe dane.")
    return render_template('credit.html')


@app.route('/loan-cost', methods=['GET', 'POST'])
def display_credit_cost_calculator():
    if request.method == "POST":
        try:
            loan = float(request.form['loan'])
            duration = int(request.form['duration'])
            rate = float(request.form['rate'])
            commission = float(request.form['commission'])
            other_costs = float(request.form['other_costs'])

            response = FC.calculate_cost_of_loan(loan, duration, rate, commission, other_costs)
            return render_template('loan_cost.html', response=response)
        except Exception as e:
            return render_template('loan_cost.html', error="Nieprawidłowe dane.")
    return render_template('loan_cost.html')


if __name__ == "__main__":
    app.run()
