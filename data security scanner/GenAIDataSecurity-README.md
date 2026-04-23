# /GenAIDataSecurity — OWASP GenAI Data Security Compliance Skill

A Claude Code slash command that automatically scans GenAI and agentic codebases against the **OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0)** — covering all 21 DSGAI risk controls across the full GenAI data lifecycle.

---

## What It Does

When you run `/GenAIDataSecurity` inside a repository, the skill:

1. **Detects** whether the repo contains GenAI/agentic patterns (LangChain, LlamaIndex, OpenAI SDK, vector stores, MCP servers, etc.) — bails out gracefully if none are found
2. **Enriches live CVEs** by querying OSV, NVD, and GitHub Advisory Database against the exact package versions pinned in the repo
3. **Scans source code** for all 21 DSGAI risk indicators — credentials, SQL injection via LLM output, vector store auth, telemetry logging, RAG access controls, MCP transport security, and more
4. **Generates `DSGAI-report.html`** — a self-contained, print-ready HTML report with findings, file paths, line numbers, remediation steps, and a live CVE advisory panel

---

## Prerequisites

- A repository containing GenAI or agentic code (Python, TypeScript, Java, Go)
- An AI coding tool with **file reading access** to your codebase (see supported tools below)
- **Web access** in your AI tool for live CVE lookups (Step 0.5) — if unavailable, the scan still runs using the embedded CVE database in the skill file

No Python packages or external tools required to generate the HTML report.

---

## Running with Claude Code (Native)

Claude Code has first-class support for this skill via its slash command system.

**Installation — macOS / Linux:**
```bash
cp GenAIDataSecurity.md ~/.claude/commands/
```

**Installation — Windows:**
```
copy GenAIDataSecurity.md %USERPROFILE%\.claude\commands\
```

**Usage:**
1. Open your GenAI repository in [Claude Code](https://claude.ai/code) (CLI, desktop app, or VS Code / JetBrains extension)
2. Type `/GenAIDataSecurity` and press Enter
3. Claude scans the codebase — typically 2–5 minutes depending on repo size
4. A `DSGAI-report.html` file is saved at the repository root and opens in your browser

---

## Running with Other AI Coding Tools

The skill file is plain Markdown. Any AI tool with file reading access to your codebase can run it — just paste the contents as your prompt.

| Tool | How to run |
|---|---|
| **Cursor** | Open `GenAIDataSecurity.md`, copy the contents, paste into Cursor's AI chat as your prompt |
| **GitHub Copilot Chat** | Open the skill file, copy contents, paste into Copilot Chat in VS Code and include the repo files as context |
| **ChatGPT / GPT-4** | Paste the skill file contents as the system prompt, then upload or paste the relevant source files |
| **Google Gemini** | Paste the skill file contents as instructions, attach source files for analysis |

The skill requires the AI tool to have **file reading access** to scan the codebase, and **web access** for live CVE lookups (Step 0.5). If web access is unavailable, the scan still runs using the embedded CVE database in the skill file.

---

## What Gets Scanned

All 21 DSGAI risks from the OWASP GenAI Data Security framework:

| Risk | Control Area |
|---|---|
| DSGAI01 | Training Data Privacy |
| DSGAI02 | Agentic Identity & Credential Management |
| DSGAI03 | Shadow AI & Unauthorized Data Flows |
| DSGAI04 | AI Supply Chain Security |
| DSGAI05 | RAG Data Security |
| DSGAI06 | MCP & Plugin Security |
| DSGAI07 | Data Lifecycle Management |
| DSGAI08 | Regulatory & Privacy Compliance |
| DSGAI09 | Multimodal AI Data Security |
| DSGAI10 | Synthetic Data Security |
| DSGAI11 | Multi-Tenant Data Isolation |
| DSGAI12 | Database Agent Security |
| DSGAI13 | Vector Store Security |
| DSGAI14 | AI Telemetry & Observability Security |
| DSGAI15 | Context Window Data Security |
| DSGAI16 | AI IDE Plugin & Extension Security |
| DSGAI17 | AI System Resilience & Availability |
| DSGAI18 | Model Output Data Security |
| DSGAI19 | AI Data Labeling Security |
| DSGAI20 | Inference API Security |
| DSGAI21 | Knowledge Store Security |

Each control is rated: **PASS** / **WARN** / **FAIL** / **NOT VALIDATED** / **NOT APPLICABLE**

---

## Report Output

The generated `DSGAI-report.html` contains:

- **Executive Summary** — overall posture and key FAIL findings
- **Dashboard** — counts of PASS / WARN / FAIL / NOT VALIDATED / NOT APPLICABLE across all 21 controls
- **AI Component Inventory** — detected frameworks, vector stores, LLM providers, MCP servers
- **Summary Table** — all 21 risks at a glance with status and key evidence
- **Detailed Findings** — one card per risk with file paths, line numbers, and remediation steps
- **Recommendations** — tiered action plan (fix today / architecture backlog / maturity program)
- **CVE Advisory Panel** — live CVEs for your exact dependency versions, grouped by DSGAI risk

The report is fully self-contained (no CDN, no external fonts) and renders correctly when saved as PDF.

---

## Exporting to PDF

**Option 1 — Browser print (simplest):**
Open `DSGAI-report.html` in Chrome or Edge → `Ctrl+P` / `Cmd+P` → Save as PDF. All cards expand automatically for print.

**Option 2 — Chrome headless (scriptable):**

macOS:
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --print-to-pdf=DSGAI-report.pdf \
  --print-to-pdf-no-header "file://$(pwd)/DSGAI-report.html"
```

Linux:
```bash
google-chrome --headless=new --print-to-pdf=DSGAI-report.pdf \
  --print-to-pdf-no-header "file://$(pwd)/DSGAI-report.html"
```

Windows (PowerShell):
```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --headless=new --print-to-pdf=DSGAI-report.pdf `
  --print-to-pdf-no-header "file:///$(pwd)/DSGAI-report.html"
```

---

## Scope Annotation

Each DSGAI control is tagged by responsibility:

- **[BUILD]** — your team implements this in the codebase
- **[BUY]** — the LLM provider / SaaS vendor is responsible
- **[BOTH]** — shared responsibility

Controls tagged `[BUY]` that are not applicable to a BUILD-only repo are automatically marked **NOT APPLICABLE** with an explanation.

---

## Based On

**OWASP GenAI Data Security Risks and Mitigations 2026 (v1.0, March 2026)**
[https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
