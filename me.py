import streamlit as st
import base64

#---Miscellaneous---#
st.set_page_config(layout="centered")
st.snow()

def get_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

image_base64 = get_image("profile.jpg")

#--- Introduction Page ---#
st.markdown("<h1 style='font-size:82px; text-align:center; text-shadow: 0 0 5px #63c5da, 0 0 5px #63c5da, 0 0 10px #63c5da;'>My Autobiography</h1>", unsafe_allow_html=True)
st.write("&nbsp;")

col1, col2 = st.columns([1,1])
with col1:
    st.markdown(f"""
        <style>
        .intro-container {{
            display: flex;
            align-items: flex-start;
            justify-content: flex-start;
        }}
    .intro-photo {{
        float: left;
        margin-right: 20px;
        border-radius: 15px;
        width: 350px;
        border: 3px solid #4a90e2;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.1);
    }}
    </style>

    <div class="intro-container">
        <img src="data:image/png;base64,{image_base64}" class="intro-photo" />
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <style>
    .intro-text {{
        text-align: justify;
        font-size: 17px;
        line-height: 1.6;
    }}
    </style>

    <div class="intro-text">
            <p>
            Hello! I'm <strong>Sydney B. Galorio</strong> — a curious mind navigating through this technological 
            world filled with knowledge waiting to be uncovered. I am an individual who persistently seeks growth 
            and has a passion for learning. As I continue my journey, I keep on seeking purpose and meaning in 
            everything I do.  
            </p>
            <p>
            My story begins in a humble city of Bayugan, Agusan del Sur where imagination was my greatest companion.
            Growing up, I found myself fascinated by both mathematics with its logic and numbers. 
            I enjoyed solving problems and exploring the beauty of mathematical concepts. 
            This passion eventually led me to the world of programming, where I could bring my ideas to 
            life through code. From coding small programs to crafting digital worlds through design and storytelling.
            </p>
            <p>
            This autobiography shares the moments that defined me: the failures that taught me resilience,  
            the friendships that strengthened me, and the dreams that continue to drive me forward.
            </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---- Education and Achievements --- #

st.markdown(f"""<h2 style='font-size:45px; text-align:center; text-shadow: 0 0 5px #63c5da, 0 0 5px #63c5da, 0 0 10px #63c5da;'>📚 Education and Achievements</h2>
                <p style='font-size:17px; text-align:justify;'>
                A journey of knowledge and accomplishments that shaped who I am today. 
                Throughout my academic path, I’ve gained not only knowledge from the classroom 
                but also valuable experiences through collaboration, projects, and personal exploration.
                </p>
            """, unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["🌱 Nursery", "🏫 Elementary", "🏫 Highschool", "🏫 Baccalaureate"])

with tab1:
    st.header("🌱 Little Steps Learning Center")
    st.markdown(f"""
            <h5>Bayugan City, Agusan del Sur</h5>
            <p> 📅 2008 - 2010<br>
                🌟 Graduated with Honors<br>
                🏅 Most Talkative Award</p>
    """,  unsafe_allow_html=True)

with tab2:
    st.header("🏫 Agusan del Sur Pilot Laboratory School")
    st.markdown(f"""
            <h5>Bayugan City, Agusan del Sur</h5>
            <p> 📅 2011 - 2017<br>
                🌟 Graduated with High Honors<br>
                🏅 Consistent Honors<br> </p>
    """,  unsafe_allow_html=True)

with tab3:
    st.header("🏫 Philippine Science High School - Caraga Region Campus")
    st.markdown(f"""
            <h5>Butuan City, Ampayon</h5>
            <p> 📅 2017 - 2023<br>
                🌟 Graduated with High Honors<br>
                🏅 Consistent Director's List<br>
                🏅 Best Speaker Awardee (Chemistry) - School Research Symposium<br>
                🏅 Best Research (Chemistry) - School Research Symposium<br>
                🏅 3rd Place - Best Research (Chemistry) - National Research Summit<br></p>
    """,  unsafe_allow_html=True)

with tab4:
    st.header("🏫 Cebu Institute of Technology - University")
    st.markdown(f"""
            <h5>Cebu City, Cebu</h5>
            <p> 📅 2023 - Present<br>
                🌟 Pursuing a Bachelor of Science in Computer Science<br>
                🏅 Consistent Academic Scholar<br></p>
    """,  unsafe_allow_html=True)

st.divider()

# --- Skills and Interests --- #

st.markdown(f"""<h2 style='font-size:45px; text-align:center; text-shadow: 0 0 5px #63c5da, 0 0 5px #63c5da, 0 0 10px #63c5da;'>⚙️ Skills and Interests</h2>
            <p style='font-size:17px; text-align:justify;'>
            A diverse set of skills and interests that I have developed along my journey.
            The different environments I've exposed myself to have allowed me to cultivate a wide range of abilities.
            These skills fuel my passion for technology and creativity.
            </p>
            """, unsafe_allow_html=True)

st.markdown("""
- **Programming Languages:** Python, Java, C++, C#
- **Frameworks:** Streamlit, Django, Firebase, Figma, Canva, Unreal Engine
- **Tools:** Git, GitHub, Visual Studio Code, Jupyter Notebook
- **Soft Skills:** Problem-Solving, Teamwork, Communication, Perseverance and Fortitude
- **Interests:** Data Analysis, Data Science, Game Development
""")

st.divider()

# ---- Future Goals and Aspirations --- #

st.markdown(f"""<h2 style='font-size:40px; text-align:center; text-shadow: 0 0 5px #63c5da, 0 0 5px #63c5da, 0 0 10px #63c5da;'>🎯 Goals and Aspirations</h2>
            <p style='font-size:17px; text-align:justify;'>
            The set of goals and aspirations that drive me forward.
            As I continue my journey, I am committed to pursuing excellence in my field and 
            making a positive impact on the world around me. I aim to continuously learn, grow, 
            and contribute to the ever-evolving landscape of technology.
            </p>
            <h4>💫 Personal Goals:</h4>
            <ul> 
                <li>Achieve 100% in all the video games in my Steam Library.</li>
                <li>Learn about game design and development, and create my own game.</li>
                <li>Stay consistent with my routine and achieve target body weight.</li>
                <li>Recreate more cooking recipes.</li>
                <li>Keep being curious. Explore new things.</li>
                <li>Always try to be better</li>
            </ul>
            <h4>🎓 Academic Goals</h4>
            <ul>
                <li>Graduate with honors in Computer Science.</li>
                <li>Develop a strong foundation in programming and software development.</li>
                <li>Participate in hackathons and coding competitions.</li>
                <li>Build a strong academic portfolio through personal and capstone projects.</li>
            </ul>
            <h4>💼 Professional Goals</h4>
            <ul>
                <li>Secure an internship or entry-level position in a reputable tech company.</li>
                <li>Contribute to open-source projects to gain real-world experience.</li>
                <li>Pass relevant certifications such as PL300, DP300, AZ-900 to enhance my credentials.</li>
                <li>Continuously improve my coding skills and stay updated with industry trends.</li>
                <li>Network with professionals in the tech industry to learn and grow.</li>
            </ul>
            """, unsafe_allow_html=True)

st.divider()

#---- Contact Information --- #

st.markdown("<h2 style='font-size:45px; text-align:center; text-shadow: 0 0 5px #63c5da, 0 0 5px #63c5da, 0 0 10px #63c5da;'>📬 Contact Information</h2>", unsafe_allow_html=True)
st.markdown(f"""
            <p>
            If you would like to get in touch with me, feel free to reach out through any of the platforms below:
            </p>
            <ul>
                <li>📧 Personal Email: sydneygalorio@gmail.com</li>
                <li>🌐 School Email: sydney.galorio@cit.edu</li>
                <li>📞 SMS/Call: +639932766074</li>
            </ul>
            """, unsafe_allow_html=True)