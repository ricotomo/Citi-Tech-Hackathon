import sqlite3
from flask import Flask, render_template, redirect, url_for, request, g
app = Flask(__name__)

conn = sqlite3.connect('database.db')
print ("Opened database successfully")
#use SQLite implicit rowid primary key instead of creating our own
conn.execute('CREATE TABLE IF NOT EXISTS isastudent1 (firstname TEXT, lastname TEXT, tuition TEXT, major TEXT, college TEXT, degree TEXT, verification INTEGER, package INTEGER, gender INTEGER, momed TEXT, daded TEXT, parusa INTEGER, granusa INTEGER, pol TEXT, msg TXT)')
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
      print("tuition from form is " + firstname)
      lastname = request.form.get('lastname')
      print("tuition from form is " + lastname)
      tuition = request.form.get('tuition')
      print("tuition from form is " + tuition)
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
        cur.execute("INSERT INTO isastudent1 (firstname, lastname, tuition, college, major, degree, verification, package, gender, momed, daded, parusa, granusa, pol, msg) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(firstname, lastname, tuition, college, major, degree, verification, package, gender, momed, daded, parusa, granusa, pol, msg) )
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
