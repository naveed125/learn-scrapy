# Learn Scrapy

Here are the steps I followed to set it up
```
python -m venv venv
.\venv\Scripts\activate.bat
pip install scrapy
scrapy startproject scraper
cd scraper
scrapy genspider reuters reuters.com
```

# Trying out the scrapy shell
Scrapy shell allows you to interact with a website. It is a good way to test some data.

```
scrapy shell
fetch('https://www.reuters.com')
news = response.css('div.media-story-card__body__3tRWy')
len(news)
news.css('a.text__text__1FZLe::text').get()
news.css('a.text__text__1FZLe::text').getall()
news.css('a.text__text__1FZLe').attrib['href']
```

# Run the full web page crawl

To get the full data we can use the `crawl` command. You need to be in the `scraper` directory to run this.
This is the same directory where you have the scrapy.cfg file. In my case its the `learn-scrapy/scraper`. Run the
**list** command to make sure you can see the spider

```
scrapy list
```

Next run the spider
```
scrapy crawl reuters
```

You can save the output a file with `-O` option
```
scrapy crawl reuters -O output.json
scrapy crawl reuters -O output.csv
```

# More tips and tricks

You may find [this](https://www.youtube.com/watch?v=s4jtkzHhLzY) Youtube video for more tips and tricks.
For example, how to paginate but using the `response.follow()`