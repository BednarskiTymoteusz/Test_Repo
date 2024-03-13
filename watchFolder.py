# import time module, Observer, FileSystemEventHandler
import global_variables
import os
import inputSelector
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class OnMyWatch:
    # Set the directory on watch
    watchDirectory = global_variables.folderPathInbound

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

    def stop(self):
        self.observer.stop()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Event is created, you can process it now
            inputSelector.InputSelector(event.src_path)
            print("Watchdog received created event - % s." % event.src_path)
        # elif event.event_type == 'modified':
        #     # Event is modified, you can process it now
        #     print("Watchdog received modified event - % s." % event.src_path)


def runBefore():
    watchDirectory = global_variables.folderPathInbound
    files = os.listdir(watchDirectory)
    for f in files:
        inputSelector.InputSelector(watchDirectory + "/" + f)

if __name__ == '__main__':

    #run before event (if some file in input folder)
    runBefore()

    # run based on event
    watch = OnMyWatch()
    watch.run()
