import os

from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print(f'Request for hello page received with name={name}')
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return '<p>No Name Found</p>'


if __name__ == '__main__':
   app.run()
