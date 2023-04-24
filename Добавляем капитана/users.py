from user import User
import datetime
import sqlalchemy


user = User()
user.name = "Ridley"
user.surname = "Scott"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"

user1 = User()
user1.name = "Ruby"
user1.surname = "Scott"
user1.age = 25
user1.position = "captain"
user1.speciality = "engineer"
user1.address = "module_1"
user1.email = "ruby_main@mail.org"

user2 = User()
user2.name = "Harry"
user2.surname = "Potter"
user2.age = 19
user2.position = "team_leader"
user2.speciality = "biologist"
user2.address = "module_1"
user2.email = "harry123@gmail.com"

user3 = User()
user3.name = "Maria"
user3.surname = "Jane"
user3.age = 24
user3.position = "captain"
user3.speciality = "programmer"
user3.address = "module_1"
user3.email = "maria_j@gmail.ru"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()
db_sess.add(user1)
db_sess.commit()
db_sess.add(user2)
db_sess.commit()
db_sess.add(user3)
db_sess.commit()





