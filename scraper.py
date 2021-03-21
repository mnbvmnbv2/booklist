from requests_html import HTMLSession

def scrapeBook(isbn):
    s = HTMLSession()
    r = s.get('https://www.amazon.com/dp/' + isbn)
    r.html.render(sleep=1)

    books = {
        'title' : r.html.xpath('//*[@id="productTitle"]', first=True).text,
        'author' : r.html.xpath('//*[@id="bylineInfo"]/span/span[1]/a[1]', first=True).text,
        'publisher' : r.html.xpath('//*[@id="anonCarousel4"]/ol/li[3]/div/div[3]/span', first=True).text,
    }

    print(book)
    return book

scrapeBook('1599869772')