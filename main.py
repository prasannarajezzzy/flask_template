from flask import Flask ,render_template,request
from datetime import datetime
app= Flask(__name__)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)#mysql://scott:tiger@localhost/mydatabase
#://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://goku:123456@127.0.0.1/codingthunder"
# ye syntax highlight q nai hua
app.config['SQLALCHEMY_ECHO'] = True

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder'
db = SQLAlchemy(app)


# haa ye hi
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.Integer, nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    reg_date = db.Column(db.String(12), nullable=True)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/contact',methods = ['GET','POST'])
def contact():

	a=[]
	if  (request.method=='POST'):
		print("here")
		name=request.form.get('name')
		email=request.form.get('email')
		phone=int(request.form.get('phone'))
		message=request.form.get('message')
		a.append([name,email,phone,message])
		print(phone)


		print(a)

		entry = Contacts(name=name, phone_num = phone, msg = message,email = email,reg_date= datetime.now())
		print(entry.name)
		# ye print horha he kya haaa
		db.session.add(entry)
		db.session.commit()
		print("ok")
	return render_template("contact.html",data=a)
'''
        db.session.add(entry)
        db.session.commit()

'''
	



@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/post')
def post():
	return render_template("post.html")




app.run(debug=True)

