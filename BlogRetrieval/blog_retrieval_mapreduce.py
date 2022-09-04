from datetime import date
from multiprocessing import Pool
from urllib import request

def generate_links(start_date, end_date):
    start = date(*start_date)
    end = date(*end_date)
    while start < end:
       pretty_date = start.strftime('%m-%d-%Y')
       yield  f'https://arch-rival-business.com/blog/{pretty_date}'
       start = date.fromordinal(start.toordinal() + 1)

def get_html(url):
    return request.urlopen(url)


if __name__ == '__main__':
  with Pool() as P:
     
    results = P.map(get_html, generate_links((2000, 1, 1), (2001, 1, 1)))

