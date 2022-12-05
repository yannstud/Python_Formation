import json

with open("dict.txt", encoding = 'utf-8') as f:
    all_text = f.read().splitlines()
    str_text = ' '.join(all_text).split(' ')
    d = {}
    banned = ["", "and", "the", "to", "for", "is", "of", "a", "are", "that", "or", "our", "It's"]
    for w in str_text:
        if w in banned:
            continue
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    sorted = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

    with open('dict.json', "w", encoding='utf-8') as d:
        json.dump(sorted, d, ensure_ascii=False)
