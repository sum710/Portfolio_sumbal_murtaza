import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Sumbal Murtaza | Portfolio", page_icon="🛡️", layout="wide")

# --- CUSTOM CSS FOR A PREMIUM PROFESSIONAL THEME ---
st.markdown("""
<style>
    /* Gradient text for the main name */
    .main-header {
        font-size: 3.2rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #2b5876, #4e4376);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }
    
    /* Sleek subtitle */
    .sub-header {
        font-size: 1.4rem;
        font-weight: 500;
        color: #555555;
        margin-top: 5px;
        margin-bottom: 25px;
    }
    
    /* Custom info box for the summary */
    .info-box {
        background-color: #f8f9fa;
        padding: 25px;
        border-radius: 8px;
        border-left: 5px solid #2b5876;
        color: #333333;
        font-size: 1.1rem;
        line-height: 1.7;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 30px;
    }
    
    /* Style for markdown links to match the theme */
    a {
        color: #2b5876;
        text-decoration: none;
        font-weight: 600;
    }
    a:hover {
        color: #4e4376;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION (NO IMAGES, FULL WIDTH) ---
st.markdown('<p class="main-header">Sumbal Murtaza</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">FinTech Senior & AI Pioneers Program Intern</p>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
    <b>Specialized in Privacy-Preserving Machine Learning (PPML), Cybersecurity, and Full-Stack Development.</b><br><br>
    Expert in implementing secure AI models using the Sequre library on Codon frameworks. Proven track record in developing GRC-compliant FinTech platforms (Civitas) and performing advanced penetration testing.
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.header("Contact Information")
st.sidebar.markdown("""
- 📍 **Location:** Islamabad, Pakistan
- 📱 **Phone:** +92 318 4669484
- ✉️ **Email:** sumbalmurtazal@gmail.com
""")

st.sidebar.write("") # Adds a little spacing

# Clean Social Links (One button each)
st.sidebar.link_button("🌐 Visit My LinkedIn", "https://www.linkedin.com/in/sumbal-murtaza-42907724a/", use_container_width=True)
st.sidebar.link_button("💻 Visit My GitHub", "https://github.com/sum710", use_container_width=True)

st.sidebar.divider()
st.sidebar.header("Core Competencies")
st.sidebar.success("🔒 Privacy-Preserving AI")
st.sidebar.success("💻 Full-Stack Development")
st.sidebar.success("🛡️ Cybersecurity & Network Defense")
st.sidebar.success("📈 Risk Modeling & Analytics")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Experience", "💻 Technical Projects", "🛠️ Skills", "🎓 Education"])

with tab1:
    st.header("Professional Experience & Research")
    
    st.markdown("> *\"Let's connect to discuss privacy-preserving AI and secure software solutions.\"*")
    st.write("")

    with st.container():
        st.subheader("AI Pioneers Program Intern")
        st.markdown("**Remote | Oct 2025 - Apr 2026** — *Project Mentored by Yale University Researcher*")
        st.markdown("""
        * **Official Contributor ([Sequre](https://github.com/sum710/sequre)):** Successfully integrated privacy-preserving Deep Learning modules into the official Sequre repository managed by Smjhlovic Haris.
        * **Privacy-Preserving Sepsis Prediction:** Developed a Deep Learning model for early sepsis detection utilizing the Sequre library on the Codon framework.
        * **Secure Multi-Party Computation (SMPC):** Implemented protocols to process sensitive medical datasets while maintaining patient confidentiality.
        * **Optimization:** Optimized SimpleRNN architecture for time-series medical data, focusing on high-speed execution through Codon's ahead-of-time (AOT) compilation.
        """)
    
    st.divider()
    
    with st.container():
        st.subheader("Chief Officer Audit & Finance Affairs")
        st.markdown("**National Youth Leadership Program | Aug - Sep 2025**")
        st.markdown("""
        * Automated financial auditing for national-scale initiatives using Python; improved data transparency and audit trails.
        * Designed documentation frameworks that reduced manual reconciliation errors and enhanced reporting standards.
        """)

with tab2:
    st.header("Featured Projects")
    
    # Project 1
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=600&q=80", use_column_width=True)
    with col2:
        st.markdown("### [Civitas: Secure FinTech Engagement Platform](https://civitas-backend.vercel.app/)")
        st.caption("Final Year Project (FYP) | Current")
        with st.expander("View Project Details", expanded=True):
            st.markdown("""
            * Developed a secure digital engagement platform ([View Live Project](https://civitas-backend.vercel.app/)) using **React.js, Node.js, and Supabase** for cloud-based data management.
            * Integrated Row Level Security (RLS) and secure authentication protocols to protect user financial transactions.
            * Showcased at the International Student Convention & Expo and reviewed by HEC during official institutional visits.
            """)
    
    st.divider()
    
    # Project 2
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&q=80", use_column_width=True)
    with col2:
        st.subheader("Cybersecurity & Network Defense")
        st.caption("Vulnerability Assessment | 2025")
        with st.expander("View Project Details"):
            st.markdown("""
            * Performed network audits via **Kali Linux**, specializing in Packet Sniffing and DDoS Attack Simulation.
            * Utilized **Metasploit** for exploit research and configured secure Ubuntu environments to mitigate server-side risks.
            * Conducted vulnerability scanning to identify and patch SQL injection and Cross-Site Scripting (XSS) threats.
            """)
            
    st.divider()

    # Project 3
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80", use_column_width=True)
    with col2:
        st.subheader("Financial Data Science")
        st.caption("Risk Modeling & Analytics | 2025")
        with st.expander("View Project Details"):
            st.markdown("""
            * **Credit Risk Optimization:** Built a Logistic Regression model to assess default probabilities.
            * **Forecasting Dashboard:** Developed an interactive Streamlit app for stock price forecasting using Scikit-learn and Pandas.
            """)

with tab3:
    st.header("Technical Stack")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🔒 Privacy & AI")
        st.code("Sequre Library | Codon Framework | SMPC | SimpleRNN", language="text")
        
        st.markdown("#### 🛡️ Cybersecurity")
        st.code("Kali Linux | Metasploit | Packet Sniffing | DDoS | GRC", language="text")

    with col2:
        st.markdown("#### 💻 Development")
        st.code("React.js | Node.js | Supabase | SQL | JavaScript | Solidity", language="text")
        
        st.markdown("#### 📈 Finance & Data")
        st.code("Financial Modeling | EViews | Power BI | Data Mining", language="text")

with tab4:
    st.header("Education & Honors")
    
    st.markdown("### FAST-NUCES, Islamabad")
    st.markdown("**BS FinTech** | *2022 - June 2026*")
    st.markdown("**Relevant Coursework:** Cybersecurity, Enterprise Architecture, Data Mining, Financial Modeling, Blockchain Technology.")
    
    st.markdown("### Achievements")
    st.markdown("""
    * 🏅 **Academic Excellence:** Gold Medalist (Semesters 2, 3, 4); Bronze Medalist (Semester 5).
    * 🎓 **Scholarship:** Recipient of PEEF Merit-Based Scholarship.
    * 🏆 **Award:** 1st Position in Punjab Govt Essay Writing Competition.
    """)

# --- FOOTER ---
st.markdown("---")
