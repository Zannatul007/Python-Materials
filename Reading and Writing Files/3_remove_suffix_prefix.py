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
    
def user_remove_suffix(s: str,s1:str)->str:
    if s1 and s.endswith(s1):
        return s[:-len(s1)]
    else:
        return s[:]
    
remove_twas = user_remove_prefix(line,"'Twas")
print(remove_twas)
remove_toves = user_remove_suffix(line,"toves")
print(remove_toves)
