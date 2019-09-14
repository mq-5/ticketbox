from src import app
from flask import render_template


# @app.route('/')
# def home():
#     return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
