from EmotionDetection import emotion_detector

if __name__ == "__main__":
    sample_text = "I hate working long hours."
    result = emotion_detector(sample_text)
    print("Emotion detection result:")
    print(result)