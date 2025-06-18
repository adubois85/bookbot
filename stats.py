def get_word_count(text):
    wc = len(text.split())
    return wc

def get_char_count(text):
    chars = {}
    for char in text:
        if char.lower() not in chars:
            chars[char.lower()] = 1
        else:
            chars[char.lower()] += 1
    return chars

def sort_char_count(character_dict):
    sorted_chars = []
    for char in character_dict:
        if char.isalpha():
            sorted_chars.append({"char": char, "num" : character_dict[char]})
    sorted_chars.sort(reverse=True, key=lambda x: x["num"])
    return sorted_chars