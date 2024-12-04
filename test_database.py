import asyncio
from database import async_add_task, async_list_tasks, async_complete_task, async_delete_task

async def test_async_operations():
    """Tests the asynchronous CRUD operations."""
    # Add task
    print("Testing task addition...")
    await async_add_task("Test async task")
    tasks = await async_list_tasks()
    assert len(tasks) > 0, "Task addition failed!"
    print("Task added successfully.")

    # Complete task
    task_id = tasks[0][0]  # Assuming first task
    print(f"Testing task completion for task ID {task_id}...")
    await async_complete_task(task_id)
    tasks = await async_list_tasks(show_all=True)
    assert tasks[0][2] == 1, "Task completion failed!"  # Check 'completed' column
    print("Task marked as completed successfully.")

    # Delete task
    print(f"Testing task deletion for task ID {task_id}...")
    await async_delete_task(task_id)
    tasks = await async_list_tasks(show_all=True)
    assert len(tasks) == 0, "Task deletion failed!"
    print("Task deleted successfully.")

# Run tests
if __name__ == "__main__":
    asyncio.run(test_async_operations())
    print("All async tests passed!")
