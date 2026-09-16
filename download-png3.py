import urllib.request

mem = urllib.request.urlopen("http://uta.pw/shodou/img/28/214.png").read()
with open(savename, mode="wd") as f:
    f.write(mem)