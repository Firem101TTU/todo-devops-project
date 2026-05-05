import os
from todo import add_task, load_tasks, mark_task_complete, delete_task


TEST_FILE = "test_tasks.json"


def cleanup():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_add_task():
    cleanup()

    task = add_task("Study for DevOps final", TEST_FILE)

    assert task["description"] == "Study for DevOps final"
    assert task["completed"] is False

    tasks = load_tasks(TEST_FILE)
    assert len(tasks) == 1

    cleanup()


def test_mark_task_complete():
    cleanup()

    add_task("Finish Dockerfile", TEST_FILE)
    result = mark_task_complete(1, TEST_FILE)

    tasks = load_tasks(TEST_FILE)

    assert result is True
    assert tasks[0]["completed"] is True

    cleanup()


def test_delete_task():
    cleanup()

    add_task("Task one", TEST_FILE)
    add_task("Task two", TEST_FILE)

    result = delete_task(1, TEST_FILE)
    tasks = load_tasks(TEST_FILE)

    assert result is True
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Task two"
    assert tasks[0]["id"] == 1

    cleanup()


def test_delete_missing_task():
    cleanup()

    add_task("Only task", TEST_FILE)
    result = delete_task(99, TEST_FILE)

    tasks = load_tasks(TEST_FILE)

    assert result is False
    assert len(tasks) == 1

    cleanup()
