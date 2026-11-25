# Independent simulated review and targeted rework

Use this stage after drafting, or directly on an existing reply. A full-panel run creates as many independent reviewer agents as there are original reviewers. A request explicitly scoped to one thread uses that reviewer alone. Inherit the author's current model and reasoning settings unless the author chooses another configuration.

## Run the panel

1. Make an inventory of reviewers. For each, package their original review, starting rating/confidence if supplied, the applicable rating scale and their own author response. Include relevant submitted text or previously visible material if available. Keep other replies, internal notes, desired outcomes, evaluation keys, live follow-ups and terminal ratings out of each packet. If replying to one reviewer depends on another thread, include only the evidence that the intended reader can actually access and say where it appears.
2. In a client with agent delegation, start a fresh context for each reviewer. In Codex use a fresh agent with history inheritance disabled. In Claude Code use separate fresh subagents, supplying only the corresponding packet. Give the reviewer the [reviewer brief](../../assets/reviewer-brief.md). Limit their work to the supplied material. Do not ask them to browse a shared workspace that contains other reviewers' records. Batch to fit available concurrency and preserve the reviewer-to-agent mapping for follow-ups. If independent delegation is unavailable, give the author one self-contained packet per fresh chat and identify which assessments are still pending. A single assistant writing several personas cannot verify an independent panel.
3. Collect each response before sharing any feedback. Ask for a natural forum-style comment first, followed by internal notes covering issues resolved or open, the strongest evidence, the most useful change, likely follow-up and simulated inclination to raise, maintain, lower or defer. Report current and proposed ratings only on a known scale with a known starting score. Allow genuine satisfaction and an unchanged rating. Avoid fabricating objections to fill a quota.
4. Summarize only actionable findings. Quote the triggering draft sentence or identify its location. Distinguish factual errors you verified from conditional questions raised by a simulator. Label the entire panel and every numeric estimate **simulated**. An agent's confidence describes its reading of this packet.
5. The author may clarify, contest a premise, supply a missing excerpt or accept an unresolved limitation. Send the clarification to the same reviewer agent. Note the before/after judgement and exactly what changed it. When the clarification belongs in the actual response, revise that response too. If agent continuation is unavailable, seed a fresh context with that same reviewer's previous packet, report and clarification, and disclose the substitution.
6. Route rework by cause: misunderstood concern → intake; untested alternative → plan; incompatible protocols or unsupported interpretation → results; unclear but supported claim → response; implemented paper change → revision. Reassess only the materially affected reviewers. Stop when open issues are understood, the author accepts the evidence boundary or the agreed budget runs out. Carry revised text and manuscript commitments to later stages. Store simulation reports outside the real discussion record.

## Panel summary

| Simulated reviewer | Original rating | Simulated judgement and reason | Open issue | Revision or author decision |
|---|---|---|---|---|

A lower or unchanged simulated score can accompany a sound response. Choose rework based on the scientific issue and available evidence. A real reviewer may reach a different judgement.
