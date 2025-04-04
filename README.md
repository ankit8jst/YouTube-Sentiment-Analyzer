# YouTube-Sentiment-Analyzer
YouTube Sentiment Analyzer 🎥📊 A Flask-based web app that analyzes YouTube video comments using sentiment analysis. It categorizes comments as Positive, Negative, or Neutral and visualizes results with graphs and charts. Built with Flask, YouTube API, TextBlob, Matplotlib, HTML, CSS. 🚀
YouTube Sentiment Analysis Tool

📌 LIVE DEMO 
    https://youtube-sentiment-analyzer-sih0.onrender.com

📌 Overview

This tool analyzes comments from a YouTube video and determines the sentiment of the audience. It categorizes comments into positive, negative, and neutral and provides a visual representation using charts.

🚀 Features

Fetches comments from a YouTube video using its video ID.

Uses TextBlob for sentiment analysis.

Displays positive, negative, and neutral comment counts.

Shows top positive and negative comments.

Generates pie charts and bar charts for sentiment distribution.

🛠️ Installation Guide

1️⃣ Clone the Repository

git clone https://github.com/ankit8jst/YouTube-Sentiment-Analyzer
cd YouTube-Sentiment-Analyzer

2️⃣ Install Required Libraries

Run the following command to install all dependencies:

pip install flask google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client textblob matplotlib

3️⃣ Set Up Google API Credentials

Go to Google Cloud Console

Enable the YouTube Data API v3

Create API credentials and obtain an API key

Replace YOUR_YOUTUBE_API_KEY in your app.py file with your API key:

YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"

🎯 How to Run the Project

1️⃣ Start the Flask Server

Run the following command in the terminal:

python app.py

2️⃣ Open the Web Application

Go to http://127.0.0.1:5000/ in your browser.

📂 Project Structure

project-root/
│-- static/
│   │-- style.css  # Contains animations and styling
│-- templates/
│   │-- index.html  # Main webpage
│   │-- result.html  # Analysis results page
│-- app.py  # Main backend script
│-- requirements.txt  # List of required libraries
│-- README.md  # This file (User Guide)

🖼️ Example Output

Sentiment Analysis Results:

Video Title: Your Video Title Here

Positive Comments: 45

Negative Comments: 30

Neutral Comments: 25

Visualizations:

Pie chart for sentiment distribution

Bar chart for sentiment polarity

📌 Troubleshooting

If you get jinja2.exceptions.TemplateNotFound: index.html, ensure index.html is inside the templates/ folder.

If API calls fail, check if your YouTube API quota is exceeded.

🏆 Contribute

Feel free to fork this repository and contribute by adding new features or fixing bugs!

✨ Happy Coding! ✨

![Screenshot 2025-04-03 002225](https://github.com/user-attachments/assets/b22b461a-2f37-41f5-82af-266176f3e76b)
![Screenshot 2025-04-03 002249](https://github.com/user-attachments/assets/fbebc12c-270b-4e97-a805-2fbcf960e898)
![Screenshot 2025-04-03 002302](https://github.com/user-attachments/assets/7d0a7358-8eda-4dd1-8930-1d28deb92f19)
![Screenshot 2025-04-03 002313](https://github.com/user-attachments/assets/a90f246c-0088-473a-a9db-1a11c34d14f4)







