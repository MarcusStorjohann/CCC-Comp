input1 = 'forloops'  #both inputs
input2 = 'forhoop' 
expected = []
actual = []
quiet = False
or_ks = ''
s_key = ''
q_key = ''

for i in input1:
    expected.append(i)
for i in input2:
    actual.append(i)
count = 1
# check for silly key 
for i in range(0,len(expected)):
    if len(expected) == len(actual): #when no quiet key 
        if expected[i] == actual[i]:
            pass
        else:
            s_key = actual[i]
            or_ks = expected[i]
            
    
    if len(expected) != len(actual):
        quiet = True
        if i > len(actual)-1:
            ai = i - count    
            if expected[i] == actual[ai]:
                pass
            else:
                if i == 0:
                    if actual[ai] == expected[i+1] or actual[ai] == expected[i+2] or actual[ai] == expected[i+3]:
                        q_key = expected[i]
        
                elif i == len(actual):
                    if actual[ai] == expected[i-1]:
                        q_key = expected[len(actual) +1]
                
                elif actual[ai] == expected[i]:
                    q_key = expected[i]

                elif actual[ai] != expected[i]:
                    s_key = actual[ai]
                    or_ks = expected[i]
        else:
            if expected[i] == actual[i]:
                pass
            else:
                if i == 0:
                    if actual[i] == expected[i+1]:
                        q_key = expected[i]
        
                elif i == len(actual):
                    if actual[i] == expected[i-1]:
                        q_key = expected[len(actual) +1]
                
                elif actual[i] == expected[i+1]:
                    q_key = expected[i-1]

                elif actual[i] != expected[i]:
                    s_key = actual[i]
                    or_ks = expected[i]
        count += 1

print(str(or_ks) + ' ' + str(s_key))
if quiet == True:
    print(q_key)
else:
    print('-')

            
