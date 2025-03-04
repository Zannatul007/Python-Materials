# import better_code
from better_code import square

# area = better_code.square(30)
area =square(30)
print(area)
print("Global namespace are")
namespace = globals().copy()
for key,value in namespace.items():
    print(key,value)