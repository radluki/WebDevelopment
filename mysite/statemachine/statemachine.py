from functools import singledispatchmethod


def dummy():
    return "dummy"


class PrivateMemory:

    def __str__(self):
        return f"PrivateMemory {self.__dict__}"


class DummyClass:
    pass


class State:

    @singledispatchmethod
    def handle_event(self, event):
        self._priv.a = 44
        priv = self._priv
        state = self.__class__
        print(f"Event {state} {priv} {event}")
        return StateTwo

    @handle_event.register
    def _(self, event: str):
        self._priv.b = 44
        print(f"String event {event}")
        return self.__class__

    @handle_event.register
    def _(self, event: DummyClass):
        print("DummyEvent")
        self._priv.c = 1
        return self.__class__


class StateTwo:

    def handle_event(self, event):
        priv = self._priv
        state = self.__class__
        print(f"Event {state} {priv} {event}")
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
