from requests_html import HTMLSession
import numpy

isbnlist = ['1599869772']
books = [['title','author','publisher']]

def scrapeBook(isbn):
    s = HTMLSession()
    r = s.get('https://www.amazon.com/dp/' + isbn)
    r.html.render(sleep=1)

    book = {
        'title' : r.html.xpath('//*[@id="productTitle"]', first=True).text,
        'author' : r.html.xpath('//*[@id="bylineInfo"]/span/span[1]/a[1]', first=True).text,
        'publisher' : r.html.xpath('//*[@id="anonCarousel4"]/ol/li[3]/div/div[3]/span', first=True).text,
    }

    return book

def outputBooklist():
    for isbn in isbnlist:
        book = scrapeBook(isbn)
        bookline = [book['title'], book['author'], book['publisher']]
        books.append(bookline)

outputBooklist()
print(books)
numpy.savetxt("booklist.csv", books, fmt="%s", delimiter=",")