# практична робота 4, варіант 20
# базова частина тімліда (частина а)

def create_initial_file(filename: str = "TF26_1.txt") -> None:
    # рядки латинських букв різної довжини з великими та малими літерами
    sample_lines = [
        "HelloWorld",
        "PythonPROGRAMMING",
        "AbCdEfGhIjKlMnOp",
        "TEXTProcessingLabWork",
        "QuickBrownFoxJumpsOverTheLazyDog",
    ]

    try:
        with open(filename, "w", encoding="utf-8") as f:
            for line in sample_lines:
                f.write(line + "\n")
        print(f"файл {filename} успішно створено")
    except OSError as e:
        print(f"помилка створення файлу {filename}: {e}")


def main() -> None:
    print("старт базової програми тімліда")
    create_initial_file()
    # todo: розробник 2 має додати читання TF26_1.txt, заміну великих літер на малі та запис у TF26_2.txt
    # todo: розробник 2 має додати читання файлу TF26_2.txt та виведення його рядків на екран

if __name__ == "__main__":
    main()