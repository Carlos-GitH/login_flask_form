from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    email = StringField('Email', [
        DataRequired(), 
        Length(min=6, message=('Email too short')), 
        Email(message=('Invalid email address'))
    ])
    password = PasswordField('Password', [
        DataRequired(message="Field can't be empty"),
        Length(min=8, message=('Password too short'))
        ])
    submit = SubmitField(label='Log In')
    
app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data =='carlos@gmail.com' and login_form.password.data == "12345678":
            print(login_form.email.data)
            print(login_form.password.data)
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', login_form=login_form)
    
if __name__ == '__main__':
    app.run(debug=True)