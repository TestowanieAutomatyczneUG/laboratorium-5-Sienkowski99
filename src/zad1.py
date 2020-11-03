class Hamming:
    def distance(self, a, b):
        if len(a) != len(b):
            raise ValueError('err')
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