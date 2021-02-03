from flask import Flask, render_template, request, redirect

app = Flask("JobScrapper")

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
  else:
    return redirect("/")
  return render_template("report.html", searchingBy = word)

# 로컬 작업시에는 매개변수 지우면 됨
app.run(host = "0.0.0.0")