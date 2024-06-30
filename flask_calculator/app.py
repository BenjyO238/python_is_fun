from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['POST'])
def input():
    if 'input' not in session:
        session['input'] = ''
    session['input'] += request.form['value']
    return redirect(url_for('index'))

@app.route('/clear')
def clear():
    session.pop('input', None)
    session.pop('result', None)
    return redirect(url_for('index'))

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = session.get('input', '')
    try:
        result = eval(expression)
    except ZeroDivisionError:
        result = 'Error: Division by zero'
    except Exception as e:
        result = f'Error: {e}'
    session['result'] = result
    session.pop('input', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
