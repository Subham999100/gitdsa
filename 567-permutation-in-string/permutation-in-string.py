class Solution(object):

    def checkInclusion(self, s1, s2):

        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        freq1 = {}
        freq2 = {}

        for k in range(len(s1)):
            freq1[s1[k]] = freq1.get(s1[k], 0) + 1

        i = 0

        for j in range(len(s2)):

            freq2[s2[j]] = freq2.get(s2[j], 0) + 1

            if j - i + 1 == len(s1):

                if freq1 == freq2:
                    return True

                freq2[s2[i]] -= 1

                if freq2[s2[i]] == 0:
                    del freq2[s2[i]]

                i += 1

        return False


        