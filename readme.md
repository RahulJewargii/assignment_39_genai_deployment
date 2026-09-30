title: GenAI App Deployment
emoji: AI
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 8501

# Assignment 39  GenAI App Deployment

# Problem Statement
Deploy a GenAI application so users can access it online.
This project is prepared for both:
1. Streamlit Community Cloud
2. Hugging Face Spaces

# Important Deployment Note
The previous assignment used Ollama locally. Ollama is not installed automatically on Streamlit Community Cloud or a normal Hugging Face Streamlit deployment. Therefore, this deployment version uses the Hugging Face Inference API through `huggingface_hub`.
The local Ollama version can still be used on your computer. This cloud version keeps the same idea of a GenAI application while using a cloudaccessible model endpoint.

# Project Files
```text
assignment_39/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

# Task 1  Deployment on Streamlit Cloud
1. Push this project to GitHub.
2. Keep `app.py` and `requirements.txt` in the repository.
3. Create a Streamlit Community Cloud account and connect GitHub.
4. Select the GitHub repository, branch, and `app.py` as the entrypoint.
5. Add the `HF_TOKEN` secret.
6. Deploy the application.
7. Open and test the generated `streamlit.app` URL.

# Streamlit Cloud Secret
In the app settings, add:
```text
HF_TOKEN = "your_huggingface_token"
```
Do not put the token directly inside `app.py` or commit it to GitHub.

# Task 2  Deployment on Hugging Face Spaces
Current Hugging Face documentation says the builtin Streamlit SDK is deprecated. For a new Streamlit Space, use the Docker SDK/template. This project therefore includes a `Dockerfile`.
Steps:
1. Create a new Space on Hugging Face.
2. Choose Docker as the Space SDK.
3. Give the Space a name.
4. Choose the visibility you want.
5. Upload or connect the GitHub repository files.
6. Make sure `README.md`, `app.py`, `requirements.txt`, and `Dockerfile` are present.
7. Add the `HF_TOKEN` secret in the Space settings.
8. Wait for the Space to build.
9. Open the Space URL and test the app.

# Hugging Face Secret
Add this as a Space secret:
```text
HF_TOKEN = your_huggingface_token
```

# Task 3  Compare Deployment Platforms

# Streamlit Community Cloud vs Hugging Face Spaces
**Streamlit Community Cloud:**
 Designed specifically for Streamlit applications.
 Connects directly with GitHub repositories.
 Provides a simple deployment workflow.
 Supports secrets and Python dependency files.

**Hugging Face Spaces:**
 Designed for hosting and sharing ML/AI applications.
 Spaces are Git repositories.
 Docker can be used for Streamlit applications.
 Useful when the project is closely connected to the Hugging Face ecosystem.

# Pros and Cons
**Streamlit Community Cloud**
Pros:
 Simple setup for Streamlit apps.
 Direct GitHub deployment.
 Easy secrets configuration.
Cons:
 Intended for Streamlit applications and its available runtime resources.
 Localonly services such as Ollama are not automatically available in the cloud runtime.

**Hugging Face Spaces**
Pros:
 Strong integration with Hugging Face models and tools.
 Gitbased workflow.
 Docker provides more control over the runtime.
Cons:
 Docker configuration can require more setup.
 Runtime resources and availability depend on the Space configuration.

# When to Use Which
Use **Streamlit Community Cloud** when the main requirement is a straightforward Streamlit application deployment.
Use **Hugging Face Spaces** when the application is strongly connected to Hugging Face models, datasets, or the Hugging Face ecosystem, or when Dockerbased deployment is useful.

# How to Run Locally
Open PowerShell in the assignment folder:
```powershell
cd C:\Assignment_GenAi\assignment_39
```
Activate the virtual environment:
```powershell
C:\Assignment_GenAi\Assignment_venv\Scripts\Activate.ps1
```
Set your Hugging Face token for the current PowerShell session:
```powershell
$env:HF_TOKEN="YOUR_HUGGINGFACE_TOKEN"
```
Optional model setting:
```powershell
$env:HF_MODEL="deepseekai/DeepSeekV30324"
```
Run:
```powershell
streamlit run app.py
```

# Task 1  GitHub Setup Commands
From the project folder:
```powershell
git init
git add .
git commit m "Assignment 39 GenAI app deployment"
git branch M main
git remote add origin https://github.com/YOUR_USERNAME/assignment_39_genai_deployment.git
git push u origin main
```
Replace `YOUR_USERNAME` with your GitHub username and use your own repository URL.
If `origin` already exists, use:
```powershell
git remote seturl origin https://github.com/YOUR_USERNAME/assignment_39_genai_deployment.git
git push u origin main
```

# Testing Checklist
After deployment, test:
1. Open the live URL.
2. Enter a simple question.
3. Click **Generate Response**.
4. Confirm that an AI response appears.
5. Ask another question to test session history.
6. Click **Clear Conversation** and confirm the history is removed.

# Requirements
Python
Git
GitHub account
Hugging Face account and access token
Streamlit
`huggingface_hub`
