class PlayfairCipher:
    def __init__(self, plain_text, keyword):
        self.plain_text = plain_text
        self.keyword = keyword
        self.matrix = self.generate_key_matrix(self.keyword)
        self.ciphertext = self.playfair_encrypt(self.plain_text)

    @staticmethod
    def generate_key_matrix(keyword):
        keyword = keyword.upper().replace("J", "I")
        seen = set()
        key = ""

        for char in keyword:
            if char not in seen and char.isalpha():
                seen.add(char)
                key += char

        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # I and J combined
            if char not in seen:
                key += char

        matrix = [list(key[i:i+5]) for i in range(0, 25, 5)]
        return matrix

    @staticmethod
    def prepare_text(text):
        text = text.upper().replace("J", "I")
        prepared = ""
        i = 0
        while i < len(text):
            char1 = text[i]
            char2 = text[i+1] if i+1 < len(text) else "X"

            if char1 == char2:
                prepared += char1 + "X"
                i += 1
            else:
                prepared += char1 + char2
                i += 2

        if len(prepared) % 2 != 0:
            prepared += "X"
        return prepared

    @staticmethod
    def find_position(matrix, char):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j
        return None, None

    @classmethod
    def encrypt_pair(cls, matrix, a, b):
        row1, col1 = cls.find_position(matrix, a)
        row2, col2 = cls.find_position(matrix, b)

        if row1 == row2:  # same row
            return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # same column
            return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # rectangle
            return matrix[row1][col2] + matrix[row2][col1]

    def playfair_encrypt(self, plaintext):
        prepared = self.prepare_text(plaintext)
        ciphertext = ""

        for i in range(0, len(prepared), 2):
            ciphertext += self.encrypt_pair(self.matrix, prepared[i], prepared[i+1])
        return ciphertext

# Example usage:
if __name__ == "__main__":
    plain_text = "HELLO WORLD"
    keyword = "KEYWORD"
    cipher = PlayfairCipher(plain_text, keyword)
    print("Plaintext:", plain_text)
    print("Keyword:", keyword)
    print("Encrypted:", cipher.ciphertext)
