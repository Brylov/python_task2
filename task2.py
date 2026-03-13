from flask import Flask, request, jsonify, render_template

persons = {1: {"name":'Moshe',"age":40,'city':"Paris","kidsName":["Vasa","Sofa","Sara"]},
           2: {"name":'Jojo',"age":32,'city':"Israel","kidsName":["Ryan","George","Dunkel"]}}

app = Flask(__name__)
# create end point GET Json data in format {"name":Moshe,"age":40,city:"Paris","kidsName":["Vasa","Sofa","Sara"]}
# create person.html template. Incase city not Paris template returns You are not from our city. else template returns data of person naME
# person age and his kid names in any format you like. Use must use if and for sentences from Jinja template
@app.route('/person/<int:person_id>', methods=['GET'])
def person(person_id):
    # Simulate database lookup
    person_data = persons.get(person_id)

    if not person_data:
        return jsonify({'person': 'unknown'})
    
    return jsonify(person_data)

@app.route('/person_html/<int:person_id>', methods=['GET'])
def person_html(person_id):
    # Simulate database lookup
    person_data = persons.get(person_id)

    if not person_data:
        return jsonify({'person': 'unknown'})
    
    return render_template('person.html', person=person_data)

if __name__ == '__main__':
    app.run(debug=True)