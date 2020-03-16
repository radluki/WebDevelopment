from functools import singledispatchmethod


class PrivateMemory:

    def __str__(self):
        return f"PrivateMemory {self.__dict__}"


class DummyClass:
    pass


class State:

    @singledispatchmethod
    def handle_event(self, event):
        self._priv.default = event
        return StateTwo

    @handle_event.register
    def _(self, event: str):
        self._priv.string = event
        return self.__class__

    @handle_event.register
    def _(self, event: DummyClass):
        self._priv.dummy = event
        return self.__class__


class StateTwo:

    def handle_event(self, event):
        return State


class StateMachine:

    def __init__(self, init_state):
        self.state = init_state
        self.set_new_state(init_state.__class__)

    def handle_event(self, event):
        new_state = self.state.handle_event(event)
        if new_state != self.state.__class__:
            self.set_new_state(new_state)

    def set_new_state(self, state):
        self.state.__class__ = state
        state._priv = PrivateMemory()
