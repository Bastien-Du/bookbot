def count_words(text):
        words = text.split()
        return len(words)

def count_char(text):
	char_count = {}
	for char in text.lower():
		if char in char_count:
			char_count[char] +=1
		else:
			char_count[char] = 1
	return char_count

def sort_on(letter):
	return letter["num"]


def sort_count_char(char_counts):
    filtered_list = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]

    filtered_list.sort(key=sort_on, reverse=True)

    return filtered_list
