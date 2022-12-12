import argparse as ap
from .storage import TASK_MAP


def log_task_list():
    for name, callback in TASK_MAP.items():
        print(f"{name}\t{callback.__doc__}")


class GetTaskListAction(ap.Action):
    def __init__(self, option_strings, dest, **kwargs):
        return super().__init__(
            option_strings,
            dest,
            nargs=0,
            default=ap.SUPPRESS,
            **kwargs,
        )

    def __call__(self, parser, namespace, values, option_string, **kwargs):
        # Do whatever should be done here
        log_task_list()
        parser.exit()
