class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""
        for word in strs:
            word_len = len(word)

            encoded_word = f"{word_len}#" + word
            encoded_str += encoded_word

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_word = ""
        decoded_array = []
        
        curr_len = ""

        i = 0
        while i < len(s):
            if s[i] == "#":
                word = s[i+1: (i+1+ int(curr_len))]
                decoded_array.append(word)
                i = i+1+ int(curr_len)
                curr_len = ""
            else:
                curr_len += s[i]
                i+=1
        return decoded_array


