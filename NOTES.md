# Teacher Notes & Scratchpad

## User Preferences & System Invariants
- **iCloud Sync**: EVERY TIME any workspace file is updated, ALWAYS run `./scripts/sync_to_icloud.sh` to sync `/Users/jeonkwan/projects/learn_ai/` to `/Users/jeonkwan/Library/Mobile Documents/com~apple~CloudDocs/learn_ai/` so the user can read lessons on iOS devices.
- **Audience & Mindset**: Cloud DevOps engineer. Comfortable with bash, shell scripts, Linux, networking, JSON, curl, GCP infrastructure (GCS, BigQuery, Cloud Run, GKE, IAM). NOT familiar with AI/ML products or AI terminology.
- **Pedagogical Strategy**:
  - Introduce and demystify the **GCP AI product portfolio** explicitly (Vertex AI, Document AI, BigQuery Vector Search, Model Garden, Vertex AI Vector Search) so the user learns the actual cloud services they will deploy and manage.
  - Zero assumed AI knowledge. Every term demystified using computing/DevOps analogies (tokens as packet payloads, embeddings as multidimensional hashes, vector search as spatial indexing, graph edges as pointers).
  - Concrete examples grounded in diverse financial crime investigation domains (Trade-Based Money Laundering, Structuring/Smurfing, Sanctions Evasion via Offshore Shells, Terrorist Financing, Mule Account Rings).
  - Clear structural diagrams alongside text. Minimal targeted code/CLI snippets (`gcloud`, `curl`, JSON payloads, Cypher) strictly to illustrate mechanics.

## Comprehensive 20-Lesson Curriculum Roadmap

### Phase 1: Foundations & The GCP AI Landscape
- **Lesson 0001: The Unstructured Data Dilemma (Vectors vs. Graphs)** [Completed]
- **Lesson 0002: Vector Pipeline Overview** [Completed]
- **Lesson 0003: The Google Cloud AI Ecosystem — A DevOps Guide to Vertex AI & Document AI**  
  *Focus:* Demystifying Google's AI portfolio for a DevOps engineer. Vertex AI umbrella (Model Garden, Endpoints, Vector Search, Search/Agent Builder), Cloud Document AI, BigQuery Vector Search. IAM roles, gcloud CLI commands, and cost/quota architecture.
- **Lesson 0004: The Fundamental Unit of AI — Tokens, Tokenizers & Context Limits**  
  *Focus:* Why LLMs don't read strings; Byte-Pair Encoding (BPE); token pricing on GCP; context window limits; calling the Vertex AI `countTokens` API.

### Phase 2: Ingestion, Parsing & Chunking
- **Lesson 0005: Document Ingestion & Parsing with Cloud Document AI**  
  *Focus:* Why naive text extraction scrambles tables; OCR, Form & Table Processors in GCP Document AI; extracting complex wire transfers, customs invoices, and bank statements without losing geometry.
- **Lesson 0006: Chunking Architectures & Boundary Strategies**  
  *Focus:* Fixed-size vs. Recursive character splitting vs. Document-aware splitting; sliding-window token overlap; parent-child hierarchical chunking; preserving financial entity context.

### Phase 3: Embeddings & Vector Search on GCP
- **Lesson 0007: Embeddings Demystified with Vertex AI text-embedding-004**  
  *Focus:* Projecting semantic meaning into 768/1536 float arrays; mathematical angles of meaning; Cosine vs. Dot Product vs. Euclidean (L2); raw `curl` request to Vertex AI Embeddings API.
- **Lesson 0008: Scalable Vector Indexing — HNSW vs. Google ScaNN**  
  *Focus:* The $O(N)$ brute-force bottleneck; Approximate Nearest Neighbor (ANN); HNSW proximity graphs vs. Google's ScaNN anisotropic quantization.
- **Lesson 0009: Vertex AI Vector Search in Production**  
  *Focus:* Deploying Google's managed vector database. Indexes, Index Endpoints, DeployedIndexes; streaming updates vs. batch GCS updates; VPC peering vs. Public endpoints; RAM sizing and cost per 1M vectors.
- **Lesson 0010: BigQuery Vector Search vs. Dedicated Vector Search**  
  *Focus:* When to use BigQuery's built-in `VECTOR_SEARCH()` SQL function vs. when to use dedicated low-latency Vertex AI Vector Search; batch analytical queries vs. real-time sub-10ms queries.

### Phase 4: Retrieval, Re-ranking & Prompt Assembly
- **Lesson 0011: Retrieval, Metadata Filtering & Cross-Encoder Re-Ranking**  
  *Focus:* Two-stage retrieval funnel; pre-filtering by metadata (jurisdiction, date, entity type); BM25 hybrid search; Cross-Encoder re-rankers separating gold nuggets from false positives.
- **Lesson 0012: Prompt Augmentation, Context Assembly & Gemini on Vertex AI**  
  *Focus:* Assembling the grounded prompt; citation injection; mitigating the "Lost in the Middle" attention curve; system prompt constraints; temperature and deterministic generation with Gemini 1.5.

### Phase 5: Knowledge Graph Pipeline Deep Dives
- **Lesson 0013: Knowledge Graphs & Property Graph Modeling (Nodes, Edges, Properties)**  
  *Focus:* Why relational SQL joins explode on multi-hop paths; Property Graph anatomy: Nodes, Edges, Properties; designing a clean AML graph schema for shell companies and beneficial owners.
- **Lesson 0014: Extracting Graphs from Unstructured Text (NER & Relation Extraction with Gemini)**  
  *Focus:* Information extraction pipeline: Named Entity Recognition (NER) and Relation Extraction; prompting Gemini with structured JSON schema/Pydantic to output deterministic graph triples.
- **Lesson 0015: Entity Resolution & Identity Disambiguation in Graph Data**  
  *Focus:* Resolving aliases and nicknames across disparate files; fuzzy string matching, shared address/tax ID clustering; preventing split nodes and fractured graphs.
- **Lesson 0016: Neo4j on GCP Architecture & Cypher Querying**  
  *Focus:* Deploying Neo4j on GCP (Marketplace, GKE, or Aura); Index-Free Adjacency (pointer chasing); Cypher syntax (`MATCH`, `WHERE`, `RETURN`); writing queries to detect circular money flows and rapid fund dissipation.
- **Lesson 0017: Graph Algorithms for Financial Crime Intelligence**  
  *Focus:* Graph data science algorithms; Centrality & PageRank (identifying central money mules/coordinators); Community Detection / Louvain (uncovering hidden fraud syndicates); Shortest Path analysis.

### Phase 6: Hybrid Retrieval, GraphRAG & Enterprise Operations
- **Lesson 0018: The GraphRAG Paradigm — Local vs. Global Retrieval**  
  *Focus:* Why vector RAG fails on global corpus questions; Microsoft GraphRAG hierarchical community summarization; Local graph hops vs Global community reports for executive compliance audits.
- **Lesson 0019: Hybrid Query Routing & Unified Retrieval Engine**  
  *Focus:* Building the query classifier/router: determining whether a question needs vector similarity, graph traversal, or both; fusing vector snippets and graph subgraphs into a unified prompt context.
- **Lesson 0020: Production GCP Architecture, Security, Evaluation & Compliance**  
  *Focus:* End-to-end cloud blueprint: Cloud Storage -> Eventarc -> Cloud Run / Document AI -> Vertex AI Vector Search + Neo4j Aura on GCP -> BigQuery -> Gemini; VPC Service Controls, IAM least privilege, audit logs & PII scrubbing; automated evaluation using RAGAS (faithfulness, answer relevance).

## Status
- 20-lesson syllabus established and generated.
- Mobile & Tablet Edition generated in `./mobile/` (`mobile/index.html`, `mobile/lessons/`, `mobile/reference/`).
  - 100% self-contained single-file HTML (embedded CSS solves the iOS Files app QuickLook sandbox issue).
  - Fluid typography (`clamp`), Apple system fonts, OLED Dark Mode, and sticky reader navigation bar.
- Synced to iCloud Drive (`~/Library/Mobile Documents/com~apple~CloudDocs/learn_ai`).
