Global Air Quality Dashboard
This is an interactive Streamlit dashboard for exploring global air quality data. Users can filter by city, view summary statistics, analyze pollution trends, and visualize correlations between pollutants and weather conditions.

🚀 Features
✅ City Selection – Choose a city from the sidebar filter.
✅ Summary Statistics – View key pollution metrics.
✅ Time-Series Analysis – Visualize pollution trends over time.
✅ Correlation Heatmap – Explore relationships between pollutants and weather factors.

📂 Project Structure
bash
Copy
Edit
air_quality_dashboard/
│── app.py              # Streamlit app
│── data/               # Folder containing air_quality.csv
│── requirements.txt    # List of dependencies
│── README.md           # Guide on running the app

 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/air_quality_dashboard.git
cd air_quality_dashboard
2️⃣ Create a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate (Mac/Linux)
venv\Scripts\activate  # Activate (Windows)
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
This will launch the dashboard in your default web browser.

📊 Sample Dataset
Place your air_quality.csv file inside the data/ folder before running the app.

🛠️ Deployment (Optional)
To deploy the app on Streamlit Cloud, follow these steps:

Push your code to GitHub.
Go to Streamlit Cloud.
Click "New app", connect your GitHub repo, and deploy!
