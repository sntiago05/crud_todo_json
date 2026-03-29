from typing import TypedDict, NotRequired


class TodoTask(TypedDict):
    id: int
    title: str
    content: str
    completed: bool


class TodoTaskInput(TypedDict):
    title: str
    content: str


class TodoTaskUpdate(TypedDict):
    title: NotRequired[str]
    content: NotRequired[str]
    completed: NotRequired[bool]
