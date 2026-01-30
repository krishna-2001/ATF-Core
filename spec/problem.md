# Problem Statement

## What ATF Solves
ATF provides request-level cryptographic identity for APIs and agents.
Each request can be verified independently to determine who authored it.

## What ATF Does Not Solve
ATF does not replace HTTPS, mTLS, or authorization systems.
It does not prevent endpoint compromise or denial-of-service attacks.

## Why Existing Solutions Fall Short
- API keys and bearer tokens can be copied and replayed.
- OAuth relies on centralized token issuers and opaque revocation.
- mTLS authenticates connections, not individual requests.
