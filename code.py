from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from email.message import EmailMessage
import smtplib
import webbrowser
import logging

logging.basicConfig(filename='logsfile.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
logger=logging.getLogger()
def sendemail():
    try:
        
        sender = account.get()
        recepient = [receiver.get()]
        sub = subject_entry.get('1.0','end')
        print(sub)
        pswrd = password.get()
        msg = msgbody.get('1.0','end')
        
        msgtosend = "Subject: %s \n\n %s" %(sub,msg)
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.starttls()
        mail.login(sender, pswrd)
        mail.sendmail(sender, recepient, msgtosend)
        mail.close()
        
        ttk.Label(mainframe, text="Email sent successfully").grid(column=4,row=14,sticky=W)
        logger.info("Email sent successfully")
    except Exception as e:
        ttk.Label(mainframe, text=str(e)).grid(column=0,row=14,sticky=W)

def setup(event):
    webbrowser.open_new(r"https://www.google.com/settings/security/lesssecureapps")
    
        
root = Tk()
root.title("Send an Email via Gmail")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

account = StringVar()
password = StringVar()
receiver = StringVar()
subject = StringVar()
msgbody = StringVar()
bit = IntVar()
byte = IntVar()
logs = StringVar()


a = Label(mainframe, text="To use this app turn this setting ON for your account", fg="blue", cursor="hand2")
a.grid(columnspan=2,column=3, row=0, sticky=W)
a.bind("<Button-1>", setup)


ttk.Label(mainframe, text="Your Email Account: ").grid(column=0, row=1, sticky=W)
account_entry = ttk.Entry(mainframe, width=30, textvariable=account)
account_entry.grid(column=4, row=1, sticky=(W, E))



ttk.Label(mainframe, text="Your Password: ").grid(column=0, row=2, sticky=W)
password_entry = ttk.Entry(mainframe, show="*", width=30, textvariable=password)
password_entry.grid(column=4, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Recepient's Email Account: ").grid(column=0, row=3, sticky=W)
receiver_entry = ttk.Entry(mainframe, width=30, textvariable=receiver)
receiver_entry.grid(column=4, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Let's Compose:").grid(column=4, row=5, sticky=W)

ttk.Label(mainframe, text="header: ").grid(column=0, row=6, sticky=W)
subject_entry = Text(mainframe, width=30, height=1)
subject_entry.grid(column=4, row=6, sticky=(W, E))

ttk.Label(mainframe, text="Message Body: ").grid(column=0, row=7, sticky=W)
msgbody = Text(mainframe, width=30, height=10)
msgbody.grid(column=4, row=7, sticky=(W, E))



def retrieve_input():
    inputValue=msgbody.get("1.0","end-1c")
    #print(inputValue)
    convert(inputValue)
    show_binary(inputValue)
    
def convert(inputValue):
    tstr=str(inputValue)
    logging.info(' '.join(format(ord(x), 'b') for x in tstr))
    logger.info("converted to binary successfully")



    return ' '.join(format(ord(x), 'b') for x in tstr)

def show_binary(inputValue):
    Ans = convert(msgbody.get("1.0","end-1c"))
    bit_entry.delete(1.0,'end')
    bit_entry.insert(1.0, Ans)
    

def utflen(inputValue):
    c=len(inputValue.encode('utf-8'))
    #print(c)
    data_entry.delete(0,'end')
    data_entry.insert(0,c)
    

def just():
    inputValue=msgbody.get("1.0","end-1c")
    inputVal=subject_entry.get("1.0","end-1c")
    utflen(inputValue)
    utf(inputVal)
    logger.info("output in bytes")

    
def retrieve():
    inputVal=subject_entry.get("1.0","end-1c")
def utf(inputVal):
    d=len(inputVal.encode('utf-8'))
    #print(d)
    header_entry.delete(0,'end')
    header_entry.insert(0,d)
    
def delete():
    bit_entry.delete(0, 'end')
    



   




    
    
    
    


ttk.Label(mainframe, text="Total bytes in header part:").grid(column=0, row=8, sticky=W)
header_entry = ttk.Entry(mainframe, width=30)
header_entry.grid(column=4, row=8, sticky=(W, E))





ttk.Label(mainframe, text="Total bytes in data part:").grid(column=0, row=9, sticky=W)
data_entry = ttk.Entry(mainframe, width=30)
data_entry.grid(column=4, row=9, sticky=(W, E))

ttk.Label(mainframe, text="email in terms of binary bits:").grid(column=0, row=10, sticky=W)


scrolW = 30 
scrolH = 3 # 5
bit_entry = scrolledtext.ScrolledText(mainframe, width=scrolW, height=scrolH) # 6
bit_entry.grid(column=4, row=10, columnspan=3) # 7


ttk.Button(mainframe, text="Send Email", command=sendemail).grid(column=4,row=12,sticky=E)
ttk.Button(mainframe, text="show binary", command=retrieve_input).grid(column=4,row=14,sticky=E)
ttk.Button(mainframe, text="show bytes", command=just).grid(column=4,row=13,sticky=E)






for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

account_entry.focus()

root.mainloop()

