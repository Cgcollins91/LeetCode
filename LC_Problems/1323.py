class Solution:
    def maximum69Number (self, num: int) -> int:

        # Convert Num to String so we can process digit by digit
        str_num = str(num)
        
        # Create empty list where we'll store the output maximum number and 
        # a flag whether we have switched one digit or not
        num_list_str = []
        switched     = False
        
        # Process each digit from left to right and turn the first 6 encountered to a 9
        # This guarantees we will get the maximum number after switching the left most 6 to a 9
        for char in str_num:
            
            if char == '6' and not switched:
                char = '9'
                switched = True
                
            num_list_str.append(char)
        
        # Convert our list of individual digit characters back to a string
        new_str = ''
        for char in num_list_str:
            new_str += char
        
        return int(new_str)
    
    

        #####     ALTERNATE SOLUTION    ######
        # Convert to string, replace only the first "6" with "9"
        
        # return int(str(num).replace("6", "9", 1))
