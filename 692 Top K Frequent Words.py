'''
692. Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/
'''
def topKFrequent(words: List[str], k: int) -> List[str]:
    book = {} # {word: frequency}
    for word in words:
        book[word] = book.get(word, 0) + 1

    ls = sorted(book.items(), key = lambda x : (-x[1], x[0]))
    return [p[0] for p in ls[:k]]
