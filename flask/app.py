from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://testuser:test123@localhost/dvdrental"

db = SQLAlchemy()
db.init_app(app)

@app.route("/")
def index():
    user_data = db.session.execute(text("SELECT * FROM user_names"))
    return render_template("index.html", users=user_data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)