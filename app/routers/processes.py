from collections import Counter
import time
from flask import Flask, render_template, request, jsonify, Response
import app.processes.youtube as yt  # Assuming this is used elsewhere

app = Flask(__name__)

# Main GUI route
@app.route('/')
def main_gui():
    return render_template('MainGUI.html')

# Info screen route
@app.route('/info_screen')
def info_screen():
    return render_template('InfoScreen.html')

# Streaming updates
@app.route('/stream')
def stream():
    def event_stream():
        yield "data: Starting query processing\n\n"
        time.sleep(1)  # Simulate delay

        query = request.args.get('query', 'default_query')
        slider = request.args.get('slider', 'Moderate')

        precision = {
            "Broad": 25,
            "Moderate": 15,
            "Precise": 10
        }.get(slider, "error")

        if precision == "error":
            yield "data: Error: Invalid slider value\n\n"
            return

        yield f"data: Query received: {query}\n\n"
        yield f"data: Precision set to: {precision}\n\n"

        time.sleep(1)  # Simulate delay
        yield "data: Parsing query...\n\n"

        try:
            jsonfile = [
                {"title": "Video 1", "weight": 20, "color": "blue", "description": "A sample video"},
                {"title": "Video 2", "weight": 15, "color": "red", "description": "Another video"}
            ]
            time.sleep(1)
        except Exception as e:
            yield f"data: Error: {str(e)}\n\n"
            return

        yield "data: Processing videos...\n\n"
        vidWeights = []
        title_counter = Counter()
        descriptions_counter = Counter()
        colors_counter = Counter()

        for item in jsonfile:
            title_counter.update(item['title'].split())
            descriptions_counter.update(item['description'].split())
            colors_counter.update([item['color']])
            vidWeights.append({
                "weight": item['weight'],
                "title": item['title'],
                "color": item['color']
            })
            yield f"data: Processed video: {item['title']}\n\n"
            time.sleep(0.5)

        yield "data: Generating graph data...\n\n"
        time.sleep(1)

        yield "data: Processing complete\n\n"

    return Response(event_stream(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=False)
