def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')

                if len(parts) >= 3:
                    id_cat = parts[0].strip()
                    name = parts[1].strip()
                    age = parts[2].strip()

                    cats_info.append({
                        'id': id_cat,
                        'name': name,
                        'age': age
                    })

    except FileNotFoundError:
        return []

    return cats_info