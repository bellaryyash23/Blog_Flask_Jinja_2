from flask import Flask, render_template, request
import os
import requests
from smtplib import SMTP

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        connection = SMTP(host="smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=os.environ.get('USERNAME'), password=os.environ.get('PASSWORD'))
        connection.sendmail(from_addr=os.environ.get('USERNAME'),
                            to_addrs=os.environ.get('ADDR'),
                            msg="Subject: New Form Entry \n\n"
                                f"Name: {name},\n"
                                f"E-mail: {email},\n "
                                f"Phone No: {phone},\n "
                                f"Message: {message}")
        print("Message Sent.")
        return render_template("contact.html", message="Successfully sent your message.")
    if request.method == "GET":
        return render_template("contact.html", message="Contact me")


@app.route("/<blog_id>")
def posts(blog_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("post.html", posts=all_posts, post_id=int(blog_id))


if __name__ == "__main__":
    app.run(debug=True)
