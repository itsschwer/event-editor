from enum import IntEnum
import json
from pathlib import Path
import typing

_actor_json_path: typing.Optional[Path] = None
def set_actor_json_path(p: typing.Optional[str]) -> None:
    if p:
        global _actor_json_path
        _actor_json_path = Path(p)

class EventType(IntEnum):
    Action = 0
    Query = 1

def load_actor_json(actor_name: str) -> dict:
    if not _actor_json_path:
        return False

    try:
        # Try loading from a single file with all actors first
        # before looking for individual actor files?
        with open(_actor_json_path/f'{actor_name}.json', 'rt') as stream:
            return json.loads(stream.read())
    except:
        return None

def load_event_parameters(actor_name: str, event_name: str, event_type: EventType) -> typing.Dict[str, typing.Any]:
    try:
        actor = load_actor_json(actor_name)

        if event_type == EventType.Action:
            return actor["actions"][event_name]
        if event_type == EventType.Query:
            return actor["queries"][event_name]
        return None
    except:
        return None
