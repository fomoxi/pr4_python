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

def convert_upper_to_lower(
            source_file: str = "TF26_1.txt", target_file: str = "TF26_2.txt"
    ) -> bool:
        # читає файл TF26_1, замінює всі великі літери на малі та пише в TF26_2
        try:
            with open(source_file, "r", encoding="utf-8") as src:
                lines = src.readlines()

            converted_lines = [line.lower() for line in lines]

            with open(target_file, "w", encoding="utf-8") as dest:
                dest.writelines(converted_lines)

            print(f"дані успішно замінено на малі літери та збережено у {target_file}")
            return True
        except FileNotFoundError:
            print(f"помилка: файл {source_file} не знайдено")
            return False
        except OSError as e:
            print(f"помилка оброблення файлів: {e}")
            return False

def print_file_content(filename: str = "TF26_2.txt") -> None:
        # читає вміст файлу та друкує його по рядках
        try:
            with open(filename, "r", encoding="utf-8") as f:
                print(f"построковий вивід вмісту {filename}:")
                line_idx = 1
                for line in f:
                    print(f"рядок {line_idx}: {line.rstrip()}")
                    line_idx += 1
        except FileNotFoundError:
            print(f"помилка: файл {filename} не знайдено для читання")
        except OSError as e:
            print(f"помилка читання файлу {filename}: {e}")

def main() -> None:
        print("тестування модуля розробника 2")
        if convert_upper_to_lower():
            print_file_content()

if __name__ == "__main__":
        main()
