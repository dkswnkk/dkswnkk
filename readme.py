import feedparser, time

URL="https://dkswnkk.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST=5

markdown_text = """
## README

#### 주니어 백엔드 개발자 안주형입니다. <img src="https://raw.githubusercontent.com/ABSphreak/ABSphreak/master/gifs/Hi.gif" width="22">
- My Resume is here! 👉 [RESUME](https://dkswnkk.notion.site/fdffe98cbe714c818dc1b009cca9b5ed?pvs=4)
- 🌱 I'm currently learning Back-end and DevOps
- 📝 I regularly write articles on [MY BLOG](https://dkswnkk.tistory.com/)
- My Email is here! 👉  dkswnkk.dev@gmail.com

### 📖 Articles

""" # list of blog posts will be appended here
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    else:
        tags = feed['tags'][0]['term']
        if tags == 'Spring' or tags == 'Java' or tags == 'Infra' or tags == 'Git & GitHub' or tags == 'SQL' or tags == '회고록': 
            feed_date = feed['published_parsed']
            markdown_text += f"- [{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        f = open("README.md", mode="w", encoding="utf-8")
        f.write(markdown_text)
        f.close()
