from utils.time_measurement import time_measurement


class LongestSubstringWithoutRepeatingCharacters:
    @staticmethod
    @time_measurement
    def solution(s: str) -> int:
        used = {}
        max_length = start = 0
        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, idx - start + 1)

            used[char] = idx
        return max_length
