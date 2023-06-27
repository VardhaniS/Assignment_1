#!/usr/bin/env python
# coding: utf-8

#  1. 1. In the below elements which of them are values or an expression? eg:- values can be
# integer or string and expressions will be mathematical operators.
*     - expressions
&     - expressions
-87.8 - value(float) 
-     - expression
/     - expression
+     - expression
6     - value(integer)
# In[2]:


print(type(-87.8))
print(type(6))


# 2. What is the difference between string and variable?
String = String is a datatype which contains data in characters 
Variable = Holds the data and process it .
# 3. Describe three different data types.
Integer - the data type which has numbers
Float  - the data type which has decimal values
String  - the datatype which contains data in characters 

# 4. What is an expression made up of? What do all expressions do?
 Expression is a combination of operators and variables.An expression returns value.
    example:
        a=4
        a=a+2
        output:6
        
        a=a+2 is an expression
# 5. This assignment statements, like spam = 10. What is the difference between an
# expression and a statement?
An expression returns the value where as the assignment statement assigns the value to the variable
# 6. After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1

# In[5]:


bacon = 22 
bacon + 1
print(bacon)


# 7. What should the values of the following two terms be?
# 'spam'+ 'spamspam'
# 'spam'*3

# In[3]:


print('spam'+ 'spamspam') 
print('spam'*3)


# 8. Why is eggs a valid variable name while 100 is invalid?
The variable name should always be the string or character but not the integer.
Here eggs is a string so it is acceptable as the variable name where as 100 is the integer which is not acceptable as a variable name
# 9. What three functions can be used to get the integer, floating-point number, or string
# version of a value?
integer- int()
Floating point- float()
string - str()
# 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten '+ 99 + 'burritos'
answer:
We need to change the type of 99 .
Here everything is in string type . So we can change the integer into string known as typecasting
# In[1]:


print('I have eaten '+ str(99) + 'burritos')

