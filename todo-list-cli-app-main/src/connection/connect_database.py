import typer
import uuid
from rich.console import Console
from rich.table import Table
from typing import Literal
from rich import print
from connection.connect_database import connect_database
from helpers.status_colors import status_colored

app = typer.Typer()
STATUS = Literal["COMPLETED", "PENDING", "IN_PROGRESS"]
console = Console()

def get_connection():
    return connect_database("./src/database/todo.db")

@app.command(short_help="Create one task")
def create(name: str, description: str, status: STATUS):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO TASKS(uuid, name, description, status) VALUES(?, ?, ?, ?)",
            (str(uuid.uuid4()), name, description, status)
        )
        conn.commit()
        conn.close()
        print("One task has been [bold green]created[/bold green]")

@app.command(short_help="List all tasks")
def list():
    conn = get_connection()
    table = Table("UUID", "Name", "Description", "Status", show_lines=True)
    if conn:
        cursor = conn.cursor()
        results = cursor.execute(
            "SELECT uuid, name, description, status FROM tasks"
        )
        for uuid_val, name, description, status in results.fetchall():
            status_with_color = status_colored(status)
            table.add_row(uuid_val, name, description, status_with_color)
        conn.close()
    table.caption = "List all tasks"
    console.print(table)

@app.command(short_help="Update one task")
def update(uuid: str, name: str = "", description: str = "", status: STATUS = "PENDING"):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM tasks WHERE uuid = ?", (uuid,)).fetchone()
        if not result:
            print(f"[red]No task found with UUID:[/red] {uuid}")
            return
        current_name, current_description, current_status = result[1], result[2], result[3]
        name = name or current_name
        description = description or current_description
        status = status or current_status
        cursor.execute(
            "UPDATE tasks SET name = ?, description = ?, status = ? WHERE uuid = ?",
            (name, description, status, uuid)
        )
        conn.commit()
        conn.close()
        print("[bold green]Task updated successfully![/bold green]")

@app.command(short_help="Delete one task")
def delete(uuid: str):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM tasks WHERE uuid = ?", (uuid,)).fetchone()
        if not result:
            print(f"[red]No task found with UUID:[/red] {uuid}")
            return
        cursor.execute("DELETE FROM tasks WHERE uuid = ?", (uuid,))
        conn.commit()
        conn.close()
        print("[bold red]Task deleted successfully![/bold red]")

if __name__ == "__main__":
    app()

