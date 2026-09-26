# Architecting Unstructured Data & Knowledge Retrieval for LLMs

[![GitHub Pages](https://github.com/Jeonkwan/learn-ai/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/Jeonkwan/learn-ai/actions/workflows/deploy-pages.yml)
[![GitHub release](https://img.shields.io/github/v/release/Jeonkwan/learn-ai?include_prereleases&style=flat-square)](https://github.com/Jeonkwan/learn-ai/releases)
[![Curriculum](https://img.shields.io/badge/curriculum-20%20Lessons%20%2B%204%20Refs-blue?style=flat-square)](#curriculum-roadmap)
[![Target Platform](https://img.shields.io/badge/GCP-Vertex%20AI%20%7C%20BigQuery%20%7C%20Neo4j-4285F4?style=flat-square)](#overview)

> **A Systems Engineering and DevOps Guide to Vectors, Embeddings, RAG, Neo4j Property Graphs, GraphRAG, and Google Cloud AI Architecture.**

---

## 🌐 Live Interactive Links

- 🖥️ **[Curriculum Web Portal (Desktop Edition)](https://jeonkwan.github.io/learn-ai/)**
- 📱 **[Mobile & Tablet Single-File Edition](https://jeonkwan.github.io/learn-ai/mobile/index.html)** — Optimized for touch devices, iOS Files Quick Look, and dark mode.

---

## 🧭 Overview

This curriculum equips engineers with the deep architectural intuition needed to evaluate, design, deploy, and operate unstructured data retrieval pipelines for Large Language Models.

Rather than treating AI services as black boxes or focusing on toy Python snippets, this curriculum analyzes real system mechanics:
- **Vector Ingestion & Retrieval Pipeline**: Chunking boundaries, token mechanics, embedding math, approximate nearest neighbors (HNSW vs. Google ScaNN), and Vertex AI Vector Search sizing.
- **Relational & Graph Data Models**: Why vector similarity fails on multi-hop joined queries; property graphs (Neo4j), Cypher querying, and extracting knowledge triples using Gemini 1.5.
- **Hybrid Retrieval & GraphRAG**: Microsoft GraphRAG hierarchical community detection (Leiden), local vs. global query routing, and reciprocal rank fusion.
- **Domain Grounding**: All systems and patterns are illustrated using real-world **Financial Crime / AML (Anti-Money Laundering)** scenarios: SAR narratives, shell company networks, circular wire transfers, and trade-based money laundering.

---

## 📚 Curriculum Roadmap

### Phase 1: Foundations & The GCP AI Landscape
- **[Lesson 0001: The Unstructured Data Dilemma — Vectors vs. Knowledge Graphs](lessons/0001-unstructured-data-vectors-vs-graphs.html)**  
  Semantic similarity vs. multi-hop topological joins; spatial proximity vs. pointer chasing.
- **[Lesson 0002: The Vector Pipeline — From Raw Narrative to 3ms Retrieval](lessons/0002-vector-pipeline-chunking-embeddings-ann.html)**  
  End-to-end data lifecycle: Document AI &rarr; Chunking &rarr; Embeddings &rarr; Vector Index &rarr; Bi-Encoder query &rarr; Cross-Encoder re-ranker.
- **[Lesson 0003: The Google Cloud AI Ecosystem — A DevOps Guide](lessons/0003-gcp-ai-ecosystem-devops-guide.html)**  
  Demystifying GCP AI: Vertex AI, Model Garden, Document AI, BigQuery Vector Search, IAM roles, and CLI commands.
- **[Lesson 0004: The Fundamental Unit of AI — Tokens, Tokenizers & Context Limits](lessons/0004-fundamental-unit-tokens-tokenizers-context.html)**  
  Byte-Pair Encoding (BPE), token pricing, context window budgeting, and calling Vertex AI's `countTokens` API.

### Phase 2: Ingestion, Parsing & Chunking
- **[Lesson 0005: Document Ingestion & Parsing with Cloud Document AI](lessons/0005-document-ingestion-parsing-document-ai.html)**  
  OCR, Form Processors, and Table extraction; parsing complex financial statements and wire transfers without losing spatial geometry.
- **[Lesson 0006: Chunking Architectures & Boundary Strategies](lessons/0006-chunking-architectures-boundary-strategies.html)**  
  Fixed vs. recursive vs. document-aware splitting; sliding-window token overlap; parent-child hierarchical chunking.

### Phase 3: Embeddings & Vector Search on GCP
- **[Lesson 0007: Embeddings Demystified with Vertex AI text-embedding-004](lessons/0007-embeddings-demystified-vertex-ai.html)**  
  Projecting meaning into 768-dim float arrays; Cosine vs. Dot Product vs. L2 distance; raw curl calls to Vertex AI.
- **[Lesson 0008: Scalable Vector Indexing — HNSW vs. Google ScaNN](lessons/0008-scalable-vector-indexing-hnsw-scann.html)**  
  The $O(N)$ brute-force bottleneck; Approximate Nearest Neighbor (ANN) trade-offs; HNSW graphs vs. ScaNN anisotropic vector quantization.
- **[Lesson 0009: Vertex AI Vector Search in Production](lessons/0009-vertex-ai-vector-search-in-production.html)**  
  Indexes, Endpoints, and DeployedIndexes; streaming vs. batch updates; VPC peering vs. Public endpoints; RAM sizing and cost estimation.
- **[Lesson 0010: BigQuery Vector Search vs. Dedicated Vector Search](lessons/0010-bigquery-vector-search-vs-dedicated.html)**  
  When to use BigQuery's `VECTOR_SEARCH()` SQL function vs. sub-10ms dedicated Vertex AI Vector Search.

### Phase 4: Retrieval, Re-Ranking & Prompt Assembly
- **[Lesson 0011: Retrieval, Metadata Filtering & Cross-Encoder Re-Ranking](lessons/0011-retrieval-metadata-filtering-reranking.html)**  
  Two-stage retrieval funnel; pre-filtering by metadata; BM25 hybrid search; Cross-Encoder re-rankers.
- **[Lesson 0012: Prompt Augmentation, Context Assembly & Gemini on Vertex AI](lessons/0012-prompt-augmentation-context-assembly-gemini.html)**  
  Assembling grounded prompts; citation injection; mitigating the "Lost in the Middle" attention curve; deterministic parameter tuning.

### Phase 5: Knowledge Graph Pipeline Deep Dives
- **[Lesson 0013: Knowledge Graphs & Property Graph Modeling](lessons/0013-knowledge-graphs-property-graph-modeling.html)**  
  Why relational joins explode on multi-hop queries; Property Graph anatomy (Nodes, Edges, Properties); AML schema design.
- **[Lesson 0014: Extracting Graphs from Unstructured Text with Gemini](lessons/0014-extracting-graphs-from-unstructured-text-gemini.html)**  
  Information extraction pipeline: Named Entity Recognition (NER) & Relation Extraction using structured JSON schema.
- **[Lesson 0015: Entity Resolution & Identity Disambiguation in Graph Data](lessons/0015-entity-resolution-identity-disambiguation.html)**  
  Deduplicating entities across disparate records; fuzzy string matching, shared address/tax ID clustering, and connected components.
- **[Lesson 0016: Neo4j on GCP Architecture & Cypher Querying](lessons/0016-neo4j-gcp-architecture-cypher-querying.html)**  
  Deploying Neo4j on GCP; index-free adjacency; Cypher querying to detect circular wire flows and nominee networks.
- **[Lesson 0017: Graph Algorithms for Financial Crime Intelligence](lessons/0017-graph-algorithms-financial-crime-intelligence.html)**  
  Graph Data Science algorithms; PageRank & Degree Centrality (identifying ringleaders); Louvain / WCC (community fraud clusters).

### Phase 6: Hybrid Retrieval, GraphRAG & Enterprise Operations
- **[Lesson 0018: The GraphRAG Paradigm — Local vs. Global Retrieval](lessons/0018-graphrag-paradigm-local-vs-global-retrieval.html)**  
  Why standard RAG fails on global corpus questions; Microsoft GraphRAG hierarchical community summarization.
- **[Lesson 0019: Hybrid Query Routing & Unified Retrieval Engine](lessons/0019-hybrid-query-routing-unified-retrieval-engine.html)**  
  Building intelligent query routers: classifying vector vs. graph vs. hybrid questions; prompt synthesis with Reciprocal Rank Fusion (RRF).
- **[Lesson 0020: Day-2 DevOps, Evaluation, Cost Optimization & Security](lessons/0020-day2-devops-evaluation-cost-security.html)**  
  RAG Triad evaluation (Faithfulness, Answer Relevance, Context Recall); cache tiers; prompt injection defense; RBAC & column-level security.

---

## 📖 Reference Architecture Guides

| Reference Document | Topic |
|---|---|
| **[REF 01: Core Terminology Glossary](reference/glossary.html)** | Authoritative definitions of 40+ vector, embedding, LLM, and graph concepts. |
| **[REF 02: Vector Chunking & Indexing Architecture Sheet](reference/vector-chunking-and-indexing.html)** | Decision matrices for chunk sizes, overlap, distance metrics, and index algorithms. |
| **[REF 03: Google Cloud AI & Data Services Cheat Sheet](reference/gcp-ai-products-cheatsheet.html)** | CLI reference, API calls, pricing tiers, and IAM roles for GCP AI services. |
| **[REF 04: Cypher & Knowledge Graph Modeling Cheat Sheet](reference/cypher-graph-modeling-cheatsheet.html)** | Cypher syntax reference, query templates, index tuning, and AML graph schema patterns. |

---

## 💻 Local Development & Usage

Clone the repository and serve locally:

```bash
git clone https://github.com/Jeonkwan/learn-ai.git
cd learn-ai

# Start a local static file server
python3 -m http.server 8000
```

Then visit [http://localhost:8000](http://localhost:8000) in your web browser.

### Scripts
- `scripts/generate_mobile_lessons.py`: Generates the standalone, single-file offline mobile edition with embedded CSS.
- `scripts/publish_release.sh`: Tags and publishes a new versioned release to GitHub via the `gh` CLI.
- `scripts/sync_to_icloud.sh`: Synchronizes workspace files to local iCloud Drive for mobile offline reading.

---

## 🚀 CI/CD & GitHub Pages

- **GitHub Pages Workflow** (`.github/workflows/deploy-pages.yml`): Automatically deploys any push to the `main` branch directly to GitHub Pages.
- **GitHub Release Workflow** (`.github/workflows/release.yml`): Automatically packages and publishes a downloadable zip archive when a git tag (e.g. `v1.0.0`) is pushed.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
