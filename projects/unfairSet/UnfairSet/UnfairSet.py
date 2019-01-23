class UnfairSet():
    def __init__(self, unfairset=[]):
        self.UnfairSet = []
        self.setup_UnfairSet(unfairset)

    def size(self):
        return len(self.UnfairSet)

    def add(self, char):
        if len(char) == 1:
            if (char == char.upper()) and char.isalpha():
                self.UnfairSet.append(char)
                return f'new character: {char}'
            else:
                if char not in self.UnfairSet:
                    self.UnfairSet.append(char)
                    return f'new character: {char}'
            return f'character {char} already exist'
        else:
            raise ValueError('The items in the unfair set must be single characters.')

    def remove(self, char):
        if self.is_in(char):
            self.UnfairSet.remove(char)
            return f'removed: {char}'
        else:
            raise ValueError('There is no such character.')

    def is_in(self, char):
        return char in self.UnfairSet

    def setup_UnfairSet(self, set):
        for item in set:
            if len(item) == 1:
                self.add(item)
            else:
                list_of_char = list(item)
                print(ValueError('The items in the unfair set must be single characters.'), f'\nconverting {item} to UnfairSet format')
                for x in list_of_char:
                    self.add(x)
        self.sort_UnfairSet()


    def sort_UnfairSet(self):
        self.UnfairSet.sort()