def total_salary(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        total = 0
        for line in lines:
            parts = line.split(',')
            if len(parts) >=2:
                try:
                    salary = float(parts[1].strip())
                    total += salary
                except ValueError:
                    continue
    
    average = total / len(lines) if lines else 0
    return total, average            
            



total_salary("path.txt")