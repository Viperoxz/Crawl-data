from bs4 import BeautifulSoup
import requests

newfile = open('output.txt', 'w')
print('Enter your familiar skills:')
familiar_skills = input('>')
print('Searching for jobs with', familiar_skills,'...')

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=1&startPage=1')
soup = BeautifulSoup(html_text.text, 'lxml')
jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx' )

for job in jobs:
    published_date = job.find('span', class_='sim-posted').text
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
        more_info = job.header.h2.a['href']
        if familiar_skills.lower() in skills or familiar_skills.capitalize() in skills or familiar_skills.upper() in skills:
            newfile.write(f'Company name: {company_name.strip()}\n')
            newfile.write(f'Required skills: {skills.strip()}\n')
            newfile.write(f'More Info: {more_info.strip()}\n')
            newfile.write('----------- \n')
newfile.close()