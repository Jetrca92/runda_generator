import csv

file_path = "Seznam.csv"

def read_csv():
    song_list = []
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            song_list.append({
                'Naslov': row.get('Naslov', ''),
                'Zasedba': row.get('Zasedba', ''),
                'Ritem': row.get('Ritem', ''),
                'Bas': row.get('Bas', ''),
            })
        print(song_list)
        return song_list

if __name__ == "__main__":
    read_csv()
