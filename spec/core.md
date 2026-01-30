# ATF Core Protocol

## Request Envelope
- Method
- Path
- Selected headers
- Body hash
- Timestamp
- Nonce
- Key ID

## Canonicalization
Define exact field order, encoding, and formatting.

## Signing
- Algorithm: Ed25519
- Input: canonical request string

## Freshness
- Timestamp validity window
- Nonce replay rules

## Verification
- Validate signature
- Check timestamp
- Check nonce
- Accept or reject
