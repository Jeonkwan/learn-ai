# Unstructured Data & Retrieval for LLMs Resources

## Knowledge

- [Paper: _Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks_ — Lewis et al. (Facebook AI / NeurIPS 2020)](https://arxiv.org/abs/2005.11401)
  The foundational paper that coined RAG. Use for: understanding why parametric LLM memory fails on proprietary data and how retrieval acts as external working memory.
- [Paper: _From Local to Global: A Graph RAG Approach to Query-Focused Summarization_ — Edge et al. (Microsoft Research 2024)](https://arxiv.org/abs/2404.16130)
  Defines GraphRAG and community summarization. Use for: understanding why vector RAG fails on multi-hop entity reasoning across large corpora and how knowledge graphs solve global synthesis.
- [Documentation: Google Cloud Vertex AI Vector Search Architecture](https://cloud.google.com/vertex-ai/docs/vector-search/overview)
  Enterprise vector indexing (ScaNN algorithm). Use for: understanding vector serving, scaling, latency trade-offs, and deployment on GCP.
- [Book & Guide: _Building Knowledge Graphs: A Practitioner's Guide_ — Neo4j Press](https://neo4j.com/developer/graph-database/)
  Practical property graph modeling. Use for: translating unstructured entity extractions (People, Accounts, Transactions) into Cypher property graphs.
- [Survey: _Retrieval-Augmented Generation for Large Language Models: A Survey_ — Gao et al. (2023)](https://arxiv.org/abs/2312.10997)
  Systematic breakdown of Naive RAG, Advanced RAG, and Modular RAG architectures. Use for: chunking, reranking, hybrid search, and evaluation metrics (RAGAS).

## Wisdom (Communities)

- [Reddit: r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)
  Practitioner community testing real-world RAG pipelines, chunking strategies, embeddings benchmarks, and quantization. Use for: pragmatic trade-offs and battle-tested advice.
- [Neo4j Community & Discord](https://community.neo4j.com)
  Graph database engineers and knowledge graph specialists. Use for: Cypher query optimization, GraphRAG schema design, and entity linking debugging.
- [Google Cloud Community - AI & Machine Learning](https://www.googlecloudcommunity.com/gc/AI-ML/bd-p/cloud-ai-ml)
  GCP engineers discussing Vertex AI Search, Cloud Storage ingestion pipelines, and Vector Search operations. Use for: GCP-specific deployment patterns and troubleshooting.
