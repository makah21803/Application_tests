import re

def solution(S):

    # extract list of sentences
    sentences = (re.split('\.|\?|\!', S))

    max_len = 0
    for sentence in sentences:
        sentence = sentence.strip()

        # extract list of words
        words = [word for word in re.split(' ', sentence) if len(word) > 0]

        # check length and write
        length = len(words)
        if length > max_len:
            max_len = length

    return max_len

print(solution("Forget  CVs..Save time . x x"))

