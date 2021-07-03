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
        loan = float(request.form['loan'])
        duration = int(request.form['duration'])
        rate = float(request.form['rate'])
        response = FC.calculate_investement(loan, duration, rate)
        return render_template('investement.html', response=response)
    return render_template('investement.html')


@app.route('/savings', methods=['GET', 'POST'])
def display_savings_calculator():
    if request.method == "POST":
        deposit = float(request.form['deposit'])
        period = int(request.form['period'])
        rate = float(request.form['rate'])
        response = FC.calculate_savings(deposit, period, rate, include_beam_tax=True)
        return render_template('savings.html', response=response)
    return render_template('savings.html')


@app.route('/interest', methods=['GET', 'POST'])
def display_interest_calculator():
    if request.method == "POST":
        expected = float(request.form['expected'])
        initial = float(request.form['initial'])
        savings = float(request.form['savings'])
        rate = float(request.form['rate'])
        response = FC.calculate_interest_saving_time(expected, initial, savings, rate)
        return render_template('interest.html', response=response)
    return render_template('interest.html')


@app.route('/credit', methods=['GET', 'POST'])
def display_credit_calculator():
    if request.method == "POST":
        loan = float(request.form['loan'])
        duration = int(request.form['duration'])
        rate = float(request.form['rate'])
        response = FC.calculate_installment(loan, duration, rate)
        return render_template('credit.html', response=response)
    return render_template('credit.html')

'''
@app.route('/rrso', methods=['GET', 'POST'])
def display_rrso_calculator():
    if request.method == "POST":
        response = ''
        return render_template('rrso.html', response=response)
    return render_template('rrso.html')
'''
if __name__ == "__main__":
    app.run()
