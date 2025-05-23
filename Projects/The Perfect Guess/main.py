import random
from rich.console import Console
from rich.prompt import Prompt
from rich import box
from rich.panel import Panel

console = Console()

# Game Introduction
console.print(Panel("[bold green]🎯 Welcome to the Perfect Guess Game![/bold green]", box=box.DOUBLE))

n = random.randint(1, 100)
number_of_guesses = 0
user_value = None

while user_value != n:
    user_value = int(Prompt.ask("[cyan]Enter your guess (1-100)[/cyan]"))
    number_of_guesses += 1

    if user_value > n:
        console.print("[bold yellow]📉 Too high! Try a lower number.[/bold yellow]")
    elif user_value < n:
        console.print("[bold magenta]📈 Too low! Try a higher number.[/bold magenta]")

# Victory Message
console.print("\n[bold green]🎉 Congratulations! You've guessed the number![/bold green]")
console.print(Panel(f"[bold blue]The correct number was: [yellow]{n}[/yellow]\n"
                    f"You took [bold red]{number_of_guesses}[/bold red] guesses.[/bold blue]",
                    title="🎊 Game Summary", box=box.ROUNDED, border_style="blue"))
