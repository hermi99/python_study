import bs4
import requests

class Blog:
    def __init__(self, title, writer, link):
        self.title = title
        self.writer = writer
        self.link = link

    def print_blog(self):
        print("제목 : {}".format(self.title))
        print("작성자 : {}".format(self.writer))
        print("링크 : {}".format(self.link))

class BlogCrawler:
    def __init__(self):
        self.blog_list = []

    def get_blog(self):
        page_link = "http://blog.daum.net"
        response = requests.get(page_link)

        # print(response.text)

        page_content = bs4.BeautifulSoup(response.text, "html.parser")

        # print(page_content)
        blogs = page_content.select(
            'ul.list_excellent > li'
        )

        for blog in blogs:
            title = blog.select('strong.tit_post')[0].text
            writer = blog.select('span.txt_name')[0].text
            link = blog.select('a.link_excellent')[0]["href"]

            b = Blog(title, writer, link)
            self.blog_list.append(b)


if __name__ == '__main__':
    crawler = BlogCrawler()
    crawler.get_blog()
    
    # 객체의 내용을 모두 출력할때
    # for blog in crawler.blog_list:
    #     print(blog.__dict__)

    # 블로그에서 가져온 내용을 출력
    for blog in crawler.blog_list:
        blog.print_blog()













