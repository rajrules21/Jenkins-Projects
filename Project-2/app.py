from flask import Flask, render_template, request, redirect, url_for
from flask_dynamo import Dynamo
from dynamodb_setup import create_dynamodb_table  # Import the function
import os

app = Flask(__name__)

# Configure DynamoDB
app.config['DYNAMO_ENABLE_LOCAL'] = True
app.config['DYNAMO_LOCAL_HOST'] = 'localhost'
app.config['DYNAMO_LOCAL_PORT'] = 8000

dynamo = Dynamo(app)

# Call the function to create DynamoDB table
create_dynamodb_table()

# Define DynamoDB table
items_table = dynamo.tables['Items']

@app.route('/')
def index():
    # Retrieve all items from DynamoDB
    items = items_table.scan()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    # Add a new item to DynamoDB
    name = request.form['name']
    description = request.form['description']
    item = {'id': str(uuid.uuid4()), 'name': name, 'description': description}
    items_table.put_item(Item=item)
    return redirect(url_for('index'))

@app.route('/edit/<string:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    # Edit an existing item in DynamoDB
    item = items_table.get_item(Key={'id': item_id})
    if request.method == 'POST':
        item['name'] = request.form['name']
        item['description'] = request.form['description']
        items_table.put_item(Item=item)
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app.route('/delete/<string:item_id>', methods=['POST'])
def delete_item(item_id):
    # Delete an item from DynamoDB
    items_table.delete_item(Key={'id': item_id})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
