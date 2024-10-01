import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# Custom CSS to style the app similar to ChatGPT or Gemini
def add_custom_css():
    st.markdown("""
        <style>
        body {
            background-color: #f5f5f5;
            color: #333;
        }
        .main .block-container {
            max-width: 700px;
            padding: 2rem;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 0.6rem 1rem;
            font-size: 16px;
        }
        .stTextInput > div > div > input {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 0.8rem;
            font-size: 16px;
        }
        .stCode {
            border-radius: 8px;
            padding: 1rem;
            background-color: #f0f0f0;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background: linear-gradient(90deg, rgba(0, 176, 155, 1) 0%, rgba(150, 201, 61, 1) 100%);
            color: white;
            text-align: center;
            padding: 15px 0;
            font-family: 'Arial', sans-serif;
            font-size: 16px;
            box-shadow: 0px -2px 5px rgba(0, 0, 0, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)

def create_streamlit_app(llm, portfolio, clean_text):
    add_custom_css()

    st.title("📧 Cold Mail Generator")
    st.subheader("Generate effective cold emails tailored to job listings!")

    # Input Section
    with st.container():
        st.markdown("### Step 1: Enter a job URL")
        url_input = st.text_input("Enter a job listing URL (e.g., Nike, Google, etc.):", 
                                  value="https://jobs.nike.com/job/R-33460")

        st.markdown("### Step 2: Submit the URL to fetch the job details")
        submit_button = st.button("Generate Email")

    # On submission, show a progress bar and then load the data
    if submit_button:
        with st.spinner("Fetching job details..."):
            try:
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)

                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)
                
                st.success("Job details fetched successfully!")
                for job in jobs:
                    st.markdown(f"**Job Title:** {job.get('role', 'N/A')}")
                    st.markdown(f"**Experience:** {job.get('experience', 'N/A')}")
                    st.markdown(f"**Skills:** {', '.join(job.get('skills', []))}")

                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)

                    # Generating the email content
                    email = llm.write_mail(job, links)
                    st.markdown("### Suggested Cold Email")
                    st.code(email, language='markdown')

            except Exception as e:
                st.error(f"An error occurred: {e}")

    # Footer for branding or additional info
    st.markdown("""
        <div class="footer">
            <p>Created with ❤️ by <a href="https://github.com/mustafashoukat" target="_blank">Mustafa Shoukat</a></p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
