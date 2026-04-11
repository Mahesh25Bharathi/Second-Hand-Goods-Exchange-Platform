from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = 'simple_key_for_lab'

# In-memory storage
users = {}  # {user_id: password}
products = [
    {'name': 'Phone', 'price': 500},
    {'name': 'Laptop', 'price': 800},
    {'name': 'Chair', 'price': 50}
]
messages = []  # list of {'from': name, 'to': name, 'msg': text}

@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', products=products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        if user_id in users:
            flash('User already exists!')
            return render_template('register.html')
        users[user_id] = password
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        if user_id in users and users[user_id] == password:
            session['user_id'] = user_id
            flash('Login successful!')
            return redirect(url_for('home'))
        flash('Invalid credentials!')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully.')
    return redirect(url_for('login'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    results = products
    if request.method == 'POST':
        query = request.form['query'].lower()
        results = [p for p in products if query in p['name'].lower()]
    return render_template('search.html', results=results, query=request.form.get('query', '') if request.method == 'POST' else '')

@app.route('/addproduct', methods=['GET', 'POST'])
def add_product():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        products.append({'name': name, 'price': price})
        flash('Product added successfully!')
        return redirect(url_for('home'))
    return render_template('add_product.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_name = session['user_id']
    if request.method == 'POST':
        to_user = request.form['to_user']
        msg = request.form['message']
        messages.append({'from': user_name, 'to': to_user, 'msg': msg})
    return render_template('chat.html', messages=messages, user_name=user_name)

if __name__ == '__main__':
    app.run(debug=True)
