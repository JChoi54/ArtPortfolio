from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')


@app.route('/projects/arduino')
def arduino():
    return render_template('arduino.html', title='Arduino')


@app.route('/projects/photography')
def photography():
    return render_template('photography.html', title='Photography')


@app.route('/projects/graphic')
def graphic():
    return render_template('graphic.html', title='Graphic Design')


@app.route('/demo')
def demo():
    return render_template('demo.html', title='Demo')


if __name__ == '__main__':
    app.run()
