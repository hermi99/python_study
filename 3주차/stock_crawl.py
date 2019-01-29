import bs4
import requests

if __name__ == '__main__':
    page_link = "http://stock.hankyung.com/apps/rank.capitalization"
    response = requests.get(page_link)

    print(response.text)

    page_content = bs4.BeautifulSoup(response.content, "html.parser")

    stocks = page_content.select(
        'tr.crUp'
    )

    company = stocks[0].select('td.sbj')[0].text
    print(company)

    price = stocks[0].select('td.num_c')[0].text
    print(price)


    # for blog in blogs:
    #     print("####################")
    #     title = blog.select('strong.tit_post')[0].text
    #     print(title)
    #
    #     writer = blog.select('span.txt_name')[0].text
    #     print(writer)
    #
    #     link = blog.select('a.link_excellent')[0]["href"]
    #     print(link)
    #     print("####################")
    #     print()









