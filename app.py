from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from flask_mysqldb import MySQL
import pdfkit


app = Flask(__name__)
app.secret_key = 'xhwbx7623bxuiwex[d3d3]3d3d3d5r'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'studenten_presentie'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

searched = False

path_wkthmltopdf = r'C:\Python\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

# Presentie page
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT
        id,
        studenten.voornaam,
        studenten.achternaam,
        studenten.student_nr,
        vakken.vak_code,
        vakken.naam,
        presentie,
        blok,
        datum
        FROM
        presenties
        INNER JOIN studenten ON studenten.student_nr = presenties.student_nr
        INNER JOIN vakken ON vakken.vak_code = presenties.vak_code
        ORDER BY datum
    """)
    joinData = cur.fetchall()

    cur.execute(""" 
        Select * from studenten
    """)
    studenten = cur.fetchall()

    cur.execute(""" 
        Select * from vakken
    """)
    vakken = cur.fetchall()
    cur.close()

    searched = False

    return render_template('index.html', presenties=joinData, studenten=studenten, vakken=vakken, searched=searched)


@app.route('/new_presentie', methods=['POST'])
def new_presentie():
    if request.method == "POST":
        student = request.form['student']
        vak = request.form['vak']
        presentie = request.form['presentie']
        blok = request.form['blok']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO presenties (student_nr, vak_code, presentie, blok) VALUES (%s, %s, %s, %s)", (student, vak, presentie, blok))
        mysql.connection.commit()
        flash("Presentie is toegevoegd!")
        return redirect(url_for('index'))


@app.route('/delete_presentie/<string:id>', methods=['GET'])
def delete_presentie(id):
    flash("Presentie is verwijderd!")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM presenties WHERE id=%s", (id))
    mysql.connection.commit()
    return redirect(url_for('index'))


@app.route('/update_presentie', methods=['POST', 'GET'])
def update_presentie():
    if request.method == 'POST':
        id = request.form['id']
        student_nr = request.form['student']
        vak_code = request.form['vak']
        presentie = request.form['presentie']
        blok = request.form['blok']
        datum = request.form['datum']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE presenties
            SET student_nr=%s, vak_code=%s, presentie=%s, blok=%s, datum=%s
            WHERE id=%s
            """, (student_nr, vak_code, presentie, blok, datum, id))
        flash("Presentie is bijgewerkt!")
        mysql.connection.commit()
        return redirect(url_for('index'))


@app.route('/search_presentie', methods=['POST', 'GETS'])
def search_presentie():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT
        id,
        studenten.voornaam,
        studenten.achternaam,
        studenten.student_nr,
        vakken.vak_code,
        vakken.naam,
        presentie,
        blok,
        datum
        FROM
        presenties
        INNER JOIN studenten ON studenten.student_nr = presenties.student_nr
        INNER JOIN vakken ON vakken.vak_code = presenties.vak_code
        ORDER BY datum
    """)
    joinData = cur.fetchall()

    cur.execute(""" 
        Select * from studenten
    """)
    studenten = cur.fetchall()

    cur.execute(""" 
        Select * from vakken
    """)
    vakken = cur.fetchall()
    # cur.close()

    if request.method == 'POST':
        search = request.form['search_presentie']

        cur.execute("""
        SELECT
        id,
        studenten.voornaam,
        studenten.achternaam,
        studenten.student_nr,
        vakken.vak_code,
        vakken.naam,
        presentie,
        blok,
        datum
        FROM
        presenties
        INNER JOIN studenten ON studenten.student_nr = presenties.student_nr
        INNER JOIN vakken ON vakken.vak_code = presenties.vak_code
        WHERE id LIKE %s OR
        studenten.voornaam LIKE %s OR
        studenten.achternaam LIKE %s OR
        studenten.student_nr LIKE %s OR
        vakken.vak_code LIKE %s OR
        vakken.naam LIKE %s OR
        presentie LIKE %s OR
        blok LIKE %s OR
        datum LIKE %s
        ORDER BY datum
        """, ([search, search, search, search, search, search, search, search, search]))
        mysql.connection.commit()
        data = cur.fetchall()
        cur.close()

        searched = True

        return render_template('index.html', presenties=joinData, studenten=studenten, vakken=vakken, search_data=data, searched=searched, term=search)


@app.route('/presentie_pdf')
def presentie_pdf():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT
        id,
        studenten.voornaam,
        studenten.achternaam,
        studenten.student_nr,
        vakken.vak_code,
        vakken.naam,
        presentie,
        blok,
        datum
        FROM
        presenties
        INNER JOIN studenten ON studenten.student_nr = presenties.student_nr
        INNER JOIN vakken ON vakken.vak_code = presenties.vak_code
        ORDER BY datum
    """)
    presenties = cur.fetchall()
    cur.close()

    rendered = render_template(
        'presenties_pdf_html.html', presenties=presenties)
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=presenties.pdf'

    return response

# Student page
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
        flash("Student " + achternaam + " is toegevoegd!")
        return redirect(url_for('studenten'))


@app.route('/delete_student/<string:student_nr>', methods=['GET'])
def delete_student(student_nr):
    flash("De student is verwijderd!")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM studenten WHERE student_nr=%s", (student_nr,))
    mysql.connection.commit()
    return redirect(url_for('studenten'))


@app.route('/update_student', methods=['POST', 'GET'])
def update_student():
    if request.method == 'POST':
        old_student_nr = request.form['id']
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
            """, (student_nr, voornaam, achternaam, cohort, leerjaar, studierichting, old_student_nr))
        flash("Student " + achternaam + " is bijgewerkt!")
        mysql.connection.commit()
        return redirect(url_for('studenten'))

# Vakken page
@app.route('/vakken')
def vakken():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM vakken")
    data = cur.fetchall()
    cur.close()

    return render_template('vakken.html', vakken=data)


@app.route('/new_vak', methods=['POST'])
def new_vak():
    if request.method == "POST":
        vak_code = request.form['vak_code']
        naam = request.form['naam']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO vakken (vak_code, naam) VALUES (%s, %s)", (vak_code, naam))
        mysql.connection.commit()
        flash("Vak " + naam + " is toegevoegd!")
        return redirect(url_for('vakken'))


@app.route('/delete_vak/<string:vak_code>', methods=['GET'])
def delete_vak(vak_code):
    flash("Het vak is verwijderd!")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM vakken WHERE vak_code=%s", (vak_code))
    mysql.connection.commit()
    return redirect(url_for('vakken'))


@app.route('/update_vak', methods=['POST', 'GET'])
def update_vak():
    if request.method == 'POST':
        old_vak_code = request.form['id']
        vak_code = request.form['vak_code']
        naam = request.form['naam']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE vakken
            SET vak_code=%s, naam=%s
            WHERE vak_code=%s
            """, (vak_code, naam, old_vak_code))
        flash("Vak " + naam + " is bijgewerkt!")
        mysql.connection.commit()
        return redirect(url_for('vakken'))


if __name__ == "__main__":
    app.run(debug=True)
