class WordError(Exception):
    def __str__(self):
        return "Wrong!"


def check_w_letter(word):
    if "w" in word:
        raise WordError
    else:
        return word
