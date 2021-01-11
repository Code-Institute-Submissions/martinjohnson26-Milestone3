import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# Environment Variable Setup
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Home page route
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# Display jargon categories and jargons route
@app.route("/get_jargons")
def get_jargons():
    """
    Displays the jargon index(Alphabetical categories) and the
    jargons when the categories are clicked on
    """
    a_e = mongo.db.jargons.find({"jargon_index": "A-E"})
    f_j = mongo.db.jargons.find({"jargon_index": "F-J"})
    k_o = mongo.db.jargons.find({"jargon_index": "K-O"})
    p_t = mongo.db.jargons.find({"jargon_index": "P-T"})
    u_z = mongo.db.jargons.find({"jargon_index": "U-Z"})

    return render_template(
        'jargons.html', A_E=a_e, F_J=f_j, K_O=k_o, P_T=p_t, U_Z=u_z)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    a_e = mongo.db.jargons.find({"$text": {"$search": query}})
    f_j = mongo.db.jargons.find({"$text": {"$search": query}})
    k_o = mongo.db.jargons.find({"$text": {"$search": query}})
    p_t = mongo.db.jargons.find({"$text": {"$search": query}})
    u_z = mongo.db.jargons.find({"$text": {"$search": query}})
    return render_template(
        'jargons.html', A_E=a_e, F_J=f_j, K_O=k_o, P_T=p_t, U_Z=u_z)


# Registration Form route
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Checks to see if username exists in users database,
    adds new users to the users database
    puts new user into a session
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Log in existing user form route
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Checks to see if username exists in database,
    checks users password is valid,
    redirects new users to registration page
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                            request.form.get("username")))
                return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# User Profile route
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    displays the users profile page
    """
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# User log out route
@app.route("/logout")
def logout():
    """
    logs out current user.
    clears session data
    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add jargons route
@app.route("/add_jargon", methods=["GET", "POST"])
def add_jargon():
    """
    gets data from the add jargons forms and adds
    to the jargons database
    """
    if request.method == "POST":
        jargon = {
            "jargon_index": request.form.get("jargon_index"),
            "sport": request.form.get("sport"),
            "jargon_name": request.form.get("jargon_name"),
            "jargon_description": request.form.get("jargon_description"),
            "created_by": session["user"],
            "creation_date": request.form.get("creation_date")
        }
        mongo.db.jargons.insert_one(jargon)
        flash("Jargon Successfully Added")
        return redirect(url_for("get_jargons"))

    jargons_index = mongo.db.jargons_index.find().sort("jargon_index", 1)
    return render_template("add_jargon.html", jargons_index=jargons_index)


# Edit jargons route
@app.route("/edit_jargon/<index>", methods=["GET", "POST"])
def edit_jargon(index):
    """
    gets data from the edit jargons form and updates
    the existing jargon in the jargons database
    """
    if request.method == "POST":
        submit = {
            "jargon_index": request.form.get("jargon_index"),
            "sport": request.form.get("sport"),
            "jargon_name": request.form.get("jargon_name"),
            "jargon_description": request.form.get("jargon_description"),
            "created_by": session["user"],
            "creation_date": request.form.get("creation_date")
        }
        mongo.db.jargons.update({"_id": ObjectId(index)}, submit)
        flash("Jargon Successfully Updated")

    jargon = mongo.db.jargons.find_one({"_id": ObjectId(index)})

    jargons_index = mongo.db.jargons_index.find().sort("jargon_index", 1)
    return render_template(
        "edit_jargon.html", jargon=jargon, jargons_index=jargons_index)


# Delete jargons route
@app.route("/delete_jargon/<index>")
def delete_jargon(index):
    """
    deletes an existing jargon from the jargons database
    """
    mongo.db.jargons.remove({"_id": ObjectId(index)})
    flash("Jargon Successfully Deleted")
    return redirect(url_for("get_jargons"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
