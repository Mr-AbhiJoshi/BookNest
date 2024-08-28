from main import app, db
from flask import render_template,redirect,url_for, flash
from main.models import User, Book, Author, Genre, Review 
from main.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required


@app.route("/")
@app.route("/cover")
def cover_page():
    return render_template('cover.html', navbar='alternate')

@app.route("/home")
@login_required
def home_page():
    return render_template('home.html')

@app.route('/register',methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        email=form.email_address.data,
                        password=form.password1.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash(f'Account created successfully! You are now logged in as: {new_user.username.capitalize()}', category='success')
        return redirect(url_for('home_page'))
	
    if form.errors != {}:
        for err_msgs in form.errors.values():
            for err_msg in err_msgs:
                flash(err_msg, category='danger')

    return render_template('register.html', form=form, navbar='alternate')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Login successful! You are logged in as: {attempted_user.username.capitalize()}', category='success')
            return redirect(url_for('home_page'))
        else:
            flash(f'Login unsuccessful!', category='danger')

    return render_template('login.html', form = form, navbar='alternate')

@app.route('/logout')
def logout_page():
	logout_user()
	flash("You have been logged out!", category='info')
	return redirect( url_for("login_page"))
