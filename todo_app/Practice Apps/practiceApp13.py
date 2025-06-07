def get_average():
    with open('todo_app/Practice Apps/files/data.txt','r') as file_local:
        data = file_local.readlines()
    
    values = data[1:]

    values = [float(value.strip()) for value in values if value.strip().isdigit()]

    average_local = sum(values) / len(values) if values else 0
    return average_local

average_global = get_average()
print(average_global)