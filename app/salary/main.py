def total_salary(path) -> list:
    try:
        with open(path, "r", encoding="utf-8") as f:
            salaries = [int(line.split(",")[1])for line in f if line.strip()]
            total = sum(salaries)
            average = total / len(salaries)
        return [total, int(average) if average.is_integer() else average]
    except FileNotFoundError:
        print("Файл не знайдено")
        return [0, 0]
    except Exception as e:
        print(f"Внутріншя помилка {e}")
        return [0, 0]
        

total, average = total_salary("file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
