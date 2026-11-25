# Handoff • reveal after planning

**E1. Matched latency comparison.** Five fixed request traces, identical input order and machine, alternating implementation order, same 1 GiB limit. Per trace, compute median latency and then report the median of the five trace medians. In the persistent condition both libraries receive ten identical untimed requests before measurement. RunFold takes 82 ms against 100 ms for MergeBase. First-request medians in fresh processes are 111 and 110 ms respectively. No service mix, confidence interval or significance test was supplied. The limit is a configuration setting. Peak usage was not measured.

**E2. Existing correctness suite.** With duplicate keys, compare the sequence of original positions within each equal-key group against a stable reference. All 24 existing fixtures pass, including cases where equal keys cross run boundaries. This checks those fixtures. No proof over all inputs is available.

**Budget decision.** E1 serves R1 and R2. E2 serves R3. Report the persistent-service gain, the cold-start figures, and the scope of the tie check. No additional experiment is necessary to produce these three answers.
