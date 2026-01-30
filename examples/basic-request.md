# ATF – Basic Signed Request Example

This example shows how a client signs a request and how a provider verifies it.

## 1. Original Request

Method: POST  
Path: /api/data  
Body: {"message":"hello"}  
Timestamp: 1700000000  
Nonce: n-12345  

## 2. Canonical Form

The client constructs the canonical representation:

{"method":"POST","path":"/api/data","body_hash":"<sha256>","timestamp":1700000000,"nonce":"n-12345"}

## 3. Signature

The canonical form is signed using the client’s private key (Ed25519).

Signature (hex):
<signature>

## 4. Verification

The provider:
- Recomputes the canonical form
- Verifies the signature
- Checks timestamp freshness
- Confirms nonce has not been reused

Result: ACCEPTED
