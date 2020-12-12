# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 09:13:18 2020

@author: Kirty
"""

"""

empty()  : O(1)
size()   : O(1)
top()    : O(1)
push(g)  : O(1)
pop()    : O(1)
"""

class conversion:
    def __init__(self):
        self.stack = []
        
        self.precedence = {"+":1,"-":1,"*":2,"/":2,"^":3}   
        self.top = -1 
    
    def push(self,data):
        self.stack.append(data)
   
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return 
    def isOperand(self,ch):
        if ch.isalpha():
            return True
        else:
            return False
    
    def isOperator(self,op):
        if op in ["/","-","^","+","*"]:
                  return True
        else:
            return False
            
    def isEmpty(self):
        return True if len(self.stack)==0 else False
    
    def isGreater(self,i):
       
        
        try:
            a = self.precedence[i]
            b  = self.precedence[self.peek()]
            return True if a<=b else False
              
        except:
            return False
    def infix_to_postfix(self,exp):
        """
        1. Scan the infix expression from left to right. 
        2. If the scanned character is an operand, output it. 
        3. Else, 
              1 If the precedence of the scanned operator is greater than the precedence of the operator in the stack(or the stack is empty           or the stack contains a ‘(‘ ), push it. 
              2 Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. After doing that Push the scanned operator to the stack. (If you encounter parenthesis while popping then stop there and push the scanned operator in the stack.) 
        4. If the scanned character is an ‘(‘, push it to the stack. 
        5. If the scanned character is an ‘)’, pop the stack and and output it until a ‘(‘ is encountered, and discard both the parenthesis. 
        6. Repeat steps 2-6 until infix expression is scanned. 
        7. Print the output 
        8. Pop and output from the stack until it is not empty.
        """
        
        # ----------------------------------------------------------------------
        output=""
        
        for i in exp:
            if self.isOperand(i):
                output+=i
            elif i=="(":
                self.push(i)
            elif i==")":
                while not self.isEmpty() and self.peek()!="(":
                    output+=self.pop()
                if not self.isEmpty() and self.peek()!="(":
                    return -1
                else:
                    self.pop()
            else:
                while not self.isEmpty() and self.isGreater(i):
                    output+=self.pop()
                self.push(i)
        while not self.isEmpty():
            output+=self.pop()
       
                
        print(output)
      

            
    def prefix_to_infix(self,exp):
        """
        see pic in the folder 
        """
        output=""
       
        for i in exp[::-1]:
            if self.isOperand(i):
                self.push(i)
            else:
                a = self.pop()
                b = self.pop()
                output = "("+a+i+b+")"
                self.push(output)
        for infix in self.stack:
            print(infix)
    def prefix_to_postfix(self,exp):
        for i in exp[::-1]:
            output=""
            if self.isOperand(i):
                self.push(i)
            else:
                a = self.pop()
                b=self.pop()
                output = a+b+i
                self.push(output)
        print(*self.stack)
    def postfix_to_infix(self,exp):
        output=""
        for i in exp:
            if self.isOperand(i):
                self.push(i)
                print(self.stack)
            else:
                a=self.stack.pop()
                b = self.stack.pop()
                output = "("+b+i+a+")"
                self.push(output)
        print(self.stack)
    
    def postfix_to_prefix(self,exp):
        output=""
        for i in exp:
            if self.isOperand(i):
                self.push(i)
            else:
                a=self.pop()
                b= self.pop()
                output = i+b+a
                self.push(output)
        print(self.stack)
    
    # def infix_to_prefix(self,exp):
      
                                                                                    
    
    
    # require little improvment
    def stock_span(self):
        arr=list(map(int,input().split()))
        span=[]
        
            
        span.append(1)
        
        for ele in range(len(arr)):
            
            
            while arr[ele]>arr[self.peek()]:
                        self.pop()
            if not self.isEmpty():    
                s = ele-self.peek()
                span.append(s)
            else:
                span[ele] = ele+1
                
            self.push(ele)
       
        print(span)
        
    
        
    
    def balancing_parantheses(self,exp):
        for i in exp:
            if i in ["(","[","{"]:
                self.push(i)
            else:
               if self.isEmpty():
                   return False
               current_char=self.pop()
               if current_char=="(":
                   if i!=")":
                       return False
               if current_char =="{":
                   if i!="}":
                       return False
               if current_char =="[":
                   if i!="]":
                       return False
            
        if not self.isEmpty():
            return False
       
        return True
    
    def next_greater_element(self,arr):
       
        for i in arr:
            next =i
            if self.isEmpty():
               
                self.push(next)
    
            elif not self.isEmpty() and next>self.peek():
               
                p=self.pop()
                
                while next > p :
                     print("{} -- {}".format(p,next))
                     if self.isEmpty():
                         break
                     p=self.pop()
                     
           
            
                self.push(i)
            else:
                self.push(i)
                
              
                
        
                
        print("{} -- {}".format(self.pop(),self.pop()))
        
    
        
                
                     
            
           
                   
                   
            
              
                        
                
                
                
            
        
        
        
            
            
        
            
           
            
        
        
c = conversion()    

arr=[4, 5, 2, 25]

c.next_greater_element(arr)

# c.stock_span()
        
# exp="[()]{}{[()()]()}"
# print(c.balancing_parantheses(exp))  

     
# exp="A + ( B * C - ( D / E ^ F ) * G ) * H"
# c.infix_to_prefix(exp)


# exp="AB+CD-*"
# c.postfix_to_prefix(exp)

# exp ="*-A/BC-/AKL"
# c.prefix_to_postfix(exp)


# exp="abc++"
# c.postfix_to_infix(exp)




# c.infix_to_postfix(exp)
# c.prefix_to_infix(exp)

        
                
                