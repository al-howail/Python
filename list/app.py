from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    item = request.form.get('item')
    if item:
        items.append(item)
    return redirect(url_for('index'))

@app.route('/delete/<item>')
def delete(item):
    if item in items:
        items.remove(item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
