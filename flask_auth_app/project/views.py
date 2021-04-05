from flask import Flask, render_template
from flask_login import login_required


@app.route('/index')
@login_required
def blog():
    return render_template('index.html')
