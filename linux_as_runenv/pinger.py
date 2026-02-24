import requests
from datetime import datetime, timedelta

url_template = "https://simurg.space/gen_file?data=obs&date={date}"

day_offset = 1
while True:
    yesterday =  datetime.now() - timedelta(days=1)

    url = url_template.format(date= yesterday.strftime("%Y-%m-%d"))

    print(f"Working with URL: {url}")

    response = requests.get(url, stream=True)


    if response.status_code == 200:
        print(f"Data are available {yesterday}")
    else:
        print("Failed to get data")
    day_offset += 1
