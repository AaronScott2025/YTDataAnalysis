from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def main_gui():
    return render_template('MainGUI.html')

@app.route('/info_screen')
def info_screen():
    return render_template('InfoScreen.html')

@app.route('/api/query')
def query_api():
    query = request.args.get('query')
    # Example data
    graph_data = {
        "labels": ["A", "B", "C", "D"],
        "values": [10, 20, 30, 40],
        "label": "Example Data"
    }
    details = [f"Detail {i} for query {query}" for i in range(1, 6)]
    return jsonify({"graphData": graph_data, "details": details})

if __name__ == '__main__':
    app.run(debug=True)