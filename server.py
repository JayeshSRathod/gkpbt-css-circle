from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400

        text = data['text']
        emotions = emotion_detector(text)

        response_str = (
            f"For the given statement, the system response is "
            f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
            f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} and "
            f"'sadness': {emotions['sadness']}. The dominant emotion is "
            f"<b>{emotions['dominant_emotion']}</b>."
        )

        return jsonify({
            "anger": emotions['anger'],
            "disgust": emotions['disgust'],
            "fear": emotions['fear'],
            "joy": emotions['joy'],
            "sadness": emotions['sadness'],
            "dominant_emotion": emotions['dominant_emotion'],
            "response": response_str
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run Flask app on all IPs, port 5000 for Cloud IDE Kubernetes environment
    app.run(host='0.0.0.0', port=5000, debug=True)