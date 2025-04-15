from analyzer import build_sentiment_prompt

def simulate_sentiment_response(prompt):
    print("PROMPT SENT TO GOOGLE AI STUDIO:\n", prompt)
    return {
        "sentiment": "Negative",
        "tone": "Frustrated",
        "risk_score": 0.76
    }

if __name__ == "__main__":
    feedback = "I feel burnt out. No recognition or support from my manager."
    prompt = build_sentiment_prompt(feedback)
    result = simulate_sentiment_response(prompt)

    print("✅ Sentiment Analysis:", result)
