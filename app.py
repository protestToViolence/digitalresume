from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Dr. Gaurav Tripathi"
PAGE_ICON = ":wave:"
NAME = "Dr. Gaurav Tripathi"
DESCRIPTION = """
Senior esearch Scientist, Computer Vision Expert for Image Processing and supports data-driven decision-making.
"""
EMAIL = "gauravtripathy@email.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com",
    "LinkedIn": "https://www.linkedin.com/in/dr-gaurav-tripathi-4b26876/",
    "GitHub": "https://github.com/protestToViolence",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Smart Parking - ANPR using deep learning",
    "🏆 Aerial Object Detections",
    "🏆 Drone Image Object Deetction & Drone as anobject detection",
    "🏆 Violence Detection in a crowd protest environment",
}


st.set_page_config(page_title=PAGE_TITLE,layout="wide", page_icon=PAGE_ICON,initial_sidebar_state="auto", menu_items=None)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=400)
    #st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 15 Years expereince including traditional programming and deep learning 
- ✔️ Strong hands on experience and knowledge in computer vision, Python
- ✔️ Good understanding of computer vision , streaming pipelines and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas),Tensorflow, PyTorch, Keras, SQL
- 📊 Data Visulization: Streamlit,Plotly
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🗄️ Databases: Postgres, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Member Research Staff | Central Research Labs, Bharat Electronics Limited**")
st.write("09/2007 - Present")

