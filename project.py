from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.geometry("600x600")
root.config(background = "black")


#Layout
label_image = Label(root, bg="white", highlightthickness=5)
label_image.place(relx=0.5, rely=0.5, anchor=CENTER)


#Function
img_path=""
def openFile():
    global img_path
    img_path = filedialog.askopenfilename(title=" Open Text File", filetypes=[("Image Files","*.jpg *.gif *.jpg *.png *.jpeg")])
    print(img_path)
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im)
    label_image["image"] = img
    img.close()

def rotateImage():
    global img_path
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im.rotate(90))
    label_image["image"] = img
    print(img_path)
    img.close()
    
def rotateImage1():
    global img_path
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im.rotate(-90))
    label_image["image"] = img
    print(img_path)
    img.close()
    
def rotateImage2():
    global img_path
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im.rotate(180))
    label_image["image"] = img
    print(img_path)
    img.close()
    
def rotateImage3():
    global img_path
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im.rotate(0))
    label_image["image"] = img
    print(img_path)
    img.close()
    

#Open Image Button    
btn=Button(root,text="Open Image",font= ("Times New Roman0", 12),bg="grey",fg="white", command=openFile, relief=SOLID, padx=15, pady=10)
btn.place(relx=0.5,rely=0.05,anchor=CENTER)

# Image Rotating Button

btn1=Button(root,text="Rotate Image 90",font= ("Times New Roman0", 12),bg="grey",fg="white", command=rotateImage, relief=SOLID, padx=15, pady=10)
btn1.place(relx=0.2,rely=0.75,anchor=CENTER)

btn2=Button(root,text="Rotate Image -90",font= ("Times New Roman0", 12),bg="grey",fg="white", command=rotateImage1, relief=SOLID, padx=15, pady=10)
btn2.place(relx=0.8,rely=0.75,anchor=CENTER)

btn3=Button(root,text="Rotate Image 180",font= ("Times New Roman0", 12),bg="grey",fg="white", command=rotateImage2, relief=SOLID, padx=15, pady=10)
btn3.place(relx=0.5,rely=0.75,anchor=CENTER)

btn4=Button(root,text="Reset The Image",font= ("Times New Roman0", 12),bg="grey",fg="white", command=rotateImage3, relief=SOLID, padx=15, pady=10)
btn4.place(relx=0.5,rely=0.85,anchor=CENTER)

label_footer = Label(root,text="Created by Rudraksh", bg="black", fg="white" ,font = 8)
label_footer.place(relx=0.5, rely=0.95, anchor=CENTER)

root.mainloop()
