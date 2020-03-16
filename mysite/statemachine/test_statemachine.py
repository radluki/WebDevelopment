from .statemachine import *
import pytest


def test_dummy():
    assert "dummy" == dummy()


def assert_state(machine, state):
    assert machine.state.__class__ == state


def test_state_machine():
    initial_state = StateTwo()
    sm = StateMachine(initial_state)
    assert_state(sm, StateTwo)
    sm.handle_event(2)
    assert_state(sm, State)
    sm.handle_event("ssss")
    assert_state(sm, State)
    sm.handle_event(44)
    assert_state(sm, StateTwo)
    sm.handle_event(44)
    assert_state(sm, State)
    sm.handle_event(DummyClass())
    assert sm.state._priv.c == 1
