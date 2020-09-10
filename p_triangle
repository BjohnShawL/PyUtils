def fibo(r):
    # returns the fibonacci sequence up to the number provided
    f_list = [0]
    n=1
    while n < r:
        f_list.append(n)
        n = f_list[-1]+f_list[-2]
                
    return f_list

def listSplit(lst, index):
    #splits the list into chunks of up to 4. Can return an empty list
    return lst[index:index+4]

def isPythagorean(f_chunk):
    #this is where the logic happens. If we have 5,8,13,21 as our f_chunk
    #a is 2 times 8 times 13 (208)
    a = 2 * f_chunk[1] * f_chunk[2]
    #b is 5 times 21 (105)
    b = f_chunk[0] * f_chunk[3]
    #and c is 8^2 + 13^2 (64 + 169 = 233)
    c = (f_chunk[1]*f_chunk[1])+(f_chunk[2]*f_chunk[2])
    #verify the logic with a bit of pythagorean theory
    if((a*a)+(b*b)==(c*c)):
        #and return a formatted string to output
        return(f'[{a},{b},{c}]')

def valList(f_chunk):
    #this is just for pleasant formatting, really
    #the logic is the same as in isPythagorean(), but here we output a list of values
    a = 2 * f_chunk[1] * f_chunk[2]
    b = f_chunk[0] * f_chunk[3]
    c = (f_chunk[1]*f_chunk[1])+(f_chunk[2]*f_chunk[2])
    if((a*a)+(b*b)==(c*c)):
        return[a,b,c]

def P_triangle(end):
    # pass your end number in to generate the fibonacci sequence up to that number (exclusive)
    f_list = fibo(end)
    for i in range(end):
        #for each index in that range, split the list into a chunk of up to 4 values
        lst = listSplit(f_list,i)
        #only operate on the chunk if the chunk contains exactly 4 values
        #this avoids null reference exceptions
        if(len(lst)==4):
            #and then it's just outputting and formatting
                    values = valList(lst)
                    a = values[0]
                    b = values[1]
                    c = values[2]
                    print(f'{lst} : {isPythagorean(lst)}')
                    print(f'{a}^2 = {a*a}, {b}^2 = {b*b}, {c}^2 = {c*c}.')
                    print(f'{a*a} + {b*b} = {(a*a)+(b*b)}')
            
