from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Настройки Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Замените на адрес SMTP-сервера
app.config['MAIL_PORT'] = 587  # Порт SMTP
app.config['MAIL_USE_TLS'] = True  # Использовать TLS (True/False)
app.config['MAIL_USE_SSL'] = False  # Использовать SSL (True/False)
app.config['MAIL_USERNAME'] = 'sulaimanovuran@gmail.com'  # Ваше имя пользователя
app.config['MAIL_PASSWORD'] = 'cbpcsgueufapmjph'  # Ваш пароль
app.config['MAIL_DEFAULT_SENDER'] = ('Your MOM', 'sulaimanovuran@gmail.com')  # Замените на ваши данные

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/bid')
def bid():
    return render_template('bid.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    recipient = request.form['tite']
    subject = request.form['intro']
    message_body = request.form['text']

    message = Message(subject=subject, recipients=[recipient])
    message.body = message_body

    try:
        mail.send(message)  # Отправляем письмо
        return "Письмо успешно отправлено!"
    except Exception as e:
        return f"Ошибка при отправке письма: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)