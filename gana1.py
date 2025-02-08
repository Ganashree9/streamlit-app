import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
@st.cache_data
def load_data():
    file_path = r"C:\Users\ganashree r\Desktop\project\extracted_csv\AQI and Lat Long of Countries.csv"
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower()  # Standardize column names
    return df

df = load_data()

# Streamlit App
st.set_page_config(page_title="Global Air Quality Dashboard", layout="wide")
st.title("🌍 Global Air Quality Dashboard")

# Sidebar filters
st.sidebar.header("🔍 Filter Options")
selected_country = st.sidebar.selectbox("Select a Country", ["All"] + sorted(df["country"].dropna().unique().tolist()))
selected_city = st.sidebar.selectbox("Select a City", ["All"] + sorted(df["city"].dropna().unique().tolist()))

# Filter Data
filtered_df = df.copy()
if selected_country != "All":
    filtered_df = filtered_df[filtered_df["country"] == selected_country]
if selected_city != "All":
    filtered_df = filtered_df[filtered_df["city"] == selected_city]

# Data Overview
st.subheader("📊 Air Quality Data Overview")
st.dataframe(filtered_df)

# Summary Statistics
st.subheader("📈 Summary Statistics")
st.write(filtered_df.describe())

# Correlation Heatmap
st.subheader("🔥 Correlation Heatmap of Air Pollutants")
pollutant_cols = ["aqi value", "co aqi value", "ozone aqi value", "no2 aqi value", "pm2.5 aqi value"]
correlation_matrix = filtered_df[pollutant_cols].corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
st.pyplot(fig)

# Top 10 Most Polluted Cities
st.subheader("🌆 Top 10 Most Polluted Cities")
top_cities = df.groupby("city")["aqi value"].mean().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_cities.index, y=top_cities.values, palette="Reds_r", ax=ax)
plt.xticks(rotation=45)
plt.ylabel("Average AQI")
plt.xlabel("City")
st.pyplot(fig)

st.sidebar.success("✅ Select filters to explore the data!")
