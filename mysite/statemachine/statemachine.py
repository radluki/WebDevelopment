

class PrivateMemory:

    def __str__(self):
        return f"PrivateMemory {self.__dict__}"


class StateMachine:

    def __init__(self, init_state, alowable_transitions=None):
        self.state = init_state
        self.set_new_state(init_state.__class__)
        self.alowable_transitions = alowable_transitions

    def handle_event(self, event):
        new_state = self.state.handle_event(event)
        if self.alowable_transitions and \
                new_state not in self.alowable_transitions[self.state.__class__]:
            raise Exception(
                f"Disalowed transition from {self.state} to {new_state}")
        if new_state != self.state.__class__:
            self.set_new_state(new_state)

    def set_new_state(self, state):
        self.state.__class__ = state
        state._priv = PrivateMemory()
