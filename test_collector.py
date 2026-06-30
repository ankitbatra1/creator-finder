from src.crawler.keyword_engine import KeywordEngine

engine = KeywordEngine()

keywords = engine.all_keywords()

print(len(keywords))

for k in keywords:

    print(k)