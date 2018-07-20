# Bilibili Force-Directed Graph

# Display

```sh
# install http-server
npm install -g http-server

# http-server start
cd path
http-server -a 0.0.0.0 -p 80
# after that you can view the page at http://127.0.0.1:80
```

also you can use python to start a http server

``````
# python2
python -m SimpleHTTPServer 80
# python3
python -m http.server 80
``````

the data is  from bilibili, some information is here

- API : https://space.bilibili.com/ajax/Bangumi/getList?mid=31390207)
- crawl repo : https://github.com/tx19980520/bilibili-demo-back-end/tree/master/scrapy_crawl/sponsor/sponsor
- source data : https://github.com/tx19980520/bilibiliData

The page shows the relationship among some of the bilibili user. Collecting the same things will shorten the distance between two people.

I use **relationship.py** to create the **study.json** to describe the similarity relationship

Also you can use the data of **local.json** to get a more wonderful result