from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
app= Flask(__name__)
app.config['SQLAlchemy_DATABAS_URI']='mysql://scott:tiger@localhost/mydatabase'
db = SQLAlchemy(app)

db= SQLAlchemy(app)

class  Example(db.Model):
	__table__name='example'
	id = db.Column('id',db.Integer,primary_key=True)
	data= db.Column('data',db.Unicode)

		