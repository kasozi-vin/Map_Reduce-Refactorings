from datetime import date
from urllib import request



def generate_links(start_date, end_date):
    blog_urls = []
    start = date(*start_date)
    end = date(*end_date)
    while start < end:
       pretty_date = start.strftime('%m-%d-%Y')
       blog_urls.append(f'https://arch-rival-business.com/blog/{pretty_date}')
       start = date.fromordinal(start.toordinal() + 1)
    return blog_urls

def get_html(urls):
    html = []
    for url in urls:
        html.append(request.urlopen(url))
    return html