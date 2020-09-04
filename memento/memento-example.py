# Memento Pattern - Used to implement undo mechanisms
# 3 participants: Originator, Memento and Caretaker

# Example: code editor that supports the undo mechanism


class Editor():
    # Originator
    def __init__(self):
        self.content = ""

    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content

    def create_state(self):
        return EditorState(self.content)

    def restore(self, state):
        self.content = state.get_content()


class EditorState():
    # Memento
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content


class History():
    # Caretaker
    def __init__(self):
        self.states = list()

    def push(self, state):
        self.states.append(state)

    def pop(self):
        return self.states.pop()


if __name__ == '__main__':

    editor = Editor()
    history = History()

    editor.set_content('a')
    history.push(editor.create_state())

    editor.set_content('b')
    history.push(editor.create_state())

    editor.set_content('c')
    editor.restore(history.pop())

    print(editor.get_content())

    editor.restore(history.pop())

    print(editor.get_content())
