from urllib import request
# from bs4 import BeautifulSoup
def crawl(url):
    response = request.urlopen(url)
    text = str(response.read())
    print(text)
    # Unfortunately, beautiful soup is not migrated to python3.
    '''
    soup = BeautifulSoup(text)
    for link in soup.findAll('a'):
        title = link.string
        href = link.get('href')
        print(title + ' : ' + href)
    '''
crawl('http://www.nytimes.com')