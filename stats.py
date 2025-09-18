def word_counter(file_content):
    words = file_content.split()
    return len(words)

def char_counter(file_content):
    words = file_content.split()
    char_dict = {}
    for word in words:
        for char in word.lower():
            if char not in char_dict:
                char_dict[char] = 0
            char_dict[char] +=  1
    return char_dict

def sort_on(items):
    return items["num"]

def sorted_char_report(file_content):
    char_dict = char_counter(file_content)
    report_list = []
    for char in char_dict:
        report_dict = {}
        number = char_dict[char]
        report_dict["char"] = char
        report_dict["num"] = number
        report_list.append(report_dict)
    report_list.sort(reverse = True, key = sort_on)

    return report_list