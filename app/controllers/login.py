from flask import url_for, redirect, render_template, flash, g, session, request
from app import app
# from app.models import User
# from app.models import getUserData

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'juanklg' or request.form['password'] != 'admin':
			error = 'Invalid credentials'
			return render_template('login.html', error=error,data={'webapp':'login'})
		else:
			session['username'] = request.form['username']
			return redirect(url_for('apk'))
	else:
		return render_template('login.html', data={'error':error,'webapp':'login'})

@app.route('/logout')
def logout():
    session.pop('username', None)
    print('que paso vamos ahi')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	error = None
	if request.method == 'POST':
		# flash('usuario registrado de forma exitosa')
		return redirect(url_for('login'))
	else:
		return render_template('register.html',data={'webapp':'register'})