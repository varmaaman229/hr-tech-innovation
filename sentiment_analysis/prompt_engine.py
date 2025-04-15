def build_sentiment_prompt(feedback_text):
    """
    Creates a structured prompt for LLM-based sentiment analysis.

    Parameters:
        feedback_text (str): Raw feedback text from employee surveys or exit interviews.

    Returns:
        str: Formatted prompt for input into an LLM.
    """
    prompt = f"""
You are an HR AI assistant.

Analyze the following employee feedback and return:
1. Sentiment (Positive / Neutral / Negative)
2. Emotional Tone (e.g., Happy, Frustrated, Motivated)
3. Attrition Risk Score (between 0 and 1)
4. Brief suggestion to improve engagement

Feedback:
\"\"\"{feedback_text}\"\"\"
"""
    return prompt
