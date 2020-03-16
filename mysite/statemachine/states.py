from functools import singledispatchmethod


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

    @handle_event.register
    def _(self, event: bool):
        return DisallowedState


class StateTwo:

    def handle_event(self, event):
        return State


class DisallowedState:

    def handle_event(self, event):
        return State


alowable_transitions = {State:           {State, StateTwo},
                        StateTwo:        {State},
                        DisallowedState: {State}}
