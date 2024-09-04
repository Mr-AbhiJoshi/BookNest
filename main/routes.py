from main import app, db
from flask import render_template, request, redirect,url_for, flash
from main.models import User, Book, Author, Genre, Review, Category, UserBook 
from main.forms import RegisterForm, LoginForm, EditProfileForm, ReviewForm
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.orm import joinedload
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

@app.route('/account/<int:user_id>')
def account_page(user_id):
    user = User.query.get(user_id)
    reviews = Review.query.filter_by(user_id=user.id).order_by(Review.created_at.desc()).all()
    return render_template('account.html', user=user, reviews=reviews)

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
    reviews = Review.query.filter_by(book_id=book_id).options(joinedload(Review.user)).order_by(Review.created_at.desc()).all()
    return render_template('preview.html', book=book, reviews=reviews)

@app.route('/read/<int:book_id>')
def read_book(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('preview.html', book=book)

@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        current_user.icon = form.icon.data
        
        if form.password1.data and form.password2.data:
            if form.password1.data == form.password2.data:
                current_user.password_hash = form.password1.data
            else:
                flash('Passwords do not match!', category='danger')
                return redirect(url_for('edit_profile'))
            
        db.session.commit()
        flash('Your profile has been updated!', category='success')
        return redirect(url_for('account_page', user_id=current_user.id))

    # Prepopulate the form with the current user's data
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.bio.data = current_user.bio
        form.icon.data = current_user.icon

    return render_template('edit_profile.html', form=form, navbar='alternate')

@app.route('/profile/delete', methods=['POST'])
@login_required
def delete_profile():
    user_id = current_user.id
    db.session.delete(current_user)
    db.session.commit()
    flash('Your profile has been deleted.', category='success')
    return redirect(url_for('register_page'))

@app.route('/review/<int:book_id>', methods=['GET', 'POST'])
@login_required
def review_book(book_id):
    form = ReviewForm()
    book = Book.query.get_or_404(book_id)  # Ensure the book exists

    if form.validate_on_submit():
        new_review = Review(
            user_id=current_user.id,
            book_id=book_id,
            rating=form.rating.data,
            review_text=form.review_text.data
        )
        db.session.add(new_review)
        db.session.commit()
        flash('Your review has been submitted!', 'success')
        return redirect(url_for('preview_page', book_id=book_id))

    return render_template('review.html', form=form, book=book)

@app.route('/review/delete/<int:review_id>', methods=['POST'])
@login_required
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    flash('Your review has been deleted.', category='success')
    return redirect(url_for('home_page'))