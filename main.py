from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import smtplib

app = Flask(__name__)

# Настройки Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Замените на адрес SMTP-сервера
app.config['MAIL_PORT'] = 587  # Порт SMTP
app.config['MAIL_USE_TLS'] = True  # Использовать TLS (True/False)
app.config['MAIL_USE_SSL'] = False  # Использовать SSL (True/False)
app.config['MAIL_USERNAME'] = 'sulaimanovuran@gmail.com'  # Ваше имя пользователя
app.config['MAIL_PASSWORD'] = 'cbpcsgueufapmjph'  # Ваш пароль
app.config['MAIL_DEFAULT_SENDER'] = ('Заявка на получение услуг', 'sulaimanovuran@gmail.com')  # Замените на ваши данные
app.config['SECRET_KEY'] = 'kjdahfjehfuiwejhf83479ur0384943-7582930yr9hwepi'

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


@app.route('/send_email', methods=['POST', 'GET'])
def send_email():
    print("hello")
    company_name = request.form['name']
    email = request.form['mail']
    
    phone_number = request.form['phone']
    message = Message(subject=f'Заявка на получение услуг от {company_name}', recipients=['redline.marketing.kg@gmail.com'])
    message.body = f'Адрес электронной почты {email}.\nНомер телефона: {phone_number}'

    try:
        mail.send(message)  # Отправляем письмо
        flash('Заявка отправлена', category='success')
    except Exception as e:
        flash('Ошибка отправки сообщения', category='error')
    return render_template('bid.html')

if __name__ == '__main__':
    app.run(debug=True)