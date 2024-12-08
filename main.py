def count_chars(s):
    count = {}
    for c in s.lower():
        if not c.isalpha():
            continue
        if c not in count:
            count[c] = 0
        count[c] += 1
    return count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = len(file_contents.split())
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} found in the document")
    print()

    counts_list = []
    counts_dict = count_chars(file_contents)
    for c in counts_dict:
        counts_list.append({ "character": c, "count": counts_dict[c]})
    counts_list.sort(reverse=True, key=lambda e: e["count"])

    for char_count in counts_list:
        character = char_count["character"]
        count = char_count["count"]
        print(f"The '{character}' was found {count} times")
    print("--- End report ---")

main()
