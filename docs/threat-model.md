# Threat Model

## Assumed Adversary
- Can observe, replay, and modify network traffic
- Does not control client private keys

## Protections
- Prevents request forgery without private key
- Limits replay through timestamp and nonce

## Out of Scope
- Endpoint compromise
- Denial-of-service
- Physical attacks

## Failure Assumptions
- Verification fails closed
- Stale or missing data causes rejection
