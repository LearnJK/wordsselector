# from flask import url_for, redirect, render_template, flash, g, session
from flask import url_for, redirect, render_template, flash, g, session, request
from app import app
# from app.models import User
from app.models import user

@app.route('/')
def index():
	return redirect(url_for('apk'))
	return redirect(url_for('ruteo',page='login'))

@app.route('/app',methods=['get'])
def apk():
	args = dict(request.args)
	if 'username' in session:
		data=user.getUserData(session["username"])
		dataApp = data['app']
		webapp = dataApp['nm']
		# por defecto viene organizada la app q mas utiliza el usuario
		page = dataApp['view'][0]
		data['webapp']=webapp
		if 'page' in args: page = args['page']
		print(data)		
		return  render_template(f'{webapp}/{page}.html',data=data)
	else:
		if 'webApp' in args:
			return  render_template(args['webApp']+'/'+args['webApp']+'.html',data={'app':args['webApp']})
		else:
			return redirect(url_for('login'))

@app.route('/<webApp>', methods=['GET','POST'])
def html(webApp=None):
	if request.method == 'POST':
		print('entrada por post de un endpont',request.form)
		return {}
	else:
		if 'username' in session:
			return redirect(url_for('apk',page=webApp))
		else:
			return redirect(url_for('login'))

# usp la app y creo un ruteo pata las paginas
# @app.route("/page/<page>", methods=['GET'])
# def ruteo(page:None):    
#     textoHtml = render_template(f'{page}.html')
#     return textoHtml

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
