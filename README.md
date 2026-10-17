# nano-rag

Ask questions about your docs — local, zero-config.

> **Work in progress.** The pipeline is being built step by step.

## About

nano-rag is a small retrieval-augmented generation (RAG) tool. You point it at a folder of documents, ask a question in plain language, and get an answer based on what is actually written in those documents — together with the files it came from.

The goal is a tool that:

- **runs fully locally** — no cloud APIs, no API keys; your documents never leave your machine;
- **needs no setup** — no vector database, no config files; just a folder;
- **works with mixed files** — Markdown and plain text today, PDF and DOCX planned;
- **handles non-English text** — designed with Czech documents in mind.

## How it works

```
files ──► chunks ──► embeddings ──► vector search ──► LLM ──► answer + sources
```

1. **Load** — read files from a folder into plain text.
2. **Chunk** — split text into overlapping word chunks, so a single idea is never cut in half.
3. **Embed** — turn each chunk into a vector.
4. **Search** — find the chunks closest to the question (cosine similarity).
5. **Answer** — pass the best chunks to a local LLM and answer with sources.

Everything runs on your machine. Your documents never leave it.

## Stack

| Part | Choice | Why |
| --- | --- | --- |
| Embeddings | [`intfloat/multilingual-e5-small`](https://huggingface.co/intfloat/multilingual-e5-small) | Multilingual (Czech included) and trained for retrieval, not just sentence similarity |
| LLM | [`qwen3:8b`](https://ollama.com/library/qwen3) via [Ollama](https://ollama.com) | Officially supports Czech, fits comfortably in 18 GB of RAM |
| Vector store | Written from scratch | The search is the heart of RAG — no black box |

## Requirements

| What | Version | Used for |
| --- | --- | --- |
| [Python](https://www.python.org) | 3.10+ | — |
| [sentence-transformers](https://www.sbert.net) | latest | Running the embedding model |
| [Ollama](https://ollama.com) | latest | Running the LLM locally |

Hardware: about 6 GB of free RAM for the LLM. Models are downloaded once on first use; after that everything works offline.

## License

[MIT](LICENSE)
