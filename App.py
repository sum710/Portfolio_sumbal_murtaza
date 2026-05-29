import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Sumbal Murtaza | Portfolio", page_icon="👩‍💻", layout="wide")

# --- HEADER SECTION ---
st.title("Sumbal Murtaza")
st.subheader("FinTech Senior & AI Pioneers Program Intern [cite: 6]")
st.markdown("""
**Specialized in Privacy-Preserving Machine Learning (PPML), Cybersecurity, and Full-Stack Development.** [cite: 7]
Expert in implementing secure AI models using the Sequre library on Codon frameworks. [cite: 8] 
Proven track record in developing GRC-compliant FinTech platforms (Civitas) and performing advanced penetration testing using Kali Linux. [cite: 9]
""")

# --- SIDEBAR (CONTACT INFO) ---
st.sidebar.header("Contact Information")
st.sidebar.markdown(f"""
- **Location:** Islamabad, Pakistan [cite: 4]
- **Phone:** +92 318 4669484 [cite: 3]
- **Email:** sumbalmurtazal@gmail.com [cite: 4]
- **LinkedIn:** [sumbal-murtaza](#) [cite: 5]
""")

st.sidebar.header("Core Competencies")
st.sidebar.markdown("""
- Privacy-Preserving AI [cite: 7]
- Full-Stack Development [cite: 7]
- Cybersecurity & Network Defense [cite: 36]
- Risk Modeling & Analytics [cite: 42]
""")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["Experience & Research", "Projects", "Skills", "Education & Awards"])

with tab1:
    st.header("Professional Experience")
    
    st.markdown("### AI Pioneers Program Intern [cite: 18]")
    st.markdown("**Remote | Oct 2025 - Apr 2026** [cite: 19, 20]")
    st.markdown("*Project Mentored by Yale University Researcher* [cite: 17]")
    st.markdown("""
    - **Official Contributor (Sequre):** Successfully integrated privacy-preserving Deep Learning modules into the official Sequre repository managed by Smjhlovic Haris (Yale University researcher). [cite: 21]
    - **Privacy-Preserving Sepsis Prediction:** Developed a Deep Learning model for early sepsis detection utilizing the Sequre library on the Codon framework. [cite: 22]
    - Implemented Secure Multi-Party Computation (SMPC) protocols to process sensitive medical datasets while maintaining patient confidentiality and data privacy. [cite: 23]
    - Optimized SimpleRNN architecture for time-series medical data, focusing on high-speed execution through Codon's ahead-of-time (AOT) compilation. [cite: 24]
    """)
    
    st.divider()
    
    st.markdown("### Chief Officer Audit & Finance Affairs [cite: 26]")
    st.markdown("**National Youth Leadership Program | Aug - Sep 2025** [cite: 25, 31]")
    st.markdown("""
    - Automated financial auditing for national-scale initiatives using Python; improved data transparency and audit trails. [cite: 27]
    - Designed documentation frameworks that reduced manual reconciliation errors and enhanced reporting standards. [cite: 28]
    """)

with tab2:
    st.header("Technical Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Civitas: Secure FinTech Engagement Platform [cite: 32]")
        st.markdown("*Final Year Project (FYP) | Current* [cite: 30, 40]")
        st.markdown("""
        - Developed a secure digital engagement platform using React.js, Node.js, and Supabase for cloud-based data management. [cite: 33]
        - Integrated Row Level Security (RLS) and secure authentication protocols to protect user financial transactions. [cite: 34]
        - Showcased at the International Student Convention & Expo and reviewed by HEC during official institutional visits. [cite: 35]
        """)
        
        st.markdown("### Cybersecurity & Network Defense [cite: 36]")
        st.markdown("*Vulnerability Assessment | 2025* [cite: 35, 41]")
        st.markdown("""
        - Performed network audits via Kali Linux, specializing in Packet Sniffing and DDoS Attack Simulation. [cite: 37]
        - Utilized Metasploit for exploit research and configured secure Ubuntu environments to mitigate server-side risks. [cite: 38]
        - Conducted vulnerability scanning to identify and patch SQL injection and Cross-Site Scripting (XSS) threats. [cite: 39]
        """)
        
    with col2:
        st.markdown("### Financial Data Science [cite: 43]")
        st.markdown("*Risk Modeling & Analytics | 2025* [cite: 42, 44]")
        st.markdown("""
        - **Credit Risk Optimization:** Built a Logistic Regression model to assess default probabilities. [cite: 45]
        - **Forecasting Dashboard:** Developed an interactive Streamlit app for stock price forecasting using Scikit-learn and Pandas. 
        """)

with tab3:
    st.header("Technical Skills [cite: 47]")
    
    st.markdown("""
    **Privacy & AI:** Sequre Library, Codon Framework, Secure Multi-Party Computation (SMPC), SimpleRNN [cite: 48]
    
    **Cybersecurity:** Kali Linux, Metasploit, Sniffing, DDoS Simulation, GRC, Penetration Testing, Ubuntu [cite: 48]
    
    **Development:** React.js, Node.js, Supabase, SQL, JavaScript, Solidity (Blockchain) [cite: 48]
    
    **Finance:** Financial Modeling, EViews, Power BI, Business Research, Data Mining, Quantitative Analysis [cite: 49]
    """)

with tab4:
    st.header("Education [cite: 10]")
    st.markdown("**FAST-NUCES, Islamabad** [cite: 11, 13]")
    st.markdown("BS FinTech | 2022 - June 2026 [cite: 12, 14]")
    st.markdown("**Relevant Coursework:** Cybersecurity, Enterprise Architecture, Data Mining, Financial Modeling, Blockchain Technology. [cite: 15]")
    
    st.divider()
    
    st.header("Achievements & Honors [cite: 50]")
    st.markdown("""
    - **Academic:** Gold Medalist (Semesters 2, 3, 4); Bronze Medalist (Semester 5) at FAST-NUCES. [cite: 51]
    - **Scholarship:** Recipient of PEEF Merit-Based Scholarship. [cite: 51]
    - **Awards:** 1st Position in Punjab Govt Essay Writing Competition. [cite: 52]
    """)

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center'>Built with Streamlit • Let's build secure, intelligent systems together.</div>", unsafe_allow_html=True)