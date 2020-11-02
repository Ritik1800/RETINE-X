import gtts
from playsound import playsound
import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image

#img is a variable in which image got passed
img = 0
# for video capturing
cam = cv2.VideoCapture(0)

# checking if camera scanning images
if cam.isOpened():
            read, frame = cam.read()
            print(read)
            print(frame)
else:
    read = False

# conversion of image into gray form
img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.title('phase1')
plt.xticks([])
plt.yticks([])
plt.show()
cam.release()
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open('IMG_20200111_235637.jpg')
text = pytesseract.image_to_string(img)
print(text)

def playaudio(path):
         playsound(path)
tts = gtts.tts.gTTS(text, lang='en')
tts.save("hello.mp3")
playaudio("hello.mp3")

