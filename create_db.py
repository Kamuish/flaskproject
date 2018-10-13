from flask import url_for
from flaskproject import create_app, db, mail
from flaskproject.models import User, Game
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
def pw_hash(passw):
	return bcrypt.generate_password_hash(passw).decode('utf-8')


def create():
	app = create_app()
	app.app_context().push()
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

	bcrypt.init_app(app)
	db.create_all()

	user = User(username='teste', email='teste@gmail.com', password=pw_hash('aaaa'))
	user1 = User(username='teste1', email='teste1@gmail.com', password= pw_hash('aaaa'))
	game = Game(name='test', password='1')

	db.session.add(user)
	db.session.add(user1)
	db.session.add(game)

	game.players.append(user)
	game.players.append(user1)

	db.session.commit()

create()