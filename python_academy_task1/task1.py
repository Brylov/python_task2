
from flask import Flask, request, jsonify

app = Flask(__name__)

#http://localhost:5000/users/Vasa/Pupkin/ID/2?hobby=walking

@app.route('/users/<fname>/<lname>/ID/<int:id>/')
def task(fname, lname, id):
    hobby = request.args.get('hobby', '')
    output = {'fname': fname, 'lname': lname, 'id': id, 'hobby': hobby}
    return jsonify(output)


# endpoint 1 /person/46   Methods  GET, POST, PUT , DELETE

@app.route('/person/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def task_two(id):
    if request.method == 'POST':
        return {"person was created":id}, 201
    elif request.method == 'PUT':
        return {"person was updates":id}, 200
    elif request.method == 'DELETE':
        return {"person was deleted":id}, 200
    else:
        return {"person was retrieved":id}, 200
    
# in case http method is GET return json {"person was retrieved":46}

# in case http method is POST return json {"person was created":46}

# in case http method is PUT return json {"person was update":46}

# in case http method is DELETE  return json {"person was deleted":46}


if __name__ == '__main__':
    app.run(debug=True)