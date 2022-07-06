from rich.console import Console

console = Console()



def error(msg):
    console.print(f"[ERROR] {msg}", style="red")

def warning(msg):
    console.print(f"[WARNING] {msg}", style="yellow")

def good(msg):
    console.print(f"[GOOD] {msg}", style="green")

def info(msg):
    console.print(f"[INFO] {msg}", style="blue")

def edited(msg):
    console.print(f"[EDITED] {msg}", style="magenta")

def debug(msg):
    console.print(f"[DEBUG] {msg}", style="cyan")

def log(msg):
    console.print(f"[LOG] {msg}", style="white")