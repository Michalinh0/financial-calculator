from flask import Flask, render_template, redirect, request
from financialcalculator import FinancialCalculator as FC
app = Flask(__name__)
app.config.update(
    TEMPLATES_AUTO_RELOAD=True,
    debug=True
)


@app.route('/')
def display_main_page():
    return redirect('/consistent-savings')


@app.route('/consistent-savings')
def display_consistent_savings():
    page_name = 'consistent-savings'
    return render_template('consistent_savings.html')


@app.route('/consistent-savings/calculate', methods=['GET', 'POST'])
def calculate_consistent_savings():
    if request.method == "POST":
        deposit = float(request.form['deposit'])
        period = int(request.form['period'])
        rate = float(request.form['rate'])
        result = FC.calculate_consistent_savings(deposit, period, rate, True)
        print(result)

    return redirect('/consistent-savings')

if __name__ == "__main__":
    app.run()


