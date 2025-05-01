from flask import Flask, Response, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    def event_stream():
        while True:
            word = "Shreyas Shridhar Kulkarni"
            for char in word:
                yield f"data: {char}\n\n"
                time.sleep(0.5)
            # Send a clear signal after the word is displayed
            time.sleep(1)
            yield "data: __CLEAR__\n\n"
    return Response(event_stream(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
