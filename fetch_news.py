#!/usr/bin/env python3
import json
from datetime import datetime

try:
    with open('news_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except:
    data = {"published": [], "pending": [], "rejected": []}

news = {
    "title": "Ministério da Saúde reforça reconhecimento de diplomas estrangeiros",
    "summary": "Portaria facilita reconhecimento de enfermeiros estrangeiros. Brasil e Itália ampliam cooperação.",
    "source_official": "Ministério da Saúde",
    "country": "Brasil",
    "link": "https://www.gov.br/saude/pt-br",
    "image_url": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=400&fit=crop",
    "published": datetime.now().isoformat(),
    "status": "pending_approval"
}

data['pending'] = [news]

with open('news_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Notícia criada!")
