from bs4 import BeautifulSoup
import requests
import pandas as pd
''' From Consumer Affairs Website '''
''' Humana '''

url="https://www.consumeraffairs.com/insurance/humana.html"
review=[]    # starting from page2
star=[]      # starting from page2
# for page1
response=requests.get(url)
data=response.text
soup=BeautifulSoup(data,'lxml')
review_first=[ span.next_sibling.next_sibling.string for span in soup.find_all('span', class_="ca-txt-cpt ca-txt--clr-gray")]
star_first=[float(div.meta.next_sibling['data-rating']) for div in soup.find_all('div', class_="rvw__hdr-stat")]
# storing the reviews and corresponding stars in review, star list which are 2D lists
sum_humana=0
for i in range(2,11,1):
    page=url + "?page="+str(i)
    response = requests.get(page)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    review.append([span.next_sibling.next_sibling.string for span in soup.find_all('span', class_="ca-txt-cpt ca-txt--clr-gray")])
    star.append([div.meta.next_sibling['data-rating'] for div in soup.find_all('div', class_="rvw__hdr-stat")])
    print("No of reviews in page",i,":",len(review[i-2]))
    sum_humana=sum_humana + len(review[i-2])
# storing the 2D list content into a 1D list
print("Total Humana Reviews:",sum_humana+len(review_first))
new_star=[]
new_review=[]
for i in range(0,len(review)):
    for j in star[i]:
        new_star.append(float(j))
for i in range(0,len(review)):
    for j in review[i]:
        new_review.append(j)
# combined list of humana reviews and stars from page-1 to page-10
humana_review = review_first+new_review
humana_star = star_first + new_star
humana_data={'Reviews':humana_review,
             'Rating':humana_star,
             'Company':'Humana'}
df1=pd.DataFrame(humana_data)
print(df1.head())


# bcbs
bcbs_url="https://www.consumeraffairs.com/insurance/bluecross_il.html"
review_bcbs=[]    # starting from page2
star_bcbs=[]      # starting from page2
response_bcbs=requests.get(bcbs_url)
data_bcbs=response_bcbs.text
soup=BeautifulSoup(data_bcbs,'lxml')
review_first_bcbs=[ span.next_sibling.next_sibling.string for span in soup.find_all('span', class_="ca-txt-cpt ca-txt--clr-gray")]
star_first_bcbs=[float(div.meta.next_sibling['data-rating']) for div in soup.find_all('div', class_="rvw__hdr-stat")]

# storing the reviews and corresponding stars in review, star list which are 2D lists
for i in range(2,5,1):
    page=bcbs_url + "?page="+str(i)
    response_bcbs = requests.get(page)
    data = response_bcbs.text
    soup = BeautifulSoup(data, 'lxml')
    review_bcbs.append([span.next_sibling.next_sibling.string for span in soup.find_all('span', class_="ca-txt-cpt ca-txt--clr-gray")])
    star_bcbs.append([div.meta.next_sibling['data-rating'] for div in soup.find_all('div', class_="rvw__hdr-stat")])
# storing the 2D list content into a 1D list
new_star_bcbs=[]
new_review_bcbs=[]
for i in range(0,len(review_bcbs)):
    for j in star_bcbs[i]:
        new_star_bcbs.append(float(j))
for i in range(0,len(review_bcbs)):
    for j in review_bcbs[i]:
        new_review_bcbs.append(j)
# combined list of humana reviews and stars from page-1 to page-10
bcbs_review = review_first_bcbs+new_review_bcbs[0:len(new_review_bcbs)-12]
bcbs_star = star_first_bcbs + new_star_bcbs
bcbs_data={'Reviews':bcbs_review,
             'Rating':bcbs_star,
             'Company':'BCBS Illinois'}
df2=pd.DataFrame(bcbs_data)

#UHC
uhc_url="https://www.consumeraffairs.com/insurance/united_health_care.html"
review_uhc=[]    # starting from page2
star_uhc=[]      # starting from page2
# storing the reviews and corresponding stars in review, star list which are 2D lists

for i in range(2,18):
    page=uhc_url + "?page="+str(i)
    response_uhc = requests.get(page)
    data = response_uhc.text
    soup = BeautifulSoup(data, 'lxml')
    review_uhc.append([span.next_sibling.next_sibling.string for span in soup.find_all('span', class_="ca-txt-cpt ca-txt--clr-gray")])
    star_uhc.append([div.meta.next_sibling['data-rating'] for div in soup.find_all('div', class_="rvw__hdr-stat")])
# storing the 2D list content into a 1D list
new_star_uhc=[]
new_review_uhc=[]
for i in range(0,len(review_uhc)):
    for j in star_uhc[i]:
        new_star_uhc.append(float(j))
for i in range(0,len(review_uhc)):
    for j in review_uhc[i]:
        new_review_uhc.append(j)
# combined list of UHC reviews and stars from page-1 to page-10
uhc_review = new_review_uhc[:]
uhc_star = new_star_uhc[:]
uhc_data={'Reviews':uhc_review,
             'Rating':uhc_star,
             'Company':'United Health Care'}
df3=pd.DataFrame(uhc_data)

#bcbs Florida
bcbsfl_url="https://www.consumeraffairs.com/insurance/bluecross_fl.html"
review_bcbsfl=[]    # starting from page2
star_bcbsfl=[]      # starting from page2

response_bcbsfl=requests.get(bcbsfl_url)
data_bcbsfl=response_bcbsfl.text
soup=BeautifulSoup(data_bcbsfl,'lxml')
review_first_bcbsfl=[ span.next_sibling.next_sibling.string for span in soup.find_all('span', class_="ca-txt-cpt ca-txt--clr-gray")]
star_first_bcbsfl=[float(div.meta.next_sibling['data-rating']) for div in soup.find_all('div', class_="rvw__hdr-stat")]

# storing the reviews and corresponding stars in review, star list which are 2D lists
for i in range(3,11,1):
    if i==5:
        continue
    page=bcbsfl_url + "?page="+str(i)
    response_bcbsfl = requests.get(page)
    data = response_bcbsfl.text
    soup = BeautifulSoup(data, 'lxml')
    review_bcbsfl.append([span.next_sibling.next_sibling.string for span in soup.find_all('span', class_="ca-txt-cpt ca-txt--clr-gray")])
    star_bcbsfl.append([div.meta.next_sibling['data-rating'] for div in soup.find_all('div', class_="rvw__hdr-stat")])
# storing the 2D list content into a 1D list
new_star_bcbsfl=[]
new_review_bcbsfl=[]
for i in range(0,len(review_bcbsfl)):
    for j in star_bcbsfl[i]:
        new_star_bcbsfl.append(float(j))
for i in range(0,len(review_bcbsfl)):
    for j in review_bcbsfl[i]:
        new_review_bcbsfl.append(j)
# combined list of humana reviews and stars from page-1 to page-10
bcbsfl_review = review_first_bcbsfl + new_review_bcbsfl[:]
bcbsfl_star = star_first_bcbsfl + new_star_bcbsfl[:]

bcbsfl_data={'Reviews':bcbsfl_review,
             'Rating':bcbsfl_star,
             'Company':'BCBS Florida'}
df4=pd.DataFrame(bcbsfl_data)

dataset=pd.concat([df1,df2,df3,df4])
export_csv = dataset.to_csv(r'C:\Users\nlakhotia\Desktop\my files\nakul\Day-2-Pandas,Numpy\Web Scraping Course\Beautifulsoup\webscraping_projects\Major Project\dataset.csv',header=True)



