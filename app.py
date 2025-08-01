from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <body>
            <form action="/greet" method="post">
                Please enter your name: <input type="text" name="username">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    user_input = request.form['username']
    if not user_input:
        return jsonify({"error": "No name provided"}), 400
    return f"Hello, {user_input}! Welcome to this Flask app for Docker demo."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)