from s2b_task import task, execute_task
from s2b_task.task_executor import TaskNotExists
from s2b_task.storage import TASK_MAP


def test_task_registration():
    assert not TASK_MAP

    @task
    def foo():
        print("foo")

    @task
    def bar():
        print("bar")

    assert TASK_MAP

    for task_name in ("foo", "bar"):
        execute_task(task_name)

    try:
        execute_task(("_", "invalid"))
        assert False, "Non existing task found"
    except TaskNotExists:
        ...
