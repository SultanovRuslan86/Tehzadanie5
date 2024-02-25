from flask import Flask, render_template, url_for, request, redirect
import requests

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone_number = request.form.get('phone_number')
    global already_submitted
    already_submitted = already_submitted if 'already_submitted' in globals() else set()

    # Проверка номера телефона
    if not validate_phone_number(phone_number):
        return render_template('error.html', message='Неверный формат ввода данных')

    # Проверка на повтор
    if (name, phone_number) in already_submitted:
        return render_template('error.html', message='You have already submitted this form')
    else:
        already_submitted.add((name, phone_number))

    if validate_phone_number(phone_number):
        return redirect(url_for('success'))

    payload = {'name': name, 'phone_number': phone_number, 'hidden_field': 'test'}
    response = requests.post('https://order.drcash.sh/v1/order', data=payload)

    if response.status_code == 200:
        return redirect(url_for('success'))
    else:
        return render_template('error.html', message='Error submitting form')

def validate_phone_number(phone_number):
    if not phone_number:
        return False
    return True


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == "__main__":
    app.run(debug=True)
