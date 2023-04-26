from data.jobs import Jobs
import data.db_session as db_session
from data.users import User
import datetime


jobs = Jobs()
db_session.global_init("db/blogs.db")
db_sess = db_session.create_session()

user = db_sess.query(User).filter(User.position == 'captain').first()
jobs.team_leader = user.id
jobs.job = 'deployment of residential modules 1 and 2'
jobs.work_size = 15
jobs.collaborators = '2, 3'
jobs.start_date = datetime.datetime.now()
jobs.is_finished = False

db_sess.add(jobs)
db_sess.commit()