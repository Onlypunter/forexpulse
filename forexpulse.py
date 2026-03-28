import streamlit as st

st.set_page_config(
    page_title="ForexPulse",
    page_icon="💱",
    layout="wide"
)

st.title("💱 ForexPulse")
st.markdown("### Real-time Forex Market Pulse")
st.caption("Free Forex App • Made for Android")

st.success("✅ App is running successfully!")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="EUR/USD", value="1.0852", delta="+0.0014")
with col2:
    st.metric(label="GBP/USD", value="1.3125", delta="-0.0021")
with col3:
    st.metric(label="USD/ZMW", value="27.85", delta="+0.12")

st.info("This app will soon be available as a downloadable Android APK!")
