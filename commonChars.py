class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counters = [Counter(word) for word in words]
        common_chars = []
        for char in counters[0]: 
            min_count = min(counter[char] for counter in counters)
            common_chars.extend([char] * min_count)
        return common_chars
            
