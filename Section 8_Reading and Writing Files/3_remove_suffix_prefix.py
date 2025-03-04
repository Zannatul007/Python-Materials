with open("D:\Python Materials\Reading and Writing Files\jabber.txt","r") as f:
    line = f.readline()

# print(line)
# remove_twas = line.removeprefix("'Twas")#built in function
# print(remove_twas)
# remove_toves = line.removeprefix("toves")#built in function
# print(remove_toves)


def user_remove_prefix(s: str,p:str)->str:
    if s.startswith(p):
        return s[len(p):]
    else:
        return s[:]
    
def user_remove_suffix(string: str, s1: str) -> str:
    if (s1 and string.endswith(s1)):  
        print(len(s1)) 
        return string[:-(len(s1))]  
    else:
        print(len(s1))  
 
remove_twas = user_remove_prefix(line,"'Twas")
print(remove_twas)
remove_toves = user_remove_suffix(line,"es")
print(remove_toves)
