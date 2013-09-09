#encoding=utf-8

"""
"""
import urllib
import urllib2
import base64
import simplejson as json
import socket
import time
from bs4 import BeautifulSoup



##################################################


personID = "441201196511284138"
personName = "牧宏博"
idAdress = "广东省 肇庆市 市辖区"
recvAddr = "清华科技园1#103"
districtAddr = "海淀区"
price_limit = 3000


orderprpmt_url = "http://mall.10010.com/mall-web/GoodsDetail/promtlyBuy"
orderconfirm_url = 'http://mall.10010.com/mall-web/OrderSubmit/submitOrder'
iphone5_url = "http://mall.10010.com/goodsdetail/111212076031.html"
phonenum_url = "http://num.10010.com/NumApp/GoodsDetail/queryMoreNums?callback=jsonp_queryMoreNums&province=11&cityCode=110&preFeeSel=0&keyValue=&rankMoney=286&goodsId=111212076031&roleValue=&mid=1100000&q_p=53&_=1378618016062"


##################################################

cookie_src = "pgv_pvi=7533068288; mallcity=11|110; gipgeo=11|110; piw=%7B%22login_name%22%3A%22wangjun0125%40gmail.com%22%2C%22nickName%22%3A%22wangjun0125%40gmail.com%22%2C%22rme%22%3A%7B%22ac%22%3A%22%22%2C%22at%22%3A%22%22%2C%22pt%22%3A%2205%22%2C%22u%22%3A%22wangjun0125%40gmail.com%22%7D%2C%22verifyState%22%3A%220%22%7D; JUT=VVbPwLw7qNJ8Sz9Y9m32J5ib/EY7exMnMU6E2KjnAyjcGpPJKMRy91K5aSBz7+rB+/wTa2zIxUvibz1HruWae7TRtZDbyK1yPbed056Vs1EqjstNOr4TyrhYWHgJSfpyKePikhfkBEgrjZyhUhXAwIjsKXWywBtGjbpFI+vB4pnbeJIz/zKogWTFtAP3RtF8nE4GRSQ6a1UG2CSdxkFdjvjQm27TZHfRgRiybl12enYS9RzWyEajjiBNWqvhl9RFsKqNqxkx+b3g1cB8zFDLrg==b6FZ6ZjPxrLixboIyFb+Bw==; pgv_si=s6846266368; WT_FPC=id=27bce9030473d09519c1378205803976:lv=1378525270849:ss=1378525157376; BrowseHistoryCookie=111212076031%3A%2Fuploader%2Ftemp%2F20121207190711-354760960_50_50.jpg%3AiPhone5(16G)%E3%80%90%E7%BD%91%E5%8E%854%E5%91%A8%E5%B9%B4%E5%BA%86%E3%80%91%3A5499%3A%3A%3A%3A; Hm_lvt_9208c8c641bfb0560ce7884c36938d9d=1378205805,1378525158; Hm_lpvt_9208c8c641bfb0560ce7884c36938d9d=1378525271; __utma=231252639.310505334.1378205805.1378205805.1378525158.2; __utmb=231252639.14.10.1378525158; __utmc=231252639; __utmz=231252639.1378205805.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=231252639.Beijing"
accept_src = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
acc_set = "GBK,utf-8;q=0.7,*;q=0.3"
acc_encoding = "deflate"
acc_lan = "zh-CN,zh;q=0.8"
host_src = "mall.10010.com"
ua_src = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11"

##################################################

def build_request(url, params=None,method=None):
    theheaders = {
        "User-Agent": ua_src,
        "Accept": accept_src,
        "Accept-Charset": acc_set,
        "Accept-Encoding": acc_encoding,
        "Referer": host_src,
        "Cookie": cookie_src,
        "Host": host_src
        }
    if params == None:
        req = urllib2.Request(url, headers=theheaders)
        return req
    else:
        thedata = urllib.urlencode(params)
        req = urllib2.Request(url, data=thedata, headers=theheaders)
        if method != None:
            req.get_method = lambda: method
        return req

def parse_price(content):
    soup = BeautifulSoup(content)
    dl = soup.find("div",attrs={"class":"detailedList"})
    price_td = dl.find_all("td")[-1]
    return str(price_td)[6:-5]
    

def parse_phone_number(content):
    target = content.split('":')[1]
    target = target[1:-14]
    items = target.split(',')
    i = 0
    while(i < len(items)-6):
        phonenum = items[i]
        t1 = int(items[i+1])
        t2 = int(items[i+2])
        t3 = int(items[i+3])
        t4 = int(items[i+4])
        i = i+5
        if (t1+t2+t3+t4) == 0:
            print "find a number..."+ phonenum
            return phonenum
    return -1

def build_order_param(phonenum):
    formdata = {
        "goodsId":"111212076031",
        "activityId":"20130524180046009697",
        "activityType":"4",
        "activityProtper":"24",
        "provinceCode":"11",
        "cityCode":"110",
        "number":phonenum,
        "numGroup":"",
        "numFrom":"A000020V000001",
        "numberFee":"0",
        "preFeeVal":"",
        "oldPreFee":"0",
        "productId": "99002309",
        "difPlace":0,
        "localFee":0,
        "remoteFee":0,
        "isOnlinepay":1,
        "isReceivepay":0,
        "totalPrice":2750000,
        "usimPrice":0,
        "productType":"iPhone",
        "productValue":286,
        "custTag":1,
        "brandCode":"AP",
        "moduleCode":"iP516G",
        "colorCode":"9809120800036799",
        "merchantId":"1100000",
        "tmpId":"60000009",
        "inventoryType":1,
        "privilegePack":""
        }
    
    return formdata

def build_confirm_param(phonenum,idname,idcardnum,idaddress,recvaddr,districtname,updatetime):
    formdata = {
        "paramStr":{"payTypeCode":"01",
                    "payWayCode":"",
                    "payInstalmentBankCode":"",
                    "payInstalmentTerm":""
            },
        "delivery":{"dispachCode":"01",
                    "dlvTypeCode":"01"
            },
        "networkData":{"hostName":idname,
                       "idCard":idcardnum,
                       "psptTypeCode":"02",
                       "idCardAddress":idaddress
            },
        "nowGiftValue":0,
        "postAddr":{"CityName":"北京市",
                    "UpdateTime":updatetime,
                    "CityCode":"110100",
                    "ReceiverPsptNo":"null",
                    "EssProvinceCode":"11",
                    "PostId":"5913090803410300",
                    "PartitionId":"3",
                    "Email":"null",
                    "DefaultTag":"1",
                    "PostCode":"100010",
                    "EssDistrictCode":"null",
                    "ProvinceCode":"110000",
                    "PostAddr":recvaddr,
                    "FixPhone":"",
                    "DistrictName":districtname,
                    "MobilePhone":phonenum,
                    "ProvinceName":"北京",
                    "DistrictCode":"110108",
                    "ReceiverName":idname,
                    "ReceiverPsptType":"null",
                    "EssCityCode":"110"
                    },
        "billingInfo":{"moneyCardNum":"",
                       "invoiceTitle":"",
                       "invoiceContent":"01",
                       "orderRemarks":"",
                       "referrerName":"",
                       "referrerCode":""                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
            },
         "inventoryType":1

    }
    return formdata

def get_html(req):
    resp = urllib2.urlopen(req)
    if resp.getcode() != 200:
        return -1, -1
    timestamp = resp.info()["Date"]
    htext = resp.read()
    return timestamp, htext

def check_confirm(content):
    return 1

def start():
    print "begin..."
    req_phone = build_request(phonenum_url)
    phonenum = -1
    index = 0
    while (phonenum==-1):
        timestamp, htext = get_html(req_phone)
        phonenum = parse_phone_number(htext)
        if index > 20:
            phonenum = "18501340542"
            break
        index += 1
        if phonenum == -1:
            print "invalid phone number, try again..." + str(index)
            time.sleep(1)
    
    params = build_order_param(phonenum)
    req_order = build_request(orderprpmt_url,params,'POST')
    ts, htext = get_html(req_order)
    price = parse_price(htext)
    if price > price_limit:
        return -1,ts       
    #open("D:/Job/tmp.html", "w").write(htext)
    confirmparams = build_confirm_param(phonenum,personName,personID,idAdress,recvAddr,districtAddr,timestamp)
    req_confirm = build_request(orderconfirm_url,confirmparams,'POST')
    ts, htext = get_html(req_confirm)
    open("D:/Job/tmp.html", "w").write(htext)
    cf = check_confirm(htext)
    return cf,ts

###################################################


if __name__ == "__main__":
    ret = -1
    tnum = 0
    while(ret==-1):
        ret,ts = start()
        time.sleep(1)
        tnum += 1
        print "try..." + str(tnum)
    
    

    
    






