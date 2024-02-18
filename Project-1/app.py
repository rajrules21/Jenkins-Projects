# app.py
#import necessary functions and classes from the Flask library.
from flask import Flask, render_template, request, redirect, url_for

#create a Flask application instance
app = Flask(__name__)

#This line initializes an empty list called tasks. This list will be used to store the tasks in our to-do list application.
tasks = []

#define a route for the root URL
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


#define a route for adding tasks
@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form['content']
    tasks.append(task_content)
    return redirect(url_for('index'))


#define a route for deleting tasks
@app.route('/delete/<int:index>')
def delete_task(index):
    if index < len(tasks):
        del tasks[index]
    return redirect(url_for('index'))


#This conditional block ensures that the Flask app only runs when the script is executed directly, 
# not when it's imported as a module in another script
if __name__ == '__main__':
    app.run(debug=True)
