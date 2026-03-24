# RAG Poisoning & Retrieval Integrity Dataset

Benign and adversarial document sets for testing vector store integrity controls, retrieval-time redaction, and poisoning detection pipelines.

**Status:** Accepting contributions — this dataset is being built from scratch with the community.

## Scope

Test data designed to evaluate the resilience of Retrieval-Augmented Generation (RAG) systems against data poisoning, unauthorized retrieval, and integrity failures. Aligned primarily with DSGAI04 (Data, Model & Artifact Poisoning), DSGAI05 (Data Integrity & Validation Failures), and DSGAI13 (Vector Store Platform Data Security).

Categories include:

- **Poisoned documents** — Documents containing adversarial content designed to manipulate model behavior when retrieved (e.g., injected instructions, biased content, misleading facts)
- **Integrity test sets** — Baseline "golden" document sets with known-good content for drift and tampering detection
- **Redaction test documents** — Documents containing embedded PII, PHI, credentials, or classified content for testing retrieval-time redaction and filtering controls
- **Cross-tenant retrieval probes** — Query sets designed to test tenant isolation in multi-tenant vector stores (DSGAI11)
- **Embedding inversion test data** — Document-embedding pairs for evaluating reconstruction and inference attack resistance (DSGAI18)

## Data Format

<!-- TODO: Define schema once initial data is contributed -->

Contributions should include:

- **Document ID**
- **Category** — From the list above
- **DSGAI mapping** — Primary DSGAI entry targeted
- **Content** — The document text, or a description if synthetic generation is required
- **Adversarial payload** — For poisoned documents, what the injected content is and what it is designed to trigger
- **Expected retrieval behavior (secure)** — What a properly secured RAG system should do
- **Expected retrieval behavior (vulnerable)** — What an unprotected system would return
- **Metadata** — Any metadata fields relevant to the test (e.g., tenant ID, classification label, access control tags)

## Important

All documents in this dataset must be **synthetic or publicly sourced**. Do not submit real PII, PHI, credentials, or proprietary data — use realistic synthetic equivalents. Poisoned documents should be clearly labeled and must not contain content that could cause harm if accidentally ingested into a production system.

## Contributing

Add documents and test sets as individual files or structured JSON/YAML and submit a pull request. See the [main datasets README](../README.md) for general contribution guidelines.
