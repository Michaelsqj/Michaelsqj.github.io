---
title: Agent Environments
description: Executable environments, scalable synthesis, verification, benchmarks, and training signals for interactive agents.
domain: Agentic AI
meta: Updated July 2026
order: 1
published: true
---

*Last updated: 24 July 2026*

This collection follows work on executable environments for training and evaluating agents. I am especially interested in how environments are grounded, verified, scaled, and adapted to a model's changing capability.

## July 2026

### SETA: Scaling Environments for Terminal Agents

[Paper](https://arxiv.org/html/2607.10891v1) · [Code](https://github.com/camel-ai/seta)

SETA builds verified terminal environments through two complementary pipelines: source-adaptive synthesis from human-validated material and difficulty-adaptive evolution from existing tasks. The released SETA-Env collection contains 4,567 grounded, executable environments.

**Why I care:** it treats the environment—not only the trajectory—as a scalable training artifact. The combination of executable verification and capability-aware evolution makes it useful for RL post-training.

- SETA-Synth converts sources such as technical Q&A and notebooks into standardized tasks.
- SETA-Evol reshapes difficulty and diversity toward the model's productive learning frontier.
- A Qwen3-8B model trained with GRPO improves strongly on Terminal-Bench 2.0 and related coding benchmarks.

> Open question: how should environment evolution change when models become capable enough to exploit weaknesses in the verifier?

### Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks

[Paper](https://arxiv.org/abs/2601.11868)

Terminal-Bench evaluates agents on long-horizon command-line tasks spanning system administration, security, data processing, and machine learning.

**Quick take:** it is a useful target for measuring broad terminal competence, but a curated evaluation set and a scalable RL environment distribution serve different roles.

## Earlier foundations

### SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

[Paper](https://arxiv.org/abs/2310.06770)

SWE-bench grounds software-engineering tasks in real repositories, issues, and tests. It established executable verification as a central design pattern for agent evaluation.

**Quick take:** repository history provides unusually strong natural supervision. General terminal environments need other grounding sources and more deliberate verifier construction.

### WebArena: A Realistic Web Environment for Building Autonomous Agents

[Paper](https://arxiv.org/abs/2307.13854)

WebArena provides realistic, self-hosted websites and functional tasks for evaluating web agents.

**Quick take:** environment fidelity matters because agents learn interface-specific strategies. The same principle applies to terminals, desktop systems, and scientific tools.

## Questions to revisit

- How can verifiers expose useful partial progress without becoming easy reward-hacking targets?
- What environment mixture produces transferable tool-use behavior?
- How should task difficulty be measured independently of a particular agent harness?
- Can environments be evolved jointly with policies while preserving grounding and auditability?
