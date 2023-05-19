import hashlib


def singular_method(data: str) -> list[str]:
    result = []

    for s in data.lower():
        result.append((ord(s) - 96) / 100)
    
    return result


def paired_method(data: str) -> list[str]:
    result = []

    for indx in range(0, len(data) - 1):
        digest = hashlib.md5(data[indx:indx + 2].encode('utf8')).hexdigest()
        i = int(digest, 16)
        result.append(i / (10 ** 39))

    return result