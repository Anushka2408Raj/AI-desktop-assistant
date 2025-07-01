from tkinter import*
from PIL import Image,ImageTk
import os
import action
import speech_to_text

def User_send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, "Me --> "+send+"\n")
    if bot != None:
        text.insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok sir":
          root.destroy()  
          

def ask():

    ask_val= speech_to_text.speech_to_text()
    bot_val = action.Action(ask_val)
    text.insert(END, "Me --> "+ask_val+"\n") 
    if bot_val != None:
       text.insert(END, "Bot <-- "+ str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()

def delete_text():
    text.delete("1.0", "end")

root=Tk()
root.title("LUCA-The AI Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="#6BB5D7")

#creating a frame

frame= LabelFrame(root,padx=100,pady=7,borderwidth=3,relief="raised")
frame.grid(row=0,column=1,padx=70,pady=10)
frame.config(bg="#E25E8C")

#text label

text_label= Label(frame,text="LUCA",font=("Times New Roman",14,"bold"),bg="#E25E8C")
text_label.grid(row=0,column=0,padx=20,pady=10)

image_path = os.path.join("image", "robo.png")  # Make sure the image is in "images" folder

# Load image
image = Image.open(image_path)

# Optional: Resize image
image = image.resize((200, 200))  # Resize as per your layout

# Convert to Tkinter-compatible image
photo = ImageTk.PhotoImage(image)

# Display image in a Label
image_label = Label(frame, image=photo, bg="#6BB5D7")
image_label.image = photo  # Keep a reference
image_label.grid(row=1, column=0, pady=20)

#adding a text

text=Text(root,font=("courier 10 bold"),bg="#D6AD30")
text.grid(row=2,column=0)
text.place(x=87,y=375,width=375,height=100)

#adding entry widget
entry=Entry(root,justify=CENTER)
entry.place(x=100,y=500,width=350,height=30)

#adding buttons

Button1= Button(root,text="ASK",bg="#8756DD",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
Button1.place(x=70,y=575)

Button2= Button(root,text="DELETE",bg="#8756DD",pady=16,padx=40,borderwidth=3,relief=SOLID,command=delete_text)
Button2.place(x=210,y=575)

Button3= Button(root,text="SEND",bg="#8756DD",pady=16,padx=40,borderwidth=3,relief=SOLID,command=User_send)
Button3.place(x=360,y=575)
root.mainloop()