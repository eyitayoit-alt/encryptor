"""
A module create gui for file encryption and fecryption. It built on Tkinter package. function showEncrypt() no argument and return statement. It create gui for file encryption, binded to tk.Radiobutton command option. The function creates an instance of Graphicsl a subclass of tk.Frame widgets function showDecrypt()
create gui for file decryption, binded to tk.Radiobutton command option
creates an instance of Graphicsl a subclass of tk.Frame widgets
"""

import os
import Utils
from tkinter import*
from tkinter import filedialog,messagebox,ttk
import Utils,uix,fileselector

window= Tk()
exc=StringVar()
msg=Message(window,textvariable=exc)
try:
	modevar=StringVar()
	
	def showEncrypt():
		try:
			encryptor=uix.Uix("Encrypt",master=window)
		except Exception as Exc:
			exc.set(Exc)
			msg.place(relx=0.5,rely=0.5)
		
		
	def showDecrypt():
		try:
			encryptor=uix.Uix("Decrypt",master=window)
		except Exception as Exc:
			exc.set(Exc)
			msg.place(relx=0.5,rely=0.5)
		
		
	modeRadio=ttk.Radiobutton(window,text="Encrypt",variable=modevar,value="Encrypt",command=showEncrypt)
	modeRadio.place(relx=0.3,rely=0.1)
	modeRadio.invoke()
	
	
	modeRadio2=ttk.Radiobutton(window,text="Decrypt",variable=modevar,value="Decrypt",command=showDecrypt)
	modeRadio2.place(relx=0.6,rely=0.1)
except Exception as Exc:
	exc.set(Exc)
	msg.place(relx=0.5,rely=0.5)
	
window.configure(background="green")
window.mainloop()
