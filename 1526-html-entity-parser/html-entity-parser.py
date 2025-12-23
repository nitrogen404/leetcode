class Solution:
    def entityParser(self, text: str) -> str:
        entity_map = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        result = []
        i = 0
        while i < len(text):
            if text[i] == '&':
                j = i
                while j < len(text) and text[j] != ';' and j - i <= 10:
                    j += 1
                if j < len(text) and text[j] == ';':
                    entity = text[i: j + 1]
                    if entity in entity_map:
                        result.append(entity_map[entity])
                        i = j + 1
                        continue
            result.append(text[i])
            i += 1
        return ''.join(result)