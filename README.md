# ResuMatchAI 🤖💼

ResuMatchAI is an AI-powered tool designed to help job seekers optimize their resumes to match job descriptions using the LLaMA 3.1 model and LangChain. By leveraging state-of-the-art natural language processing techniques, ResuMatchAI analyzes resumes and job descriptions, provides personalized suggestions, and enhances the likelihood of passing through Applicant Tracking Systems (ATS) and impressing recruiters.

## 🚀 Features
- 🔍 Resume Analysis: Extracts key skills, experiences, and qualifications from your resume using LLaMA 3.1.
- 🧠 Job Description Matching: Compares your resume against job descriptions to identify matching skills and qualifications.
- 💡 Personalized Suggestions: Provides targeted suggestions to optimize your resume based on job requirements.
- 📊 Compatibility Scoring: Generates a compatibility score showing how well your resume matches the job description.

## 🛠️ Tech Stack
- LLaMA 3.1: As the primary Large Language Model for natural language processing and resume optimization.
- LangChain: For chaining the LLM operations and creating structured workflows.
- Python: Backend language for building the core functionality.
- Streamlit : For building an intuitive and interactive user interface.
- FAISS: For vector storage and similarity matching between resumes and job descriptions.

## 🎯 How It Works
1. Upload your Resume 📄: Upload your resume in PDF or DOCX format.
2. Input Job Description 💼: Provide the job description you'd like to match your resume against.
3. AI Analysis 🧠: LLaMA 3.1 processes your resume and the job description, identifying matches and gaps.
4. Get Feedback 📋: Receive a detailed report with your compatibility score and personalized suggestions to optimize your resume.

## 🚀 Getting Started
### Prerequisites
- Python 3.8+
- Git

### Installation
1. Clone the repository:
```
git clone https://github.com/your-username/ResuMatchAI.git
cd ResuMatchAI
```

2. Create a virtual environment:
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Running the Application
Start the ResuMatchAI application using Streamlit:
```
streamlit run app.py
```

5. Access the app in your web browser at http://localhost:8501.

## 🌐 Hosted Application

You can try out the live version of ResuMatchAI here: ResuMatchAI Live App


## 🖼️ Screenshots
1. Upload Resume Page

2. Job Description Input Page

3. AI Analysis and Suggestions

## 🤝 Contributing
We welcome contributions! Feel free to submit a pull request, report issues, or suggest new features.

1. Fork the repository.
2. Create your feature branch: git checkout -b feature/YourFeature
3. Commit your changes: git commit -m 'Add new feature'
4. Push to the branch: git push origin feature/YourFeature
5. Open a pull request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

If you have any questions or need further assistance, feel free to reach out!

Happy Job Hunting with ResuMatchAI! 🎯🚀
