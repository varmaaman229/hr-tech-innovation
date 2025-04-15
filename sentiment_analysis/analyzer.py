def build_sentiment_prompt(feedback):
    return f"""
Analyze the following feedback.
Return:
- Sentiment: Positive, Neutral, Negative
- Emotional Tone
- Attrition Risk Score (0 to 1)

Feedback:
{feedback}
"""
