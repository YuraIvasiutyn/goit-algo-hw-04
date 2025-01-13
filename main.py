import sys
from pathlib import Path
from colorama import Fore, Style, init


init(autoreset=True)


def visualize_directory_structure(directory: Path, indent: str = ""):

    try:
        for item in sorted(directory.iterdir()):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
                visualize_directory_structure(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Доступ заборонено до: {directory}{Style.RESET_ALL}")


def main():

    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python main.py app" + Style.RESET_ALL)
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(Fore.RED + f"Помилка: Шлях '{directory_path}' не існує." + Style.RESET_ALL)
        sys.exit(1)

    if not directory_path.is_dir():
        print(Fore.RED + f"Помилка: Шлях '{directory_path}' не є директорією." + Style.RESET_ALL)
        sys.exit(1)

    print(Fore.YELLOW + f"Структура директорії: {directory_path}" + Style.RESET_ALL)
    visualize_directory_structure(directory_path)


if __name__ == "__main__":
    main()
