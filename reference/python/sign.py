# reference/python/sign.py

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization
import hashlib
import time
import json
import os

def canonical_request(req: dict) -> bytes:
    """
    Deterministic canonical form of the request.
    Order MUST match the spec.
    """
    canonical = {
        "method": req["method"],
        "path": req["path"],
        "body_hash": hashlib.sha256(req["body"].encode()).hexdigest(),
        "timestamp": req["timestamp"],
        "nonce": req["nonce"],
    }
    return json.dumps(canonical, separators=(",", ":"), sort_keys=True).encode()

def sign_request(req: dict, private_key: Ed25519PrivateKey) -> dict:
    message = canonical_request(req)
    signature = private_key.sign(message)

    return {
        "request": req,
        "signature": signature.hex(),
        "key_id": "example-key-1"
    }

if __name__ == "__main__":
    private_key = Ed25519PrivateKey.generate()

    request = {
        "method": "POST",
        "path": "/api/data",
        "body": '{"data":"hello"}',
        "timestamp": int(time.time()),
        "nonce": os.urandom(8).hex()
    }

    signed = sign_request(request, private_key)
    print(signed)
