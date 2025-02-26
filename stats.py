def count_words(book_text):
    list_words = book_text.split()
    return len(list_words)

def character_count(book_text):
    counts = {}
    for char in book_text:
        if char.lower() in counts:
            counts[char.lower()] += 1
        else:
            counts[char.lower()] = 1
    return counts

def sort_on(dict):
    return list(dict.values())[0]

def report(counts):
    sorted_list = []
    for char, count in counts.items():
        new_dict = {char: count}
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
