#!/usr/bin/env python3
import json
import requests
from datetime import datetime

def fetch_google_news():
    try:
        import feedparser
        keywords = ["enfermagem Brasil Itália", "mobilidade profissional saúde", "enfermeiros"]
        
        for keyword in keywords:
            url = f"https://news.google.com/rss/search?q={keyword}&hl=pt-BR&gl=BR"
            feed = feedparser.parse(url)
            if feed.entries:
                entry = feed.entries[0]
                return {
                    "title": entry.title,
                    "summary": entry.summary[:200] if hasattr(entry, 'summary') else "Notícia importante",
                    "link": entry.link,
                    "source_official": "Google News",
                    "country": "Brasil",
                    "image_url": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=400&fit=crop",
                    "published": datetime.now().isoformat(),
                    "status": "pending_approval"
                }
    except:
        pass
    return None

def main():
    try:
        with open('news_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        data = {"published": [], "pending": [], "rejected": []}
    
    news = fetch_google_news()
    if not news:
        news = {
            "title": "Oportunidades de mobilidade profissional para enfermeiros",
            "summary": "Notícias sobre reconhecimento de diplomas e trabalho no Brasil e Itália.",
            "link": "https://www.gov.br/saude/pt-br",
            "source_official": "Ministério da Saúde",
            "country": "Brasil",
            "image_url": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=400&fit=crop",
            "published": datetime.now().isoformat(),
            "status": "pending_approval"
        }
    
    data['pending'] = [news]
    
    with open('news_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Notícia: {news['title'][:50]}...")

if __name__ == "__main__":
    main()
