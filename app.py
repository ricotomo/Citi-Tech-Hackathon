import sqlite3, dataset
from flask import Flask, render_template, flash, redirect, url_for, request, jsonify, make_response
import numpy as np
import pickle
import sklearn
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True


conn = sqlite3.connect('database.db')
print ("Opened database successfully")
#use SQLite implicit rowid primary key instead of creating our own
conn.execute('CREATE TABLE IF NOT EXISTS isastudent2 (firstname TEXT, lastname TEXT, tuition TEXT, dipged TEXT, college TEXT, major TEXT, degree TEXT, verification INTEGER, package INTEGER, gender TEXT, momed TEXT, daded TEXT, sibs TEXT, family16 TEXT, parusa TEXT, granusa TEXT, pol TEXT, msg TXT)')
print ("Table created successfully")
conn.close()

#Getting the model
with open("model_pickle", "rb") as f:
  model = pickle.load(f)


@app.route("/", methods = ['GET'])
def hello():
  print("Handling request to home page.")
  return render_template('student_homepage.html')


#API to retrieve one students info
@app.route("/api/student", methods = [ 'GET'])
def getastudent():
  lastname = request.args.get("lastname")
  print(lastname)
  if request.method == 'GET':
    with sqlite3.connect("database.db") as con:
      cur = con.cursor()
      cur.execute("SELECT * FROM isastudent1  WHERE lastname is (?)", (lastname,))
      student_obj = cur.fetchall()
      print("working on api/student GET...")
      student_obj.append("test (guinea pig)")
      print(student_obj)
      print("first element in object is " +student_obj[0][1])
    if student_obj:
      return make_response(jsonify(student_obj), 200)
    else:
      return make_response(jsonify(student_obj), 404)
  else:
    return render_template('student_homepage.html')
        


@app.route('/investor_landing',methods = ['POST', 'GET'])
def investor_landing():
   if request.method == 'GET':
      return render_template('investor_logged.html')
   elif request.method=='POST':
      college = request.form.get('college')
      print("college from form is " + college)
      major = request.form.get('major')
      print("major from form is " + major) 
      with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        if(college == "Select your future college" and major != 'Select your future major'):
          cur.execute("SELECT * FROM isastudent2  WHERE major is (?)", (major,))
        elif(college != "Select your future college" and major == 'Select your future major'):
          cur.execute("SELECT * FROM isastudent2  WHERE college is (?)", (college,))
        else:
          cur.execute("SELECT * FROM isastudent2  WHERE college is (?) AND major is (?)", (college, major,))
        
        items = cur.fetchall()
        item_list=[]
        for item in items: 
          firstname = item[0]
          lastname = item[1]
          tuition = item[2]
          diploma = item[3] 
          college = item[4]
          major = item[5]
          degree = item[6]
          verification = item[7]
          package = item[8]
          gender = item[9]
          momed = item[10]
          daded = item[11]
          sibs = item[12]
          guardian = item[13] 
          parusa = item[14]
          granusa = item[15] 
          pol = item[16]
          msg = item[17]
          prediction = return_prediction(sibs, degree, daded, momed, gender, major, diploma, guardian, parusa, granusa, pol)
          roi = return_ROI(prediction, item[2])
          
          item_list.append((firstname, lastname, tuition,  diploma, college, major, degree, verification, package, gender, momed, daded, sibs, guardian, parusa, granusa, pol, msg, roi))

          print(roi)
          print(item)
        print("working...")
        for item in item_list:
            print(item)
        cur.execute("SELECT * FROM isastudent2")
        #allstudents = cur.fetchall()
        #items = make_response(jsonify(items), 200)
        #items = jsonify(items)
      #return render_template('printresults.html', items=items)
      return render_template('investor_logged.html', items=item_list)

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
      print("message from form is " + msg)
      #print message for testing purposes. Does not work! Causes an exception!
      #print("testing form elements " + firstname + " " + lastname + " " + tuition + " " + college + " " +major + " " +degree + " " +verification + " " +package + " " +gender + " " +momed + " " +daded + " " +parusa + " " +granusa + " " +pol + " " +msg)
      with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO isastudent2 (firstname, lastname, tuition, dipged, college, major, degree, verification, package, gender, momed, daded, sibs, family16, parusa, granusa, pol, msg) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(firstname, lastname, tuition, dipged, college, major, degree, verification, package, gender, momed, daded, sibs, family16, parusa, granusa, pol, msg) )
        con.commit()
        print("record successfully added to DB")
        # cur.execute("SELECT * FROM isastudent1")
        # items = cur.fetchall()
        # for item in items:
        #     print(item)
    except:
      con.rollback()
      print("exception")
    finally:
      print("entered finally block")
      return render_template('student_homepage.html')
      con.close()
  else:
    return render_template('student_homepage.html')



#Handling request
def get_input(sibs, degree, daded, momed, gender, major, diploma, guardian, parusa, granusa, pol):
  input_array = np.array([[sibs, degree, daded, momed, gender, major, diploma, guardian, parusa, granusa, pol, np.nan]])
  return pd.DataFrame(input_array, columns=['SIBS', 'DEGREE', 'PADEG', 'MADEG', 'SEX', 'MAJOR1', 'DIPGED', 'FAMILY16', 'PARBORN', 'GRANBORN', 'POLVIEWS', 'INCOME'])


def return_prediction(sibs, degree, daded, momed, gender, major, diploma, guardian, parusa, granusa, pol):
  user_input = get_input(sibs, degree, daded, momed, gender, major, diploma, guardian, parusa, granusa, pol)
  data = pd.read_csv("raw_final.csv")
  user_input = get_input(sibs, degree, daded, momed, gender, major, diploma, guardian, parusa, granusa, pol)
  data = data.append(user_input)

  data_final = pd.get_dummies(data.drop(columns=["SIBS", "INCOME"]))
  data_final["SIBS"] = data["SIBS"]

  data_final = data_final[['SIBS', 'DEGREE_BACHELOR', 'DEGREE_GRADUATE', 'DEGREE_HIGH SCHOOL', 'DEGREE_JUNIOR COLLEGE',
                           'PADEG_BACHELOR', 'PADEG_GRADUATE', 'PADEG_HIGH SCHOOL', 'PADEG_JUNIOR COLLEGE', 'PADEG_LT HIGH SCHOOL',
                           'MADEG_BACHELOR', 'MADEG_GRADUATE', 'MADEG_HIGH SCHOOL', 'MADEG_JUNIOR COLLEGE', 'MADEG_LT HIGH SCHOOL',
                           'SEX_FEMALE', 'SEX_MALE', 'MAJOR1_ACCOUNTING/BOOKKEEPING', 'MAJOR1_ADVERTISING', 'MAJOR1_AGRICULTURE/HORTICULTURE',
                           'MAJOR1_ALLIED HEALTH', 'MAJOR1_ANTHROPOLGY', 'MAJOR1_ARCHITECTURE', 'MAJOR1_ART',
                           'MAJOR1_Administrative Science/Public Administration', 'MAJOR1_Aviation/Aeronatics', 'MAJOR1_BIOLOGY',
                           'MAJOR1_BUSINESS ADMINISTRATION', 'MAJOR1_CHEMISTRY', 'MAJOR1_COMM. DISORDERS', 'MAJOR1_COMMUNICATIONS/SPEECH',
                           'MAJOR1_COMPUTER SCIENCE', 'MAJOR1_Child/Human/Family Development', 'MAJOR1_Counseling',
                           'MAJOR1_Criminology/Criminal Justice', 'MAJOR1_DENTISTRY', 'MAJOR1_Dance', 'MAJOR1_ECONOMICS',
                           'MAJOR1_EDUCATION', 'MAJOR1_ENGINEERING', 'MAJOR1_ENGLISH', 'MAJOR1_Educational administration',
                           'MAJOR1_Electronics', 'MAJOR1_Environmental Science/Ecology', 'MAJOR1_Ethnic studies', 'MAJOR1_FINANCE',
                           'MAJOR1_FOREIGN LANGUAGE', 'MAJOR1_FORESTRY', 'MAJOR1_Fashion', 'MAJOR1_Fine Arts',
                           'MAJOR1_Food Science/Nutrition/Culinary Arts', 'MAJOR1_GENERAL SCIENCES', 'MAJOR1_GENERAL STUDIES', 'MAJOR1_GEOGRAPHY',
                           'MAJOR1_GEOLOGY', 'MAJOR1_Gerontology', 'MAJOR1_HEALTH', 'MAJOR1_HISTORY', 'MAJOR1_Human Services/Human Resources',
                           'MAJOR1_INDUSTRY & TECHN', 'MAJOR1_Industrial Relations', 'MAJOR1_Information technology', 'MAJOR1_JOURNALISM',
                           'MAJOR1_LAW', 'MAJOR1_LAW ENFORCEMENT', 'MAJOR1_LIBERAL ARTS', 'MAJOR1_LIBRARY SCIENCE', 'MAJOR1_MARKETING',
                           'MAJOR1_MATHMATICS', 'MAJOR1_MEDICINE', 'MAJOR1_MUSIC', 'MAJOR1_Mechanics/Machine Trade', 'MAJOR1_NURSING',
                           'MAJOR1_OTHER', 'MAJOR1_OTHER VOCATIONAL', 'MAJOR1_PHARMACY', 'MAJOR1_PHILOSOPHY', 'MAJOR1_PHYSICAL EDUCATION',
                           'MAJOR1_PHYSICS', 'MAJOR1_POLITICAL SCIENCE/INTERNATIONAL RELATIONS', 'MAJOR1_PSYCHOLOGY', 'MAJOR1_Parks and Recreation',
                           'MAJOR1_Public Relations', 'MAJOR1_SOCIAL WORK', 'MAJOR1_SOCIOLOGY', 'MAJOR1_SPECIAL EDUCATION', 'MAJOR1_Social Sciences',
                           'MAJOR1_Statistics/Biostatistics', 'MAJOR1_THEATER ARTS', 'MAJOR1_THEOLOGY', 'MAJOR1_Television/Film', 'MAJOR1_Textiles/Cloth',
                           'MAJOR1_Urban and Regional Planning', 'MAJOR1_VETERINARY MEDICINE', 'MAJOR1_Visual Arts/Graphic Design/Design and Drafting',
                           'DIPGED_GED', 'DIPGED_HS diploma after post HS classes', 'DIPGED_High School diploma', 'DIPGED_Other', 'FAMILY16_FATHER',
                           'FAMILY16_FATHER & STPMOTHER', 'FAMILY16_FEMALE RELATIVE', 'FAMILY16_M AND F RELATIVES', 'FAMILY16_MALE RELATIVE',
                           'FAMILY16_MOTHER', 'FAMILY16_MOTHER & FATHER', 'FAMILY16_MOTHER & STPFATHER', 'FAMILY16_OTHER', 'PARBORN_BOTH IN U.S',
                           'PARBORN_DK FOR BOTH', 'PARBORN_FATHER ONLY', 'PARBORN_MOTHER ONLY', 'PARBORN_MOTHER; FA. DK', 'PARBORN_NEITHER IN U.S',
                           'PARBORN_NOT FATHER;MO.DK', 'PARBORN_NOT MOTHER;FA.DK', 'GRANBORN_1.0', 'GRANBORN_2.0', 'GRANBORN_3.0', 'GRANBORN_4.0',
                           'GRANBORN_ALL IN U.S', 'POLVIEWS_CONSERVATIVE', 'POLVIEWS_EXTREMELY LIBERAL', 'POLVIEWS_EXTRMLY CONSERVATIVE', 'POLVIEWS_LIBERAL',
                           'POLVIEWS_MODERATE', 'POLVIEWS_SLGHTLY CONSERVATIVE', 'POLVIEWS_SLIGHTLY LIBERAL']]

  return model.predict(data_final.tail(1))

def return_ROI(pred, tuition):
    duration = 10
    interest = 0.25
    tuition = int(tuition)
    if pred < 30000:
      duration = 15

    if tuition > 100000:
      interest = 0.3

    return ((((pred*duration*interest) - tuition) / tuition) * 100)/ duration

if __name__ == "__main__":
    app.run(debug=True)
