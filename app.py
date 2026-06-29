import streamlit as st

st.set_page_config(
    page_title="Dubai Ethnic Wear Market Intelligence",
    page_icon="🧣",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .main-header h1 { color: #e94560; font-size: 2.2rem; margin: 0; }
    .main-header p { color: #a0aec0; font-size: 1rem; margin-top: 0.5rem; }
    .metric-card {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        border: 1px solid #e94560;
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
        color: white;
    }
    .metric-card h3 { color: #e94560; font-size: 1.8rem; margin: 0; }
    .metric-card p { color: #a0aec0; font-size: 0.85rem; margin: 0.3rem 0 0 0; }
    .nav-card {
        background: linear-gradient(135deg, #16213e, #0f3460);
        border: 1px solid #e94560;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.3s;
    }
    .stSidebar { background-color: #0f0f1a; }
    .section-header {
        color: #e94560;
        border-bottom: 2px solid #e94560;
        padding-bottom: 0.5rem;
        margin: 1.5rem 0 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.markdown("### 🧣 Dubai Ethnic Wear")
    st.markdown("**Market Intelligence Platform**")
    st.markdown("---")
    
    page = st.radio(
        "Navigate",
        [
            "🏠 Market Overview",
            "📊 Synthetic Dataset",
            "📋 Survey Questionnaire",
            "🔍 Descriptive Analysis",
            "🩺 Diagnostic Analysis",
            "🤖 ML Classification",
            "📈 Model Performance",
            "💡 Findings & Insights"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("**Business Context**")
    st.markdown("📍 Dubai, UAE")
    st.markdown("👔 Men's Ethnic Wear")
    st.markdown("🏭 Mfg + Retail")

# Route pages
if page == "🏠 Market Overview":
    from pages import market_overview
    market_overview.show()
elif page == "📊 Synthetic Dataset":
    from pages import dataset
    dataset.show()
elif page == "📋 Survey Questionnaire":
    from pages import survey
    survey.show()
elif page == "🔍 Descriptive Analysis":
    from pages import descriptive
    descriptive.show()
elif page == "🩺 Diagnostic Analysis":
    from pages import diagnostic
    diagnostic.show()
elif page == "🤖 ML Classification":
    from pages import ml_models
    ml_models.show()
elif page == "📈 Model Performance":
    from pages import model_performance
    model_performance.show()
elif page == "💡 Findings & Insights":
    from pages import findings
    findings.show()
