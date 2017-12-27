# a = [1, 2, 3]
# b = [11, 12, 13]
# 
# c = [a[1],b[1]]
# print(c)

# '''i = 11
# while i > 1:
#     i -= 1
#     if i % 2 == 1:
#         continue
#     print(i)'''

a = [1, 2, 3, 4, 5, 6]
b = [11, 12, 13, 14, 15, 16]

i = 0
j = 0

while i < len(a):
        if i == 1:
                while j < len(b):
                                if j == 3:
                                        c = [a[i], b[j]]
                                        print(c)
                            
        i += 1
        j += 1  
                                    
        
 
            