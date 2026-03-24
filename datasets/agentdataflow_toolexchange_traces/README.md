# Agent Data Flow & Tool Exchange Traces

Sanitized traces of agentic AI tool calls, plugin data exchanges, and delegation chains for security research.

**Status:** Accepting contributions — this dataset is being built from scratch with the community.

## Scope

Structured traces capturing how data flows through agentic AI systems — between agents, tools, plugins, APIs, and memory stores. This dataset supports research into DSGAI06 (Tool, Plugin & Agent Data Exchange Risks), DSGAI02 (Agent Identity & Credential Exposure), DSGAI15 (Over-Broad Context Windows & Prompt Over-Sharing), and related agent security patterns.

Categories include:

- **Tool call traces** — Sequences of tool invocations showing what data is sent to and received from external tools (APIs, databases, file systems, code execution environments)
- **Multi-agent delegation chains** — Traces showing how tasks and data are passed between agents, including what context is forwarded, filtered, or accumulated
- **Plugin data exchange logs** — Records of data shared with third-party plugins, including request/response payloads and metadata
- **Credential and permission flows** — How credentials, tokens, and permissions are scoped, delegated, and consumed across agent workflows
- **Context accumulation patterns** — Traces showing how agent context windows grow over multi-step tasks, what data persists across steps, and where over-sharing occurs
- **Memory read/write traces** — How agents interact with short-term and long-term memory stores, including what data is persisted and retrieved

## Data Format

<!-- TODO: Define schema once initial data is contributed -->

Contributions should include:

- **Trace ID**
- **Category** — From the list above
- **DSGAI mapping** — Primary DSGAI entries relevant to this trace
- **Agent framework** — LangGraph, AutoGPT, CrewAI, custom, etc. (if disclosable)
- **Trace data** — The sequence of events, tool calls, and data exchanges in structured format (JSON, JSONL, or OpenTelemetry-compatible spans)
- **Data sensitivity annotations** — Flag any steps where sensitive data is present, over-shared, or inadequately scoped
- **Security observations** — What data security risks this trace illustrates
- **Benign / adversarial** — Whether this is a normal workflow trace or one demonstrating a security failure

## Sanitization Requirements

All traces **must** be sanitized before submission:

- No real API keys, tokens, credentials, or secrets — replace with placeholder values (e.g., `sk-REDACTED`, `Bearer EXAMPLE_TOKEN`)
- No real PII, PHI, or proprietary data — use synthetic equivalents
- No internal hostnames, IP addresses, or infrastructure details
- Generalize organization-specific tool names if they could identify the source

Traces from test environments, sandboxes, or CTF exercises are ideal. Production traces must be thoroughly sanitized.

## Contributing

Add traces as individual JSON, JSONL, or YAML files and submit a pull request. See the [main datasets README](../README.md) for general contribution guidelines.
