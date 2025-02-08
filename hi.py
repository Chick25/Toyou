import tkinter as tk
from PIL import Image, ImageTk, ImageSequence 

parent = tk.Tk()
'''
frame_gifs = tk.Frame(parent, bg="#FFE4C4")
frame_gifs.pack(side="top", fill="x", pady=10)
'''
#gif meme1
gif = Image.open("uwu-meong.gif")
frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]
gif_label = tk.Label(parent, bg="#FFE4C4")
gif_label.place(x=10, y=10)
#gif meme2
gif1 = Image.open("cute-cat.gif")
frames1 = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif1)]
gif_label1 = tk.Label(parent, bg="#FFE4C4")
gif_label1.place(relx=1, rely=1, anchor="se")



def up_gif(ind=0):
    frame = frames[ind]
    gif_label.configure(image=frame)
    parent.after(100, up_gif, (ind + 1) % len(frames))

def up_gif1(ind=0):
    frame = frames1[ind]
    gif_label1.configure(image=frame)
    parent.after(100, up_gif1, (ind + 1) % len(frames1))

up_gif()
up_gif1()
#parent = tk.Tk()
'''
width= hi.winfo_screenwidth() 
height= hi.winfo_screenheight()
parent.geometry("%dx%d" % (width, height))
#parent.geometry("full")
'''
parent.attributes('-fullscreen', True)

def exit_fullscreen(event):
    parent.attributes('-fullscreen', False)

parent.bind("<Escape>", exit_fullscreen)

parent.title("To you")
parent.iconbitmap("4096575-heart-like-love_113760 (1).ico")
parent.configure(bg='#FFE4C4')

frame_content = tk.Frame(parent, bg="#FFE4C4")
frame_content.place(relx=0.5, rely=0.5, anchor="center") 


lan_bam=0

def thay_doi_label():
    
    global lan_bam
    lan_bam +=1
    if lan_bam ==1:
        l.config(text="Nice to meet you!! 😳 ", fg="black", bg="#FFE4C4",font=("Arial", 50))
    elif lan_bam==2:
        l.config(text="I want to say something ", fg="black", bg="#FFE4C4",font=("Arial", 50))
    elif lan_bam ==3:
        l.config(text="Can you...", fg="black",bg="#FFE4C4" ,font=("Arial", 50))
    else:
        l.config(text="date with me !???  👉👈 ", fg="black",bg="#FFE4C4" ,font=("Arial", 50))

l = tk.Label(frame_content, text = "Hello there! 👋 ", fg="black",bg="#FFE4C4",font = ("Arial", 50))
l.pack(pady=25)



button = tk.Button(frame_content, text = "Next", bg = "#FFB6C1", fg = "black",font=("Arial", 20) , command=thay_doi_label)
button.pack(pady=50)
#buttonko = Button(parent, text = "Sorry", bg = "#FFB6C1", fg = "black").grid(row=1, column=1)
#button.pack(side = BOTTOM)
#buttonko.pack(side = TOP)

parent.mainloop()