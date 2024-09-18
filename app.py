from flask import Flask
from flask import request, jsonify

app = Flask(__name__)


@app.route('/sum', methods=['POST'])
def handle_sum():
    data = request.json
    return jsonify({'result': data['num1'] + data['num2']}) #making sure response is lining up with what the test expects




if __name__ == '__main__':
    app.run(debug=True)