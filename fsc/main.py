from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post():
	total=0		
	if request.method=="POST":	
		if request.form['Submit']=='Confirm':
			parts = dbHandler.Fetchparts()
			one=request.form.getlist('prefer')
			return render_template('bill.html',parts=parts,prefer=one,total=0)
		if request.form['Submit']=='Delete':
			username=request.form['selected']
			print (username)
			dbHandler.deleteUser(username)
			users=dbHandler.retrieveUsers()
			return render_template('admin.html',users=users)
		if request.form['Submit']=='Return':
			return render_template('index.html')	
	else:
		return render_template('index.html')
@app.route('/', methods=['GET'])
def get():
	login=1
	exists=0	
	username = request.args.get('username')
	password = request.args.get('password')
	Submit = request.args.get('Submit')
	if Submit=='Log In':
		users = dbHandler.CompareUsers(username, password)
		if users:
			parts = dbHandler.Fetchparts()
			return render_template('services.html',users=users,login=1,parts=parts)
		else:
			return render_template('index.html',users=users,login=0)
	
	if Submit=='Sign Up':
		login=0
		users = dbHandler.CompareUsers(username, password)
		if users:
			exists=1
		if exists==0:
			dbHandler.insertUser(username, password)
			users = dbHandler.CompareUsers(username, password)
			return render_template('index.html',users=users,login=0)
		if exists==1:
			return render_template('index.html',users=users,login=0,exists=1)
	if Submit == 'Admin':
		check = dbHandler.CompareAdmins(username, password)
		if check:
			users=dbHandler.retrieveUsers()
			return render_template('admin.html',users=users)
		else:
			return render_template('index.html',users=check,login=0)	
	else:
		return render_template('index.html')
		
if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0')
