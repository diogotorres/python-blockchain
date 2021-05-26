import hashlib
import json


def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments
    """
    
    # convert every arg into a string
    stringfiedargs = sorted(map(lambda data: json.dumps(data), args))

    #generate a single string with all args
    joined_data = ''.join(stringfiedargs)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()


def main():
    print(f"crypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")

    # should generate the same hash besides the order
    print(f"crypto_hash(2, 'one', [3]): {crypto_hash(2, 'one', [3])}")


if __name__ == '__main__':
    main()