from flask import Flask, render_template, request, jsonify
from prompt import process_transcript
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_transcript', methods=['POST'])
def process_transcript_route():
    app.logger.info('Received request to process transcript')
    data = request.json
    transcript = data['transcript']
    app.logger.info(f'Received transcript: {transcript}')
    analysis = process_transcript(transcript)
    app.logger.info(f'Generated analysis: {analysis}')
    return jsonify({'analysis': analysis})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)