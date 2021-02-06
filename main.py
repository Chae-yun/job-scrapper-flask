from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_so_jobs
from exporter import save_to_file

app = Flask("JobScrapper")

db = {}

# 함수와 이름 같을 필요 없음
# @: 데코레이터, 바로 아래에 있는 함수를 찾음
@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  word = request.args.get("word")
  if word:
    word = word.lower()
    existing_jobs = db.get(word)
    if existing_jobs:
      jobs = existing_jobs
    else:
      jobs = get_so_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template(
    "report.html", 
    resultsNumber = len(jobs), 
    searchingBy = word,
    jobs = jobs
  )

@app.route("/export")
def export():
  try:
    word = request.args.get("word")
    if not word:
      raise Exception
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception
    save_to_file(jobs)
    return send_file("jobs.csv")
  except:
    return redirect("/")

# 로컬 작업시에는 매개변수 지우면 됨
app.run(host = "0.0.0.0")