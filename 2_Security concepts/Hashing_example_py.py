import hashlib

# clear text
text = "hello world"

# use SHA-256
hash_object = hashlib.sha256(text.encode())
hash_value = hash_object.hexdigest()

print(f"Hash value for '{text}': {hash_value}")
