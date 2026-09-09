class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        res = []
        mp = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            if key in mp:
                mp[key].append(s)
            else:
                mp[key] = [s]

        for first, second in mp.items():
            res.append(second)


        return res