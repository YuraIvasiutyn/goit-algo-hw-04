def get_cats_info(path) -> list[dict[str, any]]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            cats = [line.split(",") for line in f if line.strip()]
            result = []
            for cat in cats:
                result.append({
                    "id": cat[0].strip(),
                    "name": cat[1].strip(),
                    "age": cat[2].strip()
                })
            return result
    except FileNotFoundError:
        print("Файл не знайдено")
        return [{}]


print(get_cats_info("../cats/file2.txt"))
