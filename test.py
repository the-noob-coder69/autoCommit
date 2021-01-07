from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os import system,listdir
from os.path import split
from time import strftime,sleep
from config import folder_name,ignore
class customHandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if split(event.src_path)[1] not in ignore and event.key[0] == 'modified':
            f=open('lawlgz.logzz','a')
            system(f'cd \'{split(event.src_path)[0]}\'')
            system(f'git add \'{event.src_path}\'')
            system(f'git commit -m \"{event.key} {split(event.src_path)[1]} on {strftime("%I")}:{strftime("%M")}:{strftime("%S")} {strftime("%p")},{strftime("%A")}-{strftime("%m")}-{strftime("%Y")}\"')
            f.write(f'{split(event.src_path)[1]} is {event.key[0]} at {strftime("%I")}:{strftime("%M")}:{strftime("%S")} {strftime("%p")} on {strftime("%A")} {strftime("%d")} {strftime("%b")} {strftime("%Y")}\n')
            f.close

a=Observer()
for i in folder_name:
    a.schedule(customHandler(), i, recursive=True)
a.start()
input()
a.stop()
a.join()