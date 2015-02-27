# scraPost
A demo of how to scrape webpages using HTTP POST, which is the basic form of AJAX requesting.

Just using the FormRequest from scrapy doc http://doc.scrapy.org/en/latest/topics/request-response.html#request-usage-examples

The idea is to find out what does the request body contain each time it is posted to the server and then mimic those requests 
using the formdata parameter in Request.
