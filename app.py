from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
  print("Handling request to home page.")
  return render_template('student_homepage.html')

if __name__ == "__main__":
  app.run()
