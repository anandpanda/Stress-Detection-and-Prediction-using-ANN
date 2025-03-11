from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user
from app.models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully!', 'success')

            # Redirect to the next page if available
            next_page = request.form.get('next')
            if next_page and next_page.startswith('/'):  # Ensure the next page is a valid URL
                return redirect(next_page)
            else:
                return redirect(url_for('main.home'))  # Default redirect
        else:
            flash('Invalid email or password.', 'error')

    # Pass the next parameter to the template
    next_page = request.args.get('next')
    return render_template('login.html', next=next_page)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        next_page = request.form.get('next')  # Get the next parameter from the form

        # Check if user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists!', 'error')
            return redirect(url_for('auth.signup'))

        # Hash the password
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Create a new user
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Log in the new user
        login_user(new_user)

        flash('Registration successful! You are now logged in.', 'success')

        # Redirect to the next page if available
        return redirect(next_page or url_for('main.home'))

    # Pass the next parameter to the template
    next_page = request.args.get('next')
    return render_template('signup.html', next=next_page)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('main.home'))