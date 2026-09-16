import urllib.request
import urllib.parse

#https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%B4%88%EC%BD%9C%EB%A6%BF&ackey=pcutb9lr


api="https://search.naver.com/search.naver"

values={
    "where" : "nexearch",
    "sm" : "top_hty",
    "fbm" : "0",
    "acr" : "1",
    "scq" : "초콜릿",
    "qdt" : "0",
    "ie" : "utf8",
    "query" : "초콜릿",
    "ackey" : "pcutb9lr"

}


params=urllib.parse.urlencode(values)
print("api : ", api)
print("params : ", params)

url = api + "?" + params
print ("url : ", url)

data = urllib.request.urlopen(url).read()

print("data : ", data)

text = data.decode("UTF-8")

print("text : ", text)


url = "http://uta.pw/shodou/img/28/214.png"
savename = "214.png"

urllib.request.urlretrieve(url,savename)