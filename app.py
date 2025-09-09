import streamlit as st
import pandas as pd

# --- Title ---
st.title("📊 Bihar Iss Bar - Election Sentiment Dashboard")

st.markdown("Welcome to *Bihar Iss Bar*! 🚀\n"
            "This is the first prototype of our election sentiment dashboard. "
            "Right now it shows demo data, but soon we’ll plug in live data from Twitter, YouTube, News, and ECI.")

# --- Demo Dataset ---
data = pd.DataFrame({
    "Source": ["Twitter", "YouTube", "News"],
    "Positive": [62, 55, 70],
    "Negative": [38, 45, 30]
})

# --- Display Bar Chart ---
st.subheader("Sentiment Overview (Demo Data)")
st.bar_chart(data.set_index("Source"))

# --- Download Button ---
st.subheader("Download Dataset")
st.download_button(
    label="Download Sentiment Data (CSV)",
    data=data.to_csv(index=False).encode("utf-8"),
    file_name="sentiment_demo.csv",
    mime="text/csv"
)

# --- Footer ---
st.markdown("---")
st.markdown("📝 *Prototype version – live scrapers & ECI data coming soon!*")
print("abc")