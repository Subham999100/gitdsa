class Solution(object):
    def trap(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(h)-1
        lm=h[i]
        rm=h[j]
        total=0
        while(i<=j):
            if(lm <rm):
                ch=h[i]
                if(ch>=lm):
                    lm=ch
                else:
                    total=total+(lm-ch)
                i+=1
            else:
                ch=h[j]
                if(ch>=rm):
                    rm=ch
                else:
                    total=total+(rm-ch)
                j-=1
        return total




        