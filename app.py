import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for Matplotlib
import matplotlib.pyplot as plt
import os
import base64
from io import BytesIO
from flask import Flask, render_template, request
from googleapiclient.discovery import build
from textblob import TextBlob

app = Flask(__name__)

# Replace with your YouTube API Key
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def fetch_video_title(video_id):
    """Fetch the video title from YouTube API."""
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()

    if response["items"]:
        return response["items"][0]["snippet"]["title"]
    return "Unknown Video"

def fetch_comments(video_id):
    """Fetch comments from a YouTube video using YouTube Data API v3."""
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )
    response = request.execute()

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    return comments

def analyze_sentiment(comments):
    """Analyze sentiment of YouTube comments and store top positive/negative comments."""
    sentiment_scores = []
    positive_comments = []
    negative_comments = []

    for comment in comments:
        analysis = TextBlob(comment)
        polarity = analysis.sentiment.polarity
        sentiment_scores.append(polarity)

        if polarity > 0:
            positive_comments.append((comment, polarity))
        elif polarity < 0:
            negative_comments.append((comment, polarity))

    # Sort top 3 positive and negative comments based on polarity score
    top_positive = sorted(positive_comments, key=lambda x: x[1], reverse=True)[:10]
    top_negative = sorted(negative_comments, key=lambda x: x[1])[:10]

    return sentiment_scores, top_positive, top_negative

def visualize_sentiment(sentiment_scores):
    """Generate a pie chart and bar chart for sentiment distribution and return base64 image data."""
    positive_comments = sum(1 for score in sentiment_scores if score > 0)
    negative_comments = sum(1 for score in sentiment_scores if score < 0)
    neutral_comments = len(sentiment_scores) - positive_comments - negative_comments

    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [positive_comments, negative_comments, neutral_comments]
    colors = ['gold', 'lightcoral', 'lightskyblue']

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Pie chart for sentiment distribution
    axes[0].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    axes[0].set_title('Sentiment Distribution')

    # Bar chart for sentiment polarity distribution
    axes[1].bar(labels, sizes, color=colors)
    axes[1].set_title('Sentiment Polarity Distribution')

    plt.tight_layout()

    # Save the plot as an image and encode to base64
    image_buffer = BytesIO()
    plt.savefig(image_buffer, format='png')
    plt.clf()  # Clear the previous plot
    image_buffer.seek(0)
    image_data = base64.b64encode(image_buffer.read()).decode('utf-8')

    return image_data

@app.route('/')
def index():
    """Render the index.html template."""
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    """Process the video ID and display sentiment analysis results."""
    video_id = request.form.get('video_id')

    if not video_id:
        return "Error: No video ID provided"

    video_title = fetch_video_title(video_id)
    comments = fetch_comments(video_id)
    sentiment_scores, top_positive, top_negative = analyze_sentiment(comments)

    sentiment_chart = visualize_sentiment(sentiment_scores)

    return render_template(
        'result.html', 
        video_title=video_title,  # Pass video title
        sentiment_chart=sentiment_chart,
        top_positive=top_positive, 
        top_negative=top_negative
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)

