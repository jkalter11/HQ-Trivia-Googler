import PIL
from PIL import ImageGrab
import pytesseract
import requests
from bs4 import BeautifulSoup

#grab screenshot 
img = PIL.ImageGrab.grab(bbox=(30,250,350,600))

#path for tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

# Simple image to string
raw = pytesseract.image_to_string(img)
raw = raw.splitlines()

#seperate questions and answers
answers = [line for line in raw if raw[raw.index(line)-1]=='']
first_answer = raw.index(answers[0])
question = " ".join(raw[0:first_answer])

#google the question
url = 'https://www.google.com/search?q='
query = question.replace(" ","%20")
url = url+query
source = requests.get(url).content
soup = BeautifulSoup(source,"html.parser")
descs = soup.findAll('span',{'class':'st'})

#check for answers in google descriptions
vote = {el:0 for el in answers}
for desc in descs:
    desc = str(desc)
    for answer in answers:
        if answer in desc:
            vote[answer]+=1
if sum(vote.values())== 0:
    print('BACK UP PLAN!')
    for answer in answers:
        query += answer
        source = requests.get(url).content
        soup = BeautifulSoup(source,"html.parser")
        descs = soup.findAll('span',{'class':'st'})
        for desc in descs:
            desc = str(desc)
            for answer in answers:
                if answer in desc:
                    vote[answer]+=1
        


img.show()
print(question)                
print(vote)
