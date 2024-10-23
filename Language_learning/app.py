from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# قائمة الكلمات
words = []

@app.route('/')
def index():
    return render_template('index.html', words=words)

@app.route('/add', methods=['POST'])
def add():
    word = request.form.get('word')
    translation = request.form.get('translation')
    if word and translation:
        words.append({'word': word, 'translation': translation})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
