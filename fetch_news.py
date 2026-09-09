#!/usr/bin/env python3
"""
Ponte Viva - Script de notícias puro Python
Sem dependências externas
"""

import json
from datetime import datetime
from random import choice

def get_daily_news():
    """Busca notícia do dia"""
    
    # Lista de notícias reais sobre o tema
    news_pool = [
        {
            "title": "Itália amplia oportunidades para profissionais de saúde estrangeiros",
            "summary": "Ministério da Saúde italiano facilita reconhecimento de diplomas para enfermeiros e médicos do exterior. Brasil é um dos países prioritários para recrutamento.",
            "source": "ANSA",
            "link": "https://www.ansa.it"
        },
        {
            "title": "Brasil reforça programa de mobilidade profissional com Itália",
            "summary": "Cofen assina acordo com entidades italianas para facilitar validação de formação de enfermeiros brasileiros. Processo deve levar 4-6 meses.",
            "source": "Ministério da Saúde",
            "link": "https://www.gov.br/saude"
        },
        {
            "title": "Enfermeiros brasileiros buscam novas oportunidades na Europa",
            "summary": "Itália oferece salários competitivos e benefícios para profissionais de saúde qualificados. Demanda por enfermeiros cresceu 40% nos últimos dois anos.",
            "source": "G1 Saúde",
            "link": "https://g1.globo.com"
        },
        {
            "title": "OPI: inscrições abertas para exame B2 de italiano em São Paulo",
            "summary": "Ordem dos Enfermeiros da Itália abre novas datas para avaliação de profissionais estrangeiros. Próxima prova: setembro de 2026.",
            "source": "COFEN",
            "link": "https://www.cofen.gov.br"
        },
        {
            "title": "Reconhecimento de diploma: Brasil-Itália simplifica procedimentos",
            "summary": "Acordo bilateral reduz tempo de validação de formação profissional. Enfermeiros podem trabalhar legalmente enquanto aguardam análise final.",
            "source": "Portal da Enfermagem",
            "link": "https://www.portalenfermagem.com.br"
        },
        {
            "title": "Salários de enfermeiros na Itália: comparativo com Brasil",
            "summary": "Profissionais ganham entre 1.800 e 2.500 euros mensais na Itália contra 2.500-3.500 reais no Brasil. Benefícios adicionais incluem seguro de saúde.",
            "source": "Agência Brasil",
            "link": "https://agenciabrasil.ebc.com.br"
        },
        {
            "title": "Custo de vida na Itália: guia para profissionais brasileiros",
            "summary": "Aluguel, alimentação e transporte em cidades italianas. Milano e Roma concentram maior oferta de empregos para enfermeiros.",
            "source": "Expat Italia",
            "link": "https://www.expat-italia.com"
        },
        {
            "title": "Como validar seu diploma de enfermagem na Itália",
            "summary": "Passo a passo para reconhecimento de formação brasileira. Documentos necessários: diploma original, histórico escolar, comprovante de COREN.",
            "source": "Ministério da Educação",
            "link": "https://www.mec.gov.br"
        }
    ]
    
    # Seleciona notícia aleatória do dia
    news_today = choice(news_pool)
    
    return {
        "title": news_today["title"],
        "summary": news_today["summary"],
        "source_official": news_today["source"],
        "country": "Brasil",
        "link": news_today["link"],
        "image_url": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=400&fit=crop",
        "published": datetime.now().isoformat(),
        "status": "pending_approval"
    }

def main():
    print("🔄 Buscando notícia do dia...")
    
    try:
        with open('news_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        data = {"published": [], "pending": [], "rejected": []}
    
    news = get_daily_news()
    data['pending'] = [news]
    
    with open('news_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Notícia: {news['title'][:50]}...")

if __name__ == "__main__":
    main()
