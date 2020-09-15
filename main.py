from pytube import *
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *
from threading import *

file_size=0
main=Tk()
def progress(stream=None,chunk=None,file_handle=None,remaining=None):
    #gets the percentage of the file that has been downloaded:-
    file_downloaded=(file_size-int(remaining))
    percentage=file_downloaded/(file_size)*100
    DBtn.config(text=f"{percentage}% downloaded")

def start_download():
    global file_size
    try:
        url = urlField.get()
        #changing button text
        path_to_save = askdirectory()
        DBtn.config(text='please wait')
        DBtn.config(state=DISABLED)
        if path_to_save==None:
            return
        obb = YouTube(url,on_progress_callback=progress)
        strm1 = obb.streams.first()
        file_size=strm1.filesize
        print(file_size)
        strm1.download(path_to_save)
        print("""Done""")
        DBtn.config(text='Start Download')
        DBtn.config(state=NORMAL)

        showinfo(title='Downloaded', message='Download Successful')
    except Exception as e:
        print(f"[ERROR] is {e}")

def start_download_thread():
    thread=Thread(target=start_download)
    thread.start()

#creating the GUI


main.title("Ashish Downloader")
#issue main.iconbitmap('icon2.xbm')

photo=PhotoImage(file="icon3.png")
main.iconphoto(False, photo)
main.geometry('600x500')


#heading icon
headingIcon=Label(main,image=photo)
headingIcon.pack()

#url input
urlField=Entry(main,font=('TimesNewRoman',24),justify=CENTER)
urlField.pack(fill=X,padx=10)

#defining button
DBtn=Button(main,font=('Arial',30),text="Start Download",command=start_download_thread)
DBtn.pack(side=TOP,pady=10)
main.mainloop()