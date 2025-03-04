def simple_hash(s:str)->int:
    base_hash = ord(s[0])
    return base_hash % 10
keys = [""]*20
values = keys.copy()
def get(k:str) -> str:
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


