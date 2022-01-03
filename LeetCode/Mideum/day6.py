 # Reverse Integer
  # Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], 
  # then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        if x<(-1)*2**31 or x>2**31-1 or x==0:
            return 0
        elif x>=(-1)*2**31 and x<0:
            num = str(-1*x)
            r_num = num[::-1]
            n_num = int(float(r_num))*(-1)
            if n_num<(-1)*2**31 :
                return 0
            else:
                return int(n_num)
        elif x<=2**31-1 and x>0:
            num = str(x)
            r_num = num[::-1]
            n_num = int(float(r_num))
            if n_num > 2**31-1:
                return 0
            else:
                return n_num
        
