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
Another example:
```
for news in response.css('div.media-story-card__body__3tRWy').getall():
    print(news)
    print("------------------\n")
```
You can also open the url directly (no need to use fectch)
```
scrapy shell https://docs.scrapy.org/en/latest/_static/selectors-sample1.html
response.xpath("//title/text()")
response.css("title::text").get()
```

# Implement the parse() function
Find `reuters.py` in `scraper/scraper/spiders/` directory and implement the parse function
to loop though the data. See current implementation for example.

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

* Scrapy documentation is pretty good, you can read it [here](https://docs.scrapy.org/en/latest/index.html).
* You may find [this](https://www.youtube.com/watch?v=s4jtkzHhLzY) YouTube video for more tips and tricks.
For example, how to paginate but using the `response.follow()`
* Try scraping these sites
  * https://docs.scrapy.org/en/latest/_static/selectors-sample1.html
  * http://quotes.toscrape.com/ and related https://github.com/scrapy/quotesbot has good examples.

