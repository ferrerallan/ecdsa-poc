import hashlib
from ecdsa import SigningKey, SECP256k1
from eth_keys import keys
from eth_utils import keccak

# Generate private key (SigningKey) and public key (VerifyingKey)
sk = SigningKey.generate(curve=SECP256k1)
vk = sk.verifying_key

# Convert the private key to the format used by Ethereum
private_key_bytes = sk.to_string()
private_key = keys.PrivateKey(private_key_bytes)

# Derive the public key and Ethereum address
public_key = private_key.public_key
eth_address = public_key.to_checksum_address()

print("Private Key (hex):", private_key)
print("Public Key (hex):", public_key)
print("Ethereum Address:", eth_address)

# Message to be signed (using a hash to simulate a transaction)
message = b"This is an important message in Ethereum."
message_hash = keccak(message)

print("Message Hash:", message_hash.hex())

# Sign the hash of the message with the private key
signature = private_key.sign_msg_hash(message_hash)
print("Signature:", signature)

# Verify the signature with the public key
try:
    public_key.verify_msg_hash(message_hash, signature)
    print("Signature verified successfully!")
except Exception as e:
    print("Signature verification failed:", e)
