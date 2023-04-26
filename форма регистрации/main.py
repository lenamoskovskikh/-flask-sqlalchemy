from data import db_session
from data.users import User
from data.jobs import Jobs
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, EmailField, TextAreaField, BooleanField
from wtforms.validators import DataRequired



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class RegisterForm(FlaskForm):
    login = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname')
    name = StringField('Name')
    age = StringField('Age')
    position = StringField('Position')
    speciality = StringField('Speciality')
    address = StringField('Address')
    submit = SubmitField('Sign up')



def main():
    db_session.global_init("db/data.db")
    app.run(port=8080, host='127.0.0.1')

@app.route('/index')
def table():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    res = []
    for el in jobs:
        time = f'{round((el.end_date - el.start_date).total_seconds() / 3600)} hours'
        team_leader = el.user.name + ' ' + el.user.surname
        res = [el.job, team_leader, time, el.collaborators, el.is_finished]
    return render_template('works.html', jobs=res)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.confirm.data:
            return render_template('register.html', title='Registration',
                                   form=form,
                                   message="Passwords don't match")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.login.data).first():
            return render_template('register.html', title='Registration',
                                   form=form,
                                   message="This user already exists")
        user = User(
            name=form.name.data,
            email=form.login.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/ok')
    return render_template('register.html', title='Registration', form=form)

@app.route('/ok')
def ok():
    return render_template('ok.html')





if __name__ == '__main__':
    main()
    app.run(port=8080, host='127.0.0.1')
