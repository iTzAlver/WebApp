import get_func as gf
import bb_func as bb
import es_func as es
from flask import Flask, render_template, redirect, request, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'ayush'

@app.route('/')
def home():
  return render_template("homepage2.html")

@app.route('/login')
def login():
  return render_template("loginpage3.html")

@app.route('/success',methods = ["POST"])
def success():
	if request.method == "POST":
		[authCode, exitCode] = es.searchLogin(request.form['email'],request.form['pass'])
		if authCode == True:
			session['email'] = request.form['email']
			return render_template('success3.html')
		else:
			printString = "<p>Login inválido, código de error: " + exitCode + "</p>" 
			return printString

@app.route('/logout')
def logout():
	if 'email' in session:
		session.pop('email',None)
		return render_template('logoutpage2.html');
	else:  
		return '<p>user already logged out</p>' 

@app.route('/profile')
def profile():
	if 'email' in session:
		email = session['email']
		data = es.b_usrES(email)
		numero = gf.getRND()
		bb.guardarBB(bb.bclient,email,numero)
		es.guardarES(email,numero)
		nums = data
		avg = 0
		for element in nums:
				avg = avg + element
		avg = avg/len(nums)
		return render_template('profile.html',name=email,nums=nums,avg=avg)
	else:
		return '<p>Please login first</p>'

@app.route('/register')
def register():
	return render_template("register.html")

@app.route('/registerok',methods=["POST"])
def registerok():
	if request.method == "POST":
		if es.storeRegister(request.form['email'], request.form['pass']) == True:
			return render_template('sucess_register.html')
		else:
			return render_template('wrong_register.html')

@app.route('/umbral',methods=["POST"])
def umbral():
	if request.method== "POST":
		if 'email' in session:
			email = session['email']
			data = es.b_usrES(email)
			numero = gf.getRND()
			bb.guardarBB(bb.bclient,email,numero)
			es.guardarES(email,numero)
			nums = data
			avg = 0
			for element in nums:
					avg = avg + element
			avg = avg/len(nums)
			thresh = es.b_thES(email,request.form['number'])
			return render_template('profile.html',name=email,nums=nums,avg=avg,thresh=thresh)
		else:
			return '<p>Please login first</p>'
	else:
			return '<p>Wrong POST.</p>'

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)