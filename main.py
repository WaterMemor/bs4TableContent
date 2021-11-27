import requests
from bs4 import BeautifulSoup


VisaNotRequired = []
VisaRequired = []
url=str("https://en.wikipedia.org/wiki/Visa_requirements_for_Turkish_citizens")
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')


table = soup.select('td:-soup-contains("Visa not required")')
for i in table:
    VisaNotRequired.append(i.previous_sibling.previous_sibling.text.replace('\xa0', '').replace('\n',''))

print(VisaNotRequired)

table = soup.select('td:-soup-contains("Visa required")')
for i in table:
    VisaRequired.append(i.previous_sibling.previous_sibling.text.replace('\xa0', '').replace('\n',''))

print(VisaRequired)
