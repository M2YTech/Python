import random
from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()

def playgame():
    choices = ["snake", "gun", "water"]
    user_score = 0
    computer_score = 0
    round = 3

    for i in range(1, round + 1):
        console.rule(f"[bold cyan]🐍 Round {i} 🥤")
        print("[bold yellow]Choose one from the below three:")
        print("[green]1. Water   [magenta]2. Gun   [blue]3. Snake[/]")

        while True:
            print("[bold white]Enter your choice:[/]", end=" ")
            user = input().lower()
            if user in choices:
                break
            else:
                print("[bold red]❌ Invalid input! Please choose from snake, gun, or water.")

        computer = random.choice(choices)
        print(f"[bold]You chose:[/] [cyan]{user}[/]  |  [bold]Computer chose:[/] [magenta]{computer}[/]")

        if user == "snake" and computer == "water":
            print("[green]✅ User Wins this round![/]")
            user_score += 1
        elif user == "water" and computer == "gun":
            print("[green]✅ User Wins this round![/]")
            user_score += 1
        elif user == "gun" and computer == "snake":
            print("[green]✅ User Wins this round![/]")
            user_score += 1
        elif user == computer:
            print("[yellow]🤝 It's a draw[/]")
        else:
            print("[red]💻 Computer Wins this round![/]")
            computer_score += 1

    console.rule("[bold magenta]🏁 Game Over 🏁")
    print(f"[bold white]Total rounds played:[/] {round}")
    print(f"[bold magenta]Computer scored:[/] {computer_score}")
    print(f"[bold cyan]User scored:[/] {user_score}")

    if user_score > computer_score:
        console.print(Panel.fit("🎉 [bold green]User wins the game![/]", style="bold green"))
    elif computer_score > user_score:
        console.print(Panel.fit("💻 [bold red]Computer wins the game![/]", style="bold red"))
    else:
        console.print(Panel.fit("🤝 [bold yellow]It's a tie![/]", style="bold yellow"))


# Main game loop
while True:
    playgame()
    play_again = input("\n[bold blue]Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\n[bold cyan]🎮 Thank you for playing the game! Goodbye!")
        break
