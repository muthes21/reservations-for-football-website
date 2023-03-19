from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_user():
  if request.method == 'POST':
    user = request.form['uname']
    pwd = request.form['psd']
    print(user, pwd)
  return render_template('home.html')


@app.route("/Register")
def Register():
  
  
  return render_template('RegisterHere.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
