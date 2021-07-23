import base64, M2Crypto

def generate_session_id(num_bytes=16):
    return base64.b64encode(M2Crypto.m2.rand_bytes(num_bytes))

print(generate_session_id()) 
print(generate_session_id(24))
