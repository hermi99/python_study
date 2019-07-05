import requests
import bs4

page_link = "http://blog.daum.net"

page_response = requests.get(page_link)

# print("page_content=>", page_response.content)

page_content = bs4.BeautifulSoup(page_response.content, "html.parser")
# print("예쁘게 page_conetnt=>", page_content)


blogs = page_content.select(
    'ul.list_excellent > li'
    )

print("\n\n\n\n블로그 목록 구하기\n")
#

for index, blog in enumerate(blogs):
    title = blog.select('a.link_excellent > span.post_info > strong.tit_post')[0].text
    writer = blog.select('a.link_excellent > span.post_info > span.txt_name')[0].text
    link = blog.select('a.link_excellent')[0]['href']

    print("제목 : {}\t, 글쓴이: {}\t, 링크: {}\t".format(title, writer, link))

