from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "sb.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV | Sallie Bhatia"
PAGE_ICON = "👨‍💻"
NAME = "Sallie Bhatia"
DESCRIPTION = """
Methodical and tech-savvy quick learner seeking an Office Assistant position with a growing business. Eager to use time management and communication skills to assist busy teams with business needs.
"""
EMAIL = "Salliebhatia1@gmail.com"

PROJECTS = {
    "🏆 Best Associate of the Month (multiple times)": "https://salliebhatia.onrender.com/",
    "🏆 Volunteer at Cottage Hospital - Santa Barbara": "https://salliebhatia.onrender.com/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

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


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Tech-savvy quick learner
- ✔️ Expertise in Customer service related tasks with phone etiquette
- ✔️ Proficient in managing small teams focused on increasing operational efficiency.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
- 👩‍💻 Microsoft office suite
- 📊 Managing and manipulating data in Excel using vlookups and PMT
- 📚 Expert in ICD-9 and ICD-10 CPT coding 
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Office Assistant | Goleta Neighborhood Clinic, Santa Barbara, CA**")
st.write("03/2023-08/2024")
st.write(
    """
- ► Provided friendly customer service in person and over the phone to over 50 – 80 members daily, enhancing patient satisfaction and contributing to a 10% increase in positive feedback ratings.
- ► Created comprehensive reports and PowerPoint presentations for healthcare providers, aiding in the efficient delivery of patient care and improving clinic operational efficiency by 15%.
- ► Managed patient records and appointment scheduling, ensuring accurate and timely updates, which reduced appointment errors by 20%.
- ► Assisted in inventory management, including ordering and stocking medical supplies, maintaining optimal inventory levels, and reducing supply shortages by 30%.
- ► Facilitated the onboarding process for new staff, providing orientation and training on clinic procedures, which improved new hire productivity by 25%.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Front Desk Associate | Riviera Motel, Los Angeles, CA**")
st.write("03/2016 – 04/2017")
st.write(
    """
- ► Created schedules for 8 housekeeping employees, ensuring efficient coverage and minimizing labor costs by 10%.
- ► Managed guest check-ins and check-outs, ensuring a smooth and welcoming experience that led to a 12% increase in guest satisfaction scores.
- ► Handled guest inquiries and resolved complaints in a timely and professional manner, which resulted in a 15% reduction in negative online reviews.
- ► Coordinated with maintenance staff to address urgent repairs, improving response times and guest safety by 20%.
- ► Processed daily financial transactions, including cash handling and credit card processing, with 100% accuracy, contributing to seamless motel operations. 
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Administrative Assistant	 | Nesco Resource- Downtown LA, CA**")
st.write("04/2014-02/2016")
st.write(
    """
- ► Supported daily operations by managing office correspondence, including sorting and distributing mail, which improved internal communication efficiency by 25%.
- ► Organized and maintained electronic and physical filing systems, ensuring quick retrieval of documents and reducing file search times by 40%.
- ► Scheduled and coordinated meetings and events, handling logistics such as room bookings, catering, and materials preparation, which led to a 20% improvement in event execution.
- ► Assisted in the recruitment process by screening resumes, scheduling interviews, and coordinating with hiring managers, which streamlined the hiring process and reduced time-to-hire by 15%.
- ►	Implemented office supply management procedures, leading to a 10% reduction in waste and cost savings.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")