from flask import Flask, render_template
app = Flask(__name__, template_folder = 'template')

@app.route('/')
def bot():
    return render_template("code.html")

if __name__ == '__main__' :
    app.run()