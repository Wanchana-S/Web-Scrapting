# https://www.lottery.co.th/small
import requests
from bs4 import BeautifulSoup

url = "https://www.lottery.co.th/small"
data = requests.get(url,headers={"User-Agent" : "Mozilla/5.0"})
soup = BeautifulSoup(data.text,"html.parser")
lottery = soup.find_all("button",{"class":"btn-primary"}) #html + ผลหวย
lottery_list = []

for item in lottery:
    lottery_list.append(item.text)

#ผลหวย
print("ผลฉลากกินแบ่งประจำวันที่ 16 มิถุนายน 2568") 
print("รางวัลที่ 1 :",lottery_list[0]) 
print("เลขท้าย 2 ตัว :",lottery_list[1]) 
print(f"เลขหน้า 3 ตัว :{lottery_list[2]} , {lottery_list[3]}") 
print(f"เลขท้าย 3 ตัว :{lottery_list[4]} , {lottery_list[5]}") 