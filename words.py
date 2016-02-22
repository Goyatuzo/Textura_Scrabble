class Words:
    def __init__(self):
        self.data = {}

        # Sanitize the word to be usable by the dictionary.
    def sanitize(self, word):
        return word + ' '

    def add(self, word):
        word = self.sanitize(word)

        curr_dict = self.data

        for c in word:
            # If c doesn't exist in dictionary, create new empty dict.
            if c not in curr_dict:
                curr_dict[c] = {}

            # Advance to the index of c within dictionary.
            curr_dict = curr_dict[c]

    def exists(self, query):
        word = self.sanitize(word)

        curr_dict = self.data

        for c in word:
            # If the current letter doesn't exist, return false.
            if c not in curr_dict:
                return False

            # Otherwise go one level deeper into the nested dictionaries.
            curr_dict = curr_dict[c]

        # If it's made it to here, that means the word exists.
        return True