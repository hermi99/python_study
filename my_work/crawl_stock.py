import requests
import bs4

# page_link = "http://vip.mk.co.kr/newSt/rate/item_all.php"
# page_link = "http://finance.daum.net/domestic/all_quotes"
page_link = "http://stock.hankyung.com/apps/rank.capitalization"

page_response = requests.get(page_link)

# print("page_content=>", page_response.content)

page_content = bs4.BeautifulSoup(page_response.content, "html.parser")
# print("예쁘게 page_conetnt=>", page_content)


print()
print("주식 시세 출력하기")
print("=========================")

stocks = page_content.select(
    'tr.crUp'
    )

# i = 0
for stock in stocks:
    # print("stock=>", stock, "\n")

    company_name = stock.select('td.sbj > a')[0].text
    # print("company_name:", company_name)

    num_cs = stock.select('td.num_c')
    price = num_cs[0].text
    up = num_cs[1].text
    rate = num_cs[2].text

    print("종목명 : {}\t, 현재가 : {}\t, 전일비 : {}\t, 등락율 : {}\t"
          .format(company_name, price, up, rate))

    # i += 1
    # if i >= 1:
    #     break


# print(stocks[1], "\n")
# print(stocks[2], "\n")
# print(stocks[3], "\n")
# print(stocks[4], "\n")
# print(stocks[5], "\n")

# for stock in stocks:
#     print(stock.select('td[width="60"]'))

"""
<td class="st2" width="92">
    <a href="javascript:goPrice('000020&amp;MSid=&amp;msPortfolioID=')" 
    title="000020">동화약품</a>
</td>
"""
# company_names = page_content.select(
#     'tr > td.st2 > a'
#     )
# print(company_names[0].text)
#
#
# """
# <td align="right" width="60">9,640</td>
# """
# prices = page_content.select(
#     'tr > td'
#     )
# print(prices[0].text)