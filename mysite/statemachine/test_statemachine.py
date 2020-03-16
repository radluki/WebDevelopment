from .statemachine import *
import pytest


def check_event(machine, event, target_state):
    machine.handle_event(event)
    assert machine.state.__class__ == target_state


def test_state_machine():
    initial_state = StateTwo()
    sm = StateMachine(initial_state)

    event = 10
    check_event(sm, event, State)
    event = "string"
    check_event(sm, event, State)
    event = 11
    check_event(sm, event, StateTwo)
    check_event(sm, event, State)
    event = DummyClass()
    check_event(sm, event, State)
    assert sm.state._priv.dummy.__class__ == DummyClass
