import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation
lottie_stock = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_jcikwtux.json")

# Page Configuration
st.set_page_config(page_title="Stockastic", page_icon="📈", layout="wide")

# Title and subtitle
st.title("📈 Stockastic: Predict Stock Prices with Machine Learning")
st.subheader("An intelligent tool to forecast market movement with real-time data and ARIMA models.")

# Lottie Animation and Description
col1, col2 = st.columns([1, 2])
with col1:
    if lottie_stock:
        st_lottie(lottie_stock, height=300, key="stock")
    else:
        st.warning("⚠️ Lottie animation failed to load.")
with col2:
    st.markdown("""
    ## 🚀 Features
    - 🔄 **Live Stock Data** from Yahoo Finance  
    - 📈 **ARIMA Forecasting** Model  
    - 📊 **Plotly Graphs** for rich visuals  
    - 🧪 **Backtesting** and performance metrics  
    - 🌐 **Responsive Design** for all devices  
    """)

st.markdown("---")

# App architecture
st.markdown("## 🏗️ How It Works")
st.markdown("""
1. **User selects a stock ticker**  
2. **YFinance** fetches historical data  
3. **ARIMA model** is trained on past prices  
4. Model predicts future closing prices  
5. Forecast is visualized using **Plotly**  
""")

st.markdown("---")

# Disclaimer
st.markdown("## ⚖️ Disclaimer")
st.info("This is not financial advice. Use the data for educational and informational purposes only.")

# Developer section
# Developer section
st.markdown("---")
st.markdown("## 👨‍💻 Developers Team")
st.markdown("""
### 👨‍💼 Project Contributors:
- 🧑‍💻 **Shrishail Telasang**  
  🎓 Final Year B.E. – Computer Science  
  📧 [Email](https://mailto:sktelasang990@gmail.com)   🔗 [LinkedIn](https://linkedin.com/in/shrishail-telasang-056b72207)   💻 [GitHub](https://github.com/shrishail-telasang)

- 👩‍💻 **Rekha Jambagi**  
  🎓 Final Year B.E. – Computer Science

- 👩‍💻 **Savitha M**  
  🎓 Final Year B.E. – Computer Science

- 👨‍💻 **Pradeep Kumar H M**  
  🎓 Final Year B.E. – Computer Science
""")

st.success("✨ Thank you for exploring our stock prediction app!")

