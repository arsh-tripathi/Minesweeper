import time
import tkinter as tk

screen = tk.Tk()
flag_img = tk.PhotoImage(file="./images/flag.png")
button = tk.Button(width= 15, height= 20, bg="black")
def resize():
    button.configure(image=flag_img)
def remove():
    button.configure(image='')
button2 = tk.Button(text="add image",command=resize)
button3 = tk.Button(text="add image",command=remove)
button.pack()
button2.pack()
button3.pack()
screen.mainloop()
# # define the countdown func.
# def countdown(t):
    
#     while t:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end="\r")
#         time.sleep(1)
#         t -= 1
      
#     print('Fire in the hole!!')
  
  
# # input time in seconds
# t = input("Enter the time in seconds: ")
  
# # function call
# countdown(int(t))