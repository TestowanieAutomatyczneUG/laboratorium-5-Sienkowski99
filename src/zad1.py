class Hamming:
    def distance(self, a, b):
        if a == "" and b == "":
            return 0
        if a == b:
            return 0
        if a != b:
            return 1