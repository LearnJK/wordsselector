# from flask import url_for, redirect, render_template, flash, g, session
from flask import url_for, redirect, render_template, flash, g, session, request
from app import app
# from app.models import User
from app.models import getUserData	


@app.route('/app',methods=['post','get'])
def apk():
	if 'username' in session:
		data=getUserData(session["username"])
		data['username'] = session["username"]
		if request.method == 'get':
			return  render_template('app.html',data=data)
		else:
			return  render_template('app.html',data=data)
	else:
		return redirect(url_for('login'))

@app.route('/')
def index():
	if 'username' in session:
		return redirect(url_for('apk'))
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'juanklg' or request.form['password'] != 'admin':
			error = 'Invalid credentials'
			return render_template('login.html', error=error)
		else:
			session['username'] = request.form['username']
			flash('Inicio exitoso')
			return redirect(url_for('apk'))
	else:
		return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
	error = None
	if request.method == 'POST':
		flash('usuario registrado de forma exitosa')
		return redirect(url_for('login'))
	else:
		return render_template('register.html',error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# @app.route('/new/')
# @login_required
# def new():
# 	form = ExampleForm()
# 	return render_template('new.html', form=form)


# @app.route('/save/', methods = ['GET','POST'])
# def save():
# 	form = ExampleForm()
# 	if form.validate_on_submit():
# 		print("salvando os dados:")
# 		print(form.title.data)
# 		print(form.content.data)
# 		print(form.date.data)
# 		flash('Dados salvos!')
# 	return render_template('new.html', form=form)

# @app.route('/view/<id>/')
# def view(id):
# 	return render_template('view.html')

# # === User login methods ===

# @app.before_request
# def before_request():
#     g.user = current_user

# @lm.user_loader
# def load_user(id):
#     return User.query.get(int(id))

# @app.route('/login/', methods = ['GET', 'POST'])
# def login():
#     if g.user is not None and g.user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         login_user(g.user)

#     return render_template('login.html', 
#         title = 'Sign In',
#         form = form)



# ====================
