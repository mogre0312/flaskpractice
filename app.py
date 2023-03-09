from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('form.html')

@app.route('/student')
def student():
    return 'welcome student'

@app.route('/faculty')
def faculty():
    return 'welcome faculty'

@app.route('/user/<name>')
def user(name):
    if name == 'student':
        return redirect(url_for('student'))
    if name == 'faculty':
        return redirect(url_for('faculty'))
    

    

if __name__ == '__main__':
    app.run(debug = True)