from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('Base.html')


@app.route('/market')
def market_page():
    items: list[dict] = [
        {'name': 'Product 1',
         'description': 'This is a great product that you will love. It has excellent features and is available at an amazing price.',
         'price': 20},

        {'name': 'Product 2',
         'description': 'This is a great product that you will love. It has excellent features and is available at an amazing price.',
         'price': 50},

        {'name': 'Product 3',
         'description': 'This is a great product that you will love. It has excellent features and is available at an amazing price.',
         'price': 150}
    ]
    return render_template('Market.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)