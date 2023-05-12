from flask import Flask, render_template, request

app = Flask(__name__)

state_codes = {
    "UT": "Utah",
    "NV": "Nevada",
    "TX": "Texas",
    "AL": "Alabama",
    "CA": "California"
}

tax_rates = {
    "Utah": 0.0685,
    "Nevada": 0.08,
    "Texas": 0.0625,
    "Alabama": 0.04,
    "California": 0.0825
}

def calculate_discounted_amount(quantity, price, state):
    amount = quantity * price
    discount = 0

    if amount >= 50000:
        discount = 0.15
    elif amount >= 10000:
        discount = 0.10
    elif amount >= 7000:
        discount = 0.07
    elif amount >= 5000:
        discount = 0.05
    elif amount >= 1000:
        discount = 0.03

    discounted_amount = amount - (amount * discount)

    tax = discounted_amount * tax_rates[state]
    total_amount = discounted_amount + tax

    return total_amount

@app.route('/')
def index():
    return render_template('index.html', state_codes=state_codes)

@app.route('/calculate', methods=['POST'])
def calculate():
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    state_code = request.form['state']
    state = state_codes[state_code]

    total_amount = calculate_discounted_amount(quantity, price, state)

    return render_template('result.html', total_amount=total_amount)

if __name__ == '__main__':
    app.run()
