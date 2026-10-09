# CitationChain

CitationChain evaluates whether a research citation supports a claim. Validators independently read the paper, cited source, and DOI metadata, then reach consensus on SUPPORTED, QUALIFIED, or BROKEN with evidence items and source digests.

- Network: GenLayer Studionet
- Contract: $(System.Collections.Hashtable.addr)
- Deployment transaction: $(System.Collections.Hashtable.tx)
- Reviewed source SHA-256: $(System.Collections.Hashtable.sha)
- Contract source: contracts/citation_chain.py

Run 
pm install, 
pm run contract:test, 
pm run contract:lint, and 
pm run build.
