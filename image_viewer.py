from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Let's Code with Bagul")

#(To change the window logo)
#root.iconbitmap('C:\Users\Dhananjay Bagul\PycharmProjects\Tkinter\D_logo.png')

my_img1 = ImageTk.PhotoImage(Image.open("SHIRVEL/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("SHIRVEL/2.JPG"))
my_img3 = ImageTk.PhotoImage(Image.open("SHIRVEL/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("SHIRVEL/4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("SHIRVEL/5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("SHIRVEL/6.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("SHIRVEL/7.jpg"))

img_list = [my_img1,my_img2,my_img3,my_img4,my_img5,my_img6,my_img7]
#Adding Status Bar
status = Label(root,text="Image 1 of "+str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def next(image_number):
    global button_next
    global button_prev
    global my_label

    my_label.grid_forget()
    my_label = Label(image=img_list[image_number -1])
    button_next = Button(root, text=">>", width=5, borderwidth=5, command=lambda: next(image_number+1))
    button_prev = Button(root, text="<<", width=5, borderwidth=5, command=lambda: prev(image_number-1))

    if image_number == 7:
        button_next = Button(root,text=">>",width=5,borderwidth=5,state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=1, column=2)
    button_prev.grid(row=1, column=0)
    
    #Update Status Bar
    status = Label(root, text="Image "+str(image_number)+" of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)



def prev(image_number):
    global button_next
    global button_prev
    global my_label

    my_label.grid_forget()
    my_label = Label(image=img_list[image_number - 1])
    button_next = Button(root, text=">>", width=5, borderwidth=5, command=lambda: next(image_number + 1))
    button_prev = Button(root, text="<<", width=5, borderwidth=5, command=lambda: prev(image_number - 1))

    if image_number == 1:
        button_prev = Button(root, text="<<", width=5, borderwidth=5, command=prev, state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=1, column=2)
    button_prev.grid(row=1, column=0)
    
    #Update Status Bar
    status = Label(root, text="Image "+str(image_number)+" of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

button_next = Button(root,text=">>",width=5,borderwidth=5,command=lambda:next(2))
button_prev = Button(root,text="<<",width=5,borderwidth=5,command=prev,state=DISABLED)
button_quit = Button(root,text="EXIT",command=root.quit,width=5,borderwidth=5)

button_next.grid(row=1,column=2,pady=10)
button_prev.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()
