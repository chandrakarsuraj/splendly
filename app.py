import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from database.db import init_db, seed_db, get_db
from werkzeug.security import generate_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-for-spendly")

with app.app_context():
    init_db()
    seed_db()


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if not name or not email or not password:
            flash("All fields are required", "error")
            return render_template("register.html")

        hashed_password = generate_password_hash(password)

        try:
            conn = get_db()
            with conn:
                conn.execute(
                    "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
                    (name, email, hashed_password)
                )
            flash("Account created successfully! Please sign in.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Email already registered", "error")
            return render_template("register.html")
        finally:
            conn.close()

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Mock login for testing Step 4
        session["user_id"] = 1
        session["username"] = "Demo User"
        flash("Logged in successfully!", "success")
        return redirect(url_for("profile"))
    return render_template("login.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")



# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
# ------------------------------------------------------------------ #

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been signed out.", "success")
    return redirect(url_for("landing"))


@app.route("/profile")
def profile():
    if not session.get("user_id"):
        return redirect(url_for("login"))

    # Mock data for Step 4
    user = {
        "name": "Demo User",
        "email": "demo@spendly.com",
        "join_date": "October 2023"
    }
    stats = [
        {"label": "Total Spent", "value": "₹12,450.00"},
        {"label": "Transactions", "value": "42"},
        {"label": "Top Category", "value": "Food"},
    ]
    transactions = [
        {"date": "2023-10-20", "category": "Food", "amount": "₹350.00", "note": "Starbucks Coffee"},
        {"date": "2023-10-19", "category": "Transport", "amount": "₹120.00", "note": "Uber Ride"},
        {"date": "2023-10-18", "category": "Shopping", "amount": "₹2,100.00", "note": "Amazon Order"},
    ]
    categories = [
        {"name": "Food", "percentage": 40, "color": "var(--accent)"},
        {"name": "Transport", "percentage": 25, "color": "var(--accent-2)"},
        {"name": "Shopping", "percentage": 20, "color": "var(--accent)"},
        {"name": "Other", "percentage": 15, "color": "var(--accent-2)"},
    ]

    return render_template("profile.html", user=user, stats=stats, transactions=transactions, categories=categories)


@app.route("/expenses/add")
def add_expense():
    return "Add expense — coming in Step 7"


@app.route("/expenses/<int:id>/edit")
def edit_expense(id):
    return "Edit expense — coming in Step 8"


@app.route("/expenses/<int:id>/delete")
def delete_expense(id):
    return "Delete expense — coming in Step 9"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
