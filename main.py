# Backend for PAD CTF level Medium
# This file is owned by Team D

from flask import Flask, redirect, request, make_response, render_template

app = Flask(__name__, template_folder='templates')


# This is used to redirect / to /login
@app.route('/')
def index():
    response = make_response(redirect("/login", code=303))
    return response


# This is used for the homepage / login page
@app.route('/login', methods=['GET', 'POST'])
def home():
    return render_template("home.html")


# This is used to expose the admin endpoint
# If the cookie is set to admin or Admin, we will allow access
# Otherwise return You are not admin.
@app.route('/admin', methods=['GET'])
def admin():
    return "You are not admin!"


# This part is responsible for resetting the challenge
@app.route('/reset')
@app.route('/logout')
def logout():
    response = make_response(redirect("/login", code=303))
    response.set_cookie("auth_name", "")
    return response


if __name__ == '__main__':
    app.secret_key = 'kApe8XDc5oe0F2HlHRWkN0'
    # Debug allows us to detect changes and updates it
    app.run(debug=True, host="0.0.0.0", port=3000)
