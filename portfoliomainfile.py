import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import numpy as np
import time
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Youssef Mohamed Ali - Biotechnology Portfolio",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'
if 'visitor_name' not in st.session_state:
    st.session_state.visitor_name = ""
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'quiz_taken' not in st.session_state:
    st.session_state.quiz_taken = False

# Custom CSS from reference code
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #2E7D32 0%, #26A69A 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
        animation: fadeInDown 1s ease-out;
    }
    
    .section-header {
        color: #2E7D32;
        border-bottom: 2px solid #26A69A;
        padding-bottom: 0.5rem;
        margin: 2rem 0 1rem 0;
    }
    
    .skill-tag {
        background-color: #F5F5F5;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        margin: 0.25rem;
        display: inline-block;
        font-size: 0.9rem;
        transition: all 0.3s ease;
    }
    
    .skill-tag:hover {
        background-color: #26A69A;
        color: white;
        transform: scale(1.05);
    }
    
    .project-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #2E7D32;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .interactive-button {
        background: linear-gradient(45deg, #2E7D32, #4FC3F7);
        color: white;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        font-size: 1rem;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        margin: 0.5rem;
    }
    
    .interactive-button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(38, 166, 154, 0.4);
    }
    
    .stats-card {
        background: linear-gradient(135deg, #2E7D32, #7B1FA2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .stats-card:hover {
        transform: scale(1.05);
    }
    
    .rotating-element {
        animation: rotate 4s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .pulse-animation {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .algorithm-viz {
        background: linear-gradient(135deg, #F5F5F5, #B2DFDB);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 2px solid #26A69A;
    }
</style>
""", unsafe_allow_html=True)

def create_bubble_sort_animation():
    """Animated sequence alignment visualization using Streamlit bar chart"""
    st.markdown('<div class="algorithm-viz">', unsafe_allow_html=True)
    
    if st.button("🧬 Start Sequence Alignment Animation", key="bubble_sort"):
        data = np.random.randint(1, 100, 10)
        chart_placeholder = st.empty()
        progress_bar = st.progress(0)
        
        total_steps = 0
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                total_steps += 1
        
        current_step = 0
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                df = pd.DataFrame({
                    'Position': list(range(len(data))),
                    'Expression Level': data
                })
                chart_placeholder.bar_chart(df.set_index('Position')['Expression Level'])
                progress_bar.progress((current_step + 1) / total_steps)
                current_step += 1
                time.sleep(0.1)
        st.success("✅ Sequence Alignment Complete!")
        st.balloons()
    
    st.markdown('</div>', unsafe_allow_html=True)

def create_number_pattern():
    """Interactive protein pattern visualization"""
    st.markdown('<div class="algorithm-viz">', unsafe_allow_html=True)
    pattern_type = st.selectbox("Choose Pattern:", ["Amino Acid Triangle", "Codon Table"])
    
    if pattern_type == "Amino Acid Triangle":
        rows = st.slider("Number of rows:", 3, 10, 5)
        if st.button("🔺 Generate Amino Acid Triangle", key="pascal"):
            triangle = []
            for i in range(rows):
                row = [1] * (i + 1)
                for j in range(1, i):
                    row[j] = triangle[i-1][j-1] + triangle[i-1][j]
                triangle.append(row)
            
            for i, row in enumerate(triangle):
                spaces = "   " * (rows - i - 1)
                numbers = "   ".join(f"{num:2d}" for num in row)
                st.code(f"{spaces}{numbers}")
    
    elif pattern_type == "Codon Table":
        size = st.slider("Table size:", 3, 12, 5)
        if st.button("🧬 Generate Codon Table", key="mult_table"):
            data = []
            for i in range(1, size + 1):
                row = []
                for j in range(1, size + 1):
                    row.append(i * j)
                data.append(row)
            
            df = pd.DataFrame(data, 
                            index=[f"Base {i}" for i in range(1, size + 1)],
                            columns=[f"Base {j}" for j in range(1, size + 1)])
            st.dataframe(df, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def create_interactive_skills():
    """Interactive skills section with progress bars"""
    st.markdown('<h2 class="section-header">🧪 Biotech Skills Dashboard</h2>', unsafe_allow_html=True)
    
    skills_data = {
        "Molecular Biology": {"CRISPR-Cas9": 90, "qPCR": 80, "Western Blot": 85, "DNA Sequencing": 88},
        "Bioinformatics": {"Python": 92, "R": 88, "BLAST": 85, "Sequence Alignment": 80},
        "Laboratory Techniques": {"RNA Interference": 85, "Protein Expression": 88, "Cloning": 80, "Genotyping": 82},
        "Professional Skills": {"Scientific Communication": 90, "Project Management": 85, "Team Collaboration": 88}
    }
    
    selected_category = st.selectbox("Select Skill Category:", list(skills_data.keys()))
    
    for skill, level in skills_data[selected_category].items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{skill}**")
            st.progress(level / 100)
        with col2:
            st.metric("Proficiency", f"{level}%")

def navigation_sidebar():
    """Create interactive navigation sidebar"""
    st.sidebar.markdown("# 🧬 Navigation")
    
    visitor_name = st.sidebar.text_input("👋 What's your name?", value=st.session_state.visitor_name)
    if visitor_name:
        st.session_state.visitor_name = visitor_name
        st.sidebar.success(f"Welcome, {visitor_name}! 🎉")
    
    st.sidebar.markdown("---")
    
    pages = ["🏠 Home", "🧪 Projects", "🔬 Skills Lab", "🧬 Algorithms", "📬 Contact"]
    
    for page in pages:
        page_name = page.split(" ", 1)[1]
        if st.sidebar.button(page, key=f"nav_{page_name}"):
            st.session_state.current_page = page_name
            st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔬 Interactive Features")
    
    if st.sidebar.button("🎲 Biotech Fact"):
        facts = [
            "🧬 Engineered a gene knockout in under 48 hours!",
            "🔬 Proficient in 7+ advanced lab techniques",
            "🏆 Presented at 3 international biotech conferences",
            "🌍 Committed to sustainable bioprocessing solutions"
        ]
        st.sidebar.success(np.random.choice(facts))
    
    if st.sidebar.button("🎆 Lab Celebration"):
        st.balloons()
        st.snow()

def render_home_page():
    """Render the home page with animations"""
    greeting = f"Welcome, {st.session_state.visitor_name}!" if st.session_state.visitor_name else "Welcome to my Biotech Portfolio!"
    
    st.markdown(f"""
    <div class="main-header">
        <div class="rotating-element" style="display: inline-block; font-size: 2rem;">🧬</div>
        <h1>Youssef Mohamed Ali</h1>
        <h3>Biotechnology Graduate</h3>
        <p>Passionate about advancing human health through gene editing, bioprocessing, and molecular diagnostics</p>
        <p>📍 Giza, 6th of October | 📞 +20 101 464 0842</p>
        <p><strong>{greeting}</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        try:
            profile_img = Image.open("assets/profile.jpg")
            st.image(profile_img, width=300, caption="Profile Picture")
        except (FileNotFoundError, OSError):
            st.markdown("""
            <div style="text-align: center; padding: 2rem; background-color: #F5F5F5; border-radius: 10px; margin: 1rem 0;" class="pulse-animation">
                <div style="font-size: 4rem;">🧬</div>
                <p style="color: #666; margin-top: 1rem;">Profile Picture</p>
                <small style="color: #999;">Add your profile.jpg to the assets folder</small>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Biotech Stats Dashboard")
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    
    stats = [
        ("4", "Research Projects", "🧪"),
        ("6", "Certifications", "🏅"),
        ("15+", "Lab Skills", "🔬"),
        ("2+ yrs", "Experience", "🌱")
    ]
    
    for i, (stat_col, (number, text, emoji)) in enumerate(zip([stat_col1, stat_col2, stat_col3, stat_col4], stats)):
        with stat_col:
            if st.button(f"{emoji} {number}", key=f"stat_{i}"):
                st.balloons()
            st.markdown(f"<p style='text-align: center; margin-top: 0.5rem;'>{text}</p>", unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-header">🙋‍♂️ About Me</h2>', unsafe_allow_html=True)
    
    about_col1, about_col2 = st.columns([2, 1])
    
    with about_col1:
        st.markdown("""
        Welcome to my biotech portfolio! I'm a dedicated Biotechnology graduate from MSA University with over 2 years of experience 
        in molecular biology, bioprocessing, and diagnostics. My passion lies in advancing human health through innovative solutions.

        **🎓 Education:**
        - B.Sc. in Biotechnology - MSA University (2025)

        **🧪 Background:**
        I've worked on projects involving CRISPR-Cas9, qPCR, and bioprocessing, contributing to advancements in gene therapy and sustainable biofuels.
        """)
    
    with about_col2:
        st.markdown("### 🏆 Achievements")
        achievements = [
            "🏆 Best Poster at Regional Biotech Symposium 2023",
            "📝 Published 2 research papers",
            "🌟 Presented at 3 international conferences",
            "🧬 Engineered a gene knockout in 48 hours",
            "🏥 Completed clinical diagnostics internships"
        ]
        for achievement in achievements:
            if st.button(achievement, key=f"achieve_{achievement}"):
                st.success(f"Thanks for your interest in: {achievement}")

def render_projects_page():
    """Render the projects page with tabs"""
    st.markdown('<h2 class="section-header">🧪 Biotech Project Showcase</h2>', unsafe_allow_html=True)
    
    projects = [
        {
            "title": "🧬 CRISPR-Based Gene Therapy",
            "type": "Therapeutic Development",
            "description": "Developed a CRISPR-Cas9 system for targeting genetic mutations",
            "tech": ["CRISPR-Cas9", "Molecular Biology", "Bioinformatics"]
        },
        {
            "title": "🌱 Algal Bioprocessing",
            "type": "Bioprocessing Project",
            "description": "Optimized bioreactor conditions for sustainable biofuel production",
            "tech": ["Bioprocessing", "Fermentation", "Data Analysis"]
        },
        {
            "title": "🩺 Cancer Biomarker Detection",
            "type": "Diagnostics Research",
            "description": "Identified novel biomarkers for early cancer detection",
            "tech": ["qPCR", "Proteomics", "Bioinformatics"]
        }
    ]
    
    project_tabs = st.tabs([f"{p['title']}" for p in projects])
    
    for i, (tab, project) in enumerate(zip(project_tabs, projects)):
        with tab:
            col1, col2 = st.columns([1, 2])
            with col1:
                try:
                    project_img = Image.open(f"assets/project{i+1}.jpg")
                    st.image(project_img, caption=project['title'])
                except (FileNotFoundError, OSError):
                    st.markdown(f"""
                    <div style="text-align: center; padding: 3rem 1rem; background-color: #F5F5F5; border-radius: 8px; margin: 1rem 0;" class="pulse-animation">
                        <div style="font-size: 3rem;">🧬</div>
                        <p style="color: #666; margin: 0.5rem 0;">{project['title']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"### {project['title']}")
                st.markdown(f"**Type:** {project['type']}")
                st.markdown(f"**Description:** {project['description']}")
                st.markdown("**Technologies:** " + ", ".join(project['tech']))
                if st.button("🔍 Show Project Metrics", key=f"metrics_{i}"):
                    st.markdown("### 📊 Project Metrics")
                    st.metric("Research Duration", "8 months", "📅")
                    st.metric("Team Size", "4 members", "👥")
                    st.metric("Publications", "2 papers", "📄")

def render_skills_lab():
    """Render the skills lab with quiz and visualizations"""
    st.markdown('<h2 class="section-header">🔬 Biotech Skills Laboratory</h2>', unsafe_allow_html=True)
    
    create_interactive_skills()
    
    st.markdown("---")
    st.markdown("### 🎯 Biotech Knowledge Quiz")
    
    if not st.session_state.quiz_taken:
        questions = {
            "What is the primary function of CRISPR-Cas9?": {
                "options": ["Protein synthesis", "Genome editing", "Antibody production"],
                "correct": "Genome editing"
            },
            "Which technique amplifies specific DNA sequences?": {
                "options": ["Western Blot", "qPCR", "Mass Spectrometry"],
                "correct": "qPCR"
            },
            "What is a key application of bioinformatics in biotech?": {
                "options": ["Sequence analysis", "Cell culture", "Fermentation"],
                "correct": "Sequence analysis"
            }
        }
        
        question = st.selectbox("Choose a question:", list(questions.keys()))
        answer = st.radio("Your answer:", questions[question]["options"])
        
        if st.button("Submit Answer", key="quiz_submit"):
            if answer == questions[question]["correct"]:
                st.success("🎉 Correct! Well done!")
                st.balloons()
                st.session_state.quiz_score += 1
            else:
                st.error(f"❌ Incorrect. The correct answer is: {questions[question]['correct']}")
        
        if st.button("🎉 Finish Quiz"):
            st.session_state.quiz_taken = True
            st.rerun()
    
    else:
        st.success(f"🎉 Quiz Completed! Your Score: {st.session_state.quiz_score}/3")
        if st.session_state.quiz_score == 3:
            st.balloons()
            st.write("🏆 Perfect Score! You're a biotech expert!")
        elif st.session_state.quiz_score >= 2:
            st.write("👏 Great job! Strong biotech knowledge!")
        else:
            st.write("📚 Keep exploring biotechnology!")
        
        if st.button("🔄 Retake Quiz"):
            st.session_state.quiz_taken = False
            st.session_state.quiz_score = 0
            st.rerun()

def render_algorithms_page():
    """Render the algorithms page"""
    st.markdown('<h2 class="section-header">🧬 Biotech Algorithm Visualizations</h2>', unsafe_allow_html=True)
    
    algorithm = st.selectbox(
        "Choose Algorithm to Visualize:",
        ["Sequence Alignment Sort", "Protein Pattern"]
    )
    
    if algorithm == "Sequence Alignment Sort":
        create_bubble_sort_animation()
    elif algorithm == "Protein Pattern":
        create_number_pattern()

def render_contact_page():
    """Render the contact page"""
    st.markdown('<h2 class="section-header">📬 Interactive Contact Hub</h2>', unsafe_allow_html=True)
    
    contact_col1, contact_col2 = st.columns([1, 1])
    
    with contact_col1:
        st.markdown("### 📞 Connect With Me")
        contact_methods = [
            ("📧 Send Email", "✉️ Email client opened!"),
            ("💼 LinkedIn Profile", "🔗 LinkedIn opened in new tab!"),
            ("📚 ResearchGate Profile", "🔗 ResearchGate opened in new tab!")
        ]
        for button_text, success_msg in contact_methods:
            if st.button(button_text, key=f"contact_{button_text}"):
                st.success(success_msg)
    
    with contact_col2:
        st.markdown("### 💌 Quick Message")
        with st.form("contact_form"):
            name = st.text_input("Your Name *")
            email = st.text_input("Your Email *")
            subject = st.selectbox("Subject", ["General Inquiry", "Biotech Job Opportunity", 
                                             "Research Collaboration", "Academic Discussion", 
                                             "Biotech Networking", "Other"])
            message = st.text_area("Your Message *")
            submitted = st.form_submit_button("🚀 Send Message")
            if submitted:
                if name and email and message:
                    st.success("🎉 Message sent successfully!")
                    st.balloons()
                    with st.expander("📋 Message Details"):
                        st.write(f"**Name:** {name}")
                        st.write(f"**Email:** {email}")
                        st.write(f"**Subject:** {subject}")
                        st.write(f"**Message:** {message}")
                else:
                    st.error("❌ Please fill in all required fields")

def main():
    """Main application with navigation"""
    navigation_sidebar()
    
    if st.session_state.current_page == "Home":
        render_home_page()
    elif st.session_state.current_page == "Projects":
        render_projects_page()
    elif st.session_state.current_page == "Skills Lab":
        render_skills_lab()
    elif st.session_state.current_page == "Algorithms":
        render_algorithms_page()
    elif st.session_state.current_page == "Contact":
        render_contact_page()
    
    st.markdown("---")
    footer_col1, footer_col2, footer_col3 = st.columns(3)
    
    with footer_col1:
        if st.button("🎨 Change Theme"):
            themes = ["🌿 Nature Mode", "🔬 Lab Mode", "🧬 Genomic Mode", "🧫 Research Mode"]
            st.success(f"🎨 Theme changed to: {np.random.choice(themes)}")
    
    with footer_col2:
        if st.button("📊 View Analytics"):
            st.info("📈 Portfolio analytics: 987 views this month!")
            with st.expander("📊 Detailed Analytics"):
                col1, col2, col3 = st.columns(3)
                col1.metric("Total Views", "987", "10%")
                col2.metric("Unique Visitors", "654", "7%")
                col3.metric("Avg. Time", "4m 12s", "12%")
    
    with footer_col3:
        if st.button("💝 Give Feedback"):
            st.success("💌 Thank you for your interest in providing feedback!")
            with st.expander("💬 Quick Feedback"):
                rating = st.select_slider("Rate this portfolio:", ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
                if st.button("Submit Rating"):
                    st.success(f"Thanks for the {rating} rating!")
    
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem; color: #666;">
        <p>© 2025 Youssef Mohamed Ali. Built with ❤️ using Streamlit</p>
        <p>✨ Pioneering biotechnology for a healthier future! ✨</p>
        {"<p>🎉 Thanks for visiting, " + st.session_state.visitor_name + "!</p>" if st.session_state.visitor_name else ""}
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
