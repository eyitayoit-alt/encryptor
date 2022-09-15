"""
Graphicsl is a subclass of ttk.Frame. Args are mode and master which default to none. Properties are filename,status,pswd are StingVar() which holds the filename,status and passwords. Method selectcom no arg set the filename to the filepath of the file for encryption or decryption. It is binded to the command option of instance of ttk.Button. 
Method actioncom no argument, open(filename,"rb") and pass it to encrypt or decrypt function in the Utils module. If file was succesfully encrypted or decrypted status is set to succesfull or to the exception or error that occurred


'"""
from tkinter import filedialog,messagebox,ttk
from tkinter import*
from fileselector import FileSelector
from Utils import*
import os
import shelve
import logging
import pickle
import threading
import time
logging.basicConfig(filename="log.txt",format='%(message)s-%(levelname)s-%(filename)s-%(lineno)d-%(asctime)s')



class Uix(ttk.Frame):
		
		def __init__(self,mode,master=None):
			ttk.Frame.__init__(self,master)
			self.place(relx=0.05,rely=0.2,relheight=0.6,relwidth=0.9)
			self.__filename=StringVar()
			self.status=StringVar()
			self.__pswd=StringVar()
			self.__mode=mode
			
			self.result=Message(self,		textvariable=self.status)
			
			self.resultP=self.result.place(relx=0.3,rely=0.2,relwidth=0.4)
			
			self.selecbutton=ttk.Button(self,text="Select File",command=self.selectcom,style="W.TButton")
			
			self.selecbutton.place(relx=0.01,rely=0.45,relwidth=0.3)
			
			self.entry=ttk.Entry(self,textvariable=self.__filename,width=30)
			self.entry.place(relx=0.3,rely=0.45,relwidth=0.7)
			
			self.msg=Message(self,text=" Encryption Password")
			self.msg.place(relx=0.01,rely=0.6,relwidth=0.25)
			
			self.pwd=ttk.Entry(self,textvariable=self.__pswd,width=30)
			self.pwd.place(relx=0.3,rely=0.6,relwidth=0.7)
			
			self.actionbutton=ttk.Button(self,text=self.__mode, command=self.actioncom,style="W.TButton")
			
			self.actionbutton.place(relx=0.3,rely=0.75)
			
		def selectcom(self):
			title=None
			if self.__mode=="Encrypt":
				title="Open File To Encrypt"
			else:
				title="Open File to Decrypt"
			filename2=FileSelector.filePath(title=title)
			if filename2:
				self.__filename.set(filename2)
			
		
		def actioncom(self):
			self.status.set("Processing...,Please Wait")
			time.sleep(3)
			self.displayMsg()
			filepath=self.__filename.get()
			pwd1=self.__pswd.get()
			if not filepath:
				self.status.set("No file selected")
				self.displayMsg()		
			elif len(pwd1)<16:
				self.status.set("Password less than 16 character")
				self.displayMsg()
			elif os.path.isfile(filepath):
				if self.__mode=="Encrypt":
					self.status.set("Encrypting...,please wait")
					self.displayMsg()
					time.sleep(5)
					try:
						file=open(filepath,"rb")
					except Exception as exc:
						self.status.set(exc)
						self.displayMsg()
					else:
						dfile=file.read()
						endata=encrypt(dfile,filepath,pwd1)
						nfpath=os.path.basename(filepath).split(".")
						dname=os.path.dirname(filepath)
						outfile=open(dname+"/"+nfpath[0]+"encrypted.dat","wb")
						pickle.dump(endata,outfile)
						outfile.close
						self.status.set("sucessfully Encrypted")
						self.displayMsg()
				elif self.__mode=="Decrypt":
					self.status.set("Decrypting... please wait")
					self.displayMsg()
					time.sleep(5)
					infile=open(filepath,"rb")
					filedata=pickle.load(infile)
					pwd2= pwd=hashlib.sha224(bytes(pwd1,"utf-8")).hexdigest()
					pwd3=filedata["pwd"]
					if pwd2==pwd3:
						decryp =decrypt(filedata)
						filedata2,ftype=decryp
						fname=os.path.basename(filepath).split(".")
						fname2 = fname[0]+"."+ftype
						dname=os.path.dirname(filepath)
						
						try:
							file=open(dname+"/"+fname2,"wb")
						except Exception as exc:
							self.status.set(exc)
							self.displayMsg()
						else:
							dfile=file.write(bytes(filedata2))
							file.close()
							self.status.set( "Succesfull decrypted")
							self.displayMsg()
					else:
							self.status.set("Invalid Password")
							self.displayMsg()
							
				
			
			
		def displayMsg(self):
			return self.resultP

			
			

				
				
				

				
		
	
							
		
			



	


		
