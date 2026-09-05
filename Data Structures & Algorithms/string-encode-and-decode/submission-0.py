class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word))+"#"+word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        start = 0
        i = 0
        while i<len(s):
            while s[i] != "#":
                i+=1
            num = int(s[start:i])
            decoded.append(s[i+1:num + i +1])
            i = i+1+num
            start = i
        return decoded

