from flask import Flask, render_template
app = Flask(__name__, template_folder='template')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/team")
def team():
    return render_template("team.html")

app.run(debug=True, use_reloader = False)

