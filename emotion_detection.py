import requests
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"    }
    input_json = {        "raw_document": {            "text": text_to_analyze        }
    }
    response = requests.post(url, headers=headers, json=input_json)
    response.raise_for_status()
    result = response.json()
    emotions = result.get('emotionPredictions', [{}])[0].get('emotion', {})
    return emotions
if __name__ == "__main__":
    sample_text = input("Enter the text to analyze for emotion: ")
    result = emotion_detector(sample_text)
    print("Emotion detection result:")
    print(result)