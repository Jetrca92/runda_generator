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
        count_list(song_list)
        return song_list
    
def count_categories(song_list, category_key, category_values):
    category_counts = {category: 0 for category in category_values}

    for item in song_list:
        category = item.get(category_key, '').lower()

        for cat_val in category_values:
            if cat_val in category:
                category_counts[cat_val] += 1
                break

    return category_counts
    
def count_list(list):
    zasedba_values = ['kvintet', 'trio']
    ritem_values = ['polka', 'valček']
    bas_values = ['bas', 'bariton']
    
    zasedba_counts = count_categories(list, 'Zasedba', zasedba_values)
    ritem_counts = count_categories(list, 'Ritem', ritem_values)
    bas_counts = count_categories(list, 'Bas', bas_values)

    print(f"Kvintet: {zasedba_counts['kvintet']} pesmi, Trio: {zasedba_counts['trio']} pesmi. Skupaj {[ritem_counts['polka']]} polk in {ritem_counts['valček']} valčkov. Na bas {bas_counts['bas']} komadov, na bariton {bas_counts['bariton']} komadov.")

if __name__ == "__main__":
    read_csv()
