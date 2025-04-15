from parser import extract_text_from_pdf
from prompt_engine import build_resume_prompt

def simulate_llm_response(prompt):
    print("PROMPT SENT TO GOOGLE AI STUDIO:\n", prompt)
    return {
        "match_score": 87,
        "matched_skills": ["Python", "APIs", "Machine Learning"],
        "experience_years": 3
    }

if __name__ == "__main__":
    job_description = "Looking for a Python developer with API and ML experience."

    resume_text = extract_text_from_pdf("data/resumes/sample_resume.pdf")
    prompt = build_resume_prompt(resume_text, job_description)
    result = simulate_llm_response(prompt)

    print("✅ Result:", result)
