from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/logika")
def hello_logika():
    return "<p>Hello, logika!</p>"

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу
