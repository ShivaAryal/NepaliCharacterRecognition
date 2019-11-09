from keras.models import load_model
import cv2
import numpy as np
import os

model = load_model('final_model.hs')

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

dict = {}
dict['[0]'] = '\u0915'
dict['[1]'] = '\u0916'
dict['[2]'] = '\u0917'
dict['[3]'] = '\u0918'
dict['[4]'] = '\u0919'
dict['[5]'] = '\u091A'
dict['[6]'] = '\u091B'
dict['[7]'] = '\u091C'
dict['[8]'] = '\u091D'
dict['[9]'] = '\u091E'
dict['[10]']= '\u091F'
dict['[11]'] = '\u0920'
dict['[12]'] = '\u0921'
dict['[13]'] = '\u0922'
dict['[14]'] = '\u0923'
dict['[15]'] = '\u0924'
dict['[16]'] = '\u0925'
dict['[17]'] = '\u0926'
dict['[18]'] = '\u0927'
dict['[19]'] = '\u0928'
dict['[20]'] = '\u092A'
dict['[21]'] = '\u092B'
dict['[22]'] = '\u092C'
dict['[23]'] = '\u092D'
dict['[24]'] = '\u092E'
dict['[25]'] = '\u092F'
dict['[26]'] = '\u0930'
dict['[27]'] = '\u0932'
dict['[28]'] = '\u0935'
dict['[29]'] = '\u0936'
dict['[30]'] = '\u0937'
dict['[31]'] = '\u0938'
dict['[32]'] = '\u0939'
dict['[33]'] = 'alpha'
dict['[34]'] = '\u0915'
dict['[35]'] = 'omega'

from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *

width = 200
height = 200
center = height//2
white = (255, 255, 255)
green = (0,128,0)
totalString=''

def main():
    global root
    root = Tk()
    global cv
    global text2
    text1 = Text(root,height=1,font=('Arial', 12, 'bold', 'italic'))
    text2  = Text(root,height=2,font=('Arial', 12, 'bold', 'italic'))
    # Tkinter create a canvas to draw on
    text1.insert(INSERT, "                       Please write the Nepali image")
    text1.pack()
    cv = Canvas(root, width=width, height=height, bg='white')
    cv.master.title("A Simple Nepali Character Recognizer")
    cv.pack()
    global image1
    image1 = PIL.Image.new("RGB", (800,400), white)
    global draw
    draw = ImageDraw.Draw(image1)
    cv.pack(expand=NO, fill=BOTH)
    
    cv.bind("<B1-Motion>", paint)
    button=Button(text="SUBMIT",command=save)
    button.pack()
    button1=Button(text="CLEAR",command=clear)
    button1.pack()
    root.mainloop()


def save():
    filename = "image.png"
    global image1
    image1.save(filename)
    resize(filename)
    global cv
    # cv.delete("all")
    # os.remove("image.png")

def paint(event):
    x1, y1 = (event.x - 3), (event.y - 3)
    x2, y2 = (event.x + 3), (event.y + 3)
    global cv
    cv.create_line(x1, y1, x2, y2, fill="black",width=4,capstyle=ROUND,smooth=TRUE,splinesteps=36)
    global draw
    draw.line([x1, y1, x2, y2],fill="black",width=3)

def resize(image):
    # code for converting black and white to white and black
    from PIL import Image
    from matplotlib import pyplot as plt
    img1 = Image.open(image)
    width, height = img1.size
    px = img1.load()
    for i in range(width):
        for j in range(height):
            if ( px[i,j] < (150,150,150) ):
                px[i,j] = (255, 255, 255)
            elif ( px[i,j] > (150,150,150) ):
                px[i,j] = (0,0,0)
    img1.save("ConvertedImg1.png", "PNG")
    # code for croping the image
    im2 = Image.open("ConvertedImg1.png")
    img = im2.load()
    width , height = im2.size
    posX = []
    for i in range(width):
        for j in range(height):
            if (img[i,j] == (255,255,255)):
                posX.append([i,j])
            else:
                pass
    x = []
    y = []
    for i in range(len(posX)):
        x.append(posX[i][0])
        y.append(posX[i][1])
    im = im2.crop((min(x) , min(y), max(x) , max(y)))
    im.save("ConvertedImg.png")
    # code for prediction
    # image = cv2.imread("ConvertedImg.png")
    # image = cv2.resize(image,(150,150))
    # image= np.reshape(image,[1,150,150,3])
    # predict(image)
    segment("ConvertedImg.png")
 
def segment(image):
    #print(image)
    heightArray=[]
    segmentPoint=[]
    from PIL import Image
    img = Image.open(image)
    height, width = img.size
    px = img.load()
    for j in range(height):
        for i in range(width):
            if(px[j,i]==(255,255,255)):
                #print(str(i)+"'",str(j))
                if j not in heightArray:
                    heightArray.append(j)
    for k in range(len(heightArray)-1):
        if(abs(heightArray[k]-heightArray[k+1])>15):
            segmentPoint.append(heightArray[k])
            segmentPoint.append(heightArray[k+1])
    # print("Segment Ppoint:"+str(segmentPoint))
    i=0
    if(len(segmentPoint)>0):
        for k in range(len(segmentPoint)):
            im = ""
            if(k==0):
                initialPointX = 0
                finalPointX = segmentPoint[0]+10
                im = img.crop((initialPointX,0,finalPointX,150))
                im.save("segmented"+str(i)+".png")
                newImage = Image.open("segmented"+str(i)+".png")
                height,width = newImage.size
                px = newImage.load()
                for heightIndex in range(height):
                    px[heightIndex,0]=(255,255,255)
                    px[heightIndex,1]=(255,255,255)
                    px[heightIndex,2]=(255,255,255)
                    px[heightIndex,3]=(255,255,255)
                    px[heightIndex,4]=(255,255,255)
                    px[heightIndex,5]=(255,255,255)
                    px[heightIndex,6]=(255,255,255)
                newImage.save("segmented"+str(i)+".png")
                i=i+1
            elif(k==len(segmentPoint)-1):
                initialPointX=segmentPoint[len(segmentPoint)-1]-30
                if(len(segmentPoint)==2):
                    #print("i m here")
                    finalPointX = width-20
                if(len(segmentPoint)>2):
                    #print(width)
                    finalPointX = segmentPoint[len(segmentPoint)-1]+50
                im = img.crop((initialPointX+20,0,finalPointX,150))
                im.save("segmented"+str(i)+".png")
                newImage = Image.open("segmented"+str(i)+".png")
                height,width = newImage.size
                px = newImage.load()
                for heightIndex in range(height):
                    px[heightIndex,0]=(255,255,255)
                    px[heightIndex,1]=(255,255,255)
                    px[heightIndex,2]=(255,255,255)
                    px[heightIndex,3]=(255,255,255)
                    px[heightIndex,4]=(255,255,255)
                    px[heightIndex,5]=(255,255,255)
                    px[heightIndex,6]=(255,255,255)   
                newImage.save("segmented"+str(i)+".png")
                i=i+1
            else:
                if(k%2==1):
                    initialPointX = segmentPoint[k]-10
                    finalPointX = segmentPoint[k+1]+10
                    im = img.crop((initialPointX,0,finalPointX,150))
                    im.save("segmented"+str(i)+".png")
                    newImage = Image.open("segmented"+str(i)+".png")
                    height,width = newImage.size
                    px = newImage.load()
                    for heightIndex in range(height):
                        px[heightIndex,0]=(255,255,255)
                        px[heightIndex,1]=(255,255,255)
                        px[heightIndex,2]=(255,255,255)
                        px[heightIndex,3]=(255,255,255)
                        px[heightIndex,4]=(255,255,255)
                        px[heightIndex,5]=(255,255,255)
                        px[heightIndex,6]=(255,255,255)
                    
                    
                    newImage.save("segmented"+str(i)+".png")
                    i=i+1
        noofImages = i
        for k in range(noofImages):
            crop("segmented"+str(k)+".png",k)
        predict(k)
        # os.remove("ConvertedImg.png")
        # os.remove("ConvertedImg1.png")
    else:
        im=img.crop((0,0,width,height))
        im.save("segmented0.png")
        predict(0)

def crop(imageName,k):
    from PIL import Image
    im = Image.open(imageName)
    img = im.load()
    width , height = im.size
    posX = []
    for i in range(width):
        for j in range(height):
            if (img[i,j] == (255,255,255)):
                posX.append([i,j])
            else:
                pass
    x = []
    y = []
    for i in range(len(posX)):
        x.append(posX[i][0])
        y.append(posX[i][1])
    myImage = im.crop((min(x) , min(y), max(x) , max(y)))
    myImage.save(imageName)
    
def predict(noofImages):
    global totalString
    totalString=""
    for i in range(noofImages+1):
        image = cv2.imread("segmented"+str(i)+".png")
        image = cv2.resize(image,(150,150))
        image= np.reshape(image,[1,150,150,3])
        classes = model.predict_classes(image)
        totalString=totalString+dict[str(classes)]
        os.remove("segmented"+str(i)+".png")
    print("The character is",totalString)
    global text2
    text2.insert(INSERT, "                       The written character is "+totalString)
    text2.pack()
    image=""

def clear():
    os.remove("ConvertedImg.png")
    os.remove("ConvertedImg1.png")
    os.remove("Image.png")
    global root
    global cv
    global totalString
    totalString=''
    cv.delete("all")
    global text2
    #text2.delete(1.0,END)
    root.destroy()
    main()
    
if __name__ == "__main__":
    main()
