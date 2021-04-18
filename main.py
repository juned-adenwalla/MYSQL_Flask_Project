from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "myusers"

mysql = MySQL(app)


@app.route("/",methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (fullname,phone) VALUES (%s,%s)", (name, phone))

        mysql.connection.commit()
        cur.close()
        return "success"

    return render_template("index.html")

@app.route("/data",methods = ['GET','POST'])
def collect():
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT * FROM users")
    if users > 0:
        userDetails = cur.fetchall()

    return render_template("data.html", userDetails = userDetails)

if __name__ == "__main__":
    app.run(debug=True)