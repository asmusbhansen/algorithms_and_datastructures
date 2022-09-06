
class NaiveSymbolTable:

    def __init__(self):

        self.keys_ = []
        self.vals_ = []

    def get_key_idx(self, key):

        idx = 0

        for key_ in self.keys_:
            if key == key_:
                #print(f'key: {key}, idx: {idx}')
                return idx
            idx += 1

        return None

    def get(self, key):

        idx = self.get_key_idx(key)

        if idx == None:
            return None

        else:
            return self.vals_[idx]

    def contains(self, key):
        #print(f'Contains: {key}, {self.get_key_idx(key)}')
        return self.get_key_idx(key) != None

    def put(self, key, val):

        idx = self.get_key_idx(key)

        if idx == None:

            self.keys_ += [key]
            self.vals_ += [val]
            #print(f'Put self.keys_[-1]: {self.keys_[-1]}, self.vals_[-1]: {self.vals_[-1]}')
            #print(f'self.keys_: {self.keys_}')
            #print(f'self.vals_: {self.vals_}')
        else:

            self.vals_[idx] = val


    def keys(self):
        return self.keys_