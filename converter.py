#@Authir Justinross5 12/7/2021

from tkinter.constants import ANCHOR, BOTTOM, CENTER, LEFT, TOP
import tkinter as tk
from tkinter import ttk
import getpass
from moviepy.editor import *
import logging, os
from pytube import YouTube
from PIL import ImageTk, Image

def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s : %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler) 

def convert():
    bar()
    url = str(urlresult.get())
    log1.info(f'URL Entered: {url}')
    
    try:
        yt = YouTube(url)
    except:
        print('error')
        log1.error('Error getting video from youtube')
    print(f'yt object created {yt}')
    stream = yt.streams.first()
    output_path = f'C:/Users/{getpass.getuser()}/Downloads/'
    print(f'stream created {stream}')
    try:
        outfile = stream.download(output_path)
        print(outfile)
    except:
        log1.error(f'Error downloading video from youtube')

    videoclip = AudioFileClip(outfile)
    videoclip.write_audiofile(f'C:/Users/{getpass.getuser()}/Downloads/' + yt.title + '.mp3')
    videoclip.close()
    #deletes video 
    garbagevideo = f'C:/Users/{getpass.getuser()}/Downloads/{yt.title}'
    garbagevideo = garbagevideo.replace('.', '')
    garbagevideo = garbagevideo + '.3gpp'
    os.remove(garbagevideo)

# Function responsible for the updation
# of the progress bar value
def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(0.1)
  
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(0.1)
  
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(0.1)
  
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(0.1)
  
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(0.1)
    progress['value'] = 100

if __name__ == "__main__":
    open("ConverterLog.txt", "w")
    setup_logger("ConverterLog.txt", r"ConverterLog.txt")
    log1 = logging.getLogger("ConverterLog")
    root = tk.Tk()
    
    root.geometry('{0}x{1}+0+0'.format(int(root.winfo_screenwidth()/1.5), int(root.winfo_screenheight()/1.8)))
    root.rowconfigure(10, minsize=100)
    root.columnconfigure(10, minsize=100)
    titleimg = Image.open("Title.png")
    labelimg = Image.open('pasteurl.png')
    background = Image.open("mainbackground.jpg")
    background = background.resize((int(root.winfo_screenwidth()/1.5), int(root.winfo_screenheight()/1.5)))
    background.paste(titleimg, (230, 50), titleimg)
    background.paste(labelimg, (330, 100), labelimg)
    background.save('NewImg.png',"PNG")

    NewImg = Image.open('NewImg.png')

    # Use Image
    tkimage = ImageTk.PhotoImage(NewImg, master=root)
    
    title = tk.Label(root, image=tkimage, bg='black')
    title.place(x=0, y=0, relheight=1, relwidth=1)

    s = ttk.Style()
    s.theme_use('clam')
    s.configure("blue.Horizontal.TProgressbar", foreground='blue', background='black')
    progress = ttk.Progressbar(root, orient = 'horizontal',
    length = 300, mode = 'determinate', cursor='spider', style='blue.Horizontal.TProgressbar')
    progress.place(x=360, y=300)

    convertbutton = tk.Button(root, text='Convert', command=lambda: convert(), width=10, font=('Roboto', 18), bg='lightblue')
    convertbutton.place(x=430, y=200)

    urlresult = tk.Entry(root, width=100, borderwidth=2)
    urlresult.place(x=210, y=150)
    
    root.mainloop()

