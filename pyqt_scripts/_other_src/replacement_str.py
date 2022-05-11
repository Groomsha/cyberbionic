class ReplacementStr:
    def __init__(self) -> None:
        self.ch_old = 'test'
        self.ch_new = []
        self.counter = 0

    def example_one(self):
        self.counter = 1

        for ch in self.ch_old:
            if self.counter % 2:
                self.ch_new.append(ch)
            else:
                self.ch_new.append('!')

            self.counter += 1

        print(''.join(self.ch_new))

    def example_two(self):
        self.counter = 0

        while True:
            if self.counter == len(self.ch_old):
                break

            if self.counter % 2:
                self.ch_new += '!'
            else:
                self.ch_new += self.ch_old[self.counter]

            self.counter += 1

        print(self.ch_new)


if __name__ == '__main__':
    repl = ReplacementStr()

    repl.example_one()
    repl.example_two()
