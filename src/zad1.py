class Hamming:
    def distance(self, a, b):
        if a == "" and b == "":
            return 0
        if a == b:
            return 0
        # if a != b:
        #     return 1
        arrA = []
        arrB = []
        for letter in a:
            arrA.append(letter)
        for letter in b:
            arrB.append(letter)
        result = 0
        for i in range(0, len(arrA)):
            if arrA[i] != arrB[i]:
                result +=1
            else:
                pass
        return result