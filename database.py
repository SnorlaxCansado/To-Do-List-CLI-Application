import aiosqlite
import datetime
import pandas as pd

# Asynchronous CRUD Operations

async def async_add_task(description):
    """Adds a new task asynchronously to the database."""
    async with aiosqlite.connect('tasks.db') as db:
        await db.execute(
            "INSERT INTO tasks (description, completed, created_at) VALUES (?, ?, ?)",
            (description, False, datetime.datetime.utcnow())
        )
        await db.commit()

async def async_list_tasks(show_all=False):
    """Lists tasks asynchronously from the database."""
    query = "SELECT * FROM tasks" if show_all else "SELECT * FROM tasks WHERE completed = 0"
    async with aiosqlite.connect('tasks.db') as db:
        async with db.execute(query) as cursor:
            tasks = await cursor.fetchall()
            return tasks

async def async_complete_task(task_id):
    """Marks a task as completed asynchronously."""
    async with aiosqlite.connect('tasks.db') as db:
        await db.execute(
            "UPDATE tasks SET completed = 1 WHERE id = ?",
            (task_id,)
        )
        await db.commit()

async def async_delete_task(task_id):
    """Deletes a task asynchronously."""
    async with aiosqlite.connect('tasks.db') as db:
        await db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        await db.commit()

async def async_export_tasks_to_csv(filename):
    """Exports tasks to a CSV file asynchronously."""
    query = "SELECT id, description, completed, created_at FROM tasks"
    async with aiosqlite.connect('tasks.db') as db:
        async with db.execute(query) as cursor:
            rows = await cursor.fetchall()
            # Convert rows to a list of dictionaries
            task_list = [
                {
                    'ID': row[0],
                    'Description': row[1],
                    'Completed': row[2],
                    'Created At': row[3]
                }
                for row in rows
            ]
            df = pd.DataFrame(task_list)
            df.to_csv(filename, index=False)