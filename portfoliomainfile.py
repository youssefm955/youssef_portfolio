import streamlit as st
import base64
from PIL import Image
import requests
from io import BytesIO
import time
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Configure page
st.set_page_config(
    page_title="Youssef Mohamed Ali - Biotechnology Portfolio",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for interactions
if 'visitor_name' not in st.session_state:
    st.session_state.visitor_name = ""
if 'show_details' not in st.session_state:
    st.session_state.show_details = {}
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'quiz_taken' not in st.session_state:
    st.session_state.quiz_taken = False

# Custom CSS for biotechnology-themed styling and animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Open Sans', sans-serif;
    }
    
    .main-header {
        text-align: center;
        padding: 3rem 0;
        background: linear-gradient(135deg, #2e7d32 0%, #4caf50 50%, #81c784 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
        animation: fadeInDown 1s ease-out;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-50px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(50px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .section-header {
        color: #1b5e20;
        border-bottom: 3px solid #4caf50;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
        animation: fadeInUp 0.8s ease-out;
        position: relative;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -3px;
        left: 0;
        width: 0;
        height: 3px;
        background: linear-gradient(90deg, #4caf50, #81c784);
        animation: expandWidth 2s ease-out forwards;
    }
    
    @keyframes expandWidth {
        to { width: 100%; }
    }
    
    .skill-tag {
        background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
        padding: 0.4rem 1rem;
        border-radius: 25px;
        margin: 0.3rem;
        display: inline-block;
        font-size: 0.9rem;
        color: #1b5e20;
        border: 2px solid transparent;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .skill-tag:hover {
        background: linear-gradient(135deg, #4caf50, #81c784);
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
        animation: pulse 1s infinite;
    }
    
    .project-card {
        background: linear-gradient(135deg, #f1f8e9, #e8f5e9);
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #4caf50;
        margin-bottom: 1.5rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        cursor: pointer;
        animation: fadeInUp 1s ease-out;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        border-left: 5px solid #1976d2;
    }
    
    .interactive-btn {
        background: linear-gradient(135deg, #1976d2, #2196f3);
        color: white;
        padding: 0.8rem 2rem;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        font-size: 1rem;
        transition: all 0.3s ease;
        margin: 0.5rem;
        box-shadow: 0 5px 15px rgba(25, 118, 210, 0.4);
    }
    
    .interactive-btn:hover {
        background: linear-gradient(135deg, #2196f3, #1976d2);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(25, 118, 210, 0.6);
    }
    
    .certification-card {
        background: linear-gradient(135deg, #ffffff, #f1f8e9);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #1976d2;
        margin-bottom: 1rem;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .certification-card:hover {
        transform: translateX(10px);
        box-shadow: 0 5px 20px rgba(25, 118, 210, 0.3);
    }
    
    .quiz-container {
        background: linear-gradient(135deg, #4fc3f7, #0288d1);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        animation: fadeInUp 1s ease-out;
    }
    
    .contact-form {
        background: linear-gradient(135deg, #f1f8e9, #e8f5e9);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 1rem;
        border: 1px solid #e8f5e9;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .stats-card {
        background: linear-gradient(135deg, #43a047, #66bb6a);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .stats-card:hover {
        transform: scale(1.05);
    }
    
    .floating-icon {
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("## 🧬 Navigation")
    
    # Visitor greeting
    visitor_name = st.text_input("👋 What's your name?", value=st.session_state.visitor_name)
    if visitor_name:
        st.session_state.visitor_name = visitor_name
        st.success(f"Welcome, {visitor_name}! 🎉")
    
    st.markdown("---")
    
    # Interactive menu
    menu_option = st.selectbox(
        "🔍 Explore Sections:",
        ["🏠 Home", "👨‍🔬 About Me", "🔬 Skills", "🏅 Certifications", 
         "💼 Projects", "🎯 Interactive Quiz", "📊 Skills Chart", "📞 Contact"]
    )
    
    st.markdown("---")
    
    # Quick stats
    st.markdown("### 📊 Biotech Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Research Projects", "4", "🧪")
    with col2:
        st.metric("Certifications", "6", "🏅")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Lab Skills", "15+", "🔬")
    with col2:
        st.metric("Experience", "2+ yrs", "🌱")

# Main content based on menu selection
if menu_option == "🏠 Home" or menu_option == "":
    # Header Section with animation
    greeting = f"Welcome, {st.session_state.visitor_name}!" if st.session_state.visitor_name else "Welcome to my Biotech Portfolio!"
    
    st.markdown(f"""
    <div class="main-header">
        <div class="floating-icon">🧬</div>
        <h1>Youssef Mohamed Ali</h1>
        <h3>Biotechnology Graduate</h3>
        <p>Passionate about advancing human health through gene editing, bioprocessing, and molecular diagnostics</p>
        <p>📍 Giza, 6th of October | 📞 +20 101 464 0842</p>
        <p><strong>{greeting}</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive profile section
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image("https://via.placeholder.com/300x300/4caf50/FFFFFF?text=Biotech+Profile+Photo", width=300)
        
        # Interactive buttons
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

elif menu_option == "👨‍🔬 About Me":
    st.markdown('<h2 class="section-header">🎯 About Me</h2>', unsafe_allow_html=True)
    
    # Interactive timeline
    if st.button("📅 Show Biotech Journey"):
        with st.expander("🎓 My Biotech Journey", expanded=True):
            st.markdown("""
            *2020* - 🏁 Began B.Sc. in Biotechnology at MSA University
            
            *2021* - 🧪 Conducted first molecular biology experiments
            
            *2022* - 🔬 Mastered CRISPR-Cas9 and qPCR techniques
            
            *2023* - 🏆 Awarded Best Poster at Regional Biotech Symposium
            
            *2024* - 🏥 Completed internships in clinical diagnostics
            
            *2025* - 🎓 Graduated with honors in Biotechnology
            """)
    
    # Interactive personality test
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

elif menu_option == "🔬 Skills":
    st.markdown('<h2 class="section-header">🚀 Biotech Skills Showcase</h2>', unsafe_allow_html=True)
    
    # Skill categories with interactive elements
    skill_category = st.selectbox(
        "🎯 Choose a skill category to explore:",
        ["🧬 Molecular Biology", "🔬 Laboratory Techniques", "💻 Bioinformatics", "🤝 Professional Skills"]
    )
    
    if skill_category == "🧬 Molecular Biology":
        skills = ["CRISPR-Cas9", "qPCR", "Western Blot", "DNA Sequencing", 
                 "RNA Interference", "Protein Expression", "Cloning", "Genotyping"]
        
        st.markdown("*Click on any skill to learn more!*")
        
        cols = st.columns(4)
        for i, skill in enumerate(skills):
            with cols[i % 4]:
                if st.button(skill, key=f"bio_{i}"):
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
        tech_skills = ["Python", "R", "BLAST", "Sequence Alignment", "Molecular Modeling"]
        
        # Interactive skill rating
        st.markdown("### 📊 Skill Proficiency Levels")
        for skill in tech_skills:
            proficiency = st.slider(f"{skill}", 1, 10, 8, key=f"tech_{skill}")
            st.write(f"{skill}: {'⭐' * proficiency}")

elif menu_option == "🏅 Certifications":
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
        with st.expander(f"{cert['title']} - {cert['provider']}", expanded=False):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.write(cert['description'])
                st.write("*Skills Gained:*")
                for skill in cert['skills']:
                    st.write(f"• {skill}")
            with col2:
                if st.button(f"🎖 Verify", key=f"cert_{i}"):
                    st.success("Certificate verified! ✅")

elif menu_option == "💼 Projects":
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
    
    selected_project = st.selectbox("🔍 Select a project to explore:", 
                                   [f"{p['title']} - {p['type']}" for p in projects])
    
    project_index = next(i for i, p in enumerate(projects) 
                        if f"{p['title']} - {p['type']}" == selected_project)
    project = projects[project_index]
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"### {project['title']}")
        st.write(f"*Type:* {project['type']}")
        st.write(f"*Description:* {project['description']}")
        st.write(f"*Impact:* {project['impact']}")
        
        if st.button("🔍 Show Technical Details", key=f"proj_{project_index}"):
            st.write("*Technologies Used:*")
            for tech in project['tech']:
                st.write(f"• {tech}")
    
    with col2:
        st.markdown("### 📊 Project Metrics")
        st.metric("Research Duration", "8 months", "📅")
        st.metric("Team Size", "4 members", "👥")
        st.metric("Publications", "2 papers", "📄")

elif menu_option == "🎯 Interactive Quiz":
    st.markdown('<h2 class="section-header">🎯 Biotechnology Knowledge Quiz</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="quiz-container">
        <h3>🧠 Test Your Biotech Knowledge!</h3>
        <p>Take this fun quiz to explore biotechnology concepts!</p>
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.quiz_taken:
        questions = [
            {
                "question": "What is the primary function of CRISPR-Cas9?",
                "options": ["Protein synthesis", "Genome editing", "Antibody production"],
                "correct": 1
            },
            {
                "question": "Which technique amplifies specific DNA sequences?",
                "options": ["Western Blot", "qPCR", "Mass Spectrometry"],
                "correct": 1
            },
            {
                "question": "What is a key application of bioinformatics in biotech?",
                "options": ["Sequence analysis", "Cell culture", "Fermentation"],
                "correct": 0
            }
        ]
        
        score = 0
        for i, q in enumerate(questions):
            st.write(f"*Question {i+1}:* {q['question']}")
            answer = st.radio(f"Choose your answer for Q{i+1}:", q['options'], key=f"q{i}")
            if st.button(f"Submit Answer {i+1}", key=f"submit_{i}"):
                if q['options'].index(answer) == q['correct']:
                    st.success("✅ Correct!")
                    score += 1
                else:
                    st.error(f"❌ Incorrect. The right answer is: {q['options'][q['correct']]}")
        
        if st.button("🎉 Finish Quiz"):
            st.session_state.quiz_score = score
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

elif menu_option == "📊 Skills Chart":
    st.markdown('<h2 class="section-header">📊 Biotech Skills Visualization</h2>', unsafe_allow_html=True)
    
    # Create interactive charts
    skills_data = {
        'Skill Category': ['CRISPR-Cas9', 'qPCR', 'Bioinformatics', 
                          'Bioprocessing', 'Molecular Diagnostics', 'Scientific Communication'],
        'Proficiency Level': [9, 8, 7, 8, 9, 9],
        'Experience (Months)': [18, 24, 12, 15, 20, 36]
    }
    
    df = pd.DataFrame(skills_data)
    
    chart_type = st.selectbox("📈 Choose visualization type:", 
                             ["Bar Chart", "Radar Chart", "Scatter Plot"])
    
    if chart_type == "Bar Chart":
        fig = px.bar(df, x='Skill Category', y='Proficiency Level', 
                     title="🎯 Biotech Skill Proficiency",
                     color='Proficiency Level',
                     color_continuous_scale='Greens')
        st.plotly_chart(fig, use_container_width=True)
    
    elif chart_type == "Radar Chart":
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=df['Proficiency Level'],
            theta=df['Skill Category'],
            fill='toself',
            name='Proficiency'
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            showlegend=False,
            title="🕸 Biotech Skills Radar"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    elif chart_type == "Scatter Plot":
        fig = px.scatter(df, x='Experience (Months)', y='Proficiency Level',
                        size='Proficiency Level', hover_name='Skill Category',
                        title="📈 Experience vs Proficiency in Biotech")
        st.plotly_chart(fig, use_container_width=True)

elif menu_option == "📞 Contact":
    st.markdown('<h2 class="section-header">📬 Let\'s Connect!</h2>', unsafe_allow_html=True)
    
    # Interactive contact form
    contact_reason = st.selectbox(
        "🎯 What's the purpose of your message?",
        ["👋 General Inquiry", "💼 Biotech Job Opportunity", "🔬 Research Collaboration", 
         "🎓 Academic Discussion", "🤝 Biotech Networking", "💡 Other"]
    )
    
    if contact_reason:
        st.write(f"Great! You selected: *{contact_reason}*")
        
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("👤 Your Name *")
            email = st.text_input("📧 Your Email *")
        
        with col2:
            company = st.text_input("🏢 Company/Institution")
            phone = st.text_input("📞 Phone Number")
        
        message = st.text_area("💬 Your Message *", height=150,
                              placeholder="Share your thoughts on biotech collaboration, opportunities, or research ideas...")
        
        if st.button("🚀 Send Message"):
            if name and email and message:
                st.success("🎉 Thank you! Your message has been sent successfully!")
                st.balloons()
                st.info("I'll respond within 24 hours!")
            else:
                st.error("❗ Please fill in all required fields (Name, Email, Message)")

# Footer with visitor counter simulation
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #4caf50; padding: 2rem 0;">
    <p>© 2025 Youssef Mohamed Ali | Built with ❤ using Streamlit</p>
    <p>🧬 <em>Pioneering biotechnology for a healthier future</em></p>
    {"<p>🎉 Thanks for visiting, " + st.session_state.visitor_name + "!</p>" if st.session_state.visitor_name else ""}
</div>
""", unsafe_allow_html=True)

# Add some interactive elements at the bottom
if st.button("🎊 Celebrate Biotech Innovation!"):
    st.balloons()
    st.success("🎉 Thank you for exploring my biotech portfolio!")
