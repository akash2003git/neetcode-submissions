class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        sizes = []
        for s in strs:
            sizes.append(str(len(s)))

        encodedStr = ",".join(sizes) + "#"

        for s in strs:
            encodedStr += s

        return encodedStr


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        decodedStrs = []
        delimiter_index = s.find("#")
        sizes_str = s[:delimiter_index]
        content = s[delimiter_index + 1:]

        sizes = sizes_str.split(",")

        current_pos = 0
        for size in sizes:
            length = int(size)
            decodedStrs.append(content[current_pos : current_pos + length])
            current_pos += length

        return decodedStrs