from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')


@app.route('/projects/flyer-design')
def design():
    return render_template('design.html', title='Flyer Design')


@app.route('/projects/photography')
def photography():
    return render_template('photography.html', title='Photography')


@app.route('/projects/digital-art')
def graphic():
    return render_template('graphic.html', title='Digital Art')


@app.route('/demo')
def demo():
    return render_template('demo.html', title='Demo')


if __name__ == '__main__':
    app.run()
