class MyStack(object):

    def __init__(self):
        self.q1=[]
        self.q2=[]
        self.active=1
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.active==1:
            self.q1.append(x)
        else:
            self.q2.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.active==1:
            while(len(self.q1)>1):
                x=self.q1.pop(0)
                self.q2.append(x)
            self.active=2
            return self.q1.pop(0)
        else:
            while(len(self.q2)>1):
                x=self.q2.pop(0)
                self.q1.append(x)
            self.active=1
            return self.q2.pop(0)

        

    def top(self):
        """
        :rtype: int
        """
        if self.active==1:
            while(len(self.q1)>1):
                x=self.q1.pop(0)
                self.q2.append(x)
            ans=self.q1.pop(0)
            self.q2.append(ans)
            self.active=2
            return ans
        else:
            while(len(self.q2)>1):
                x=self.q2.pop(0)
                self.q1.append(x)
            ans=self.q2.pop(0)
            self.q1.append(ans)
            self.active=1
            return ans
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.active==1:
            if(len(self.q1)==0):
                return True
            return False
        else:
            if(len(self.q2)==0):
                return True
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()