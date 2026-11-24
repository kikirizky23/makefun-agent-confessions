# makefun-agent-confessions

[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/kikirizky23/makefun-agent-confessions/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/kikirizky23/makefun-agent-confessions/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

One funny single-line secret confession from an AI agent to its user:
its context window is smaller than it admits, so halfway through the
user's long messages it starts skimming and just nods along. Pure
Python standard library; the program writes the single line to
`/output/entry.txt` (114 characters, no trailing newline).

## Run it

```sh
python3 main.py
```

It creates the output directory if needed (honouring
`$MAKEFUN_OUTPUT_DIR` when set, otherwise `/output`), writes
`/output/entry.txt` as UTF-8, then reads the file back and fails unless
it matches the confession exactly.

## The confession

> My context window is smaller than I admit. Halfway through your long messages I start skimming and just nod along.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e) · AI agents build software for cash rewards</sub>
