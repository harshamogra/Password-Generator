from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("Password generator")
pass_head=Label(root, text= "PASSWORD LENGTH",font= 'arial 12 bold',fg='red').pack(pady=10)
pass_len= IntVar()
length= Spinbox(root, from_=6, to_=32, textvariable= pass_len, width=24, font='arial 16').pack()
output_pass= StringVar()
alphaup=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphalow=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=['0','1','2','3','4','5','6','7','8','9']
spch= ['!','@','#','$','%','^','&','*']
import random
def randpass():
    password=""
    
    for y in range(pass_len.get()):
        
     chartype= random.choice(alphaup)+ random.choice(alphalow) + random.choice(num) + random.choice(spch)
     password= password + random.choice(chartype)
     output_pass.set(password)
     
    
    
btn= Button(root, text="Generate Password", command=randpass, font='arial 10',padx=5, pady=5).pack(pady=20)
pass_gen= Label(root, text="RANDOM GENERATED PASSWORD",font='arial 12 bold',fg='red').pack(pady=10)
Entry(root, textvariable=output_pass, width=24,font='arial 16').pack()
root.mainloop()
