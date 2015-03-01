from scrapy.contrib.spiders.crawl import CrawlSpider
from scrapy.selector import Selector
import re
from scrapy.http.request.form import FormRequest
from scrapy.http import Request
from scraPost.items import ScrapostItem
from scrapy import log

import urllib


__author__ = "Kui Xiong"
__contact__ = "kuixiong at gmail"

class PostSpider(CrawlSpider):
    name = "postSpider"
    allowed_domains = ["search.mlslistings.com",]
    start_urls = ["http://search.mlslistings.com/Matrix/Public/Portal.aspx?L=1&k=529746X7NCW&p=ALL-0-0-H",]
    
    # static posted data
    formdata = {
                "m_scriptManager" : "m_scriptManager|_ctl0$m_DisplayCore",
                "_ctl0$m_hfDisplayMode" : "1",
                "_ctl0$m_ddlPageSize" : "25",
                "_ctl0$m_hfKeys" : "6857105,6857160,6857236,6857475,6857518,6857642,6857643,6857944,6857947,6858190,6858611,6858715,6858965,6859309,6859341,6859426,6859513,6859559,6859646,6859701,6859764,6859768,6859839,6859899,6860147,6860162,6860306,6860358,6860429,6860664,6860963,6860992,6861219,6861261,6861262,6861434,6861536,6861907,6861911,6862070,6862077,6862092,6862414,6862438,6862553,6863124,6863179,6863277,6864086,6864303,6864383,6864412,6864432,6864624,6864709,6864811,6864871,6865146,6865221,6865422,6865496,6865729,6865796,6865818,6865907,6865952,6865963,6865993,6866169,6866233,6866297,6866595,6866638,6866639,6866708,6866792,6866886,6866888,6866926,6866948,6866949,6866973,6867307,6867319,6867328,6867357,6867371,6867432,6867441,6867466,6867626,6867727,6867728,6867796,6867798,6867848,6867921,6867923,6867924,6867968,6867970,6868059,6868062,6868103,6868143,6868242,6868243,6868302,6868322,6868325,6868520,6868548,6868573,6868713,6868793,6868821,6868925,6869100,6869142,6869148,6869186,6869253,6869313,6869416,6869453,6869504,6869589,6869623,6869686,6869710,6869896,6869923,6869954,6870086,6870140,6870238,6870239,6870276,6870314,6870339,6870364,6870389,6870402,6870406,6870587,6870592,6870612,6870613,6870614,6870679,6870704,6870819,6870849,6870885,6870909,6870956,6870958,6871043,6871108,6871109,6871237,6871253,6871269,6871273,6871274,6871360,6871383,6871411,6871456,6871491,6871574,6871615,6871695,6871719,6871728,6871771,6871801,6871808,6871850,6871900,6872052,6872084,6872138,6872309,6872353,6872600,6872602,6872641,6872644,6872735,6872897,6872898,6872899,6873066,6873100,6873164,6873252,6873254,6873271,6873272,6873291,6873330,6873331,6873332,6873390,6873463,6873505,6873715,6873777,6873822,6873845,6873960,6873986,6874035,6874128,6874199,6874301,6874403,6874573,6874574,6874743,6874769,6874782,6874815,6874816,6874817,6874836,6874869,6874924,6874961,6874981,6874983,6875059,6875124,6875151,6875153,6875205,6875246,6875247,6875248,6875249,6875295,6875297,6875298,6875299,6875300,6875301,6875360,6875362,6875363,6875410,6875411,6875413,6875419,6875477,6875478,6875483,6875544,6875545,6875631,6875632,6875685,6875688,6875739,6875771,6875772,6878132,6878320,6879625,6879690,6879857,6879878,6879898,6879956,6879957,6880009,6880068,6880228,6880241,6880270,6880276,6880303,6880319,6880334,6880355,6880381,6880383,6880423,6880424,6880425,6880426,6880502,6880553,6880554,6880555,6880586,6880590,6880621,6880660,6880703,6880738,6880781,6880868,6880869,6880922,6880962,6881042,6881071,6881072,6881157,6881254,6881255,6881312,6881354,6881355,6881426,6881455,6881466,6881783,6881801,6881802,6881820,6881864,6881915,6881918,6881944,6881948,6881981,6881982,6881984,6882030,6882062,6882114,6882117,6882215,6882239,6882272,6882390,6882407,6882422,6882551,6882552,6882593,6882669,6882704,6882705,6882707,6882731,6882756,6882783,6882804,6882822,6882823,6882850,6882883,6882884,6882885,6882907,6882908,6882960,6882996,6883029,6883037,6883038,6883061,6883154,6883164,6883348,6883362,6883394,6883440,6883441,6883442,6883455,6883526,6883547,6883588,6883606,6883609,6883737,6883760,6883761,6883808,6883809,6883810,6883884,6883978,6884209,6884312,6884380,6884405,6884432,6884449,6884476,6884478,6884500,6884521,6884558,6884650,6884922,6884932,6884974,6885031,6885175,6885212,6885225,6885281,6885300,6885326,6885522,6885542,6885564,6885580,6885586,6885624,6885639,6885657",
                "__ASYNCPOST" : "true",
#                 "_ctl0$m_hfCriteriaChanged":"",
#                 "_ctl0$m_hfMapArea" :"",
#                 "_ctl0$m_hfMapShape" : "",
#                 "Fm35_Ctrl1152_LB" : "",
#                 "Fm35_Ctrl1152_LB" : "",
#                 "Fm35_Ctrl1153_LB" : "",
#                 "Fm35_Ctrl1153_LB" : "",
#                 "Fm35_Ctrl1154_LB" : "",
#                 "Fm35_Ctrl1154_LB" : "",
#                 "Fm35_Ctrl1155_LB" : "",
#                 "Fm35_Ctrl1155_LB" : "",
#                 "Fm35_Ctrl1156_LB" : "",
#                 "Fm35_Ctrl1156_LB" : "",
#                 "Fm35_Ctrl1157_LB" : "",
#                 "Fm35_Ctrl1157_LB" : "",
#                 "Fm35_Ctrl1158_TB" : "",
#                 "Fm35_Ctrl1160_TB" : "",
#                 "_ctl0$m_hfResultsHeight":"",
#                 "_ctl0$m_hfVisibleKeys" : "",
#                 "m_hfShowingEmailPopup": "",
#                 "_ctl0$m_tbSearchName" : "",
#                 "_ctl0$m_hfClientSearchID" : "",
#                 "":""
               }
    
    js_call_pat = re.compile(r".*?__doPostBack\('(.*?)',\s*'(.*?)'\)")
    page_count = 0
    item_count = 0
    
    # form data request to further parse, must use 'parse' as its name because start_urls is parsed with function named as "parse"
    def parse(self, response):
#         print(response.request.headers)
        sel = Selector(response)
        
        if len(sel.extract()) < 10000:      # this is an empirical value to prevent error page
#             log.msg(str(len(sel.extract())) + "Retrying page with " + response.request.body, level = log.INFO)
            new_request = response.request.copy()
            new_request.dont_filter = True
            yield new_request
        else:
#             file = open("C:/Users/Dell/Desktop/test/page_%s.html"%str(self.page_count), "w")
#             for line in sel.extract():
#                 file.write(line.encode("utf-8"))
#             file.close()
#             self.page_count = self.page_count + 1
            
            log.msg("page length is " + str(len(sel.extract())))
            next_formdata = self.formdata.copy()
            
            
            next_page_js = sel.css("a#_ctl0_m_DisplayCore_dpy2")
            
            hasNext = True
            
            if next_page_js:
                next_page_js = next_page_js.xpath("@href").extract()[0]
                mat = self.js_call_pat.match(next_page_js)
                next_formdata["__EVENTTARGET"] = urllib.unquote(mat.group(1))
                next_formdata["__EVENTARGUMENT"] = urllib.unquote(mat.group(2))
                viewstate = sel.css("input#__VIEWSTATE")[0].xpath("@value").extract()[0]
            else:
                body = ""
                for line in sel.extract():
                    body += line
                start = body.rfind("_ctl0_m_DisplayCore_dpy2")
                end =  body.find("Next")
                if start >= end:
                    hasNext = False
                body = body[start:end]
                mat = re.match(r".*?%5C'(.*?)%5C.*%5C'(.*?)%5C'", body)
                next_formdata["__EVENTTARGET"] = urllib.unquote(mat.group(1))
                next_formdata["__EVENTARGUMENT"] = urllib.unquote(mat.group(2))
                start = body.find("__VIEWSTATE")
    #             print start
                end = body.find("|", start+12)
    #             print end
                viewstate =  body[start+12:end]
                
            if hasNext:
                next_formdata["__VIEWSTATE"] = urllib.unquote(viewstate)
        #         print(next_page_js)
                log.msg("Yield Next Request %d"%self.page_count, level=log.INFO)
                yield FormRequest(url=self.start_urls[0], 
                                  formdata=next_formdata,
                                  callback=self.parse)
            
            contents = sel.css("div.singleLineDisplay.ajax_display.d1085m_show table.d1085m2 td.d1085m10 a")
            for ele in contents:
                item_str = ele.extract()
                mat = self.js_call_pat.match(item_str)
                
                cur_formdata = self.formdata.copy()
                cur_formdata["__EVENTTARGET"] = urllib.unquote(mat.group(1))
                cur_formdata["__EVENTARGUMENT"] = urllib.unquote(mat.group(2))
                cur_formdata["__VIEWSTATE"] = urllib.unquote(viewstate)
                
                yield FormRequest(url=self.start_urls[0],
                                  formdata=cur_formdata,
                                  callback=self.parse_item)
            
        
    # parse each item to get detailed information
    def parse_item(self, response):
#         print(response.request.headers)
        sel = Selector(response)
        
        if len(sel.extract()) < 10000:      # this is an empirical value to prevent error page
#             log.msg(str(len(sel.extract())) + " Retrying item with " + response.request.body, level=log.INFO)
            new_request = response.request.copy()
            new_request.dont_filter = True
            yield new_request
        else:
#             file = open("C:/Users/Dell/Desktop/test/itme_%s.html"%str(self.item_count), "w")
#             for line in sel.extract():
#                 file.write(line.encode("utf-8"))
#             file.close()
#             self.item_count = self.item_count + 1
            
            log.msg("item length is " + str(len(sel.extract())))
            item = ScrapostItem()
            item["number"] = sel.xpath('//td[@class="d1045m32"]/span[@class="label d1045m33"]')[0].xpath("text()").extract()
            con1 = sel.xpath('//td[@class="d1045m10"]/span')
            item["status"] = con1[0].xpath("text()").extract()
            item["price"] = con1[1].xpath("text()").extract()
            item["location"] = sel.xpath('//td[@class="d1045m36"]/span')[0].xpath("text()").extract()
            
            yield item
    
    
    
    