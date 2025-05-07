import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
import pandas as pd # type: ignore
from datetime import datetime
import schedule # type: ignore
import time

def fetch_article():
    #Gửi yêu cầu đến trang chủ
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Đang lấy bài viết...")

    response = requests.get("https://nhandan.vn/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        #Lấy bài viết đầu tiên
        first_news = soup.find('h2', class_='story__heading')
        if first_news:
            a_tag = first_news.find('a')
            if a_tag and 'href' in a_tag.attrs:
                link = a_tag['href']

                #Lấy nội dung bài viết
                article = requests.get(link)
                soup = BeautifulSoup(article.content, "html.parser")

                #Lấy thông tin chi tiết
                title_tag = soup.find("h1", class_="article__title cms-title")
                title = title_tag.text.strip() if title_tag else ""

                summary_tag = soup.find("div", class_="article__sapo cms-desc")
                summary = summary_tag.text.strip() if summary_tag else ""

                body = soup.find("div", class_="article__body cms-body")
                content = body.decode_contents() if body else ""

                image_tag = body.find("img") if body else None
                image = image_tag['src'] if image_tag and 'src' in image_tag.attrs else ""

                #Gắn thêm thời gian (giờ phút giây)
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # In kết quả
                print("Tiêu đề:", title)
                print("Thời gian lấy:", timestamp)
                print("Link:", link)
                print("Tóm tắt:", summary)
                print("Ảnh:", image)
                print("Nội dung (HTML):", content[:200], "...")  # In thử 200 ký tự đầu

                # Lưu vào Excel
                df = pd.DataFrame([[title, summary, content, image, link, timestamp]],
                                columns=["title", "summary", "content", "image", "url", "timestamp"])
                df.to_excel("baoNhanDan.xlsx", index=False)
            else:
                print("Không tìm thấy thẻ <a> trong bài viết đầu tiên.")
        else:
            print("Không tìm thấy bài viết đầu tiên.")
    else:
        print("Không thể truy cập trang Dân Trí.")

schedule.every().day.at("06:00").do(fetch_article)

print("Đang chờ đến 6h sáng để chạy")

while True:
    schedule.run_pending()
    time.sleep(30) 