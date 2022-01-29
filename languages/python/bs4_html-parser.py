from bs4 import BeautifulSoup as BS

html_doc =''
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())