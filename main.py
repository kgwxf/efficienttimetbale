from flask import Flask, render_template, request, url_for
import csv 

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
  if request.method == "GET":
    return render_template("index.html")
  
  else:
    cls = request.form.get('cls')
    dy = request.form.get('dy')
    tme = request.form.get('tme')
    
    with open("35timetable.csv", 'r', newline="") as infile:
      records = csv.reader(infile, delimiter=";")
      for record in records:
        if cls == "5C35":
          if record[0] == dy:
            if tme <= record[1]:
              return render_template("page1.html", c=record[2],t=record[1])
          #   else:
          #     return render_template("page1.html", c=record[2],t=record[1])
          # else:
          #   return render_template("page1.html", c=record[2],t=record[1])

        elif cls == "computing" and dy == "is" and tme == "cool":
          return render_template("easter.html")
        else:
          return render_template("page3.html")
        
          

    #     print("DAY:", record[0])
    #     print("TIME:", record[1])
    #     print("LESSON:", record[2])
    # return render_template("page1.html",c=cls, d=dy, t=tme)

# @app.route('/back', methods=["GET", "POST"])
# def back():
#   return render_template("index.html")


app.run(host='0.0.0.0', port=8080)
