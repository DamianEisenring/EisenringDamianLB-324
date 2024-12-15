from flask import Flask, render_template, request
from helper import greet_user, calculate_sum

app = Flask(__name__)

@app.route('/')
def home():
    # Benutzer begrüßen und die Webseite anzeigen
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    # Den Namen des Benutzers von der HTML-Seite abholen und begrüßen
    user_name = request.form['name']
    greeting_message = greet_user(user_name)
    return render_template('index.html', greeting=greeting_message)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    # Berechnet die Summe zweier Zahlen, die vom Benutzer eingegeben wurden
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = calculate_sum(num1, num2)
    return render_template('index.html', sum_result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

