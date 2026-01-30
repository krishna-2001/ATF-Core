# reference/python/verify.py

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
import hashlib
import json
import time

MAX_SKEW = 300  # 5 minutes

def canonical_request(req: dict) -> bytes:
    canonical = {
        "method": req["method"],
        "path": req["path"],
        "body_hash": hashlib.sha256(req["body"].encode()).hexdigest(),
        "timestamp": req["timestamp"],
        "nonce": req["nonce"],
    }
    return json.dumps(canonical, separators=(",", ":"), sort_keys=True).encode()

def verify_request(signed: dict, public_key: Ed25519PublicKey) -> bool:
    req = signed["request"]
    signature = bytes.fromhex(signed["signature"])

    # Freshness check
    now = int(time.time())
    if abs(now - req["timestamp"]) > MAX_SKEW:
        return False

    message = canonical_request(req)

    try:
        public_key.verify(signature, message)
        return True
    except Exception:
        return False
