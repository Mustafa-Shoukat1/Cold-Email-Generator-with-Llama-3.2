# 📧 Cold Mail Generator with LLama 3.2

Cold email generator for services companies using Groq, Langchain, Streamlit, and Llama 3.2. It allows users to input the URL of a company's careers page. The tool then extracts job listings from that page and generates personalized cold emails. These emails include relevant portfolio links sourced from a vector database, based on the specific job descriptions.  

** Scenario:**
![image](https://github.com/user-attachments/assets/10e5a9c2-b1f8-46a9-b876-b7f081433f06)
![image](https://github.com/user-attachments/assets/6005f6d8-894a-4f10-b455-41c018e79707)


- Adidas needs a Principal Software Engineer and is spending time and resources in the hiring process, onboarding, training, etc.
- COMET, an AI Application and Software Development company, can provide a dedicated software development engineer to Nike. So, the business development executive (Mohan) from Atliq is going to reach out to Nike via a cold email. 

## 📊 Architecture Diagram
![Architecture Diagram](imgs/architecture.png)

## ⚙️ Set-up
1. To get started, first, obtain an API_KEY from [Groq Console](https://console.groq.com/keys). Inside `app/.env`, update the value of `GROQ_API_KEY` with the API_KEY you created. 

2. Install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Run the Streamlit app:
   ```bash
   streamlit run app/main.py
   ```

## 🌐 Connect with Me
- [LinkedIn](https://www.linkedin.com/in/mustafashoukat) | 🔗
- [GitHub](https://github.com/mustafashoukat) | 💻
- [Twitter](https://twitter.com/mustafashoukat) | 🐦
- [Email](mailto:mustafa@example.com) | 📧
![image](https://github.com/user-attachments/assets/75749cf8-5ea7-456a-b41c-c2282669550b)

