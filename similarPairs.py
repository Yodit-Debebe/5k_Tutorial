class Solution:
    def similarPairs(self, words: List[str]) -> int:
        unique_char_sets = [''.join(sorted(set(word))) for word in words]
        count_map = Counter(unique_char_sets) 
        pairs = 0
        for freq in count_map.values():
            if freq > 1:        
                pairs += freq * (freq - 1) // 2
        return pairs
                        
