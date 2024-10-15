from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'vibecheck.db'


def query_db(query):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    res = cur.execute(query)
    result = res.fetchall()
    con.close()
    return result


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    message = "Hello world"
    return render_template("intro.html", msg=message)


@app.route('/get/patients', methods=['GET'])
def get_patients():
    rows = query_db("SELECT * FROM patients")
    print(rows)
    return rows


@app.route('/add/patient', methods=['POST'])
def add_patient():
    content = request.get_json(silent=True)
    return jsonify(content)


if __name__ == "__main__":
    app.run(debug=True)

# endpoint to add patient to DB
# endpoint to delete patient from DB
# endpoint to get patients from DB
# endpoint to modify patient data based on given data in DB
# endpoint to send a questionnaire to all users where the current date matches the contactDate
