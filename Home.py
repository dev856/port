import streamlit as st
import base64
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from st_on_hover_tabs import on_hover_tabs
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit_analytics
import base64
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
import sqlite3
from bs4 import BeautifulSoup
from streamlit_extras.echo_expander import echo_expander


def home():
    # Page configs (tab title, favicon)
   
    st.set_page_config(
        page_title="Dev Kotak",
        page_icon="👨‍💻",
        layout="wide",
        initial_sidebar_state="auto"
    )
    #st.sidebar.success("Select a page above.")

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    def render_lottie(url, width, height):
        lottie_html = f"""
        <html>
        <head>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
        </head>
        <body>
            <div id="lottie-container" style="width: {width}; height: {height};"></div>
            <script>
                var animation = lottie.loadAnimation({{
                    container: document.getElementById('container'),
                    renderer: 'svg',
                    loop: true,
                    autoplay: true,
                    path: '{url}'
                }});
                animation.setRendererSettings({{
                    preserveAspectRatio: 'xMidYMid slice',
                    clearCanvas: true,
                    progressiveLoad: false,
                    hideOnTransparent: true
                }});
            </script>
        </body>
        </html>
        """
        return lottie_html
    def load_lottieurl(url):
    # use the request method to send a get to request URL
        r = requests.get(url)
    # if status is successful it will return 
        if r.status_code != 200: 
            return None
    # return the json data of the lottie animation
        return r.json()

    lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_dl87KC.json")
    # Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("styles/main.css")


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

    img_utown = Image.open("images/lh.jpeg")
    img_lh = Image.open("images/lh.jpeg")
    img_ifg = Image.open("images/lh.jpeg")

    #Assets for internship
    img_bitmetrix = Image.open("images/isro.png")
    img_scor = Image.open("images/jupiter.png")
    img_zummit = Image.open("images/zummit.png")
    img_dep = Image.open("images/depstar.png")
    img_kintu = Image.open("images/kintu.jpeg")
    img_spark = Image.open("images/spark.png")
    # Assets for education
    
    img_nus = Image.open("images/charusat.jpg")
    img_poc = Image.open("images/hira.jpg")
    img_tpjc = Image.open("images/ultra.jpeg")
    # Assets for projects
    
    #images_projects = [Image.open(f"images/{name}.{'jpg' if name not in ('map', 'gephi', 'health') else 'png'}") for name in image_names_projects]
    # Assets for volunteering
    
    
    #img_lottie_animation = Image.open("images/lottie_animation.gif")
    # Assets for contact
    #lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

    img_linkedin = Image.open("images/linkedin.png")
    img_github = Image.open("images/github.png")
    img_email = Image.open("images/email.png")

    def social_icons(width=24, height=24, **kwargs):
            icon_template = '''
            <a href="{url}" target="_blank" style="margin-right: 20px;">
                <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
            </a>
            '''

            icons_html = ""
            for name, url in kwargs.items():
                icon_src = {
                   
                    "linkedin": "https://img.icons8.com/ios-filled/100/ff8c00/linkedin.png",
                    "github": "https://img.icons8.com/ios-filled/100/ff8c00/github--v2.png",
                    "email": "https://img.icons8.com/ios-filled/100/ff8c00/filled-message.png"
                }.get(name.lower())

                if icon_src:
                    icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

            return icons_html
    #####################
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

    #def txt3(a, b):
    #col1, col2 = st.columns([1,2])
    #with col1:
        #st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
    #with col2:
        # Split the text at the comma and wrap each part in backticks separately
        #b_parts = b.split(',')
        #b_formatted = '`' + ''.join(b_parts) + '`'
        #st.markdown(f'<p style="font-size: 20px; font-family: monospace;">{b_formatted}</p>', unsafe_allow_html=True)
        #st.markdown(f'<p style="font-size: 20px; color: red;"></code>{b}</code></p>', unsafe_allow_html=True)

    def txt3(a, b):
        col1, col2 = st.columns([1,4])
        with col1:
            st.markdown(f'<p style="font-size: 18px;">{a}</p>', unsafe_allow_html=True)
        with col2:
            b_no_commas = b.replace(',', '')
            st.markdown(b_no_commas)

    def txt4(a, b):
        col1, col2 = st.columns([1.5,2])
        with col1:
            st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
        with col2: #can't seem to change color besides green
            st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

    #####################
# Sidebar: If using streamlit_option_menu
    with st.sidebar:
        with st.container():
            l, m, r = st.columns((1,3,1))
            with l:
                st.empty()
            with m:
                st.image(img_lh, width=175)
            with r:
                st.empty()
        
        choose = option_menu(
                            "Dev Kotak", 
                            ["About Me", "Site Overview", "Experience", "Technical Skills", "Education", "Projects", "Volunteering", "Resume", "Contact"],
                            icons=['person fill','globe','clock history', 'tools', 'book half', 'clipboard', 'heart', 'paperclip', 'envelope'],
                            menu_icon="mortarboard", 
                            default_index=0,
                            styles={
            "container": {"padding": "0!important", "background-color": "#181818"},
            "icon": {"color": "white", "font-size": "20px"}, 
            "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#192538"},
            "nav-link-selected": {"background-color": "#192538"},
        }
        )
        linkedin_url = "https://www.linkedin.com/in/dev-kotak/"
        github_url = "https://github.com/dev856"
        email_url = "mailto:devhkotak@gmail.com"
        with st.container():
            l, m, r = st.columns((0.11,2,0.1))
            with l:
                st.empty()
            with m:
                st.markdown(
                    social_icons(30, 30, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url)
                    ,unsafe_allow_html=True)
            with r:
                st.empty()

    st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
    st.title("Dev Kotak")
    # Create header
    if choose == "About Me":
        #aboutme.createPage()
        with st.container():
            left_column, middle_column, right_column = st.columns((2,0.1,1))
            with left_column:
                st.header("About Me")
                st.subheader("Aspiring Machine Learnign Engineer/Data Scientist")
                st.write("👋🏻 Hi, I'm Dev! I'm a data science and analytics undergraduate based in Singapore. Having prior relevant experiences in tech, reinsurance and consulting sectors, I am constantly seeking unique internships to broaden my horizons before embarking on my data career upon graduation.")
                st.write("💼 With the COVID-19 pandemic behind us, I believe there is potential for data science to be applied in the retail industry. In response to the increasing demand for data analytics from both online and brick-and-mortar sales, I am thus aiming to enter this industry for my first full-time job.")
                st.write("🏋🏻 In addition, I like to exercise in the gym, run, write, play video games and... enjoy eating good food in my free time!")
                st.write("👨🏼‍💻 Academic interests: Data Visualization, Market Basket Analysis, Recommendation Systems, Natural Language Processing")
                st.write("💭 Ideal Career Prospects: Data Analyst, Data Scientist, Data Engineer, Business Intelligence Analyst, Product Manager")
            with right_column:
                st_lottie(lottie_coding, height=500, key="coding")
            
    elif choose == "Site Overview":   
        #overview.createPage()
        st.header("Site Overview")
        st.markdown("""
        - Originally, I started developing this website as a portfolio, essentially an extended resume. During the process, I realized the distinctive qualities of Streamlit compared to traditional front-end frameworks. While Streamlit is primarily used for creating web application dashboards, its extensive features make it more visually appealing to explore than alternatives such as Plotly and Shiny.
        """)
        with st.container():
                col1, col2, col3 = st.columns((1,3,1))
                with col1:
                    st.empty()
                with col2:
                    st.empty()
                with col3:
                    st.empty()
        st.markdown("""
        """)
# Create section for Work Experience
    elif choose == "Experience":
        #st.write("---")
        st.header("Experience")
        with st.container():
            image_column, text_column = st.columns((1,5))
            with image_column:
                st.image(img_bitmetrix)
            with text_column:
                st.subheader("Research Intern, [Space Application Center, ISRO](https://www.isro.gov.in/)")
                st.write("*December 2022 to May 2023*")
                st.markdown("""
                - Worked on Machine learning techniques to estimate hydrological flues over different river basins of India.
                - Performed Analysis on Indian river basins dataset.
                - Analysis of Rainfall, Evapotranspiration, Groundwater Recharge helped to manage water resources across rivers.
                - Technical Skills: `Python` `Google Earth Engine` `JavaScript` `Google Colab, Git`.
                - Soft Skills: `Presentation` `problem solving` `Time management` `Communication skills`.
                
                """)
        st.divider()        
        with st.container():
            image_column, text_column = st.columns((1,5))
            with image_column:
                st.image(img_scor)
            with text_column:
                st.subheader("Machine Learning Intern, [Jupiter AI Labs Pvt. Ltd.](https://juppiterailabs.com/)")
                st.write("*Dec 2022 to Feb 2023* | [*Certificate*](https://drive.google.com/file/d/1VYHlbY-K7cDr96Mv-6pRR6ev3idHyPeA/view?usp=sharing)")
                st.markdown("""
                - Created End to End Machine Learning solutions for Knowledge hut Client.
                - Worked on integration of ChatGpt and Chrome extensions.
                - Worked on AI Prompt Engineering project.
                - Technical Skills: `Python` `OpenAI` `TensorFlow` `Scikit-learn` `Git`
                - Soft Skills: `Innovation` `Detail oriented` `Decision-making` `Prioritization`

                """)
        st.divider()
        with st.container():
            image_column, text_column = st.columns((1,5))
            with image_column:
                st.image(img_zummit)
            with text_column:
                st.subheader("Data Science Intern, [Zummit Infolabs Pvt. Ltd.](https://zummitlabs.com/)")
                st.write("*June 2022 to Sept 2022*")
                st.markdown("""
                - Completed learning path containing python programming concepts.
                - Facial Features Detection using Dlib.
                - Worked on Emotion detection classifier model for Kaggle FER Dataset.
                - Performed Object Detection using YOLO.
                - Technical Skills: `Python` `NumPy` `Matplotlib` `Pandas` `TensorFlow` `Scikit-learn` `Git`
                - Soft Skills: `Teamwork` `Presentation skills` `Decision-making` `Dedication`
                """)
        st.divider()
        with st.container():
            image_column, text_column = st.columns((1,5))
            with image_column:
                st.image(img_dep)
            with text_column:
                st.subheader("Machine Learning Intern, [Devang Patel Institute of Advance Technology and Research(CHARUSAT)](https://charusat.ac.in/)")
                st.write("*May 2022 to June 2022* | [*Certificate*]()")
                st.markdown("""
                - Produced a lightweight solution for Yoga Pose estimation which predicts the yoga asanas using MediaPipe.
                - Classified Yoga poses using angle heuristic approach by detecting human poses and also worked on Research paper.
                - Worked on Deep Learning based solution for classification of Yoga asanas for the best results.
                - Technical Skills: `Python` `NumPy` `MediaPipe` `Pose Detection` `Pose Estimation` `OpenCV` `Git`
                - Soft Skills: `Research skills` `Time Management` `Writing Skills` `punctuality`
                """)
        st.divider()
        with st.container():
            image_column, text_column = st.columns((1,5))
            with image_column:
                st.image(img_kintu)
            with text_column:
                st.subheader("NodeJS and Botpress.io Intern, [Kintu Designs Pvt. Ltd.](https://kintudesigns.com/public/)")
                st.write("*June 2021 to September 2021*")
                st.markdown("""
                - Completed Node.JS course as a learning path for internship.
                - Worked on ChatBot using Botpress for Zipply - delivery Application.
                - Configured google maps API and other live tasks during the internship.
                - Technical Skills: `Botpress.io` `Node.js` `Express.Js` `MySql`
                - Soft Skills: `Cooperation` `Communication` `Problem Solving` `Logical Thinking`
                
                """)
        st.divider()
        with st.container():
            image_column, text_column = st.columns((1,5))
            with image_column:
                st.image(img_spark)
            with text_column:
                st.subheader("Data Science and Business Analytics Intern, [The Sparks Foundation](https://www.thesparksfoundationsingapore.org/)")
                st.write("*Jan 2021 to Feb 2021* | [*Testimonial*](https://drive.google.com/file/d/1O6Yu0P65dU8LCSDuXkf9BvlQJoz_5mRW/view?usp=sharing)")
                st.markdown("""
                - Predicted the study hours of students using Supervised Machine Learning algorithms.
                - Worked on Iris dataset and predicted the optimum number of clusters and represented it visually.
                - Used supervised and Unsupervised Machine learning algorithms for prediction tasks
                - Technical Skills: `Python` `Machine Learning`
                - Soft Skills: `Adaptability` `Work ethic` `Honesty`
                
                """)
        st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:0px;
        }
        </style>
        ''', unsafe_allow_html=True)
    # Subtitle

    elif choose == "Technical Skills":
    #st.write("---")
        st.header("Technical Skills")
        txt3("Programming Languages","`C/C++`, `Python`, `SQL`, `Java`, `MATLAB`")
        txt3("Academic Interests","`Data Visualization`, `Recommendation Systems`, `Natural Language Processing`")
        txt3("Data Visualization", "`matplotlib`, `seaborn`, `Plotly`, `Folium`, `GIS`,`Google Data Studio`")
        txt3("Database Systems", "`MySQL`, `SQLite`, `NoSQL`")
        txt3("Cloud Platforms", "`Google Cloud Platform`, `Streamlit Cloud`, `Hugging Face`")
        txt3("Natural Language Processing", "`NLTK`, `Word2Vec`, `TF-IDF`, `TextStat`")
        txt3("Version Control", "`Git`")
        txt3("Design and Front-end Development", "`Canva`, `HTML`, `CSS`, `Streamlit`, `Wordpress`")
        txt3("Data Science Techniques", "`Regression`, `Clustering`, `Random Forest`, `Decison Trees`, `Text Classification`, `Sentiment Analysis`, `Matrix Factorisation`")
        txt3("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `TensorFlow`, `Keras`")
        txt3("Task Management Tools", "`Notion`, `ClickUp`, `Slack`, `Jira`")
        txt3("Miscellaneous", "`Microsoft Office`, `Google Ads`")

# Create section for Education
#st.write("---")
    elif choose == "Education":
        st.header("Education")
        selected_options = ["Summary", "Modules"
                            ]
        selected = st.selectbox("Which section would you like to read?", options = selected_options)
        st.write("Current selection:", selected)
        if selected == "Summary":
            st.subheader("Summary")
            st.write("*Summary of education from primary school till university*")
            with st.container():
                image_column, text_column = st.columns((1,2.5))
                with image_column:
                    st.image(img_nus)
                with text_column:
                    st.subheader("Master of Engineering - [Electrical and Computer Engineering with collaborative specialization in Data Science], [Carleton University](https://carleton.ca/discover/) (2023-2025)")
                    st.write("Relevant Coursework: Pattern Classification and Experiment design , Applied Programming , Design Secure Network and Computer System")
                    st.markdown("""
                    - CGPA - 9.25/10.00 | WES-ICAP-Eveluation- 3.92/4.00
                    - Recipient of Mukhyamantri Yuva Swavalamban Yojana Scholarship.- 2019-23
                    
                    """)
            with st.container():
                image_column, text_column = st.columns((1,2.5))
                with image_column:
                    st.image(img_nus)
                with text_column:
                    st.subheader("Bachelor of Technology - [Computer Science and Engineering], [Charotar University of Science and Technology ](https://www.charusat.ac.in/) (2019-2023)")
                    st.write("Relevant Coursework: Java Programming, Object-oriented Programming with C++, Programming in Python, Data Structure & Algorithms, Design & Analysis of algorithms, Machine learning, Artificial Intelligence, Software Engineering, Theory of Computation, Data Communication & Networking, Computer Networks, Modern Networks")
                    st.markdown("""
                    - CGPA - 9.25/10.00 | WES-ICAP-Eveluation- 3.92/4.00
                    - Recipient of Mukhyamantri Yuva Swavalamban Yojana Scholarship.- 2019-23
                    
                    """)
            with st.container():
                image_column, text_column = st.columns((1,2.5))
                with image_column:
                    st.image(img_nus)
                with text_column:
                    st.subheader("Bachelor of Technology - [Computer Science and Engineering], [Charotar University of Science and Technology ](https://www.charusat.ac.in/) (2019-2023)")
                    st.write("Relevant Coursework: Java Programming, Object-oriented Programming with C++, Programming in Python, Data Structure & Algorithms, Design & Analysis of algorithms, Machine learning, Artificial Intelligence, Software Engineering, Theory of Computation, Data Communication & Networking, Computer Networks, Modern Networks")
                    st.markdown("""
                    - CGPA - 9.25/10.00 | WES-ICAP-Eveluation- 3.92/4.00
                    - Recipient of Mukhyamantri Yuva Swavalamban Yojana Scholarship.- 2019-23
                    
                    """)
            with st.container():
                image_column, text_column = st.columns((1,2.5))
                with image_column:
                    st.image(img_poc)
                with text_column:
                    st.subheader("Higher Secondary Education (Class- XI,XII) [Hiramohan Vidhyalaya](https://schools.org.in/surendranagar/24080503891/hira-mohan-vidhyalaya.html) (2017-2019)")
                    st.write("Coursework: Physics, Chemistry, Mathematics")
                    st.markdown("""
                    - Percentage - 82% Grade - A2
                    """)
            with st.container():
                image_column, text_column = st.columns((1,2.5))
                with image_column:
                    st.image(img_tpjc)
                with text_column:
                    st.subheader("Secondary Education (Class- X) [Ultravision Academy](http://www.ultravisionschool.com/) (2016 - 2017)")
                    st.write("Coursework: ")
                    st.markdown(""" 
                    - 
                    - 
                    """)
            
        elif selected == "Modules":
            st.subheader("Modules")
            st.write("*List of courses taken at Charotar University of Science and Technology*")
            with st.container():
                sem1, mid, sem2 = st.columns((1,0.1,1))
                with sem1:
                    st.write("**Academic Year 2019/20 Semester 1**")
                    st.markdown("""
                    |Code|Module Title                       |Credit|
                    |--------|--------------------------------------|---------|
                    |CE143| Computer Concepts and Programming       |5|
                    |CL142.01| Environmental Sciences              |2|
                    |EE145| Basics of Electronics and Electrical Engineering  |4|
                    |HS105.01 A| Liberal Arts - Media and Graphic Design          |2|
                    |IT144| ICT workshop         |1|
                    |MA143| Engineering Mathematics- I |4|
                    """)
                    st.write("")
                    st.markdown("""
                    Total Workload for Semester: **18 Modular Credits (Credit)**
                    """)
                with mid:
                    st.empty()
                with sem2:
                    st.write("**Academic Year 2020/21 Semester 2**")
                    st.markdown("""
                    |Code|Module Title                       |Credits|
                    |--------|--------------------------------------|---------|
                    |CE144|Object Oriented Programming with C++|5|
                    |HS126.01A|Communication Skills - I|2|
                    |MA144|Engineering Mathematics - II|4|
                    |ME145|Elements of Engineering |4|
                    |PY141.01|Engineering Physics|4|
                    """)
                    st.write("")
                    st.markdown("""
                    Total Workload for Semester: **19 Modular Credits (MCs)**
                    """)
            with st.container():
                sem1, mid, sem2 = st.columns((1,0.1,1))
                with sem1:
                    st.write("**Academic Year 2020/21 Semester 3**")
                    st.markdown("""
                    |Code|Module Title                       |Workload|
                    |--------|--------------------------------------|---------|
                    |CE244|Software Group Project - I|2|
                    |CE251|Java Programming|5|
                    |CE252|Digital Electronics|4|
                    |CE257|Data Communications and Networking|5|
                    |EC281.01|Introduction to Matlab Programming|2|
                    |HS121.02A|Creativity, Problem Solving and Innovation|2|
                    |MA253|Discrete Mathematics and Algebra|4|
                    """)
                    st.write("")
                    st.markdown("""
                    Total Workload for Semester: **24 Modular Credits (MCs)**
                    """)
                with mid:
                    st.empty()
                with sem2:
                    st.write("**Academic Year 2020/21 Semester4**")
                    st.markdown("""
                    |Code|Module Title                       |Workload|
                    |--------|--------------------------------------|---------|
                    |CS245|Data Structures and Algorithms|4|
                    |CE246|DataBase Management System|6|
                    |CE255|Software Group Project- II|2|
                    |CE258|Microprocessor and Computer Organization|5|
                    |CE259|Programming in Python|1|
                    |EC282.01|Prototyping Electronics with Arduino|2|
                    |HS111.02A|Human Values and Professional Ethics|2|
                    """)
                    st.write("")
                    st.markdown("""
                    Total Workload for Semester: **4 Modular Credits (MCs)**
                    """)
            with st.container():
                sem1, mid, sem2 = st.columns((1,0.1,1))
                with sem1:
                    st.write("**Academic Year 2021/22 Semester **")
                    st.markdown("""
                    |Code|Module Title                       |Workload|
                    |--------|--------------------------------------|---------|
                    |DSA2102|Essential Data Analytics Tools: Numerical Computation|4 MCs|
                    |EC2101|Microeconomic Analysis I|4 MCs|
                    |EC2102|Macroeconomic Analysis I|4 MCs|
                    |EC2204|Financial Accounting for Economists|4 MCs|
                    |EC3305|Programming Tools for Economics|4 MCs|
                    |GEH1049|Public Health in Action|4 MCs|
                    """)
                    st.write("")
                    st.markdown("""
                    Total Workload for Semester: **24 Modular Credits (MCs)**
                    """)
                with mid:
                    st.empty()
                with sem2:
                    st.write("**Academic Year 2021/22 Semester 2**")
                    st.markdown("""
                    |Code|Module Title                       |Workload|
                    |--------|--------------------------------------|---------|
                    |ALS1010|Learning to Learn Better|2 MCs|
                    |DSA2101|Essential Data Analytics Tools: Data Visualization|4 MCs|
                    |GES1037|A History of Singapore in Ten Objects|4 MCs|
                    |IS1103|Ethics in Computing|4 MCs|
                    |IT2002|Database Technology and Management|4 MCs|
                    |MA2104|Multivariable Calculus|4 MCs|
                    |ST2132|Mathematical Statistics|4 MCs|
                    """)
                    st.write("")
                    st.markdown("""
                    Total Workload for Semester: **26 Modular Credits (MCs)**
                    """)
            with st.container():
                sem1, mid, sem2 = st.columns((1,0.1,1))
                with sem1:
                    st.write("**Academic Year 2022/23 Semester 1**")
                    st.markdown("""
                    |Code|Module Title                       |Workload|
                    |--------|--------------------------------------|---------|
                    |CFG1003|Financial Wellbeing - Introduction|0 MCs|
                    |CS3244|Machine Learning|4 MCs|
                    |DSA3101|Data Science in Practice|4 MCs|
                    |DSA3102|Essential Data Analytics Tools: Convex Optimization|4 MCs|
                    |ST3131|Regression Analysis|4 MCs|
                    |ST3248|Statistical Learning I|4 MCs|
                    """)
                    st.write("")
                    st.markdown("""
                    Total Workload for Semester: **20 Modular Credits (MCs)**
                    """)
                with mid:
                    st.empty()
                with sem2:
                    st.write("**Academic Year 2022/23 Semester 2**")
                    st.markdown("""
                    |Code|Module Title                       |Workload|
                    |--------|--------------------------------------|---------|
                    |DSA4212|Optimization for Large-Scale Data-Driven Inference|4 MCs|
                    |LSM1301|General Biology|4 MCs|
                    |ST4248|Statistical Learning II|4 MCs|
                    """)
                    st.write("")
                    st.markdown("""
                    Total Workload for Semester: **12 Modular Credits (MCs)**
                    """)
            with st.container():
                sem1, mid, sem2 = st.columns((1,0.1,1))
                with sem1:
                    st.write("**Academic Year 2023/24 Semester 1 (Expected)**")
                    st.markdown("""
                    |Code|Module Title                       |Workload|
                    |--------|--------------------------------------|---------|
                    |CS4225|Big Data Systems for Data Science|4 MCs|
                    |DSA4299|Applied Project in Data Science and Analytics|16 MCs|
                    """)
                    st.write("")
                    st.markdown("""
                    Total Workload for Semester: **20 Modular Credits (MCs)**
                    """)
                with mid:
                    st.empty()
                with sem2:
                    st.write("**Academic Year 2022/23 Semester 2 (Expected)**")
                    st.markdown("""
                    |Code|Module Title                       |Workload|
                    |--------|--------------------------------------|---------|
                    |DSA426X|Sense-Making Case Analysis|4 MCs|
                    |ST4234|Bayesian Statistics|4 MCs|
                    """)
                    st.write("")
                    st.markdown("""
                    Total Workload for Semester: **8 Modular Credits (MCs)**
                    """)
            with st.container():
                left, mid, right = st.columns((0.1,1,0.1))
                with left:
                    st.empty()
                with mid:
                    st.write("**Graduation Requirements**")
                    st.image(img_dsa)
                with right:
                    st.empty()
        #elif selected == "Module Reviews":
            #st.subheader("Module Reviews")
            #st.write("*Reviews for selected modules taken in university*")


    elif choose == "Projects":
        # Create section for Projects
        #st.write("---")
        st.header("Projects")
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Blockchain Social Media Webscraper")
                st.write("*Project for US-based stealth startup, Bitmetrix.ai (in progress)*")
                st.markdown("""
                - Utilised snscrape to scrape tweets from top blockchain websites such as CoinGecko and CoinMarketCap
                - Built webscraper using BeautifulSoup4 to scrape content from fintech news websites such as https://blockchain.news
                """)
                # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
                mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/blockchain-webscraping",)
            with image_column:
                st.image(images_projects[14])
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Enhanced TikTok Analytics Dashboard")
                st.write("*Self-initiated project*")
                st.markdown("""
                - Provided options to plot Tiktok user overview data using 3D lineplots, 3D scatterplots, 3D surfaceplots and radar chart from Plotly
                - Filtered number of hashtags per Tiktok video to investigate relationship between hashtag count and other variables: views, comments, likes and shares
                - Performed hashtag analysis using Word2Vec to calculate cosine similarity scores and deduce correlation with average performance scores of each hashtag
                """)
                # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
                mention(label="Streamlit App", icon="streamlit", url="https://huggingface.co/spaces/harrychangjr/tiktok_analytics",)
                mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/tiktok-analytics",)
            with image_column:
                st.image(images_projects[13])
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Creating Sales Volume Prediction Model with Regression Methods")
                st.write("*Self-initiated project based on e-commerce case study*")
                st.markdown("""
                - Conducted exploratory data analysis (EDA) to identify relationships between variables using correlation heatmaps and histograms
                - Trained and compared multiple regression, random forest and XGBoost to build optimal model for sales volume prediction
                - Performed randomized search with cross-validation to increase performance of random forest regressor and reduce MSE
                """)
                # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
                mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/sales-prediction",)
            with image_column:
                st.image(images_projects[0])
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Optimising Article Quality with ChatGPT and NLP")
                st.write("*Self-initiated project using past articles written for module SP1541: Exploring Science Communication in Popular Science in Academic Year 2020/21 Semester 1*")
                st.markdown("""
                - Preliminary analysis - comparing word counts, readability scores and sentiment (compound) scores of all 6 article variants using NLTK and Textstat
                - Generated word clouds to highlight frequently used words in each article variant
                - Identified top 10 most commonly used words between variants of the same article to assess suitability of ChatGPT in enhancing article quality
                """)
                #st.write("[Github Repo](https://github.com/harrychangjr/sp1541-nlp)")
                mention(label="Streamlit App", icon="streamlit", url="https://sp1541-nlp.streamlit.app",)
                mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/sp1541-nlp",)
            with image_column:
                st.image(images_projects[1])
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Statistical Learning: Analysis on Video Game Sales")
                st.write("*Completed project within 48 hours for module ST4248: Statistical Learning II in Academic Year 2022/23 Semester 2*")
                #st.write("Methods performed on [Kaggle dataset](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings):")
                st.markdown("""
                - Utilised multiple regression to investigate impact of publishers on global sales by regression coefficient, including performing one-hot encoding on 'Publisher' categorical variable
                - Compared performances of multiple linear regression, random forest and XGBoost to predict global sales using critic scores and user scores from Metacritic
                - Trained linear mixed-effects model to investigate impact of publishers, platform and genres in global sales
                """)
                #st.write("[Github Repo](https://github.com/harrychangjr/st4248-termpaper) | [Term Paper](https://github.com/harrychangjr/st4248-termpaper/blob/main/ST4248%20Term%20Paper%20(A0201825N)%20v5.pdf)")
                mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/st4248-termpaper",)
            with image_column:
                st.image(images_projects[2])
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Statistical Learning: Nourish Your Body with Data")
                st.write("*Completed group project for module ST4248: Statistical Learning II in Academic Year 2022/23 Semester 2*")
                st.markdown("""
                - Adapted [previous project](https://drive.google.com/file/d/10ZOdQ8Q7UnevXxODAQs1YOstNSsiKh7G/view?usp=sharing) from DSA3101: Data Science in Practice, with the usage of statistical learning methods instead
                - Performed random forest classification and clustering methods to identify different consumer segments of grocery shoppers in supermarkets
                - Built recommendation system using matrix factorisation to recommend healthier food alternatives for grocery shoppers from different backgrounds
                """)
                #st.write("[Final Report](https://drive.google.com/file/d/1YuYxSTuDstSvyUa-bn782sLE5kCfbyH8/view?usp=sharing) | [Pitch Deck](https://www.canva.com/design/DAFeSnJeqgM/uXpz0kw8e7If4T1PG2tpaQ/view?utm_content=DAFeSnJeqgM&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Product Demo](https://www.youtube.com/watch?v=XMlt-kfdC7g)")
                mention(label="Final Report", icon="📄", url="https://drive.google.com/file/d/1YuYxSTuDstSvyUa-bn782sLE5kCfbyH8/view?usp=sharing",)
            with image_column:
                st.image(images_projects[3])
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Data Science Project on Biopics Dataset from Kaggle")
                st.write("*Self-initiated project using various machine learning methods on [biopics dataset](https://www.kaggle.com/datasets/fivethirtyeight/fivethirtyeight-biopics-dataset)*")
                st.markdown("""
                - Ran regression models to predict box office revenue (linear regression, random forest, support vector machines)
                - Used k-means clustering with principal components analysis to identify similar types of movies
                - Built content-based recommendation system using cosine similarity to recommend similar movies based on input title
                """)
                #st.write("[Github Repo](https://github.com/harrychangjr/biopics) | [RPubs](https://rpubs.com/harrychangjr/biopics)")
                mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/biopics",)
            with image_column:
                st.image(images_projects[4])
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Optimisation for Large-Scale Data-Driven Inference: Anime Recommendation System")
                st.write("*Completed assignment for module DSA4212: Optimisation for Large-Scale Data-Driven Inference in Academic Year 2022/23 Semester 2*")
                st.markdown("""
                - Built recommendation system using various non-factor models, including content-based collaborative filtering and clustering
                - Utilised matrix factorisation (single value decomposition) to optimise performance of recommendation system with lower test MSE
                - Provided optional recommendations to further optimise performance e.g scraping additional data, using deep learning methods
                """)
                #st.write("[Github Repo](https://github.com/harrychangjr/dsa4212) | [Report](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%202%20Group%2039%20Report.pdf)")
                mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/dsa4212",)
            with image_column:
                st.image(images_projects[5])
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Optimisation for Large-Scale Data-Driven Inference: Word Embedding")
                st.write("*Completed assigmment for module DSA4212: Optimisation for Large-Scale Data-Driven Inference in Academic Year 2022/23 Semester 2*")
                st.markdown("""
                - Trained Word2Vec model on 20 Newsgroups dataset from scikit-learn package in Python, which provides a number of similar words based on input word
                - Evaluated usefulness of model by applying model to text classification (46% accuracy) and sentiment analysis (86.4% accuracy)
                """)
                #st.write("[Github Code](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039.ipynb) | [Report](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039%20Report.pdf)")
                mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039.ipynb",)
            with image_column:
                st.image(images_projects[6])
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Data-Driven Marketing: Exploration of cellphone billing and subscriber data")
                st.write("*Self-initiated project based on past assignment from module BT4211: Data-Driven Marketing*")
                st.markdown("""
                - Performed preliminary churn analysis, customer segmentation and descriptive analysis to understand more about dataset
                - Trained logit and probit models, as well as providing model estimations for duration models
                - Utilised random forest classifier to predict customer churn
                """)
                #st.write("[Github Repo](https://github.com/harrychangjr/cellphone-billing) | [RPubs](https://rpubs.com/harrychangjr/cellphone)")
                mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/cellphone-billing",)
            with image_column:
                st.image(images_projects[7])
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Data Visualization: Analysis on Spotify Dataset from [tidytuesday](https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-01-21)")
                st.write("*Completed group project for module DSA2101: Essential Data Analytics Tools: Data Visualization in Academic Year 2021/22 Semester 2*")
                st.markdown("""
                - Investigated variables that differentiates songs of different genres, which could be useful in designing recommendation systems
                - Explored how do the four seasons affect number of songs produced in each period
                - Visualizations used: ridgeline faceted density plot, boxplot, line chart, faceted donut chart
                """)
                #st.write("[Github Code](https://github.com/harrychangjr/dsa2101/blob/main/DSA2101_Group%20B.Rmd) | [RPubs](https://rpubs.com/harrychangjr/dsa2101-groupb)")
                mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/dsa2101/blob/main/DSA2101_Group%20B.Rmd",)
            with image_column:
                st.image(images_projects[8])
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Computers and the Humanities: Chloropleths using Google Sheets and Folium in Python")
                st.write("*Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
                st.markdown("""
                - Visualized the total number of performances of A Doll's House by country, using a chloropleth from Google Sheets
                - Drafted scatterplots and boxplots using seaborn to investigate relationship between number of events per country and number of years these plays have been performed
                - Created chloropleth using Folium in Google Colab to compare total performance counts in China, categorised by province
                """)
                #st.write("[Google Sheets](https://docs.google.com/spreadsheets/d/1NBlGM7Sjcybbpl1Esa55qLRJw-Seti1LhC93EhV_68w/edit?usp=sharing) | [Google Colab](https://colab.research.google.com/drive/1RHqtb5XC7PkJDpNEb-BY3tO-8mI2j32E?usp=sharing)")
                mention(label="Google Drive", icon="🗂️", url="https://drive.google.com/drive/folders/1Iva0oLZim6zJlAndoSzR63pUq4NCznim?usp=share_link",)
            with image_column:
                st.image(images_projects[9])
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Computers and the Humanities: Network Analysis on Harry Potter Film Database")
                st.write("*Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
                st.markdown("""
                - Utilised custom Python file based on NetworkX and Glob to create networks using Harry Potter film database
                - Drafted visualizations using matplotlib and seaborn to compare densities and weighted degree values of nodes from generated networks
                - Customised network visualization using Gephi to investigate relationship between various Harry Potter film directors
                """)
                #st.write("[Github Code](https://github.com/harrychangjr/get1030/blob/main/A0201825N_GET1030_Tutorial_4.ipynb)")
                mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/get1030/blob/main/A0201825N_GET1030_Tutorial_4.ipynb",)
            with image_column:
                st.image(images_projects[10])
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Computers and the Humanities: Text Processing and Analysis on Song Lyrics")
                st.write("*Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
                st.markdown("""
                - Utilised custom Python file based on NetworkX and Glob to create networks using Harry Potter film database
                - Drafted visualizations using matplotlib and seaborn to compare proportions of nouns and verbs between different songs
                - Analysed type/token ratios of songs from both albums to evaluate which album produced better quality songs based on words used
                """)
                #st.write("[Github Code](https://github.com/harrychangjr/get1030/blob/main/A0201825N%20-%20GET1030%20Tutorial%203.ipynb)")
                mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/get1030/blob/main/A0201825N%20-%20GET1030%20Tutorial%203.ipynb",)
            with image_column:
                st.image(images_projects[11])
        with st.container():
            text_column, image_column = st.columns((3,1))
            with text_column:
                st.subheader("Computers and the Humanities: Spotify in the Covid-19 Era")
                st.write("*Completed group project for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
                st.markdown("""
                - Compiled and scraped Spotify data from [Spotify](https://www.spotifycharts.com), [Kaggle](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks), and [OWID](https://ourworldindata.org/coronavirus/country/singapore) to analyse top songs played in Singapore during Covid-19
                - Drafted Tableau dashboard to showcase correlation between various features of top songs, including tempo, acousticness and popularity
                - Embedded 30-second snippet of featured song on dashboard for increased interactiveness
                """)
                #st.write("[Github Code](https://github.com/harrychangjr/get1030/blob/main/A0201825N%20-%20GET1030%20Tutorial%203.ipynb)")
                mention(label="Final Report", icon="📄", url="https://github.com/harrychangjr/get1030/blob/main/GET1030%20Final%20Project.pdf",)
            with image_column:
                st.image(images_projects[12])
    elif choose == "Volunteering":
        st.header("Volunteering")
        with st.container():
            text_column, mid, image_column = st.columns((3,0.4,1))
            with text_column:
                st.subheader("NUS Product Club")
                st.write("*April 2023 to April 2024*")
                st.markdown("""
                Co-founder & President

                - Spearheaded design of club's logo
                - Drafted publicity posters on Canva to drive publicity and outreach efforts for recruitment
                - Oversaw committee of 24 members in carrying out operations, partnerships efforts and curriculum workshops for NUS students
                """)
            with mid:
                st.empty()
            with image_column:
                st.image(images_vol[9])
        with st.container():
            text_column, mid, image_column = st.columns((3,0.4,1))
            with text_column:
                st.subheader("NUS Statistics and Data Science Society")
                st.write("*May 2021 to November 2022*")
                st.markdown("""
                - President (2022) - Increased recruitment of student club by 50% while overseeing execution of career-related events and technical workshops organised by 56 members
                - Marketing Director (2021-22) - Led 10 students to secure over $19,000 worth of sponsorships for 850 participants in annual Data Analytics Competition and increase society's merchandise sales revenue by over 50% compared to previous year
                """)
            with mid:
                st.empty()
            with image_column:
                st.image(images_vol[0])
        with st.container():
            text_column, mid, image_column = st.columns((3,0.4,1))
            with text_column:
                st.subheader("NUS Students' Sports Club")
                st.write("*February to August 2022*")
                st.markdown("""
                Publicity Executive, NUS Inter-Faculty Games

                - Designed storyboard for publicity videos to hype up school-wide event
                - Increased publicity of event through extended outreach to over 5,000 students in various Telegram groups
                """)
            with mid:
                st.empty()
            with image_column:
                st.image(images_vol[1])
        with st.container():
            text_column, mid, image_column = st.columns((3,0.4,1))
            with text_column:
                st.subheader("Google Developer Student Clubs NUS")
                st.write("*September 2021 to April 2022*")
                st.markdown("""
                Deputy Head of Finance

                - Managed budget of student club alongside Core Team to ensure sufficient funds for technical workshops, hackathon and external projects
                - Liaised with staff advisors and administrative staff to seek funding approvals and process financial claims for other student members
                """)
            with mid:
                st.empty()
            with image_column:
                st.image(images_vol[2])
        with st.container():
            text_column, mid, image_column = st.columns((3,0.4,1))
            with text_column:
                st.subheader("NUS Students' Community Service Club")
                st.write("*March to July 2021*")
                st.markdown("""
                Organising Committee, Project Safe Space

                - Organised weekly sessions to empower individuals from Anglican Care Centre (Yishun) with important life skills (e.g Zumba, cooking)
                - Drafted write-ups on psychiatric conditions to raise awareness on debunked mental health myths and promote mental welness
                """)
            with mid:
                st.empty()
            with image_column:
                st.image(images_vol[3])
        with st.container():
            text_column, mid, image_column = st.columns((3,0.4,1))
            with text_column:
                st.subheader("NUS Students' Union")
                st.write("*January to March 2021*")
                st.markdown("""
                Public Relations Executive, Open Day Student Village

                - Liaised with participating student residences and clubs to increase awareness of event to prospective students
                - Enforced rules and regulations imposed by school administrative staff to ensure smooth execution of event
                """)
            with mid:
                st.empty()
            with image_column:
                st.image(images_vol[4])
        with st.container():
            text_column, mid, image_column = st.columns((3,0.4,1))
            with text_column:
                st.subheader("Saturday Kids")
                st.write("*October 2020 to December 2021 - Seasonal*")
                st.markdown("""
                Python Instructor, Code in the Community

                - Conducted weekly lessons for classes of 3-4 secondary school students on Python programming 
                - Customised curriculum structure to suit the learning needs of students
                """)
            with mid:
                st.empty()
            with image_column:
                st.image(images_vol[5])
        with st.container():
            text_column, mid, image_column = st.columns((3,0.4,1))
            with text_column:
                st.subheader("Singapore Institiute of Management - University of London")
                st.write("*November 2017*")
                st.markdown("""
                Fundraising Volunteer, SIM-UOL Transformers

                - Collected unwanted items from residents in heartland areas
                - Successfully raised $8000 from sale of items to refurbish the homes of the less fortunate
                """)
            with mid:
                st.empty()
            with image_column:
                st.image(images_vol[6])
        with st.container():
            text_column, mid, image_column = st.columns((3,0.4,1))
            with text_column:
                st.subheader("Tampines Junior College")
                st.write("*March 2015 to January 2016 - Seasonal*")
                st.markdown("""
                Values in Action (VIA) Projects

                - Climb for A Cause - Organised and participated in games and activities with members of Singapore Disability Sports Council
                - Project Ohana - Collaborated with Kwong Wai Shiu Hospital to engage patients in handicraft and games
                """)
            with mid:
                st.empty()
            with image_column:
                st.image(images_vol[7])
        with st.container():
            text_column, mid, image_column = st.columns((3,0.4,1))
            with text_column:
                st.subheader("Saint Joseph's Institution")
                st.write("*June 2012 to June 2013 - Seasonal*")
                st.markdown("""
                Values in Action (VIA) Projects

                - Josephian International Experience Programme - Conducted English lessons at orphanage in Siem Reap, Cambodia
                - SJIJ Primary 4 Chinese Language Camp - Acted as group facilitator to orientate primary four students in Chinese lessons
                """)
            with mid:
                st.empty()
            with image_column:
                st.image(images_vol[8])
    elif choose == "Contact":
    # Create section for Contact
        #st.write("---")
        st.header("Contact")
        def social_icons(width=24, height=24, **kwargs):
            icon_template = '''
            <a href="{url}" target="_blank" style="margin-right: 10px;">
                <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
            </a>
            '''

            icons_html = ""
            for name, url in kwargs.items():
                icon_src = {
                    "linkedin": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
                    "github": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
                    "email": "https://cdn-icons-png.flaticon.com/512/561/561127.png"
                }.get(name.lower())

                if icon_src:
                    icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

            return icons_html
        with st.container():
            text_column, mid, image_column = st.columns((1,0.2,0.5))
            with text_column:
                st.write("Let's connect! You may either reach out to me at devhkotak@gmail.com or use the form below!")
                #with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
                    #st.write('Please help us improve!')
                    #Name=st.text_input(label='Your Name',
                                        #max_chars=100, type="default") #Collect user feedback
                    #Email=st.text_input(label='Your Email', 
                                        #max_chars=100,type="default") #Collect user feedback
                    #Message=st.text_input(label='Your Message',
                                            #max_chars=500, type="default") #Collect user feedback
                    #submitted = st.form_submit_button('Submit')
                    #if submitted:
                        #st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')
                def create_database_and_table():
                    conn = sqlite3.connect('contact_form.db')
                    c = conn.cursor()
                    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                                (name TEXT, email TEXT, message TEXT)''')
                    conn.commit()
                    conn.close()
                create_database_and_table()

                st.subheader("Contact Form")
                if "name" not in st.session_state:
                    st.session_state["name"] = ""
                if "email" not in st.session_state:
                    st.session_state["email"] = ""
                if "message" not in st.session_state:
                    st.session_state["message"] = ""
                st.session_state["name"] = st.text_input("Name", st.session_state["name"])
                st.session_state["email"] = st.text_input("Email", st.session_state["email"])
                st.session_state["message"] = st.text_area("Message", st.session_state["message"])


                column1, column2= st.columns([1,5])
                if column1.button("Submit"):
                    conn = sqlite3.connect('contact_form.db')
                    c = conn.cursor()
                    c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                            (st.session_state["name"], st.session_state["email"], st.session_state["message"]))
                    conn.commit()
                    conn.close()
                    st.success("Your message has been sent!")
                    # Clear the input fields
                    st.session_state["name"] = ""
                    st.session_state["email"] = ""
                    st.session_state["message"] = ""
                def fetch_all_contacts():
                    conn = sqlite3.connect('contact_form.db')
                    c = conn.cursor()
                    c.execute("SELECT * FROM contacts")
                    rows = c.fetchall()
                    conn.close()
                    return rows
                
                if "show_contacts" not in st.session_state:
                    st.session_state["show_contacts"] = False
                if column2.button("View Submitted Forms"):
                    st.session_state["show_contacts"] = not st.session_state["show_contacts"]
                
                if st.session_state["show_contacts"]:
                    all_contacts = fetch_all_contacts()
                    if len(all_contacts) > 0:
                        table_header = "| Name | Email | Message |\n| --- | --- | --- |\n"
                        table_rows = "".join([f"| {contact[0]} | {contact[1]} | {contact[2]} |\n" for contact in all_contacts])
                        markdown_table = f"**All Contact Form Details:**\n\n{table_header}{table_rows}"
                        st.markdown(markdown_table)
                    else:
                        st.write("No contacts found.")


                st.write("Alternatively, feel free to check out my social accounts below!")
                linkedin_url = "https://www.linkedin.com/in/dev-kotak/"
                github_url = "https://github.com/dev856"
                email_url = "mailto:devhkotak@gmail.com"
                st.markdown(
                    social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                    unsafe_allow_html=True)
                st.markdown("")
                
            with mid:
                st.empty()
            with image_column:
                st.image(img_ifg)
    
    st.divider()

    st.write("##")
    
    st.write(f"""<div class="subtitle" style="text-align: center;">⬅️ Check out my Projects and other details in the navigation menu!</div>""", unsafe_allow_html=True)


if __name__=="__main__":
    home()


