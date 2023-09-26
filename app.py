from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home/<user_typed>")      
def home(user_typed):
    return render_template('home.html', user_typed=user_typed)


if __name__  == '__main__':
    app.run(debug=True, port=8080)