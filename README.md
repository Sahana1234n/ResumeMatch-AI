# AI-Resume-Analyzer <br>

AI-powered Resume & Job Description Matcher with Score, Gaps & Suggestions <br>

ResumeMatch AI is an intelligent web application that compares a candidate’s resume with a job description, delivering an ATS Compatibility Score and actionable improvement suggestions by analyzing missing skills, keywords, and essential sections to boost resume effectiveness.

---

## 🚀 Live Demo
Click below to try the live version of **ResumeMatch AI**:<br>
👉 **[Live Demo](https://ai-resume-match-analyzer.streamlit.app/)**  

---

🚀 Features

---


📄 Upload Resume (PDF)

📝 Paste Job Description

🤖 AI-Powered Matching using LLM's

📊 Match Score 

🧩 Missing Skills & Gaps Detection

✨ Tailored Suggestions for Improvement

🔄 Easy-to-use Web UI (Streamlit cloud)

---

🛠️ Tech Stack
- Python
- pdfminer
- Sentence Transformers
- GROQ API
- Scikit-learn
- Regex
  
---

🧩 How It Works

1. Extract Text from the uploaded resume.
2. Parse Job Description into skills, responsibilities, qualifications.
3. Generate vector embeddings of JD & resume.
4. Compute:
   - Match Score
   - Missing Skills
   - Strengths
   - Suggestions
5.Display everything cleanly on the UI.

---

▶️ Run Locally


1️⃣ Clone the Repository
```
git clone https://github.com/your-username/resumematch-ai.git

```
2️⃣ Navigate into the Project Folder
```
cd resumematch-ai
```

3️⃣ Create a .env File
```
GROQ_API_KEY=your_api_key_here
```
4️⃣ Run the Streamlit Application
```
streamlit run app.py

```
---

🌐 Deployment

---

This project is deployed on Streamlit Cloud.<br>
You can try the live demo here:<br>
👉 Live Demo: https://ai-resume-match-analyzer.streamlit.app/
















 
  
