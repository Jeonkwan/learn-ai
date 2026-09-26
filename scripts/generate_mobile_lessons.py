#!/usr/bin/env python3
import os
import re
from pathlib import Path

WORKSPACE = Path("/Users/jeonkwan/projects/learn_ai")
LESSONS_DIR = WORKSPACE / "lessons"
REF_DIR = WORKSPACE / "reference"
MOBILE_DIR = WORKSPACE / "mobile"
MOBILE_LESSONS_DIR = MOBILE_DIR / "lessons"
MOBILE_REF_DIR = MOBILE_DIR / "reference"

MOBILE_LESSONS_DIR.mkdir(parents=True, exist_ok=True)
MOBILE_REF_DIR.mkdir(parents=True, exist_ok=True)

MOBILE_CSS = """
:root {
  --bg: #faf9f5;
  --surface: #ffffff;
  --text: #1d1d1f;
  --text-muted: #6e6e73;
  --border: #e5e5ea;
  --accent: #0071e3;
  --accent-light: #e8f2ff;
  --accent-dark: #0056b3;
  --success-bg: #eaf8ee;
  --success-text: #1e7e34;
  --danger-bg: #fdeeee;
  --danger-text: #d93025;
  --code-bg: #f2f2f7;
  --code-border: #e5e5ea;
  --font-serif: -apple-system-ui-serif, "Charter", "New York", Palatino, serif;
  --font-sans: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Segoe UI", system-ui, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #000000;
    --surface: #1c1c1e;
    --text: #f2f2f7;
    --text-muted: #8e8e93;
    --border: #2c2c2e;
    --accent: #2997ff;
    --accent-light: #152942;
    --accent-dark: #58a6ff;
    --success-bg: #142e1b;
    --success-text: #34c759;
    --danger-bg: #321617;
    --danger-text: #ff453a;
    --code-bg: #1c1c1e;
    --code-border: #38383a;
  }
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
}

body {
  background-color: var(--bg);
  color: var(--text);
  font-family: var(--font-serif);
  font-size: clamp(16px, 3.8vw, 18px);
  line-height: 1.65;
  padding: 1rem 1rem 5.5rem;
  max-width: 680px;
  margin: 0 auto;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}

@media (min-width: 768px) {
  body {
    max-width: 760px;
    padding: 2rem 2rem 6.5rem;
  }
}

.mobile-top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 0.75rem;
  margin-bottom: 1.25rem;
  border-bottom: 1px solid var(--border);
  font-family: var(--font-sans);
  font-size: 0.82rem;
  color: var(--text-muted);
}

.mobile-top-bar a {
  color: var(--accent);
  text-decoration: none;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.lesson-meta {
  font-family: var(--font-sans);
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent);
  font-weight: 700;
  margin-bottom: 0.4rem;
}

h1 {
  font-family: var(--font-sans);
  font-size: clamp(1.45rem, 5vw, 2.05rem);
  line-height: 1.22;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--text);
  margin-bottom: 0.5rem;
}

.subtitle {
  font-size: clamp(0.92rem, 3.4vw, 1.05rem);
  color: var(--text-muted);
  font-style: italic;
  margin-bottom: 1.5rem;
  line-height: 1.45;
}

h2 {
  font-family: var(--font-sans);
  font-size: clamp(1.15rem, 3.8vw, 1.4rem);
  font-weight: 600;
  margin: 2rem 0 0.75rem;
  border-bottom: 1px solid var(--border);
  padding-bottom: 0.3rem;
  letter-spacing: -0.01em;
}

h3 {
  font-family: var(--font-sans);
  font-size: clamp(1.02rem, 3.4vw, 1.15rem);
  font-weight: 600;
  margin: 1.4rem 0 0.45rem;
}

p {
  margin-bottom: 1.15rem;
}

ul, ol {
  margin-bottom: 1.25rem;
  padding-left: 1.3rem;
}

li {
  margin-bottom: 0.35rem;
}

code {
  font-family: var(--font-mono);
  font-size: 0.85em;
  background-color: var(--code-bg);
  border: 1px solid var(--code-border);
  padding: 0.15em 0.35em;
  border-radius: 4px;
  word-break: break-word;
}

pre {
  background-color: var(--code-bg);
  border: 1px solid var(--code-border);
  border-radius: 8px;
  padding: 0.9rem;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 1.1rem 0 1.4rem;
  font-family: var(--font-mono);
  font-size: clamp(0.75rem, 2.7vw, 0.84rem);
  line-height: 1.45;
}

pre code {
  background: none;
  border: none;
  padding: 0;
  font-size: inherit;
  word-break: normal;
}

.callout {
  background-color: var(--surface);
  border-left: 4px solid var(--accent);
  border-top: 1px solid var(--border);
  border-right: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  padding: 0.85rem 1rem;
  margin: 1.4rem 0;
  border-radius: 0 8px 8px 0;
}

.callout.tip {
  border-left-color: var(--success-text);
}

.callout.warning {
  border-left-color: #f59e0b;
}

.callout-title {
  font-family: var(--font-sans);
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
  margin-bottom: 0.3rem;
}

.comparison-grid, .service-card-grid, .algo-compare-grid, .algo-grid, .compare-rag-grid, .metric-grid, .scramble-box {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.9rem;
  margin: 1.4rem 0;
}

@media (min-width: 641px) {
  .comparison-grid, .service-card-grid, .algo-compare-grid, .algo-grid, .compare-rag-grid, .metric-grid, .scramble-box {
    grid-template-columns: 1fr 1fr;
  }
}

.grid-col, .service-card, .algo-card, .algo-box, .rag-col, .metric-card, .scramble-col, .math-box {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1rem;
}

.infra-diagram, .hierarchy-box, .funnel-container, .graph-schema-box, .extraction-flow, .er-diagram, .router-diagram, .blueprint-box, .prompt-template-box, .artifact-snippet, .cypher-box {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.9rem;
  margin: 1.25rem 0;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  font-family: var(--font-mono);
  font-size: clamp(0.72rem, 2.5vw, 0.82rem);
  line-height: 1.42;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.25rem 0;
  font-family: var(--font-sans);
  font-size: clamp(0.8rem, 2.8vw, 0.88rem);
  display: block;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

table th, table td {
  border: 1px solid var(--border);
  padding: 0.6rem 0.75rem;
  text-align: left;
}

table th {
  background: var(--code-bg);
  font-weight: 600;
}

.quiz-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1.2rem;
  margin: 1.8rem 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.quiz-badge {
  display: inline-block;
  font-family: var(--font-sans);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 0.2rem 0.5rem;
  border-radius: 999px;
  background: var(--accent-light);
  color: var(--accent);
  margin-bottom: 0.5rem;
}

.quiz-question {
  font-family: var(--font-sans);
  font-size: clamp(0.92rem, 3.6vw, 1.02rem);
  font-weight: 600;
  line-height: 1.4;
  margin-bottom: 0.9rem;
  color: var(--text);
}

.quiz-options {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.quiz-option-btn {
  display: block;
  width: 100%;
  min-height: 48px;
  text-align: left;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.75rem 0.9rem;
  font-family: var(--font-sans);
  font-size: clamp(0.82rem, 3vw, 0.88rem);
  line-height: 1.4;
  color: var(--text);
  cursor: pointer;
  touch-action: manipulation;
  transition: transform 0.1s ease, background 0.15s ease;
}

.quiz-option-btn:active {
  transform: scale(0.98);
}

.quiz-option-btn.selected-correct {
  background: var(--success-bg);
  border-color: var(--success-text);
  color: var(--success-text);
  font-weight: 600;
}

.quiz-option-btn.selected-incorrect {
  background: var(--danger-bg);
  border-color: var(--danger-text);
  color: var(--danger-text);
}

.quiz-feedback {
  display: none;
  font-family: var(--font-sans);
  font-size: 0.86rem;
  padding: 0.8rem 0.9rem;
  border-radius: 8px;
  margin-top: 0.9rem;
  line-height: 1.42;
}

.quiz-feedback.show-correct {
  display: block;
  background: var(--success-bg);
  color: var(--success-text);
}

.quiz-feedback.show-incorrect {
  display: block;
  background: var(--danger-bg);
  color: var(--danger-text);
}

.mobile-bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(250, 249, 245, 0.92);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-top: 1px solid var(--border);
  padding: 0.65rem 1rem max(0.65rem, env(safe-area-inset-bottom));
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.5rem;
  z-index: 1000;
}

@media (prefers-color-scheme: dark) {
  .mobile-bottom-nav {
    background: rgba(18, 18, 20, 0.92);
  }
}

.nav-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 42px;
  padding: 0.4rem 0.8rem;
  border-radius: 8px;
  font-family: var(--font-sans);
  font-size: 0.82rem;
  font-weight: 600;
  text-decoration: none;
  color: var(--text);
  background: var(--surface);
  border: 1px solid var(--border);
  touch-action: manipulation;
}

.nav-btn:active {
  transform: scale(0.96);
}

.nav-btn.primary {
  background: var(--accent);
  color: #ffffff;
  border-color: var(--accent);
}

.nav-btn.disabled {
  opacity: 0.3;
  pointer-events: none;
}
"""

lesson_files = sorted(list(LESSONS_DIR.glob("*.html")))

for i, file_path in enumerate(lesson_files):
    content = file_path.read_text(encoding="utf-8")
    
    # Extract title
    title_match = re.search(r"<title>(.*?)</title>", content)
    title = title_match.group(1) if title_match else "Lesson"
    
    # Extract body content (everything inside <main>...</main>)
    main_match = re.search(r"<main>(.*?)</main>", content, re.DOTALL)
    main_body = main_match.group(1) if main_match else ""
    
    # Extract header content (everything inside <header>...</header>)
    header_match = re.search(r"<header>(.*?)</header>", content, re.DOTALL)
    header_body = header_match.group(1) if header_match else ""
    
    # Extract script content
    script_match = re.search(r"<script>(.*?)</script>", content, re.DOTALL)
    script_body = script_match.group(1) if script_match else ""
    
    # Determine prev and next links
    prev_link = f"{lesson_files[i-1].name}" if i > 0 else "#"
    prev_class = "nav-btn" if i > 0 else "nav-btn disabled"
    
    next_link = f"{lesson_files[i+1].name}" if i < len(lesson_files) - 1 else "#"
    next_class = "nav-btn primary" if i < len(lesson_files) - 1 else "nav-btn disabled"
    
    lesson_num_str = f"{i+1:02d}"
    
    mobile_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{title}</title>
  <style>
{MOBILE_CSS}
  </style>
</head>
<body>
  <div class="mobile-top-bar">
    <a href="../index.html">&larr; Course Index</a>
    <span>Lesson {lesson_num_str} of {len(lesson_files)}</span>
  </div>

  <header>
    {header_body}
  </header>

  <main>
    {main_body}
  </main>

  <div class="mobile-bottom-nav">
    <a class="{prev_class}" href="{prev_link}">&larr; Prev</a>
    <a class="nav-btn" href="../index.html">📚 Index</a>
    <a class="{next_class}" href="{next_link}">Next &rarr;</a>
  </div>

  <script>
{script_body}
  </script>
</body>
</html>
"""
    # Replace relative link paths to stay within mobile directory
    mobile_html = mobile_html.replace('href="../reference/', 'href="../reference/')
    mobile_html = mobile_html.replace('href="reference/', 'href="../reference/')
    
    target_path = MOBILE_LESSONS_DIR / file_path.name
    target_path.write_text(mobile_html, encoding="utf-8")
    print(f"Generated mobile lesson: {target_path.name}")

# Now generate mobile reference sheets
ref_files = sorted(list(REF_DIR.glob("*.html")))
for file_path in ref_files:
    content = file_path.read_text(encoding="utf-8")
    title_match = re.search(r"<title>(.*?)</title>", content)
    title = title_match.group(1) if title_match else "Reference"
    
    main_match = re.search(r"<main>(.*?)</main>", content, re.DOTALL)
    main_body = main_match.group(1) if main_match else ""
    
    header_match = re.search(r"<header>(.*?)</header>", content, re.DOTALL)
    header_body = header_match.group(1) if header_match else ""
    
    mobile_ref_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{title}</title>
  <style>
{MOBILE_CSS}
  </style>
</head>
<body>
  <div class="mobile-top-bar">
    <a href="../index.html">&larr; Course Index</a>
    <span>Reference Document</span>
  </div>

  <header>
    {header_body}
  </header>

  <main>
    {main_body}
  </main>

  <div class="mobile-bottom-nav">
    <a class="nav-btn" href="../index.html">&larr; Back to Dashboard</a>
    <a class="nav-btn primary" href="../lessons/0001-unstructured-data-vectors-vs-graphs.html">Start Course &rarr;</a>
  </div>
</body>
</html>
"""
    mobile_ref_html = mobile_ref_html.replace('href="../lessons/', 'href="../lessons/')
    target_path = MOBILE_REF_DIR / file_path.name
    target_path.write_text(mobile_ref_html, encoding="utf-8")
    print(f"Generated mobile reference: {target_path.name}")

# Now generate mobile index.html
mobile_index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>AI & Knowledge Retrieval Masterclass (Mobile Edition)</title>
  <style>
{MOBILE_CSS}
.course-card {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 0.9rem 1rem;
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  text-decoration: none;
  color: var(--text);
  touch-action: manipulation;
  transition: transform 0.1s ease, border-color 0.15s ease;
}}
.course-card:active {{
  transform: scale(0.98);
  border-color: var(--accent);
}}
.card-left {{
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}}
.card-num {{
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--accent);
  text-transform: uppercase;
}}
.card-title {{
  font-family: var(--font-sans);
  font-size: 0.95rem;
  font-weight: 600;
  line-height: 1.35;
}}
.card-arrow {{
  color: var(--text-muted);
  font-size: 1.1rem;
  margin-left: 0.5rem;
}}
.phase-header {{
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin: 1.75rem 0 0.65rem;
}}
.ref-pill-grid {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.6rem;
  margin-bottom: 1.5rem;
}}
@media (min-width: 500px) {{
  .ref-pill-grid {{
    grid-template-columns: 1fr 1fr;
  }}
}}
.ref-pill {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.7rem 0.85rem;
  text-decoration: none;
  color: var(--text);
  font-family: var(--font-sans);
  font-size: 0.82rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}}
</style>
</head>
<body>
  <header>
    <div class="lesson-meta">Mobile & Tablet Edition</div>
    <h1>AI & Retrieval Masterclass</h1>
    <div class="subtitle">Optimized for iPhone, iPad, and offline reading in the iOS Files app.</div>
  </header>

  <main>
    <div class="phase-header">Reference Cheat Sheets</div>
    <div class="ref-pill-grid">
      <a class="ref-pill" href="reference/glossary.html">📖 Core Glossary</a>
      <a class="ref-pill" href="reference/vector-chunking-and-indexing.html">📐 Vector Architecture</a>
      <a class="ref-pill" href="reference/gcp-ai-products-cheatsheet.html">☁️ GCP Services Sheet</a>
      <a class="ref-pill" href="reference/cypher-graph-modeling-cheatsheet.html">🕸️ Cypher Graph Sheet</a>
    </div>

    <div class="phase-header">Phase 1: Foundations & GCP AI</div>
    <a class="course-card" href="lessons/0001-unstructured-data-vectors-vs-graphs.html">
      <div class="card-left"><span class="card-num">Lesson 01</span><span class="card-title">Vectors vs. Knowledge Graphs</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
    <a class="course-card" href="lessons/0002-vector-pipeline-chunking-embeddings-ann.html">
      <div class="card-left"><span class="card-num">Lesson 02</span><span class="card-title">The Vector Pipeline Overview</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
    <a class="course-card" href="lessons/0003-gcp-ai-ecosystem-devops-guide.html">
      <div class="card-left"><span class="card-num">Lesson 03</span><span class="card-title">The Google Cloud AI Ecosystem</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
    <a class="course-card" href="lessons/0004-fundamental-unit-tokens-tokenizers-context.html">
      <div class="card-left"><span class="card-num">Lesson 04</span><span class="card-title">Tokens, BPE & Context Limits</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>

    <div class="phase-header">Phase 2: Ingestion & Parsing</div>
    <a class="course-card" href="lessons/0005-document-ingestion-parsing-document-ai.html">
      <div class="card-left"><span class="card-num">Lesson 05</span><span class="card-title">Document Parsing with Document AI</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
    <a class="course-card" href="lessons/0006-chunking-architectures-boundary-strategies.html">
      <div class="card-left"><span class="card-num">Lesson 06</span><span class="card-title">Chunking & Boundary Strategies</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>

    <div class="phase-header">Phase 3: Embeddings & Vector Search</div>
    <a class="course-card" href="lessons/0007-embeddings-demystified-vertex-ai.html">
      <div class="card-left"><span class="card-num">Lesson 07</span><span class="card-title">Embeddings Demystified</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
    <a class="course-card" href="lessons/0008-scalable-vector-indexing-hnsw-scann.html">
      <div class="card-left"><span class="card-num">Lesson 08</span><span class="card-title">Scalable Indexing: HNSW vs. ScaNN</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
    <a class="course-card" href="lessons/0009-vertex-ai-vector-search-in-production.html">
      <div class="card-left"><span class="card-num">Lesson 09</span><span class="card-title">Vertex AI Vector Search in Prod</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
    <a class="course-card" href="lessons/0010-bigquery-vector-search-vs-dedicated.html">
      <div class="card-left"><span class="card-num">Lesson 10</span><span class="card-title">BigQuery vs. Dedicated Vector Search</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>

    <div class="phase-header">Phase 4: Retrieval & Grounding</div>
    <a class="course-card" href="lessons/0011-retrieval-metadata-filtering-reranking.html">
      <div class="card-left"><span class="card-num">Lesson 11</span><span class="card-title">Filtering & Cross-Encoder Re-Ranking</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
    <a class="course-card" href="lessons/0012-prompt-augmentation-context-assembly-gemini.html">
      <div class="card-left"><span class="card-num">Lesson 12</span><span class="card-title">Prompt Assembly & Hallucination Defense</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>

    <div class="phase-header">Phase 5: Knowledge Graphs (Neo4j)</div>
    <a class="course-card" href="lessons/0013-knowledge-graphs-property-graph-modeling.html">
      <div class="card-left"><span class="card-num">Lesson 13</span><span class="card-title">Property Graph Modeling for AML</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
    <a class="course-card" href="lessons/0014-extracting-graphs-from-unstructured-text-gemini.html">
      <div class="card-left"><span class="card-num">Lesson 14</span><span class="card-title">Extracting Graphs with Gemini</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
    <a class="course-card" href="lessons/0015-entity-resolution-identity-disambiguation.html">
      <div class="card-left"><span class="card-num">Lesson 15</span><span class="card-title">Entity Resolution & Disambiguation</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
    <a class="course-card" href="lessons/0016-neo4j-gcp-architecture-cypher-querying.html">
      <div class="card-left"><span class="card-num">Lesson 16</span><span class="card-title">Neo4j on GCP & Cypher Querying</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
    <a class="course-card" href="lessons/0017-graph-algorithms-financial-crime-intelligence.html">
      <div class="card-left"><span class="card-num">Lesson 17</span><span class="card-title">Graph Algorithms & Community Detection</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>

    <div class="phase-header">Phase 6: GraphRAG & Cloud Operations</div>
    <a class="course-card" href="lessons/0018-graphrag-paradigm-local-vs-global.html">
      <div class="card-left"><span class="card-num">Lesson 18</span><span class="card-title">GraphRAG: Local vs. Global</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
    <a class="course-card" href="lessons/0019-hybrid-query-routing-unified-retrieval.html">
      <div class="card-left"><span class="card-num">Lesson 19</span><span class="card-title">Hybrid Query Routing Engine</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
    <a class="course-card" href="lessons/0020-production-gcp-architecture-security-compliance.html">
      <div class="card-left"><span class="card-num">Lesson 20</span><span class="card-title">Production GCP Blueprint & VPC-SC</span></div>
      <span class="card-arrow">&rsaquo;</span>
    </a>
  </main>
</body>
</html>
"""
(MOBILE_DIR / "index.html").write_text(mobile_index_html, encoding="utf-8")
print("Generated mobile/index.html dashboard!")
