# HQ-Trivia-Googler
Googles HQ Trivia Questions And Returns An Answer

Uses sidesync to show the screen of my samsungy galaxy s6 on my laptop which is screenshotted by pillow imagegrab and transcribed using tesseract in python with pytesseract. The question is then googled using requests, parsed using bs4, and the descriptions of the search is checked to see if any of the answers can be found within. If none of the answers are found the answer is added to the search and the count is done again. 
