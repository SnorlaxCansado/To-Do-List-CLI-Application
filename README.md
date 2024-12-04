# To-Do List CLI Application (Async)

An asynchronous command-line to-do list application built in Python. This application allows you to manage your tasks directly from the command line with support for asynchronous operations, data export, and statistics.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Activate the Virtual Environment](#activate-the-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Initialize the Database](#initialize-the-database)
- [Usage](#usage)
  - [Add a Task](#add-a-task)
  - [List Tasks](#list-tasks)
  - [Complete a Task](#complete-a-task)
  - [Delete a Task](#delete-a-task)
  - [Export Tasks to CSV](#export-tasks-to-csv)
  - [View Task Statistics](#view-task-statistics)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Asynchronous Operations**: Utilizes `asyncio` and `aiosqlite` for non-blocking database interactions.
- **SQLAlchemy ORM**: Simplifies database operations with Object-Relational Mapping.
- **Command-Line Interface**: User-friendly CLI built with `argparse` for task management.
- **Logging**: Records application events and errors using Python's `logging` module.
- **Data Export**: Exports tasks to CSV files using `pandas` for data analysis.
- **Task Statistics**: Provides basic statistics about completed and pending tasks.

## Requirements

- Python 3.7 or higher
- Packages listed in `requirements.txt`

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/TODO_CLI_APP.git
cd TODO_CLI_APP
```

### Create a Virtual Environment

```bash
python3 -m venv venv
```

### Activate the Virtual Environment

- **On Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **On Unix or MacOS**:

  ```bash
  source venv/bin/activate
  ```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Initialize the Database

Before using the application, you need to create the database schema. Run the following commands:

1. **Create an Initialization Script**

   Create a file named `initialize_db.py` with the following content:

   ```python
   import asyncio
   import aiosqlite

   async def initialize_database():
       async with aiosqlite.connect('tasks.db') as db:
           await db.execute('''
               CREATE TABLE IF NOT EXISTS tasks (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   description TEXT NOT NULL,
                   completed BOOLEAN NOT NULL DEFAULT 0,
                   created_at DATETIME NOT NULL
               )
           ''')
           await db.commit()

   asyncio.run(initialize_database())
   print("Database initialized successfully.")
   ```

2. **Run the Initialization Script**

   ```bash
   python initialize_db.py
   ```

## Usage

Run the main script followed by a command:

```bash
python main.py <command> [options]
```

### Add a Task

Adds a new task to your to-do list.

```bash
python main.py add "Your task description"
```

**Example:**

```bash
python main.py add "Finish the project documentation"
```

### List Tasks

Lists all pending tasks. Use `--all` to include completed tasks.

```bash
python main.py list [--all]
```

**Example:**

```bash
python main.py list --all
```

### Complete a Task

Marks a task as completed.

```bash
python main.py complete <task_id>
```

**Example:**

```bash
python main.py complete 1
```

### Delete a Task

Deletes a task from the list.

```bash
python main.py delete <task_id>
```

**Example:**

```bash
python main.py delete 2
```

### Export Tasks to CSV

Exports all tasks to a CSV file.

```bash
python main.py export <filename>
```

**Example:**

```bash
python main.py export tasks.csv
```

### View Task Statistics

Displays statistics about your tasks.

```bash
python main.py stats
```

## Project Structure

```
TODO_CLI_APP/
├── __pycache__/
├── logs/
├── venv/
├── database.py
├── initialize_db.py
├── logger.py
├── main.py
├── models.py
├── requirements.txt
├── tasks.db
└── test_database.py
```

### Folder and File Descriptions

- `__pycache__/` - Compiled Python files.
- `logs/` - Directory for storing log files.
- `venv/` - Virtual environment for managing dependencies.
- `database.py` - Handles database-related functionality.
- `initialize_db.py` - Script to initialize the database.
- `logger.py` - Manages logging throughout the application.
- `main.py` - Main script to run the application.
- `models.py` - Defines data models using SQLAlchemy.
- `requirements.txt` - Lists Python dependencies for the project.
- `tasks.db` - SQLite database file.
- `test_database.py` - Unit tests for database functions.

## Running Tests

To run the unit tests for database functions:

```bash
python test_database.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or additions.