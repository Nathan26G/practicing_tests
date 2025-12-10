# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        print(self.text)
        while i < len(self.text):
            print('on ', self.text[i])
            if self.text[i].lower() in self.vowels:
                print('got rid off ', self.text[i])
                self.text = self.text[:i] + self.text[i+1:]
                print('now text is: ', self.text)
                i -= 1
            i += 1
        return self.text
