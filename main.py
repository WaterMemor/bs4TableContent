import requests
from bs4 import BeautifulSoup


VisaRequired_second = []
VisaRequired = []
#for the first
url=str("https://en.wikipedia.org/wiki/Visa_requirements_for_Turkish_citizens")
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')


# table = soup.select('td:-soup-contains("Visa not required")')
# for i in table:
#     VisaNotRequired.append(i.previous_sibling.previous_sibling.text.replace('\xa0', '').replace('\n',''))

# print(VisaNotRequired)

table = soup.select('td:-soup-contains("Visa required")')
for i in table:
    VisaRequired.append(i.previous_sibling.previous_sibling.text.replace('\xa0', '').replace('\n',''))

#for the second country
url_second=str("https://en.wikipedia.org/wiki/Visa_requirements_for_Russian_citizens")
r = requests.get(url_second)
soup = BeautifulSoup(r.text,'html.parser')
table_second = soup.select('td:-soup-contains("Visa required")')
for i in table_second:
    VisaRequired_second.append(i.previous_sibling.previous_sibling.text.replace('\xa0', '').replace('\n',''))

result=list(set(VisaRequired_second) & set(VisaRequired))
for i in result:
    print(i)



