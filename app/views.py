# from flask import url_for, redirect, render_template, flash, g, session
from flask import url_for, redirect, render_template, flash, g, session, request
from app import app
# from app.models import User
from app.models import getUserData

@app.route('/app',methods=['get'])
def apk():
	if 'username' in session:
		data=getUserData(session["username"])
		args = dict(request.args)
		if 'app' in args: 
			app = args['app']
			data['app'] = app
		else: app = data['app']
		if request.method == 'get':
			return  render_template(f'{app}.html',data=data)
		else:
			return  render_template(f'{app}.html',data=data)
	else:
		return redirect(url_for('login'))

@app.route('/')
def index():	
	return redirect(url_for('apk'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'juanklg' or request.form['password'] != 'admin':
			error = 'Invalid credentials'
			return render_template('login.html', error=error)
		else:
			session['username'] = request.form['username']
			return redirect(url_for('apk'))
	else:
		return render_template('login.html', data={'error':error})

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

@app.route('/<param>', methods=['GET','POST'])
def html(param=None):
	if request.method == 'POST':
		print(request.form)
	else:
		if 'username' in session:
			return redirect(url_for('apk',app=param))
		else:
			return render_template('app.html',	data={'app':'MakerDream'})

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
