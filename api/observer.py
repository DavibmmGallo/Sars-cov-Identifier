import os 
from  abc import ABC, abstractmethod
from typing import List
import uuid
from watchdog.observers import Observer as fObserver
from watchdog.events import FileSystemEventHandler


class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass
    
    def detach(self, observer):
        pass
    
    @abstractmethod
    def notify(self) -> None:
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, subject:Subject) -> None:
        pass

class ConcreteObserverUploadFile(Observer):
    def update(self, subject:Subject) -> None:
        if subject._state == 101:
            print("Detectado envio de arquivo")
            
class MyHandler(FileSystemEventHandler):
    # def on_any_event(self, event):
    #     print(event.event_type, event.src_path)

    def on_created(self, event):
        pass
        #print("on_created", event.src_path)

    def on_deleted(self, event):
        print("on_deleted", event.src_path)

    def on_modified(self, event):
        file_name_with_extension = str(event.src_path).split('.')
        extension = file_name_with_extension[-1]
        nfilename = f'{uuid.uuid1()}.{extension}'
        os.rename(event.src_path,os.getcwd() + f"\\upload\\{nfilename}" )
        mainsub.run()


    def on_moved(self, event):
        pass
        #print("on_moved", event.src_path)

class ConcreteSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []      

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def run(self) -> None:
        self._state = 101
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()
        self._state = 0


if __name__ == '__main__':
    print('Observer Online.\n')
    mainsub = ConcreteSubject()
    observerf = ConcreteObserverUploadFile()
    mainsub.attach(observerf)

    event_handler = MyHandler()
    observer = fObserver()
    observer.schedule(event_handler, path=os.getcwd() + f"\\upload\\", recursive=False)
    observer.start()
    while True:
        pass
    
