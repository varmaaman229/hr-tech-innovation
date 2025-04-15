def build_resume_prompt(resume_text, job_description):
    return f"""
You are an AI assistant for HR.
Compare the following resume with the job description. Return:
- Match score out of 100
- Skills matched
- Experience matched

Job Description:
{job_description}

Resume:
{resume_text}
"""
