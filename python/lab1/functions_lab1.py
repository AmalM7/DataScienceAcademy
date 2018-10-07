def character_distance(left, right):
    return abs(ord(left) - ord(right))

def is_surpassing_word(word):
    distances = [character_distance(left, right) for left, right in zip(word, word[1:])]
    return all(left < right for left, right in zip(distances, distances[1:]))

def is_cyclone_word(word):
    word = word.upper()
    letters = [None] * len(word)
    half = (len(word) + 1) // 2
    letters[::2] = word[:half]
    letters[1::2] = word[:half - 1:-1]
    return all([left <= right for left, right in zip(letters, letters[1:])])