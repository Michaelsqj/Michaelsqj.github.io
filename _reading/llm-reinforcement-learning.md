---
title: LLM Reinforcement Learning
description: From PPO to GRPO, with emphasis on the staleness–stability–efficiency trade-off.
domain: LLM post-training
meta: Started July 2026
order: 2
published: true
---

*Started: 25 July 2026*

This topic follows reinforcement-learning algorithms for LLM post-training, with particular attention to the gap between clean algorithm descriptions and distributed training systems.

## Algorithm foundations

### Proximal Policy Optimization

[Paper](https://arxiv.org/abs/1707.06347)

PPO constrains policy updates through a clipped surrogate objective. In LLM training, it provides a useful reference point for thinking about policy ratios, value estimation, KL control, and repeated optimization over collected trajectories.

**Quick take:** PPO makes many stabilizing choices explicit, but its critic and training state increase memory and systems complexity.

### Group Relative Policy Optimization

[DeepSeekMath paper](https://arxiv.org/abs/2402.03300)

GRPO replaces a learned value model with relative rewards computed across groups of sampled outputs. It has become a useful baseline for verifiable reasoning and agent tasks where several responses can be sampled for the same prompt.

**Quick take:** removing the critic simplifies one part of the system, but reward scaling, group composition, clipping, and sample reuse still shape stability.

## The staleness–stability–efficiency trade-off

In distributed RL, rollout generation and policy optimization do not always use exactly the same weights. Asynchronous systems can improve hardware utilization and end-to-end efficiency, but the training policy can move while older trajectories are still being consumed.

- **Policy staleness:** how far the behavior policy that produced a trajectory is from the policy currently being optimized.
- **Importance ratios:** a signal for detecting and correcting policy drift, but one that can become high variance.
- **Clipping and KL control:** mechanisms that limit destructive updates without eliminating useful learning.
- **System efficiency:** accelerator utilization, rollout throughput, synchronization overhead, and time-to-train.
- **Weight synchronization:** the operational decision connecting policy freshness and training stability to system efficiency.

> The central question is how to balance policy staleness, optimization stability, and system efficiency rather than maximizing any one of them in isolation.

## Reading questions

- When does GRPO behave differently from PPO beyond the absence of a critic?
- How should clipping thresholds change with long agent trajectories?
- Which metrics reveal stale rollouts before reward or benchmark performance collapses?
- When do the efficiency gains of asynchronous rollout generation justify additional staleness and off-policy correction?
- How do partial-progress rewards interact with group-relative advantage estimation?
