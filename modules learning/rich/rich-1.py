# from rich import print

# print("[bold green]Hello Sahil![/bold green]")
# print("[red]Error![/red]")
# print("[yellow]Warning![/yellow]")



# console = Console() #console object that provides many advanced terminal operations

# console.print("Hello World")
# console.print("[green]Success![/green]")
# console.print("[red]Error![/red]")

# console.print()
# console.input()
# console.log()
# console.clear()
# console.rule()
# console.status()
# console.print_exception()

from rich.console import Console
from rich.table import Table
console = Console()
table = Table()

table.add_column("[red]NAME[/red]")
table.add_column("age")
table.add_column("department")

table.add_row("sahil","21")
table.add_row("nayan","20","cit")

console.print(table)
# name = console.input("Enter your name: ")
# console.print(f"[magenta]{name}[/magenta]")
# console.print(name, style = "bold magenta")

