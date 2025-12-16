import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'е')
    text = re.sub(r'[\t\r\n]', ' ', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()

def tokenize(text: str) -> list[str]:
    text = normalize(text)
    return re.findall(r'\w+(?:-\w+)*', text) # регулярное выражение для поиска слов

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_dict = {}
    for token in tokens:
        if token in freq_dict:
            freq_dict[token] += 1
        else:
            freq_dict[token] = 1
    sorted_dict = {}

    for item in sorted(freq_dict.items(), key=lambda x: (-x[1], x[0])):
        sorted_dict[item[0]] = item[1]

    return sorted_dict
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

