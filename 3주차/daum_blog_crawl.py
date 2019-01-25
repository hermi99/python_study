import bs4
import requests

if __name__ == '__main__':
    page_link = "http://blog.daum.net"
    response = requests.get(page_link)

    # print(response.text)

    page_content = bs4.BeautifulSoup(response.text, "html.parser")

    blogs = page_content.select(
        'ul.list_excellent > li'
    )

    for blog in blogs:
        print("####################")
        title = blog.select('strong.tit_post')[0].text
        print(title)

        writer = blog.select('span.txt_name')[0].text
        print(writer)

        link = blog.select('a.link_excellent')[0]["href"]
        print(link)
        print("####################")
        print()









