from flask import Flask,render_template,request,url_for,redirect,session
from models.model import user_exists,save_user

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/')
def home():
    return render_template('home.html',title='home')

@app.route('/about')
def about():
    return render_template('about.html',title='about')

@app.route('/contact')
def contact():

    return render_template('contact.html')

@app.route('/signup',methods=['POST','GET'])
def signup():

	if request.method == 'POST':

		user_info={}

		user_info['username'] = request.form['username']
		user_info['password'] = request.form['password1']
		password2 = request.form['password2']
		user_info['c_type'] = request.form['type']
		if user_info['c_type']=='buyer':
			user_info['cart']=[]

		if user_exists(user_info['username']):
			return "user already exists. Enter another username"
		if user_info['password']!=password2:
			return "passwords don't match. Try again"

		save_user(user_info)
		session['username']=user_info['username']
		session['type']=user_info['c_type']
		return redirect(url_for('home'))

	return redirect(url_for('home'))

@app.route('/login',methods=['POST','GET'])
def login():

	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		

		if user['username'] == username:
			if user['password'] == password:
				session['username']=user['username']
				session['type']=c_type
				return redirect(url_for('home'))
			return "password doesn't match"
		return "username doesn't match"
	return redirect(url_for('home'))	

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('home'))


app.run(debug=True)
