class Sticks:
    def __init__(self, n, stick_length=50):
        self.sticks = [True] * n
        self.stick_length = stick_length

    def __len__(self):
        return len(self.sticks)

    def __repr__(self):
        n = len(self.sticks)
        max_len_number = len(str(n))
        stick_strs = []
        for i, stick in enumerate(self.sticks):
            stick_str = "{0:0{1}d} ".format(i + 1, max_len_number)
            if stick:
                stick_str += "-" * self.stick_length
            stick_str += "\n\n"
            stick_strs.append(stick_str)
        return "".join(stick_strs)

    def __getitem__(self, idx):
        return self.sticks[idx]
    
    def __setitem__(self, idx, item):
        self.sticks[idx] = item

    def pick(self, idx):
        assert 0 <= idx < len(self.sticks)
        self.sticks[idx] = False