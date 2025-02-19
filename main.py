from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello, Flask API!", "status": "success"}
    return jsonify(data)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Hello, {name}!"
    return '''
        <form method="POST">
            Name: <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
