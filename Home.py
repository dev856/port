import streamlit as st
import base64
!pip install streamlit_option_menu
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
    
    # Assets for education
    img_sji = Image.open("images/charusat.jpg")
    img_nus = Image.open("images/charusat.jpg")
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
                st.write("👋🏻 Hi, I'm Harry! I'm a data science and analytics undergraduate based in Singapore. Having prior relevant experiences in tech, reinsurance and consulting sectors, I am constantly seeking unique internships to broaden my horizons before embarking on my data career upon graduation.")
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
        - Originally, I started developing this website as a portfolio, essentially an extended resume. During the process, I realized the distinctive qualities of Streamlit compared to traditional front-end frameworks like Angular and Bootstrap. While Streamlit is primarily used for creating web application dashboards, its extensive features make it more visually appealing to explore than alternatives such as Plotly and Shiny.
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
                - Built social media scraper using snscrape to scrape Tweets from popular blockchain websites based on rankings from CoinGecko and CoinMarketCap.
                - Constructed webscraper using Streamlit and BeautifulSoup4 to collate news articles from various sources (e.g https://blockchain.news) into Pandas dataframe for future analysis using natural language processing methods.
                
                `Python` `BeautifulSoup4` `snscrape` `Streamlit` `Pandas`
                """)
        with st.container():
            image_column, text_column = st.columns((1,5))
            with image_column:
                st.image(img_scor)
            with text_column:
                st.subheader("Actuarial Intern, [SCOR](https://scor.com)")
                st.write("*May to August 2022* | [*Testimonial*](https://drive.google.com/file/d/1seUP5OcXV5irA1Y1qt0cKnd7uQnLJLzw/view?usp=share_link)")
                st.markdown("""
                - Performed actuarial analysis of reinsurance treaties in various APAC markets, including entry of client portfolio and loss data into xAct (treaty pricing system)
                - Regularly updated and analysed risk profiles and claims databases for insurance markets in Pakistan, Thailand and Vietnam
                - Trained machine learning models (logistic regression, random forest) to predict insurance claims, with an average accuracy of 80% for each model

                `Excel` `Python` `R` `xAct` `VBA`
                """)
        with st.container():
            image_column, text_column = st.columns((1,5))
            with image_column:
                st.image(img_sshsph)
            with text_column:
                st.subheader("Public Health Intern, [Saw Swee Hock School of Public Health](https://sph.nus.edu.sg/)")
                st.write("*January to May 2021*")
                st.markdown("""
                - Conducted literature reviews and summarized papers related to public health
                - Drafted case study report on British population health system, including impacts from COVID-19
                - Collaborated with other students to compare successes and challenges of Britain, Canada and New Zealand’s healthcare systems
                """)
        with st.container():
            image_column, text_column = st.columns((1,5))
            with image_column:
                st.image(img_iasg)
            with text_column:
                st.subheader("Data Migration Intern, [Immigration@SG LLP](https://iasg.com.sg/)")
                st.write("*October 2020 to January 2021* | [*Testimonial*](https://drive.google.com/file/d/11qFI-9TMfjOk1OxuyQ9ho9A7D6KuIsXp/view?usp=sharing)")
                st.markdown("""
                - Cleaned over 30,000 records using Pandas to facilitate smooth data migration into new CRM system
                - Derived customer segmentation models using regression models and market basket analysis (association rule mining) to improve company’s marketing strategies
                - Completed time series analysis using past sales data to forecast future monthly revenue

                `Excel` `ggplot2` `Python` `pandas` `R`
                """)
        with st.container():
            image_column, text_column = st.columns((1,5))
            with image_column:
                st.image(img_yll)
            with text_column:
                st.subheader("Temporary Management Support Staff, [Yong Loo Lin School of Medicine](https://medicine.nus.edu.sg/)")
                st.write("*February to June 2019*")
                st.markdown("""
                - Answered up to 100 different queries daily regarding undergraduate admissions
                - Managed venue preparations for admissions interviews involving over 1,000 candidates over the span of 2 weeks
                - Supported set-up of faculty booth for NUS Open House, with an estimated attendance of 30,000 visitors in one day
                """)
        with st.container():
            image_column, text_column = st.columns((1,5))
            with image_column:
                st.image(img_saf)
            with text_column:
                st.subheader("Administrative Support Assistant, [Singapore Armed Forces](https://www.mindef.gov.sg/web/portal/mindef/home)")
                st.write("*January 2017 to January 2019* | [*Testimonial*](https://drive.google.com/file/d/1O6Yu0P65dU8LCSDuXkf9BvlQJoz_5mRW/view?usp=sharing)")
                st.markdown("""
                - Assisted in organising division-level In-Camp Trainings, conferences and welfare events
                - Handled daily administration of Operations Branch, including indentation of office equipment, budget management and food rations
                - Promoted to Corporal First Class (CFC) for outstanding efforts
                
                `Excel` `GeBiz` `GIS` `Outlook` `PowerPoint` `Word`
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
        txt3("Programming Languages","`R`, `Python`, `SQL`, `Java`, `Stata`, `MATLAB`")
        txt3("Academic Interests","`Data Visualization`, `Market Basket Analysis`, `Recommendation Systems`, `Natural Language Processing`")
        txt3("Data Visualization", "`ggplot2`, `matplotlib`, `seaborn`, `Plotly`, `Folium`, `Gephi`, `GIS`, `Tableau`, `Power BI`, `Google Data Studio`, `Domo`, `Google Analytics`")
        txt3("Database Systems", "`MySQL`, `PostgreSQL`, `SQLite`, `NoSQL`, `Google BigQuery`, `Cloud Firestore`")
        txt3("Cloud Platforms", "`Google Cloud Platform`, `Amazon Web Services`, `Heroku`, `Streamlit Cloud`, `Render`, `Hugging Face`")
        txt3("Natural Language Processing", "`NLTK`, `Word2Vec`, `TF-IDF`, `TextStat`")
        txt3("Version Control", "`Git`, `Docker`")
        txt3("Design and Front-end Development", "`Canva`, `Figma`, `HTML`, `CSS`, `Streamlit`, `Wordpress`")
        txt3("Data Science Techniques", "`Regression`, `Clustering`, `Association Rules Mining`, `Random Forest`, `Decison Trees`, `Principal Components Analysis`, `Text Classification`, `Sentiment Analysis`, `Matrix Factorisation`, `Collaborative Filtering`")
        txt3("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `TensorFlow`, `Keras`, `JAX`")
        txt3("Task Management Tools", "`Asana`, `Notion`, `ClickUp`, `Slack`, `Jira`, `Confluence`")
        txt3("Miscellaneous", "`Google Firebase`, `Microsoft Office`, `Retool`, `Google Ads`")

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
                    st.subheader("Bachelor of Science - [Data Science and Analytics](https://www.stat.nus.edu.sg/wp-content/uploads/sites/8/2022/12/NUS-CHS-DSA-Print-FA.pdf), [National University of Singapore](https://nus.edu.sg) (2020-2024)")
                    st.write("Relevant Coursework: Computers and the Humanities, Convex Optimization, Data Science in Practice, Data Structures and Algorithms, Data Visualization, Database Technology and Management, Linear Algebra, Multivariable Calculus, Optimization for Large-Scale Data-Driven Inference, Probability, Programming Tools for Economics, Regression Analysis, Statistical Learning")
                    st.markdown("""
                    - [NUS Product Club](https://linkedin.com/company/nusproductclub) - Co-founder & President (2023-24)
                    - [NUS Statistics and Data Science Society](https://sites.google.com/view/nussds/home) - President (2022), Marketing Director (2021-22)
                    - [Google Developer Student Clubs NUS](https://dsc.comp.nus.edu.sg/) - Deputy Head of Finance (2021-22)
                    """)
            with st.container():
                image_column, text_column = st.columns((1,2.5))
                with image_column:
                    st.image(img_poc)
                with text_column:
                    st.subheader("Bachelor of Science - Pharmaceutical Science, [National University of Singapore](https://nus.edu.sg) (2019)")
                    st.write("Coursework: Foundations of Medicinal Chemistry, Pharmaceutical Biochemistry, Statistics for Life Sciences, Human Anatomy and Physiology, Quantitative Reasoning")
                    st.markdown("""
                    Withdrew from course in 2020, before performing a clean slate transfer to pursue a Bachelor's Degree in Data Science and Analytics
                    - [NUS Students' Science Club](https://www.nussciencelife.com/) - Marketing Executive, Welfare Subcommittee
                    - Pharmaceutical Science (Class of 2023) - Assistant Class Representative
                    """)
            with st.container():
                image_column, text_column = st.columns((1,2.5))
                with image_column:
                    st.image(img_tpjc)
                with text_column:
                    st.subheader("GCE A Level - [Tampines Junior College](https://www.tmjc.moe.edu.sg/our-heritage/tampines-jc/) (2015 - 2016)")
                    st.write("Coursework: H2 Chemistry, H2 Economics, H2 Mathematics, H1 Project Work, H1 Chinese, H1 History")
                    st.markdown(""" 
                    - Track and Field - 100m (2016 A Division Semi-finalist), 200m, 4x100m
                    - TPJC Economics and Financial Literacy Fair 2015 - Games Facilitator
                    """)
            with st.container():
                image_column, text_column = st.columns((1,2.5))
                with image_column:
                    st.image(img_sji)
                with text_column:
                    st.subheader("GCE O Level - [Saint Joseph's Institution](https://www.sji.edu.sg/) (2012 - 2014)")
                    st.write("Coursework: English, Mathematics, Additional Mathematics, Physics, Chemistry, History, Geography Elective, Chinese")
                    st.markdown(""" 
                    - Track and Field (Long Jump, 100m)
                    - [Business Design Thinking](https://www.sp.edu.sg/sp/news/sp/Secondary-students-learn-to-innovate)
                    - Josephian International Experience Programme (Siem Reap, Cambodia)
                    """)
            with st.container():
                image_column, text_column = st.columns((1,2.5))
                with image_column:
                    st.image(img_gmss)
                with text_column:
                    st.subheader("Secondary One - [Geylang Methodist School (Secondary)](https://www.geylangmethodistsec.moe.edu.sg/) (2011)")
                    st.write("Coursework: English, Mathematics, Science, History, Geography, Literature, Chinese, Design & Technology, Home Economics")
                    st.markdown(""" 
                    - Volleyball
                    """)
            with st.container():
                image_column, text_column = st.columns((1,2.5))
                with image_column:
                    st.image(img_sjij)
                with text_column:
                    st.subheader("Primary School Leaving Examination - [Saint Joseph's Institution Junior](https://www.sjijunior.moe.edu.sg/) (2005 - 2010)")
                    st.write("Coursework: English, Mathematics, Science, Chinese, Higher Chinese")
                    st.markdown(""" 
                    - Art Club
                    """)
        elif selected == "Modules":
            st.subheader("Modules")
            st.write("*List of modules taken at National University of Singapore*")
            with st.container():
                sem1, mid, sem2 = st.columns((1,0.1,1))
                with sem1:
                    st.write("**Academic Year 2019/20 Semester 1**")
                    st.markdown("""
                    |Code|Module Title                       |Workload|
                    |--------|--------------------------------------|---------|
                    |AY1130| Human Anatomy and Physiology I       |4 MCs|
                    |GER1000| Quantitative Reasoning              |4 MCs|
                    |PR1110A| Foundations for Medicinal Chemistry |4 MCs|
                    |PR1111A|Pharmaceutical Biochemistry          |4 MCs|
                    |ST1232| Statistics for Life Sciences         |4 MCs|
                    """)
                    st.write("")
                    st.markdown("""
                    Total Workload for Semester: **20 Modular Credits (MCs)**
                    """)
                with mid:
                    st.empty()
                with sem2:
                    st.write("**Academic Year 2020/21 Semester 1**")
                    st.markdown("""
                    |Code|Module Title                       |Workload|
                    |--------|--------------------------------------|---------|
                    |CS1010S|Programming Methodology|4 MCs|
                    |DSA1101|Introduction to Data Science|4 MCs|
                    |GER1000|Quantitative Reasoning|4 MCs|
                    |MA1102R|Calculus|4 MCs|
                    |SP1541|Exploring Science Communication Through Popular Science|4 MCs|
                    """)
                    st.write("")
                    st.markdown("""
                    Total Workload for Semester: **20 Modular Credits (MCs)**
                    """)
            with st.container():
                sem1, mid, sem2 = st.columns((1,0.1,1))
                with sem1:
                    st.write("**Academic Year 2020/21 Semester 2**")
                    st.markdown("""
                    |Code|Module Title                       |Workload|
                    |--------|--------------------------------------|---------|
                    |CFG1002|Career Catalyst|2 MCs|
                    |EC1301|Principles of Economics|4 MCs|
                    |GEQ1000|Asking Questions|4 MCs|
                    |GES1010|Nation-Building in Singapore|4 MCs|
                    |GET1030|Computers and the Humanities|4 MCs|
                    |MA1101R|Linear Algebra I|4 MCs|
                    |ST2131|Probability|4 MCs|
                    """)
                    st.write("")
                    st.markdown("""
                    Total Workload for Semester: **26 Modular Credits (MCs)**
                    """)
                with mid:
                    st.empty()
                with sem2:
                    st.write("**Academic Year 2020/21 Special Term (Part II)**")
                    st.markdown("""
                    |Code|Module Title                       |Workload|
                    |--------|--------------------------------------|---------|
                    |CS2040|Data Structures and Algorithms|4 MCs|
                    """)
                    st.write("")
                    st.markdown("""
                    Total Workload for Semester: **4 Modular Credits (MCs)**
                    """)
            with st.container():
                sem1, mid, sem2 = st.columns((1,0.1,1))
                with sem1:
                    st.write("**Academic Year 2021/22 Semester 1**")
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
   
    
    st.divider()

    st.write("##")
    
    st.write(f"""<div class="subtitle" style="text-align: center;">⬅️ Check out my Projects and other details in the navigation menu! )</div>""", unsafe_allow_html=True)


if __name__=="__main__":
    home()


