### Liu Weixu's Python Spider Program

##### 此处是我的爬虫的学习和实践的整理，部分程序有相应的笔记

##### 如果发现爬取失败的问题，可以发邮箱：liuweixu2018@gmail.com 或 wei_xu_liu@163.com，这样我可以及时地收到消息。

- #### BeautifulSoup4的使用
  
  - [百度贴吧一个投票贴的票数统计](https://github.com/liuweixu/Python-crawler/tree/master/Beautifulsoup/百度贴吧一个投票贴的票数统计)
  
  - [笔趣阁里的《极品家丁》爬取笔记](https://github.com/liuweixu/Python-crawler/tree/master/Beautifulsoup/笔趣阁里的《极品家丁》爬取笔记)
  
  - [高考一分一段表爬取](https://github.com/liuweixu/Python-crawler/tree/master/Beautifulsoup/%E9%AB%98%E8%80%83%E4%B8%80%E5%88%86%E4%B8%80%E6%AE%B5%E7%88%AC%E5%8F%96)
  
    
  
- Xpath的使用（比较简单，可以直接利用Google的“Copy Xpath”功能来辅助）
  - [AcFun的网页版里面的番剧页面的爬虫](https://github.com/liuweixu/Python-crawler/tree/master/xpath/AcFun的网页版里面的番剧页面爬虫)
  
  - [b站通过av号爬取视频的封面](https://github.com/liuweixu/Python-crawler/tree/master/xpath/b站通过av号爬取视频的封面)
  
    
  
- PyQuery
  
  - [用Pyquery重写崔庆才的《Python3网络爬虫开发实战》的猫眼爬取](https://github.com/liuweixu/Python-crawler/tree/master/PyQuery/用Pyquery重写崔庆才的《Python3网络爬虫开发实战》的猫眼爬取)
  
    
  
- Ajax处理（需要在开发者工具中选择network的XHR或JS，找到符合条件的网址，一般内容为json格式）
  
  - [Bilibili新番表爬虫](https://github.com/liuweixu/Python-crawler/tree/master/Ajax/Bilibili新番表爬虫)
  
  - [半次元周榜部分爬虫](https://github.com/liuweixu/Python-crawler/tree/master/Ajax/半次元周榜部分爬虫)
  
  - [疫情数据爬取（国外数据），截止到2020年12月30日](https://github.com/liuweixu/Python-crawler/tree/master/Ajax/%E7%99%BE%E5%BA%A6%E7%96%AB%E6%83%85%E5%AE%9E%E6%97%B6%E6%95%B0%E6%8D%AE%E7%88%AC%E5%8F%96%E5%B9%B6%E5%8F%AF%E8%A7%86%E5%8C%96%EF%BC%88%E5%9B%BD%E5%A4%96%E6%95%B0%E6%8D%AE%EF%BC%89)
  
  - [教育部第四轮评估爬取](https://github.com/liuweixu/Python-crawler/tree/master/Ajax/%E6%95%99%E8%82%B2%E9%83%A8%E7%AC%AC%E5%9B%9B%E8%BD%AE%E8%AF%84%E4%BC%B0)
  
  - [股票历史数据](https://github.com/liuweixu/Python-crawler/tree/master/Ajax/%E8%82%A1%E7%A5%A8%E6%95%B0%E6%8D%AE%E7%88%AC%E5%8F%96) （涉及到字典的使用）
  
    
  
- Scrapy
  - [Scrapy爬取Bing美图](https://github.com/liuweixu/Python-crawler/tree/master/Scrapy/Bing美图/Bing)
  - [b站画友的最热图片](https://github.com/liuweixu/Python-crawler/tree/master/Scrapy/b站画友的最热图)
  - [半次元的周榜上的封面图](https://github.com/liuweixu/Python-crawler/tree/master/Scrapy/半次元的周榜上的封面图)
  - [唯1图片的动漫美女图片下载](https://github.com/liuweixu/Python-crawler/tree/master/Scrapy/唯1图片的动漫美女图片下载)
  - [对scrapyd爬虫实验网站的爬虫](https://github.com/liuweixu/Python-crawler/tree/master/Scrapy/对scrapyd爬虫实验网站的爬虫)
  - [火熊网图片爬取下载](https://github.com/liuweixu/Python-crawler/tree/master/Scrapy/火熊网图片爬取下载)（这个涉及到表单的提交，个人认为这个比较重要）
  - [爬取《极品家丁》小说](https://github.com/liuweixu/Python-crawler/tree/master/Scrapy/爬取《极品家丁》小说) （笔趣看的小说）
  - [爬取阳光高考网的院校库的大学信息](https://github.com/liuweixu/Python-crawler/tree/master/Scrapy/爬取阳光高考网的大学信息/gaokao) （scrapy和openpyxl相结合，涉及到open_spider()和close_spider()的用法）