from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'xhwbx7623bxuiwex[d3d3]3d3d3d5r'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'studenten_presentie'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/studenten')
def studenten():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM studenten")
    data = cur.fetchall()
    cur.close()

    return render_template('studenten.html', students=data)


@app.route('/new_student', methods=['POST'])
def new_student():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        student_nr = request.form['student_nr']
        voornaam = request.form['voornaam']
        achternaam = request.form['achternaam']
        cohort = request.form['cohort']
        leerjaar = request.form['leerjaar']
        studierichting = request.form['studierichting']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO studenten (student_nr, voornaam, achternaam, cohort, leerjaar, studierichting) VALUES (%s, %s, %s, %s, %s, %s)", (student_nr, voornaam, achternaam, cohort, leerjaar, studierichting))
        mysql.connection.commit()
        return redirect(url_for('studenten'))


@app.route('/delete_student/<string:student_nr>', methods=['GET'])
def delete_student(student_nr):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM studenten WHERE student_nr=%s", (student_nr,))
    mysql.connection.commit()
    return redirect(url_for('studenten'))


@app.route('/update_student', methods=['POST', 'GET'])
def update_student():
    if request.method == 'POST':
        student_nr = request.form['student_nr']
        voornaam = request.form['voornaam']
        achternaam = request.form['achternaam']
        cohort = request.form['cohort']
        leerjaar = request.form['leerjaar']
        studierichting = request.form['studierichting']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE studenten
               SET student_nr=%s, voornaam=%s, achternaam=%s, cohort=%s, leerjaar=%s, studierichting=%s
               WHERE student_nr=%s
            """, (student_nr, voornaam, achternaam, cohort, leerjaar, studierichting, student_nr))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('studenten'))


if __name__ == "__main__":
    app.run(debug=True)
