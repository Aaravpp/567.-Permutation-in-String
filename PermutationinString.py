class Solution(object):
    def is_hash_same(self, hashS, hashW):
        return hashS == hashW
        # for i in range(26):
        #     if hashS[i] != hashW[i]:
        #         return False
        # return True

    def checkInclusion(self, s1, s2):

        if len(s1) > len(s2):
            return False

        hashS = [0] * 26
        hashW = [0] * 26
        window_length = len(s1)

        for i in range(window_length):
            hashS[ord(s1[i]) - 97] += 1
            hashW[ord(s2[i]) - 97] += 1

        i, j = 0, window_length - 1

        while j < len(s2):
            if self.is_hash_same(hashS, hashW):
                return True
            hashW[ord(s2[i]) - 97] -= 1
            i += 1
            j += 1
            if j < len(s2):
                hashW[ord(s2[j]) - 97] += 1
        return False