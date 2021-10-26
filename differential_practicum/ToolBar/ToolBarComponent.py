from abc import abstractmethod


class ToolBarComponent:
    @abstractmethod
    def get_object(self):
        pass
