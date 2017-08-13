import csv


def get_id_form_file(filename='data.csv'):
    try:
        with open('data.csv', newline='') as f:
            reader = csv.reader(f)
            data_list = [item for item in reader]
            if data_list:
                return max(int(item[0]) for item in data_list) + 1
            else:
                return 1
    except FileNotFoundError:
        with open(filename, 'w', newline='') as f:
            return 1


def write_form_to_file(request_form_dict, id_story, filename='data.csv'):
    data_labels = ['title', 'story', 'criteria', 'value', 'estimation', 'status']
    to_write = [request_form_dict[label] for label in data_labels]
    to_write.insert(0, str(id_story))
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(to_write)


def read_file(filename='data.csv'):
    try:
        with open('data.csv', newline='') as f:
            reader = csv.reader(f)
            return [item for item in reader]
    except FileNotFoundError:
        with open(filename, 'w', newline='') as f:
            return []


def update_file(id_story, data_update_list, filename='data.csv'):
    data_current = read_file()
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for item in data_current:
            if item[0] == id_story:
                writer.writerow(data_update_list)
            else:
                writer.writerow(item)


def delete_story_from_file(id_story, filename='data.csv'):
    data_current = read_file()
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for item in data_current:
            if item[0] == id_story:
                continue
            else:
                writer.writerow(item)
