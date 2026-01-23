# ATF Overview

ATF provides request-level cryptographic identity for APIs and agents.

Each request is signed by the caller using a private key.
Verifiers validate requests using public keys obtained from trusted sources.

This document describes the core goals and assumptions of the framework.
