from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_session import Session
import logging

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configure server-side session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/input', methods=['POST'])
def input():
    if 'input' not in session:
        session['input'] = ''
    session['input'] += request.form['value']
    app.logger.debug(f"Button clicked - new input: {session['input']}")
    return redirect(url_for('index'))


@app.route('/clear')
def clear():
    session.pop('input', None)
    session.pop('result', None)
    app.logger.debug("Session cleared")
    return redirect(url_for('index'))


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    try:
        result = eval(expression)
        return jsonify(result=result)
    except ZeroDivisionError:
        return jsonify(result='Error: Division by zero')
    except Exception as e:
        return jsonify(result=f'Error: {e}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
