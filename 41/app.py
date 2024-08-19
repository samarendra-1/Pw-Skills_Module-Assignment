from flask import Flask, render_template

app = Flask(__name__)

@app.route('/display/<name>')
def display_name(name):
    return render_template('display.html', name=name)

if __name__ == '__main__':
    app.run(debug=False)
