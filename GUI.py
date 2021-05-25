from os import rename
from tkinter import *
from tkinter import filedialog
import subprocess
import shutil

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Image files",
                                                        "*.png*"), ))
    filename=str(filename).replace("/","\\")
    print(filename)
    #os.rename(filename,"C:\\Users\\zmana\\Desktop\\BEStuff\\MAINTEST.png")
    shutil.copy(filename,"C:\\Users\\zmana\\Desktop\\BEStuff\\Uploads\\1.png")



    #subprocess.run(["xcopy",filename,"C:\\Users\\zmana\\Desktop\\BEStuff\\Uploads\\"])
    
def colorit():
    subprocess.run([ "python","PATH TO MODEL FILE" ])

    #   RUNS THE MAIN MODEL CODE 
    pass




root  =  Tk()
root.configure(background="Light Gray")
root.geometry("1400x700+10+20")
root.minsize(1400,700)
root.maxsize(1400,700)


canvas = Canvas(root, width = 1400, height = 700)      
canvas.pack()      
img = PhotoImage(file="C:\\Users\\zmana\\Desktop\\BEStuff\\im1.png")      
canvas.create_image(0,0, anchor=NW, image=img)












b2 = Button(root,text="Colour It",font=("Comic Sans MS",14),activebackground='sky blue',padx=10,pady=10,relief=SUNKEN,justify=CENTER,background="#ccdde3",command=colorit)
b2.place(x=600,y=600,height=60,width=200)


b3=Button(root,text="+",font=("Comic Sans MS",26),activebackground='sky blue',padx=10,pady=10,relief=SUNKEN,justify=CENTER,height=200,command=browseFiles)
b3.place(x=200,y=50,width=512,height=512)

im2  = PhotoImage(file="C:\\Users\\zmana\\Desktop\\BEStuff\\img2.png")
#b4=Button(root,text="",font=("Comic Sans MS",9),activebackground='sky blue',padx=10,pady=10,background="White", relief=SUNKEN,justify=CENTER,height=200)
#b4.place(x=700,y=50,width=512,height=512)


canvas2 = Canvas(root, width = 512, height = 512,background="White")      
canvas2.place(x=700,y=50)
    
canvas2.create_image(0,0, anchor=NW, image=im2)



root.mainloop()

