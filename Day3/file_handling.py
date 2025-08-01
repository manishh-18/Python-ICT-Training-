'''
    File := 
        File in reference to python is a logical entity
    File Handling :- 
        Access modifiers :
            r   , w   , a
            r+  , w+  , a+
            rb  , wb  , ab
            rb+ , wb+ , ab+
            x
'''


var = open('<filename>0','am')
var.close()

#  OR

with open('<filename>0','am') as var: