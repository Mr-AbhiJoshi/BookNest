from main import app, db
from flask import render_template,redirect,url_for, flash
from main.models import User, Book, Author, Genre, Review, Category, UserBook 
from main.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user
import random

@app.route("/")
@app.route("/cover")
def cover_page():
    return render_template('cover.html', navbar='alternate')

@app.route("/home")
@login_required
def home_page():
    random_num = random.randint(1,20)
    top_book = Book.query.get(random_num)
    categories = Category.query.all()
    continue_reading = UserBook.query.filter_by(user_id=current_user.id, is_reading=True).all()
    return render_template('home.html', categories=categories, continue_reading=continue_reading, top_book=top_book)

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

@app.route('/account')
def account_page():
    return render_template('account.html', user=current_user)

@app.route('/start-reading/<int:book_id>', methods=['POST'])
@login_required
def start_reading(book_id):
    user_book = UserBook.query.filter_by(user_id=current_user.id, book_id=book_id).first()
    if user_book:
        user_book.is_reading = True
    else:
        user_book = UserBook(user_id=current_user.id, book_id=book_id)
        db.session.add(user_book)
    db.session.commit()
    return redirect(url_for('homepage'))

@app.route('/preview/<int:book_id>')
def preview_page(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('preview.html', book=book)

@app.route('/read/<int:book_id>')
def read_book(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('preview.html', book=book)

@app.route('/review/<int:book_id>')
def review_book(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('preview.html', book=book)