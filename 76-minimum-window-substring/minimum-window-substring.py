class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freq1={}
        freq2={}
        for k in range(len(t)):
            freq1[t[k]]=freq1.get(t[k],0)+1
        need=0
        for key in freq1:
            need+=1
        have=0
        i=0
        mini=""
        min_len=float('inf')
        for j in range(len(s)):
            if s[j] in freq1:
                freq2[s[j]]=freq2.get(s[j],0)+1
                if(freq1[s[j]]==freq2[s[j]]):
                    have+=1
            while have==need:
                if j-i+1<min_len:
                    min_len=j-i+1
                    mini=s[i:j+1]
                if s[i] in freq1:
                    freq2[s[i]]-=1
                    if freq2[s[i]]<freq1[s[i]]:
                        have-=1
                i+=1
        return mini



            
                



        