import pandas as pd
import feedparser
from datetime import datetime

def get_top_contacts(filepath):
    df = pd.read_csv(filepath)
    top_contacts = df.sort_values("Engagement Score", ascending=False).head(5)
    return top_contacts

def fetch_industry_news(rss_url):
    feed = feedparser.parse(rss_url)
    news = [{"title": entry.title, "link": entry.link, "summary": entry.summary} for entry in feed.entries]
    return news

def generate_followup_template(contact, news_item):
    template = f"""
    ## Follow-Up with {contact['Name']}

    Hi {contact['Name']},

    I came across this article that I thought would interest you: [{news_item['title']}]({news_item['link']})
    Summary: {news_item['summary']}

    Since you are an expert in {contact['Expertise Area']}, I’d love to hear your thoughts. Let me know if you'd like to discuss this further.

    Best regards,  
    [Your Name]
    """
    return template

def main():
    contacts = get_top_contacts("relationship_data.csv")
    news = fetch_industry_news("https://rss.sciencedaily.com/top.xml")

    for index, contact in contacts.iterrows():
        news_item = news[index % len(news)]
        message = generate_followup_template(contact, news_item)
        filename = f"{contact['Name']}_followup.md"
        with open(filename, "w") as file:
            file.write(message)
        print(f"Generated follow-up for {contact['Name']}: {filename}")

if __name__ == "__main__":
    main()

