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

/* Modern Responsive Architecture Diagram */
.gcp-arch-diagram {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1rem 0.8rem;
  margin: 1.5rem 0;
}
.arch-layer {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 0.9rem 0.8rem;
}
.layer-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.8rem;
}
.layer-badge {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  background: var(--accent-light);
  color: var(--accent);
  border: 1px solid var(--border);
}
.layer-header h4 {
  margin: 0;
  font-family: var(--font-sans);
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--text);
}
.layer-flow {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}
@media (min-width: 600px) {
  .layer-flow {
    flex-direction: row;
    align-items: center;
  }
}
.arch-node {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.75rem 0.85rem;
  display: flex;
  gap: 0.6rem;
  align-items: flex-start;
}
.arch-node.highlight {
  border-color: var(--accent);
}
.arch-node.wide {
  width: 100%;
}
.arch-node.final {
  border-color: #8b5cf6;
}
.node-icon {
  font-size: 1.25rem;
  line-height: 1;
  flex-shrink: 0;
}
.node-content {
  flex: 1;
  min-width: 0;
}
.node-content strong {
  display: block;
  font-family: var(--font-sans);
  font-size: 0.88rem;
  color: var(--text);
  margin-bottom: 0.15rem;
}
.node-content code {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--accent);
}
.node-content p {
  margin: 0.3rem 0 0;
  font-family: var(--font-sans);
  font-size: 0.8rem;
  line-height: 1.35;
  color: var(--text-muted);
}
.tech-tag {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 600;
  color: var(--success-text);
  background: var(--success-bg);
  padding: 0.1rem 0.35rem;
  border-radius: 3px;
}
.flow-arrow {
  text-align: center;
  font-size: 1.2rem;
  color: var(--text-muted);
  font-weight: 700;
}
@media (max-width: 599px) {
  .flow-arrow {
    transform: rotate(90deg);
  }
}
.layer-connector {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.5rem 0;
  color: var(--text-muted);
}
.connector-arrow {
  font-size: 1.15rem;
  line-height: 1;
  color: var(--accent);
  font-weight: bold;
}
.connector-label {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  margin-top: 0.15rem;
  color: var(--text-muted);
  text-align: center;
}
.layer-top-node {
  margin-bottom: 0.75rem;
}
.layer-fork-label {
  font-family: var(--font-sans);
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-muted);
  margin: 0.65rem 0 0.45rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.layer-branches {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.75rem;
}
@media (min-width: 600px) {
  .layer-branches {
    grid-template-columns: 1fr 1fr;
  }
}
.branch-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.75rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.branch-header {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  margin-bottom: 0.35rem;
}
.branch-header strong {
  font-family: var(--font-sans);
  font-size: 0.85rem;
  color: var(--text);
}
.branch-badge {
  display: inline-block;
  align-self: flex-start;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  padding: 0.1rem 0.35rem;
  border-radius: 3px;
}
.branch-badge.live {
  background: var(--accent-light);
  color: var(--accent);
}
.branch-badge.batch {
  background: #fef7e0;
  color: #b06000;
}
@media (prefers-color-scheme: dark) {
  .branch-badge.batch {
    background: #3e2e0e;
    color: #f9ab00;
  }
}
.branch-desc {
  font-family: var(--font-sans);
  font-size: 0.8rem;
  line-height: 1.35;
  color: var(--text-muted);
  margin: 0 0 0.5rem;
}
.branch-specs {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
  font-family: var(--font-sans);
  font-size: 0.72rem;
  color: var(--text-muted);
  border-top: 1px dashed var(--border);
  padding-top: 0.45rem;
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

/* ==========================================================================
   Diagrams Styles for Mobile Lessons
   ========================================================================== */
.resource-hierarchy, .retrieval-funnel, .property-graph-chain,
.knowledge-extraction-visual, .er-pipeline-visual, .router-pipeline-visual,
.gcp-blueprint-visual {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1rem 0.8rem;
  margin: 1.5rem 0;
}

/* Lesson 0009: 3-Tier Resource Hierarchy */
.tier-card {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 0.9rem 0.85rem;
  position: relative;
}
.tier-card.tier-1 { border-left: 4px solid var(--accent); }
.tier-card.tier-2 { border-left: 4px solid #8b5cf6; }
.tier-card.tier-3 { border-left: 4px solid #10b981; }

.tier-badge {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  margin-bottom: 0.5rem;
}
.tier-1 .tier-badge { background: var(--accent-light); color: var(--accent); }
.tier-2 .tier-badge { background: #f3e8ff; color: #7c3aed; }
.tier-3 .tier-badge { background: #d1fae5; color: #047857; }

.tier-header {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  margin-bottom: 0.4rem;
}
.tier-icon {
  font-size: 1.4rem;
  line-height: 1;
}
.tier-header h4 {
  margin: 0;
  font-family: var(--font-sans);
  font-size: 0.95rem;
  color: var(--text);
}
.tier-header code {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--accent);
}
.tier-card p {
  margin: 0.35rem 0;
  font-family: var(--font-sans);
  font-size: 0.82rem;
  color: var(--text);
  line-height: 1.4;
}
.tier-note {
  font-family: var(--font-sans);
  font-size: 0.75rem;
  color: var(--text-muted);
  font-style: italic;
}
.tier-specs {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
  margin-top: 0.65rem;
  padding-top: 0.5rem;
  border-top: 1px dashed var(--border);
}
.tier-specs span {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--text-muted);
}
.tier-connector {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.5rem 0;
}
.connector-badge {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--text-muted);
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 0.15rem 0.5rem;
  border-radius: 12px;
  text-align: center;
}
.connector-arrow {
  color: var(--accent);
  font-size: 1.15rem;
  font-weight: bold;
  line-height: 1;
  margin-top: 0.15rem;
}

/* Lesson 0011: Funnel */
.funnel-tier {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 0.85rem 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}
.funnel-tier.level-corpus { border-left: 4px solid #64748b; }
.funnel-tier.level-candidates { border-left: 4px solid #f59e0b; }
.funnel-tier.level-gold { border-left: 4px solid #10b981; background: #f0fdf4; }
.funnel-count {
  font-family: var(--font-mono);
  font-size: 1.25rem;
  font-weight: 800;
}
.level-corpus .funnel-count { color: #64748b; }
.level-candidates .funnel-count { color: #d97706; }
.level-gold .funnel-count { color: #059669; }
.funnel-info strong {
  display: block;
  font-family: var(--font-sans);
  font-size: 0.88rem;
  color: var(--text);
}
.funnel-info span {
  font-family: var(--font-sans);
  font-size: 0.78rem;
  color: var(--text-muted);
}
.funnel-divider {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  padding: 0.5rem 0;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--text-muted);
  text-align: center;
}
.divider-icon {
  color: var(--accent);
  font-size: 1.1rem;
  font-weight: bold;
}
.funnel-stage-box {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
  margin: 0.4rem 0;
}
.stage-subcard {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.75rem 0.85rem;
}
.stage-subcard.highlight {
  border-color: #f59e0b;
  background: #fffbeb;
}
.stage-tag {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  padding: 0.1rem 0.35rem;
  border-radius: 4px;
  background: #e2e8f0;
  color: #475569;
  margin-bottom: 0.25rem;
}
.stage-tag.deep { background: #fef3c7; color: #b45309; }
.stage-subcard h4 {
  margin: 0 0 0.2rem;
  font-family: var(--font-sans);
  font-size: 0.86rem;
  color: var(--text);
}
.stage-subcard p {
  margin: 0;
  font-family: var(--font-sans);
  font-size: 0.78rem;
  color: var(--text-muted);
  line-height: 1.35;
}
.stage-plus {
  text-align: center;
  font-weight: bold;
  font-size: 1.1rem;
  color: var(--text-muted);
}

/* Lesson 0013: Property Graph Chain */
.graph-chain-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.graph-node-chip {
  width: 100%;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 0.75rem 0.85rem;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}
.node-label-pill {
  display: inline-block;
  align-self: flex-start;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}
.node-label-pill.person { background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }
.node-label-pill.company { background: #fef3c7; color: #b45309; border: 1px solid #fde68a; }
.node-label-pill.account { background: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; }
.node-label-pill.account-frozen { background: #fee2e2; color: #b91c1c; border: 1px solid #fecaca; }
.node-properties {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  font-family: var(--font-mono);
  font-size: 0.74rem;
}
.prop-item { color: var(--text-muted); }
.prop-item strong { color: var(--text); }
.graph-edge-connector {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.6rem 0;
}
.edge-pill {
  background: #f3e8ff;
  border: 1px solid #e9d5ff;
  color: #7e22ce;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  font-weight: 700;
  padding: 0.15rem 0.6rem;
  border-radius: 12px;
  text-align: center;
}
.edge-pill.money-flow { background: #ffe4e6; border-color: #fecdd3; color: #e11d48; }
.edge-props {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: var(--text-muted);
  margin-top: 0.15rem;
  text-align: center;
}
.edge-arrow {
  color: #7e22ce;
  font-size: 1.1rem;
  line-height: 1;
  font-weight: bold;
}
.edge-pill.money-flow ~ .edge-arrow { color: #e11d48; }

/* Lesson 0014: Extraction Visual Flow */
.raw-narrative-card {
  background: var(--bg);
  border: 1px solid var(--border);
  border-left: 4px solid #f59e0b;
  border-radius: 8px;
  padding: 0.85rem 1rem;
  margin-bottom: 0.85rem;
}
.narrative-header {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  color: #d97706;
  margin-bottom: 0.25rem;
}
.narrative-quote {
  font-family: var(--font-serif);
  font-size: 0.95rem;
  line-height: 1.45;
  color: var(--text);
}
.entity-highlight {
  background: #fef3c7;
  color: #92400e;
  padding: 0.1rem 0.25rem;
  border-radius: 3px;
  font-weight: 600;
}
.llm-transform-step {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  padding: 0.4rem 0;
  color: var(--accent);
  font-family: var(--font-mono);
  font-size: 0.74rem;
  font-weight: 600;
  text-align: center;
}
.triples-list {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}
.triple-card {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.75rem 0.85rem;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}
.triple-chip {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  padding: 0.2rem 0.45rem;
  border-radius: 4px;
}
.triple-chip.subject { background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }
.triple-chip.predicate { background: #f3e8ff; color: #7c3aed; border: 1px solid #e9d5ff; font-weight: 700; text-align: center; }
.triple-chip.object { background: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; }
.triple-arrow { display: none; }

/* Lesson 0015: Entity Resolution */
.er-disparate-records {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 0.85rem;
}
.variant-card {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.65rem 0.75rem;
}
.variant-source {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: var(--text-muted);
  text-transform: uppercase;
}
.variant-name {
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--text);
  margin: 0.15rem 0;
}
.variant-detail {
  font-size: 0.72rem;
  color: var(--text-muted);
}
.er-stages-stack {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin: 0.5rem 0;
}
.er-stage-item {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.65rem 0.8rem;
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}
.er-stage-badge {
  display: inline-block;
  align-self: flex-start;
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 0.1rem 0.4rem;
  border-radius: 3px;
  background: #e2e8f0;
  color: #475569;
}
.er-stage-content strong {
  display: block;
  font-family: var(--font-sans);
  font-size: 0.84rem;
  color: var(--text);
}
.er-stage-content span {
  font-family: var(--font-sans);
  font-size: 0.75rem;
  color: var(--text-muted);
}
.er-resolved-master {
  background: #f0fdf4;
  border: 2px solid #86efac;
  border-radius: 10px;
  padding: 0.85rem 1rem;
  margin-top: 0.85rem;
  text-align: center;
}
.master-badge {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  background: #dcfce7;
  color: #15803d;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  margin-bottom: 0.35rem;
}
.master-node-code {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  color: #166534;
  font-weight: 600;
  word-break: break-all;
}

/* Lesson 0016: Cypher Box */
.cypher-box {
  background: #1e1e2e;
  color: #cdd6f4;
  border: 1px solid #313244;
  border-radius: 8px;
  padding: 0.85rem 1rem;
  margin: 1.1rem 0;
  font-family: var(--font-mono);
  font-size: clamp(0.75rem, 2.7vw, 0.84rem);
  line-height: 1.45;
  white-space: pre-wrap;
  overflow-x: auto;
  position: relative;
}
.cypher-box::before {
  content: "CYPHER";
  display: block;
  font-family: var(--font-mono);
  font-size: 0.62rem;
  font-weight: 700;
  color: #89b4fa;
  margin-bottom: 0.4rem;
  letter-spacing: 0.08em;
  opacity: 0.7;
}

/* Lesson 0019: Router Visual */
.router-query-box {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.75rem 0.85rem;
  text-align: center;
}
.router-query-box strong {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  text-transform: uppercase;
  color: var(--accent);
  display: block;
  margin-bottom: 0.15rem;
}
.router-query-box p {
  margin: 0;
  font-family: var(--font-serif);
  font-size: 0.95rem;
  color: var(--text);
}
.router-gateway-card {
  background: #f8fbff;
  border: 1px solid #bfdbfe;
  border-radius: 10px;
  padding: 0.8rem 0.9rem;
  text-align: center;
}
.gateway-badge {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  background: #dbeafe;
  color: #1e40af;
  padding: 0.12rem 0.45rem;
  border-radius: 4px;
}
.router-gateway-card h4 {
  margin: 0.3rem 0 0.15rem;
  font-family: var(--font-sans);
  font-size: 0.9rem;
  color: var(--text);
}
.router-gateway-card p {
  margin: 0;
  font-family: var(--font-sans);
  font-size: 0.76rem;
  color: var(--text-muted);
}
.router-paths-grid {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
  margin: 0.75rem 0;
}
.path-card {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.75rem;
}
.path-badge {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  padding: 0.12rem 0.4rem;
  border-radius: 3px;
  margin-bottom: 0.3rem;
}
.path-badge.p1 { background: #e0f2fe; color: #0284c7; }
.path-badge.p2 { background: #f3e8ff; color: #7c3aed; }
.path-badge.p3 { background: #dcfce7; color: #16a34a; }
.path-card strong {
  display: block;
  font-family: var(--font-sans);
  font-size: 0.84rem;
  color: var(--text);
  margin-bottom: 0.15rem;
}
.path-card p {
  margin: 0;
  font-family: var(--font-sans);
  font-size: 0.76rem;
  color: var(--text-muted);
  line-height: 1.35;
}
.fusion-card {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.75rem 0.85rem;
  text-align: center;
}
.fusion-card strong {
  display: block;
  font-family: var(--font-sans);
  font-size: 0.86rem;
  color: var(--text);
}
.fusion-card span {
  font-family: var(--font-sans);
  font-size: 0.75rem;
  color: var(--text-muted);
}
.final-gen-card {
  background: #faf5ff;
  border: 1px solid #e9d5ff;
  border-radius: 8px;
  padding: 0.75rem 0.85rem;
  text-align: center;
}
.final-gen-card strong {
  display: block;
  font-family: var(--font-sans);
  font-size: 0.88rem;
  color: #6b21a8;
}
.final-gen-card span {
  font-family: var(--font-sans);
  font-size: 0.76rem;
  color: #7e22ce;
}

/* Lesson 0020: GCP Blueprint */
.gcp-blueprint-visual {
  border: 2px solid #3b82f6;
}
.perimeter-header {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid var(--border);
  margin-bottom: 1rem;
}
.perimeter-badge {
  align-self: flex-start;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  background: #eff6ff;
  color: #1d4ed8;
  border: 1px solid #bfdbfe;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}
.perimeter-header h3 {
  margin: 0;
  font-family: var(--font-sans);
  font-size: 0.98rem;
  color: var(--text);
}
.blueprint-phases {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
}
.blueprint-phase-row {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.85rem;
}
.phase-tag {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 0.12rem 0.45rem;
  border-radius: 4px;
  margin-bottom: 0.45rem;
}
.phase-1 .phase-tag { background: #e0f2fe; color: #0284c7; }
.phase-2 .phase-tag { background: #fef3c7; color: #b45309; }
.phase-3 .phase-tag { background: #f3e8ff; color: #7c3aed; }
.phase-4 .phase-tag { background: #dcfce7; color: #16a34a; }
.phase-grid {
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
}
.phase-node {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 0.65rem 0.75rem;
}
.phase-node strong {
  display: block;
  font-family: var(--font-sans);
  font-size: 0.84rem;
  color: var(--text);
}
.phase-node code {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--accent);
}
.phase-node p {
  margin: 0.2rem 0 0;
  font-family: var(--font-sans);
  font-size: 0.75rem;
  color: var(--text-muted);
}
.phase-link-arrow {
  text-align: center;
  color: var(--accent);
  font-weight: bold;
  font-size: 1.1rem;
}

@media (prefers-color-scheme: dark) {
  .tier-1 .tier-badge { background: #152942; color: #58a6ff; }
  .tier-2 .tier-badge { background: #2e1a47; color: #c084fc; }
  .tier-3 .tier-badge { background: #064e3b; color: #6ee7b7; }
  .funnel-tier.level-gold { background: #062e1e; border-left-color: #34d399; }
  .stage-subcard.highlight { background: #2a2007; border-color: #b45309; }
  .node-label-pill.person { background: #0c2d48; color: #7dd3fc; border-color: #0369a1; }
  .node-label-pill.company { background: #382506; color: #fde047; border-color: #b45309; }
  .node-label-pill.account { background: #052e16; color: #86efac; border-color: #15803d; }
  .node-label-pill.account-frozen { background: #450a0a; color: #fca5a5; border-color: #b91c1c; }
  .edge-pill { background: #2e1065; border-color: #581c87; color: #d8b4fe; }
  .edge-pill.money-flow { background: #4c0519; border-color: #881337; color: #fda4af; }
  .raw-narrative-card { background: #1c1917; border-left-color: #d97706; }
  .entity-highlight { background: #451a03; color: #fde047; }
  .triple-chip.subject { background: #0c2d48; color: #7dd3fc; border-color: #0369a1; }
  .triple-chip.predicate { background: #2e1065; color: #d8b4fe; border-color: #581c87; }
  .triple-chip.object { background: #052e16; color: #86efac; border-color: #15803d; }
  .er-resolved-master { background: #052e16; border-color: #22c55e; }
  .master-badge { background: #14532d; color: #86efac; }
  .master-node-code { color: #86efac; }
  .router-gateway-card { background: #111d33; border-color: #1e3a8a; }
  .gateway-badge { background: #1e3a8a; color: #93c5fd; }
  .final-gen-card { background: #28143d; border-color: #581c87; }
  .final-gen-card strong { color: #e9d5ff; }
  .final-gen-card span { color: #c084fc; }
  .gcp-blueprint-visual { border-color: #2563eb; }
  .perimeter-badge { background: #172554; color: #93c5fd; border-color: #1e40af; }
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
  <div style="display: flex; justify-content: flex-end; align-items: center; padding: 0.75rem 0.5rem 0; font-family: var(--font-sans); font-size: 0.82rem;">
    <a href="../index.html?view=desktop" onclick="sessionStorage.setItem('prefer-desktop', 'true')" style="color: var(--accent); text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 0.35rem; background: var(--surface); border: 1px solid var(--border); padding: 0.3rem 0.65rem; border-radius: 6px;">🖥️ Switch to Desktop Edition</a>
  </div>

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
