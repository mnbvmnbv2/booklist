from requests_html import HTMLSession
import numpy as np

isbnlist = np.genfromtxt("isbnlist.txt", delimiter=",", dtype=str).tolist()

books = [['isbn','title','author','publisher','pages','words','link']]

def scrapeBook(isbn):
    s = HTMLSession()
    r = s.get('https://www.amazon.com/dp/' + isbn)
    r.html.render(sleep=1)

    try:
        book = {
            'isbn' : isbn,
            'title' : r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'author' : r.html.xpath('//*[@id="bylineInfo"]/span/span[1]/a[1]', first=True).text,
            'publisher' : r.html.xpath('//*[@id="anonCarousel4"]/ol/li[3]/div/div[3]/span', first=True).text,
            'pages' : r.html.xpath('//*[@id="anonCarousel4"]/ol/li[1]/div/div[3]/span', first=True).text,
            'words' : str(int(r.html.xpath('//*[@id="anonCarousel4"]/ol/li[1]/div/div[3]/span', first=True).text.split(' ')[0]) * 250),
            'link' : 'https://www.amazon.com/dp/' + isbn
        }
    except:
        print('something went wrong during scraping')
        book = {
            'isbn' : isbn,
            'title' : '',
            'author' : '',
            'publisher' : '',
            'pages' : '',
            'words' : '',
            'link' : 'https://www.amazon.com/dp/' + isbn
        }

    return book

def outputBooklist():
    for isbn in isbnlist:
        book = scrapeBook(isbn)
        bookline = [book['isbn'], book['title'], book['author'], book['publisher'], book['pages'], book['words'], book['link']]
        books.append(bookline)

outputBooklist()
print(books)
np.savetxt("booklist.csv", books, fmt="%s", delimiter=",")