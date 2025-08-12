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

# Custom CSS for biotech-themed styling
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
    
    .quiz-container {
        background: linear-gradient(135deg, #F5F5F5, #B2DFDB);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 2px solid #26A69A;
    }
    
    .certification-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #26A69A;
        transition: all 0.3s ease;
    }
    
    .certification-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

def navigation_sidebar():
    """Create interactive navigation sidebar"""
    st.sidebar.markdown("# 🧬 Navigation")
    
    # Visitor greeting
    visitor_name = st.sidebar.text_input("👋 What's your name?", value=st.session_state.visitor_name)
    if visitor_name:
        st.session_state.visitor_name = visitor_name
        st.sidebar.success(f"Welcome, {visitor_name}! 🎉")
    
    st.sidebar.markdown("---")
    
    # Navigation buttons
    pages = ["🏠 Home", "👨‍🔬 About Me", "🔬 Skills", "🏅 Certifications", 
             "💼 Projects", "🎯 Quiz", "📊 Skills Lab", "📞 Contact"]
    
    for page in pages:
        page_name = page.split(" ", 1)[1]
        if st.sidebar.button(page, key=f"nav_{page_name}"):
            st.session_state.current_page = page_name
            st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Biotech Stats")
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.metric("Research Projects", "4", "🧪")
    with col2:
        st.metric("Certifications", "6", "🏅")
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.metric("Lab Skills", "15+", "🔬")
    with col2:
        st.metric("Experience", "2+ yrs", "🌱")
    
    if st.sidebar.button("🎲 Biotech Fact"):
        facts = [
            "🧬 Engineered a gene knockout in under 48 hours!",
            "🔬 Proficient in 7+ advanced lab techniques",
            "🏆 Presented at 3 international biotech conferences",
            "🌍 Committed to sustainable bioprocessing solutions"
        ]
        st.sidebar.success(np.random.choice(facts))

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
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            if st.button("💼 LinkedIn", key="linkedin_btn"):
                st.balloons()
                st.success("Opening LinkedIn profile...")
        with col_b:
            if st.button("📚 ResearchGate", key="researchgate_btn"):
                st.balloons()
                st.success("Opening ResearchGate profile...")
        with col_c:
            if st.button("📧 Email", key="email_btn"):
                st.balloons()
                st.success("Opening email client...")

def render_about_page():
    """Render the about page with interactive timeline"""
    st.markdown('<h2 class="section-header">🎯 About Me</h2>', unsafe_allow_html=True)
    
    if st.button("📅 Show Biotech Journey"):
        with st.expander("🎓 My Biotech Journey", expanded=True):
            st.markdown("""
            **2020** - 🏁 Began B.Sc. in Biotechnology at MSA University
            
            **2021** - 🧪 Conducted first molecular biology experiments
            
            **2022** - 🔬 Mastered CRISPR-Cas9 and qPCR techniques
            
            **2023** - 🏆 Awarded Best Poster at Regional Biotech Symposium
            
            **2024** - 🏥 Completed internships in clinical diagnostics
            
            **2025** - 🎓 Graduated with honors in Biotechnology
            """)
    
    st.markdown("### 🧬 Discover My Biotech Passion!")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔬 My Research Interests"):
            st.info("🧬 Genome Editing | 🩺 Molecular Diagnostics | 🌿 Bioprocessing")
    
    with col2:
        if st.button("⚡ Biotech Fun Facts"):
            fun_facts = [
                "🧬 Engineered a gene knockout in under 48 hours!",
                "🔬 Proficient in 7+ advanced lab techniques",
                "🏆 Presented at 3 international biotech conferences",
                "🌍 Committed to sustainable bioprocessing solutions"
            ]
            for fact in fun_facts:
                st.write(fact)

def render_skills_page():
    """Render the skills page with interactive elements"""
    st.markdown('<h2 class="section-header">🔬 Biotech Skills Showcase</h2>', unsafe_allow_html=True)
    
    skill_category = st.selectbox(
        "🎯 Choose a skill category to explore:",
        ["🧬 Molecular Biology", "🔬 Laboratory Techniques", "💻 Bioinformatics", "🤝 Professional Skills"]
    )
    
    if skill_category == "🧬 Molecular Biology":
        skills = ["CRISPR-Cas9", "qPCR", "Western Blot", "DNA Sequencing", 
                 "RNA Interference", "Protein Expression", "Cloning", "Genotyping"]
        
        st.markdown("**Click on any skill to learn more!**")
        cols = st.columns(4)
        for i, skill in enumerate(skills):
            with cols[i % 4]:
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
                if st.button(f"Explore {skill}", key=f"bio_{i}"):
                    st.balloons()
                    if skill == "CRISPR-Cas9":
                        st.success("🧬 Precision genome editing with CRISPR-Cas9!")
                    elif skill == "qPCR":
                        st.success("📊 Quantitative PCR for gene expression analysis!")
                    elif skill == "DNA Sequencing":
                        st.success("🧬 Next-generation sequencing for genomic insights!")
                    else:
                        st.success(f"✨ Expert in {skill} - Driving biotech innovation!")
    
    elif skill_category == "💻 Bioinformatics":
        skills_data = {
            "Skill": ["Python", "R", "BLAST", "Sequence Alignment", "Molecular Modeling"],
            "Proficiency": [92, 88, 85, 80, 82]
        }
        df = pd.DataFrame(skills_data)
        for _, row in df.iterrows():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{row['Skill']}**")
                st.progress(row['Proficiency'] / 100)
            with col2:
                st.metric("Proficiency", f"{row['Proficiency']}%")

def render_certifications_page():
    """Render the certifications page"""
    st.markdown('<h2 class="section-header">🏅 Biotech Certifications</h2>', unsafe_allow_html=True)
    
    certifications = [
        {
            "title": "🧬 Advanced CRISPR Techniques",
            "provider": "BioTech Academy",
            "description": "Mastered cutting-edge genome editing technologies",
            "skills": ["CRISPR-Cas9", "Base Editing", "Prime Editing"]
        },
        {
            "title": "🔬 Clinical Diagnostics",
            "provider": "Global Diagnostics Institute",
            "description": "50-hour training in molecular and clinical diagnostics",
            "skills": ["qPCR", "ELISA", "Flow Cytometry"]
        },
        {
            "title": "🌿 Bioprocessing Fundamentals",
            "provider": "BioProcess International",
            "description": "Training in upstream and downstream bioprocessing",
            "skills": ["Fermentation", "Purification", "Process Optimization"]
        }
    ]
    
    for i, cert in enumerate(certifications):
        st.markdown(f'<div class="certification-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"**{cert['title']} - {cert['provider']}**")
            st.write(cert['description'])
            st.write("**Skills Gained:**")
            for skill in cert['skills']:
                st.write(f"• {skill}")
        with col2:
            if st.button(f"🎖️ Verify", key=f"cert_{i}"):
                st.success("Certificate verified! ✅")
        st.markdown('</div>', unsafe_allow_html=True)

def render_projects_page():
    """Render the projects page with tabs"""
    st.markdown('<h2 class="section-header">💼 Biotech Project Showcase</h2>', unsafe_allow_html=True)
    
    projects = [
        {
            "title": "🧬 CRISPR-Based Gene Therapy",
            "type": "Therapeutic Development",
            "description": "Developed a CRISPR-Cas9 system for targeting genetic mutations",
            "impact": "Potential treatment for hereditary diseases",
            "tech": ["CRISPR-Cas9", "Molecular Biology", "Bioinformatics"]
        },
        {
            "title": "🌱 Algal Bioprocessing",
            "type": "Bioprocessing Project",
            "description": "Optimized bioreactor conditions for sustainable biofuel production",
            "impact": "Eco-friendly energy solutions",
            "tech": ["Bioprocessing", "Fermentation", "Data Analysis"]
        },
        {
            "title": "🩺 Cancer Biomarker Detection",
            "type": "Diagnostics Research",
            "description": "Identified novel biomarkers for early cancer detection",
            "impact": "Improved diagnostic accuracy",
            "tech": ["qPCR", "Proteomics", "Bioinformatics"]
        }
    ]
    
    project_tabs = st.tabs([f"{p['title']}" for p in projects])
    
    for i, (tab, project) in enumerate(zip(project_tabs, projects)):
        with tab:
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f'<div class="project-card">', unsafe_allow_html=True)
                st.markdown(f"**{project['title']}**")
                st.write(f"**Type:** {project['type']}")
                st.write(f"**Description:** {project['description']}")
                st.write(f"**Impact:** {project['impact']}")
                if st.button("🔍 Show Technical Details", key=f"proj_{i}"):
                    st.write("**Technologies Used:**")
                    for tech in project['tech']:
                        st.write(f"• {tech}")
                st.markdown('</div>', unsafe_allow_html=True)
            with col2:
                st.markdown("### 📊 Project Metrics")
                st.metric("Research Duration", "8 months", "📅")
                st.metric("Team Size", "4 members", "👥")
                st.metric("Publications", "2 papers", "📄")

def create_bubble_sort_animation():
    """Animated sequence alignment visualization using Streamlit bar chart"""
    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
    
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

def render_quiz_page():
    """Render the interactive quiz page"""
    st.markdown('<h2 class="section-header">🎯 Biotechnology Knowledge Quiz</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="quiz-container">
        <h3>🧠 Test Your Biotech Knowledge!</h3>
        <p>Take this fun quiz to explore biotechnology concepts!</p>
    </div>
    """, unsafe_allow_html=True)
    
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

def render_skills_lab_page():
    """Render the skills lab with visualizations"""
    st.markdown('<h2 class="section-header">📊 Biotech Skills Laboratory</h2>', unsafe_allow_html=True)
    
    skills_data = {
        "Skill": ["CRISPR-Cas9", "qPCR", "Bioinformatics", "Bioprocessing", "Molecular Diagnostics", "Scientific Communication"],
        "Proficiency": [90, 80, 70, 80, 90, 90]
    }
    df = pd.DataFrame(skills_data)
    
    for _, row in df.iterrows():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{row['Skill']}**")
            st.progress(row['Proficiency'] / 100)
        with col2:
            st.metric("Proficiency", f"{row['Proficiency']}%")
    
    st.markdown("### 🔬 Sequence Alignment Visualization")
    create_bubble_sort_animation()

def render_contact_page():
    """Render the interactive contact page"""
    st.markdown('<h2 class="section-header">📬 Let\'s Connect!</h2>', unsafe_allow_html=True)
    
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
    elif st.session_state.current_page == "About Me":
        render_about_page()
    elif st.session_state.current_page == "Skills":
        render_skills_page()
    elif st.session_state.current_page == "Certifications":
        render_certifications_page()
    elif st.session_state.current_page == "Projects":
        render_projects_page()
    elif st.session_state.current_page == "Quiz":
        render_quiz_page()
    elif st.session_state.current_page == "Skills Lab":
        render_skills_lab_page()
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
