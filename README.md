# CitationChain

CitationChain is a GenLayer Intelligent Contract for verifying the identity of an academic work across DOI metadata and a publisher page. An owner registers an expected title, year, normalized DOI, and two HTTPS sources on distinct hosts. Validators independently fetch both sources and compare title, authors, year, and DOI. The receipt stores `VERIFIED`, `MISMATCH`, or `UNAVAILABLE`, normalized identity fields, mismatches, and both source digests.

Lifecycle: `OPEN` -> `VERIFIED` or `REVIEWED`. A deterministic policy guard prevents a `VERIFIED` receipt from bypassing the registered identity. Duplicate IDs, same-host sources, malformed DOI values, unavailable pages, and validator disagreement fail closed.

Studionet contract: `0x79F212bAc64bb8AAD79d703bc9535F87ea5df81d`
Deployment transaction: `0x8be530f3b3380fe77ed13ecbe16002ea69d1819fce1b674c77f99f2164872a68`
Source SHA-256: `79299956b690bbd9e06202834174dd69f5b7ea283fa62e532a5ddf66783335fa`

Tests: `python -m pytest test_citation_chain.py -q`
Lint: `PYTHONUTF8=1 genvm-lint citation_chain.py`
