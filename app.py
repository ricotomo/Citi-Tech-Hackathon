import sqlite3
from flask import Flask, render_template, redirect, url_for, request, g

app = Flask(__name__)

conn = sqlite3.connect('database.db')
print ("Opened database successfully")
#use SQLite implicit rowid primary key instead of creating our own
conn.execute('CREATE TABLE IF NOT EXISTS isastudent2 (firstname TEXT, lastname TEXT, tuition TEXT, dipged TEXT, college TEXT, major TEXT, degree TEXT, verification INTEGER, package INTEGER, gender TEXT, momed TEXT, daded TEXT, sibs TEXT, family16 TEXT, parusa TEXT, granusa TEXT, pol TEXT, msg TXT)')
print ("Table created successfully")
conn.close()

@app.route("/", methods = ['GET'])
def hello():
  print("Handling request to home page.")
  return render_template('student_homepage.html')

@app.route('/investor_landing',methods = ['GET'])
def investor_landing():
   if request.method == 'GET':
      return render_template('investor_logged.html')
   else:
      return render_template('student_homepage.html')

@app.route('/ISA_form',methods = ['POST','GET'])
def ISA_form():
  if request.method == 'GET':
    return render_template('ISA_form.html')
  elif request.method=='POST':
    print("HTTP POST handler")
    try:
      print("enter try for DB connection")
      firstname = request.form.get('firstname')
      print("firstname from form is " + firstname)
      lastname = request.form.get('lastname')
      print("lastname from form is " + lastname)
      tuition = request.form.get('tuition')
      print("tuition from form is " + tuition)
      dipged = request.form.get('dipged')
      print("dipged from form is " + dipged)
      college = request.form.get('college')
      print("college from form is " + college)
      major = request.form.get('major')
      print("major from form is " + major)
      degree = request.form.get('degree')
      print("degree from form is " + degree)
      verification = request.form.get('verification')
      print("ver from form is " + verification)
      package = request.form.get('package')
      print("package from form is " + package)
      gender = request.form.get('gender')
      print("gender from form is " + gender)
      momed = request.form.get('momed')
      print("momed from form is " + momed)
      daded = request.form.get('daded')
      print("daded from form is " + daded)
      sibs = request.form.get('sibs')
      print("sibs from form is " + sibs)
      family16 = request.form.get('family16')
      print("family16 from form is " + family16)
      parusa = request.form.get('parusa')
      print("parusa from form is " + parusa)
      granusa = request.form.get('granusa')
      print("granusa from form is " + granusa)
      pol = request.form.get('pol')
      print("politics from form is " + pol)
      msg = request.form.get('msg')
      print("degree from form is " + msg)
      #print message for testing purposes. Does not work! Causes an exception!
      #print("testing form elements " + firstname + " " + lastname + " " + tuition + " " + college + " " +major + " " +degree + " " +verification + " " +package + " " +gender + " " +momed + " " +daded + " " +parusa + " " +granusa + " " +pol + " " +msg)
      with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO isastudent2 (firstname, lastname, tuition, dipged, college, major, degree, verification, package, gender, momed, daded, sibs, family16, parusa, granusa, pol, msg) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(firstname, lastname, tuition, dipged, college, major, degree, verification, package, gender, momed, daded, sibs, family16, parusa, granusa, pol, msg) )
        con.commit()
        print("record successfully added to DB")
    except:
      con.rollback()
      print("exception")
    finally:
      print("entered finally block")
      return render_template('student_homepage.html')
      con.close()
  else:
    return render_template('student_homepage.html')

if __name__ == "__main__":
  app.run()
