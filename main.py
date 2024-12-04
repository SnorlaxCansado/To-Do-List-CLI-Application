import argparse
import asyncio
import pandas as pd
from database import (
    async_add_task,
    async_list_tasks,
    async_complete_task,
    async_delete_task,
    async_export_tasks_to_csv,
)
from logger import logger

async def handle_add_task(description):
    """Handles the add task command asynchronously."""
    await async_add_task(description)
    logger.info(f"Added task asynchronously: {description}")
    print("Task added.")

async def handle_list_tasks(show_all):
    """Handles the list tasks command asynchronously."""
    tasks = await async_list_tasks(show_all=show_all)
    logger.info("Listed tasks asynchronously")
    for task in tasks:
        status = '✓' if task[2] else '✗'  # Assuming the columns are [id, description, completed, created_at]
        print(f"{task[0]}: {task[1]} [{status}]")

async def handle_complete_task(task_id):
    """Handles the complete task command asynchronously."""
    await async_complete_task(task_id)
    logger.info(f"Completed task ID asynchronously: {task_id}")
    print(f"Task {task_id} marked as completed.")

async def handle_delete_task(task_id):
    """Handles the delete task command asynchronously."""
    await async_delete_task(task_id)
    logger.info(f"Deleted task ID asynchronously: {task_id}")
    print(f"Task {task_id} deleted.")

async def handle_export_tasks(filename):
    """Handles the export tasks command asynchronously."""
    await async_export_tasks_to_csv(filename)
    logger.info(f"Exported tasks to {filename}")
    print(f"Tasks exported to {filename}")

async def handle_task_statistics():
    """Handles the statistics command asynchronously."""
    # Fetch all tasks
    tasks = await async_list_tasks(show_all=True)
    # Create a DataFrame
    df = pd.DataFrame([{
        'Completed': task[2]  # Assuming 'completed' is at index 2
    } for task in tasks])
    # Calculate statistics
    stats = df['Completed'].value_counts().rename(index={0: 'Pending', 1: 'Completed'})
    print("Task Statistics:")
    print(stats)
    logger.info("Displayed task statistics")

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="To-Do List CLI Application (Async)")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', help='Description of the task')

    # List command
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('--all', action='store_true', help='Include completed tasks')

    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark a task as completed')
    complete_parser.add_argument('task_id', type=int, help='ID of the task to complete')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('task_id', type=int, help='ID of the task to delete')

    # Export command
    export_parser = subparsers.add_parser('export', help='Export tasks to CSV')
    export_parser.add_argument('filename', help='Filename for the exported CSV')

    # Stats command
    stats_parser = subparsers.add_parser('stats', help='Show task statistics')

    # Parse the arguments
    args = parser.parse_args()

    # Handle the commands asynchronously
    try:
        if args.command == 'add':
            asyncio.run(handle_add_task(args.description))
        elif args.command == 'list':
            asyncio.run(handle_list_tasks(show_all=args.all))
        elif args.command == 'complete':
            asyncio.run(handle_complete_task(args.task_id))
        elif args.command == 'delete':
            asyncio.run(handle_delete_task(args.task_id))
        elif args.command == 'export':
            asyncio.run(handle_export_tasks(args.filename))
        elif args.command == 'stats':
            asyncio.run(handle_task_statistics())
        else:
            parser.print_help()
    except Exception as e:
        logger.error(f"Error executing command '{args.command}': {e}")
        print("An error occurred. Check the logs for details.")

if __name__ == "__main__":
    main()
