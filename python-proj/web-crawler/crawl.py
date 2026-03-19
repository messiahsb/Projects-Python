from urllib.parse import urlsplit
from bs4 import BeautifulSoup


def normalize_url(input:str):

    normalized_string = urlsplit(input).hostname + urlsplit(input).path
    normalized_string = normalized_string.rstrip("/")
    return normalized_string 

def get_heading_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    heading = soup.h1.getText() if soup.h1.getText()

    print(f'{heading}')
    return heading

def get_first_paragraph_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraph = soup.p.get_text()
    return paragraph

def test_get_first_paragraph_from_html_main_priority():
    input_body = '''<html><body>
        <p></p>
        <main>
            <p>Main paragraph.</p>
        </main>
    </body></html>'''
    actual = get_first_paragraph_from_html(input_body)
    expected = "Main paragraph."
    return(actual == expected)

# test_get_first_paragraph_from_html_main_priority()
def test_get_heading_from_html_basic():
    input_body = '<html><body><h1></h1></body></html>'
    actual = get_heading_from_html(input_body)
    expected = "Test Title"
    return(actual == expected)

test_get_heading_from_html_basic()