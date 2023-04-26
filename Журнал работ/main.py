from data import db_session
from data.jobs import Jobs
from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/data.db")
    app.run(port=8080, host='127.0.0.1')


@app.route('/')
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


if __name__ == '__main__':
    main()


