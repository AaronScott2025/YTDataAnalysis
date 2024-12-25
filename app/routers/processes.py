from collections import Counter
from flask import Flask, render_template, request, jsonify, Response
import app.processes.youtube as yt
app = Flask(__name__)

# Main GUI route
@app.route('/')
def main_gui():
    return render_template('MainGUI.html')

# Info screen route
@app.route('/info_screen')
def info_screen():
    return render_template('InfoScreen.html')

# Main process route
@app.route('/querydata', methods=['GET'])
def query_api():
    query = request.args.get('query', '').strip()
    slider = request.args.get('slider')

    if not query:
        return jsonify({"error": "Query cannot be empty"}), 400

    precision = {
        "Broad": 25,
        "Moderate": 15,
        "Precise": 10
    }.get(slider)

    if precision is None:
        return jsonify({"error": "Invalid slider value"}), 400

    try:
        title = Counter()
        descriptions = Counter()
        colors = Counter()

        # Parse and process videos
        vidWeights = yt.parse_and_process(query, title, descriptions, colors)

        # Ensure sorting won't fail
        vidWeights.sort(key=lambda x: getattr(x, 'weight', 0), reverse=True)

        # Prepare graph data
        graph_data = {
            "labels": [f"Video {i}" for i in range(1, len(vidWeights) + 1)],
            "values": [video.weight for video in vidWeights],
            "label": "Video Weights"
        }
        details = [f"Video {i}: {query}" for i in range(1, len(vidWeights) + 1)]

        return jsonify({"graphData": graph_data, "details": details})
    except Exception as e:
        return jsonify({"error": f"Processing error: {str(e)}"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
