class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # HashMap
        # Key : Value
        # int[] : ["eat", "tea", ...]
        # Time: O(m * n) Space: 

        result = defaultdict(list) # Just a default HashMap
        for str in strs:
            curr = [0] * 26
            for i in range(len(str)):
                curr[ord(str[i]) - ord('a')] += 1

            result[tuple(curr)].append(str) # Keys cannot be lists, so TUPLE
        return list(result.values())

        # Create a hash map where each key is a 26-length tuple representing character 
        #     frequencies, and each value is a list of strings belonging to that anagram group.
        # For each string in the input:
        # Initialize a frequency array of size 26 with all zeros.
        # For each character in the string, increment the count at the corresponding index.
        # Convert the frequency array to a tuple and use it as the key.
        # Append the string to the list associated with this key.
        # After processing all strings, return all the lists stored in the hash map.

