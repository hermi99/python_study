import requests
import bs4

isdns = ["9788950959005", "9788989938590", "9788972916802", "9791188990238"]


def print_book_info(isdn):
    # page_link = "http://www.kyobobook.co.kr/search/SearchKorbookMain.jsp?vPstrCategory=KOR&vPstrKeyWord=9788950959005&vPplace=top"
    page_link = "http://www.kyobobook.co.kr/search/SearchKorbookMain.jsp?vPstrCategory=KOR" \
                "&vPstrKeyWord={}&vPplace=top".format(isdn)

    page_response = requests.get(page_link)

    page_content = bs4.BeautifulSoup(page_response.content, "html.parser")
    # print("page_conetnt=>", page_content)


    # print()
    # print("도서 정보 출력하기")
    # print("=========================")

    books = page_content.select(
        'div.title'
        )
    book = books[0]

    title = book.select('a')[0].text
    author = page_content.select('a.author')[0].text

    print("===============================")
    print("o ISDN 검색 : {}".format(isdn))
    print("- 제목 : {}".format(title))
    print("- 작가 : {}".format(author))
    print("===============================")
    print("")


if __name__ == '__main__':
    for isdn in isdns:
        print_book_info(isdn)