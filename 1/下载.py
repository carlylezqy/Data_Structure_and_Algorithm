import requests
import json
import wget
from tqdm import tqdm

def get_url(sort):
    headers = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac",
        "Referer": "https://servicewechat.com/wxf257f70a11081083/109/page-frame.html",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNjM0NzI0NTk0NTQzNTUwNDY1IiwiaWF0IjoxNjc4NTg4NjYyLCJleHAiOjE2Nzg4NDc4NjJ9.0Inz2P-BspD_SigWrO2hCGqnimWgcoKcTJOYLsyZyCCjLN4ZoI3ztmS7jvsyWIC48dJLlLF5Qlt6ALnq9X0ZTw",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9"
    } 
    url = f"https://mp.huayinculture.com/huayinbk/album?albumId=1512632325010538498&sort={sort}&_t=1678589082330" # 等价下面的 
    response = requests.get(url, headers=headers).text 

    response_dict = json.loads(response)
    return response_dict["data"]["episodeName"].replace(" ", "_"), response_dict["data"]["pathUrl"]

if __name__ == "__main__":
    for i in tqdm(range(20, 97)):
        name, url = get_url(i)
        wget.download(url, f"/Users/akiyo/Downloads/{name}.mp3")