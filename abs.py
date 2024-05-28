from abc import ABC, abstractmethod


class Bus(ABC):
    @abstractmethod
    def start(self):
        return 'Bus is started'

    @abstractmethod
    def stop(self):
        return 'Bus is stopped'

    @abstractmethod
    def tape_recorder(self):
        return 'The tape is recorder is running'

    def get_info(self):
        print("Get info")


class Transport(Bus):
    def start(self):
        return "Transport is started"

    def stop(self):
        return "Transport is stopped"

    def tape_recorder(self):
        return "The tape is recorder is running"


transport = Transport()
print(transport.start())
print(transport.stop())
print(transport.tape_recorder())



