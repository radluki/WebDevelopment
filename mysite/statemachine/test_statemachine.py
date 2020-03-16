from .statemachine import *
import pytest


def check_event(machine, event, target_state):
    machine.handle_event(event)
    assert machine.state.__class__ == target_state


@pytest.fixture
def machine_one():
    return StateMachine(State())


@pytest.fixture
def machine_two():
    return StateMachine(StateTwo())


def test_state_one_string(machine_one):
    event = "string"
    check_event(machine_one, event, State)
    assert machine_one.state._priv.string == event


def test_state_one_number(machine_one):
    event = 10
    check_event(machine_one, event, StateTwo)
    assert not machine_one.state._priv.__dict__


def test_state_one_dummy_class(machine_one):
    event = DummyClass()
    check_event(machine_one, event, State)
    assert machine_one.state._priv.dummy == event


def test_state_two_number(machine_two):
    event = 10
    check_event(machine_two, event, State)
    assert not machine_two.state._priv.__dict__
