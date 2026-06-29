# 🧣 Dubai Men's Ethnic Wear — Market Intelligence Dashboard

A full-stack Streamlit analytics application for researching and entering the Dubai Men's Ethnic Wear market.

## 📦 Features

| Page | What it covers |
|---|---|
| 🏠 Market Overview | Competitors, market share, seasonality, consumer behaviour |
| 📊 Synthetic Dataset | 1,000 consumer records, 22 columns, downloadable CSV |
| 📋 Survey Questionnaire | 42-question consumer survey across 7 sections |
| 🔍 Descriptive Analysis | Summary stats, cross-tabs, heatmaps, bivariate analysis |
| 🩺 Diagnostic Analysis | Driver analysis, chi-square/ANOVA, marketing & inventory diagnostics |
| 🤖 ML Classification | Feature engineering pipeline + KNN / Decision Tree / Random Forest / Gradient Boosting |
| 📈 Model Performance | Accuracy, Precision/Recall/F1, ROC Curves, Confusion Matrices, Feature Importance |
| 💡 Findings & Insights | Market findings, consumer insights, ML findings, Go-to-Market roadmap |

## 🚀 Run Locally

```bash
# 1. Clone repo
git clone https://github.com/YOUR_USERNAME/dubai-ethnic-wear.git
cd dubai-ethnic-wear

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run app
streamlit run app.py
```

## ☁️ Deploy to Streamlit Community Cloud

1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app**
4. Set:
   - **Repository:** `YOUR_USERNAME/dubai-ethnic-wear`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click **Deploy!**

## 📁 Project Structure

```
dubai_ethnic_wear/
├── app.py                    # Main entry point
├── requirements.txt
├── README.md
├── pages/
│   ├── market_overview.py    # Competitor & market analysis
│   ├── dataset.py            # Synthetic data generator & viewer
│   ├── survey.py             # Survey questionnaire
│   ├── descriptive.py        # Descriptive & cross-tab analysis
│   ├── diagnostic.py         # Diagnostic & root cause analysis
│   ├── ml_models.py          # Feature engineering & model setup
│   ├── model_performance.py  # Training, evaluation, plots
│   └── findings.py           # Insights & recommendations
└── utils/
    └── data_generator.py     # Synthetic data generation functions
```

## 🎯 Target Variable

**Purchase Intent** (Multi-class: Low / Medium / High) — derived from:
- Repeat purchase history
- Festive/seasonal timing
- Price tier and income alignment
- Location preference
- Social media engagement

## 📊 ML Algorithms

All algorithms use 31 engineered features with StandardScaler normalisation:
- **KNN** (k=7, Euclidean distance)
- **Decision Tree** (max_depth=8, min_samples_split=15)
- **Random Forest** (150 trees, max_depth=10)
- **Gradient Boosting** (150 estimators, lr=0.08, max_depth=5)

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Visualisation:** Plotly
- **ML:** scikit-learn
- **Data:** pandas, numpy, scipy
