import streamlit as st
import base64


def home():
    # Page configs (tab title, favicon)
   
    st.set_page_config(
        page_title="Dev Kotak's Portfolio",
        page_icon="👨‍💻",
    )
    st.sidebar.success("Select a page above.")


    # CSS styles file
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/phot.jpeg", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # PDF CV file
    with open("assets/Profile.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    
    # Top title
    st.write(f"""<div class="title"><strong>Hi! My name is</strong> Dev Kotak👋</div>""", unsafe_allow_html=True)

    # Profile image
    st.write(f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Dev Kotak">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, 
    unsafe_allow_html=True)

    # Alternative image (static and rounded) uncomment it if you prefer this one
    # st.write(f"""
    # <div style="display: flex; justify-content: center;">
    #    <img src="{img}" alt="Enric Domingo" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    # </div>
    # """, unsafe_allow_html=True)
       # Custom function for printing text
    def txt(a, b):
        col1, col2 = st.columns([4,1])
        with col1:
            st.markdown(a)
        with col2:
            st.markdown(b)

    def txt2(a, b):
        col1, col2 = st.columns([1,4])
        with col1:
            st.markdown(f'`{a}`')
        with col2:
            st.markdown(b)

    def txt3(a, b):
        col1, col2 = st.columns([1,2])
        with col1:
            st.markdown(a)
        with col2:
            st.markdown(b)
    
    def txt4(a, b, c):
        col1, col2, col3 = st.columns([1.5,2,2])
        with col1:
            st.markdown(f'`{a}`')
        with col2:
            st.markdown(b)
        with col3:
            st.markdown(c)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Machine Learning and Deep Learning Enthusiast</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        # Platform: [URL, Icon]
        "Kaggle": ["https://www.kaggle.com/devkotak", "https://www.kaggle.com/static/images/site-logo.svg"],
        "LinkedIn": ["https://www.linkedin.com/in/dev-kotak", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/dev856", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        "Googl Cloud":["https://www.cloudskillsboost.google/public_profiles/2ea83866-2659-422e-955c-2b92e671aac2", "https://icon-library.com/images/google-cloud-platform-icon/google-cloud-platform-icon-9.jpg"]            
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

    st.write("##")

    # About me section
    st.subheader("About Me")
    st.info("""
    - 🧑‍💻 Self-motivated and hardworking Computer Science and Engineering student eager to work in the field of Data
         Science, Machine Learning, and Deep Learning. Bringing forth a motivated attitude and a variety of powerful
         skills to become an excellent computer science engineer by polishing technical and analytical abilities for
         personal development and making a valuable contribution to the institute and the technological field. 
    
    - ❤️ I am passionate about **Machine Learning/Deep Learning, MLOps, Data, Software Engineering, Computer Vision, Optimization, Automation**, and more!
    
    - 📫 How to reach me: devhkotak@gmail.com

    """)
    
    st.write("##")
    st.subheader("Education")
    txt("Bachelor of Technology in Computer Science and Engineering","July 2019 to May 2023")
    txt("**Charotar University of Science and Technology**","Anand,Gujarat")
    st.markdown("""
    - CGPA - **9.25**
    - Recipient of Mukhyamantri Yuva Swavalamban Scholarship Yojana.
    - Courses: 
    - Java Programming, Object-oriented Programming with C++, Programming in Python, Data Struc-ture & Algorithms, 
      Design & Analysis of algorithms, Machine learning, Artificial Intelligence, Software Engineering, 
      Theory of Computation, Data Communication & Networking, Computer Networks, Modern Net-works

    """)
    txt("Higher Secondary Education (Class- XI, XII)","2017 to 2019")
    txt("**Hiramohan Vidhyalaya**", "Gujarat")
    st.markdown("""
    - Percentage - **82%** Grade- **A2**
    - Specialised in Physics , Chemistry and Mathematics
    """)
    txt("Secondary Education (Class - X)","2016 to 2017")
    txt("**Ultra Vision Academy**","Gujarat")
    st.markdown("""
    - Percentage - **92%** Grade- **A1**
    - Activities-  Reached the second round of Quiz on Digital India: Digital Gujarat held at LDRP organized by GUJCOST. 
      Participated in Science Competition organized by Institute for Plasma Research, Gandhinagar.
    """)

    # Download CV button
    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="Profile.pdf",
        mime="application/pdf",
    )

    st.write("##")
    
    st.write(f"""<div class="subtitle" style="text-align: center;">⬅️ Check out my Projects and other details in the navigation menu! )</div>""", unsafe_allow_html=True)


if __name__=="__main__":
    home()
