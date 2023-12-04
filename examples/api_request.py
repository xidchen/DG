import json

import requests


url = "http://127.0.0.1:8000"
headers = {"Content-Type": "text/event-stream"}

config = {
    "character_gender": "女",
    "character_age": 28,
    "character_emotion": "喜悦",
    "brand_promotion_pct": 90,
    "homepage_pct": 90,
    "pinned_video_pct": 90,
    "promotion_link_pct": 90,
    "promotion_link_list": ["a.com", "b.com"],
    "account_promotion_pct": 90,
    "account_list": ["8237ak"],
    "contact_insertion_pct": 90,
    "contact_list": ["+8695555"]
}

message1 = {
    "uuid": "1",
    "blogger_account": "adam_smith",
    "video_content": "就差你了#赚钱#赚钱的方法#灰产偏门#兼职副业#偏门项目#捞偏门",
    "comment_content": "日四位数，免费带"
}
message2 = {
    "uuid": "2",
    "blogger_account": "adam_smith",
    "video_content": "就差你了#赚钱#赚钱的方法#灰产偏门#兼职副业#偏门项目#捞偏门",
    "comment_content": "日五位数，免费带"
}
message3 = {
    "uuid": "3",
    "blogger_account": "adam_smith",
    "video_content": "就差你了#赚钱#赚钱的方法#灰产偏门#兼职副业#偏门项目#捞偏门",
    "comment_content": "周六位数，免费带"
}
message4 = {
    "uuid": "4",
    "blogger_account": "adam_smith",
    "video_content": "就差你了#赚钱#赚钱的方法#灰产偏门#兼职副业#偏门项目#捞偏门",
    "comment_content": "月七位数，免费带"
}
messages = [message1, message2, message3, message4]

data = {"config": config, "messages": messages}


res = requests.post(url=url, json=data, headers=headers, stream=True)
if res.status_code == 200:
    for line in res.iter_lines():
        if line:
            print(json.loads(line[6:]))
else:
    print(f"Error: {res.status_code}")
