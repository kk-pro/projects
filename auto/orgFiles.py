from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import time

class MyHandler(FileSystemEventHandler):
    
    def on_modified(self, event):
        if not os.path.exists(image):
            os.makedirs(image)
        if not os.path.exists(video):
            os.makedirs(video)
        if not os.path.exists(documents):
            os.makedirs(documents)
        if not os.path.exists(compress):
            os.makedirs(compress)
        for filename in os.listdir(folder_to_track):
            
            src = folder_to_track + "/" + filename

            if filename.endswith(tuple(pic_ext)):
                image_dst = image + '/' + filename
                os.rename(src, image_dst)
            if filename.endswith(tuple(vid_ext)):
                vid_dst = video + "/" + filename
                os.rename(src, vid_dst)
            if filename.endswith(tuple(doc_ext)):
                doc_dst = documents + '/' + filename
                os.rename(src, doc_dst)
            if filename.endswith(tuple(com_ext)):
                com_dst = compress + "/" + filename
                os.rename(src, com_dst)

folder_to_track = '/Users/kkhh/Documents/orgtest'
# folders
image = folder_to_track+'/images'
documents= folder_to_track+'/documents'
video= folder_to_track + '/video'
compress = folder_to_track + '/compress'

#extentions
vid_ext = [".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv",".m2ts", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg",".rm", ".swf", ".vob", ".wmv"]
pic_ext =['.png', 'jpg', 'jpeg', 'gif']
doc_ext = ['.doc','.docx','.odt','.pdf','.rtf','.tex','.txt','.wpd','xls','xlsm','xlsx','pptx','ppt','pps']
com_ext = ['.7z','.arj','.deb','.pkg','.rar','.rpm','.tar.gz','.z','.zip']



event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()