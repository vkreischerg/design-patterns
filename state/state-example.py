# State Pattern - Allows an object to behave differently when its state changes

# Participants: Context, State, ConcreteStateA, ConcreteStateB, ...

# Example: Drawing application with different tools


from abc import ABCMeta, abstractmethod

class Canvas():
    # Context
    def __init__(self):
        self._current_tool = None

    def mouse_down(self):
        self._current_tool.mouse_down()

    def mouse_up(self):
        self._current_tool.mouse_up()

    def get_current_tool(self):
        return self._current_tool

    def set_current_tool(self, tool):
        self._current_tool = tool


class Tool(metaclass=ABCMeta):
    # State
    @abstractmethod
    def mouse_up(self):
        pass

    @abstractmethod
    def mouse_down(self):
        pass


class Selection(Tool):
    # ConcreteStateA
    def mouse_down(self):
        print('Selection icon')

    def mouse_up(self):
        print('Draw a dashed rectangle')


class Brush(Tool):
    # ConcreteStateB
    def mouse_down(self):
        print('Brush icon')

    def mouse_up(self):
        print('Draw a line')


if __name__ == '__main__':

    canvas = Canvas()

    canvas.set_current_tool(Selection())
    canvas.mouse_down()
    canvas.mouse_up()

    canvas.set_current_tool(Brush())
    canvas.mouse_down()
    canvas.mouse_up()
