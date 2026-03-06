import streamlit as st

# Configure page
st.set_page_config(
    page_title="Premium AI Intelligence",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for premium dark theme
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #0a1929;
        color: #ffffff;
    }
    
    [data-testid="stAppViewContainer"] {
        background: #0a1929;
        position: relative;
        overflow: hidden;
    }
    
    [data-testid="stAppViewContainer"]::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 10% 20%, rgba(0, 180, 240, 0.06) 0%, transparent 40%),
            radial-gradient(circle at 90% 80%, rgba(0, 100, 180, 0.04) 0%, transparent 40%),
            radial-gradient(circle at 50% 50%, rgba(0, 150, 200, 0.02) 0%, transparent 60%);
        pointer-events: none;
        z-index: 0;
    }
    
    [data-testid="stAppViewContainer"]::after {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20% 30%, rgba(0, 200, 255, 0.15), rgba(0, 200, 255, 0) 2px),
            radial-gradient(2px 2px at 60% 70%, rgba(0, 150, 200, 0.1), rgba(0, 150, 200, 0) 2px),
            radial-gradient(1px 1px at 50% 10%, rgba(0, 180, 230, 0.12), rgba(0, 180, 230, 0) 1px),
            radial-gradient(1px 1px at 80% 40%, rgba(0, 120, 180, 0.08), rgba(0, 120, 180, 0) 1px),
            radial-gradient(2px 2px at 30% 60%, rgba(0, 200, 255, 0.1), rgba(0, 200, 255, 0) 2px),
            radial-gradient(1px 1px at 90% 20%, rgba(0, 150, 200, 0.09), rgba(0, 150, 200, 0) 1px);
        background-size: 200% 200%, 150% 150%, 180% 180%, 220% 220%, 170% 170%, 190% 190%;
        background-position: 0% 0%, 40% 60%, 50% 50%, 80% 80%, 20% 40%, 60% 20%;
        pointer-events: none;
        z-index: 0;
        animation: floatingDots 20s ease-in-out infinite;
    }
    
    @keyframes floatingDots {
        0%, 100% {
            background-position: 0% 0%, 40% 60%, 50% 50%, 80% 80%, 20% 40%, 60% 20%;
        }
        25% {
            background-position: 10% 20%, 50% 70%, 55% 45%, 85% 75%, 25% 50%, 65% 25%;
        }
        50% {
            background-position: 20% 40%, 60% 80%, 60% 40%, 90% 70%, 30% 60%, 70% 30%;
        }
        75% {
            background-position: 10% 20%, 50% 70%, 55% 45%, 85% 75%, 25% 50%, 65% 25%;
        }
    }
    
    [data-testid="stMain"] {
        background: transparent;
        position: relative;
        z-index: 1;
    }
    
    .main {
        background: transparent;
        position: relative;
        z-index: 1;
    }
    
    /* Remove default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Hero section styling */
    .hero-section {
        text-align: center;
        padding: 80px 20px;
        background: transparent;
    }
    
    .hero-section h1 {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 20px;
        background: linear-gradient(90deg, #ffffff 0%, #ffffff 60%, #00d4ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 0 30px rgba(0, 200, 255, 0.3);
        filter: drop-shadow(0 0 20px rgba(0, 212, 255, 0.2));
    }
    
    .hero-section p {
        font-size: 1.3rem;
        color: #b0bec5;
        margin-bottom: 40px;
        line-height: 1.6;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    
    /* Button styling */
    .btn-primary {
        display: inline-block;
        padding: 14px 40px;
        background: linear-gradient(90deg, #00d4ff 0%, #00a8cc 100%);
        color: #000;
        border: none;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        margin: 10px;
        text-decoration: none;
        transition: all 0.4s ease;
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .btn-primary::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255, 255, 255, 0.3) 0%, transparent 70%);
        transition: all 0.6s ease;
    }
    
    .btn-primary:hover {
        transform: translateY(-3px);
        box-shadow: 
            0 15px 40px rgba(0, 212, 255, 0.4),
            0 0 30px rgba(0, 212, 255, 0.2);
    }
    
    .btn-secondary {
        display: inline-block;
        padding: 14px 40px;
        background: transparent;
        color: #ffffff;
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        margin: 10px;
        transition: all 0.4s ease;
    }
    
    .btn-secondary:hover {
        background: rgba(0, 212, 255, 0.1);
        border-color: #00d4ff;
        color: #00d4ff;
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.2);
        transform: translateY(-3px);
    }
    
    /* Section heading */
    .section-title {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin: 60px 0 50px;
        color: #ffffff;
    }
    
    .section-subtitle {
        font-size: 1.1rem;
        text-align: center;
        color: #90caf9;
        margin-bottom: 50px;
    }
    
    /* Feature cards */
    .feature-card {
        background: linear-gradient(135deg, 
            rgba(20, 50, 80, 0.3),
            rgba(15, 40, 70, 0.3)
        );
        border: 1px solid rgba(0, 212, 255, 0.25);
        border-radius: 12px;
        padding: 30px;
        margin: 15px;
        text-align: center;
        transition: all 0.4s ease;
        backdrop-filter: blur(15px);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle, rgba(0, 212, 255, 0.1) 0%, transparent 70%);
        transition: left 0.6s ease;
    }
    
    .feature-card:hover::before {
        left: 100%;
    }
    
    .feature-card:hover {
        background: linear-gradient(135deg,
            rgba(20, 50, 80, 0.6),
            rgba(15, 40, 70, 0.6)
        );
        border-color: rgba(0, 212, 255, 0.6);
        transform: translateY(-8px);
        box-shadow: 
            0 20px 40px rgba(0, 212, 255, 0.15),
            0 0 50px rgba(0, 212, 255, 0.1),
            inset 0 0 30px rgba(0, 212, 255, 0.05);
    }
    
    .feature-card h3 {
        font-size: 1.5rem;
        margin: 15px 0;
        color: #ffffff;
    }
    
    .feature-card p {
        color: #b0bec5;
        line-height: 1.6;
        font-size: 0.95rem;
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 10px;
    }
    
    /* Trust section */
    .trust-section {
        background: linear-gradient(135deg,
            rgba(30, 60, 100, 0.25),
            rgba(20, 50, 80, 0.25)
        );
        padding: 60px 20px;
        border-radius: 12px;
        margin: 60px 0;
        border: 1px solid rgba(0, 212, 255, 0.2);
        backdrop-filter: blur(15px);
        box-shadow: 
            0 20px 60px rgba(0, 212, 255, 0.1),
            inset 0 0 50px rgba(0, 212, 255, 0.03);
    }
    
    .trust-title {
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 20px;
        color: #ffffff;
    }
    
    .trust-subtitle {
        text-align: center;
        color: #90caf9;
        font-size: 1.1rem;
        margin-bottom: 40px;
    }
    
    /* Divider */
    .divider {
        height: 2px;
        background: linear-gradient(90deg, 
            transparent,
            rgba(0, 212, 255, 0.1),
            rgba(0, 212, 255, 0.4),
            rgba(0, 212, 255, 0.1),
            transparent
        );
        margin: 40px 0;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1>AI Intelligence Redefined</h1>
    <p>Transform your data into actionable insights with cutting-edge artificial intelligence.<br>Built for professionals who demand precision and reliability.</p>
    <div>
        <button class="btn-primary" onclick="alert('Start Analysing')">Start Analysing</button>
        <button class="btn-secondary" onclick="alert('Learn More')">Learn More</button>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Why Choose Section
st.markdown('<h2 class="section-title">Why Choose Us</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Advanced AI technology meets professional excellence</p>', unsafe_allow_html=True)

# Feature Cards Grid
col1, col2, col3 = st.columns(3)

features = [
    {
        "icon": "🧠",
        "title": "Advanced AI",
        "description": "State-of-the-art machine learning models trained on extensive datasets for superior accuracy."
    },
    {
        "icon": "🔐",
        "title": "Enterprise Security",
        "description": "Enterprise-grade security with end-to-end encryption ensuring complete data protection."
    },
    {
        "icon": "⚡",
        "title": "Real-time Analysis",
        "description": "Instant processing and reporting for rapid decision-making and patient care."
    }
]

with col1:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon">{features[0]['icon']}</div>
        <h3>{features[0]['title']}</h3>
        <p>{features[0]['description']}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon">{features[1]['icon']}</div>
        <h3>{features[1]['title']}</h3>
        <p>{features[1]['description']}</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon">{features[2]['icon']}</div>
        <h3>{features[2]['title']}</h3>
        <p>{features[2]['description']}</p>
    </div>
    """, unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

features_2 = [
    {
        "icon": "🔮",
        "title": "Predictive Insights",
        "description": "Anticipate trends and patterns with advanced predictive analytics."
    },
    {
        "icon": "🤝",
        "title": "Seamless Integration",
        "description": "Works with your existing systems and workflows effortlessly."
    },
    {
        "icon": "📊",
        "title": "Clinical Evidence",
        "description": "Backed by peer-reviewed research and international clinical guidelines."
    }
]

with col4:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon">{features_2[0]['icon']}</div>
        <h3>{features_2[0]['title']}</h3>
        <p>{features_2[0]['description']}</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon">{features_2[1]['icon']}</div>
        <h3>{features_2[1]['title']}</h3>
        <p>{features_2[1]['description']}</p>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon">{features_2[2]['icon']}</div>
        <h3>{features_2[2]['title']}</h3>
        <p>{features_2[2]['description']}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Trust Section
st.markdown("""
<div class="trust-section">
    <h2 class="trust-title">Trusted by Healthcare Institutions Worldwide</h2>
    <p class="trust-subtitle">Proven reliability and clinical excellence</p>
</div>
""", unsafe_allow_html=True)

# Trust badges
trust_col1, trust_col2, trust_col3 = st.columns(3)

trust_items = [
    {
        "icon": "✅",
        "title": "Clinical Validation",
        "description": "Tested and validated in leading hospitals and medical centers across multiple countries."
    },
    {
        "icon": "📋",
        "title": "Evidence-Based",
        "description": "Algorithms based on peer-reviewed research and international clinical guidelines."
    },
    {
        "icon": "👨‍⚕️",
        "title": "Expert Designed",
        "description": "Developed in collaboration with endocrinologists and diabetes care specialists."
    }
]

with trust_col1:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon" style="font-size: 2.5rem;">{trust_items[0]['icon']}</div>
        <h3>{trust_items[0]['title']}</h3>
        <p>{trust_items[0]['description']}</p>
    </div>
    """, unsafe_allow_html=True)

with trust_col2:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon" style="font-size: 2.5rem;">{trust_items[1]['icon']}</div>
        <h3>{trust_items[1]['title']}</h3>
        <p>{trust_items[1]['description']}</p>
    </div>
    """, unsafe_allow_html=True)

with trust_col3:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon" style="font-size: 2.5rem;">{trust_items[2]['icon']}</div>
        <h3>{trust_items[2]['title']}</h3>
        <p>{trust_items[2]['description']}</p>
    </div>
    """, unsafe_allow_html=True)

trust_col4, trust_col5, trust_col6 = st.columns(3)

trust_items_2 = [
    {
        "icon": "✔️",
        "title": "Regulatory Approved",
        "description": "Meets international standards and regulatory requirements for medical software."
    },
    {
        "icon": "🔒",
        "title": "Data Privacy",
        "description": "Compliant with GDPR, HIPAA, and all major data protection regulations."
    },
    {
        "icon": "🌍",
        "title": "Global Support",
        "description": "24/7 technical and clinical support available in multiple languages worldwide."
    }
]

with trust_col4:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon" style="font-size: 2.5rem;">{trust_items_2[0]['icon']}</div>
        <h3>{trust_items_2[0]['title']}</h3>
        <p>{trust_items_2[0]['description']}</p>
    </div>
    """, unsafe_allow_html=True)

with trust_col5:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon" style="font-size: 2.5rem;">{trust_items_2[1]['icon']}</div>
        <h3>{trust_items_2[1]['title']}</h3>
        <p>{trust_items_2[1]['description']}</p>
    </div>
    """, unsafe_allow_html=True)

with trust_col6:
    st.markdown(f"""
    <div class="feature-card">
        <div class="feature-icon" style="font-size: 2.5rem;">{trust_items_2[2]['icon']}</div>
        <h3>{trust_items_2[2]['title']}</h3>
        <p>{trust_items_2[2]['description']}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div style="text-align: center; padding: 60px 20px;">
    <h2 style="font-size: 2.5rem; margin-bottom: 20px; color: #ffffff;">Ready to Transform Your Business?</h2>
    <p style="color: #b0bec5; font-size: 1.1rem; margin-bottom: 30px;">Join leading organizations using AI to drive results.</p>
    <button class="btn-primary">Get Started Today</button>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 30px; color: #607d8b; border-top: 1px solid rgba(0, 212, 255, 0.1); margin-top: 60px;">
    <p>© 2026 Premium AI Intelligence. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
