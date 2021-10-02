from gtts import gTTS
import PyPDF2
import os

pdfFileObj = open("Intern Completion Letter.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
myText = pageObj.extractText()

language = 'en'
audio = gTTS(text=myText, lang=language, slow=False)

audio.save("audiobook.mp3")
os.system("start audiobook.mp3")