# Discussion, global response and revision • worked answer

## Stage 6 • reply to R2

We computed a median within each of the five fixed traces and then took the median of those five values. Under equal warm-up the medians are 82 ms for RunFold and 100 ms for MergeBase. For the first request they are 111 and 110 ms. The revised deployment paragraph now identifies persistent services as the setting for the observed improvement.

## Stage 7 • global response to the AC

The matched comparison establishes an 18% median-latency reduction in persistent operation. Both libraries received the same warm-up, and fresh-process measurements specify the deployment boundary. A separate reference check confirmed stable tie order on all 24 duplicate-key fixtures. R1 confirmed that the matched protocol addresses fairness and updated their rating. R2 acknowledged the cold-start result and requested the trace aggregation, which we supplied. R2 indicated a conditional intention to raise their rating, with the displayed rating still at 2. R3 confirmed that the tie fixtures address their question.

## Stage 8 • locally revised synthetic manuscript excerpt

**Abstract.** Across five fixed traces, RunFold reduces warm median latency from 100 to 82 ms after identical warm-up. First-request latencies are 111 ms for RunFold and 110 ms for MergeBase.

**Deployment.** The warm result applies to long-running services. Each implementation received ten untimed requests. We computed the median within each trace and report the median across traces.

**Correctness.** Comparison against a stable reference preserved the sequence of original positions within every equal-key group in all 24 fixtures, including ties spanning run boundaries.

| Commitment | Local location | Exercise status |
|---|---|---|
| R1 matched schedule and aggregation | Deployment | Applied to the excerpt |
| R2 qualify service claim and show cold results | Abstract and Deployment | Applied to the excerpt |
| R3 document duplicate-key coverage | Correctness | Applied to the excerpt |

Platform upload is unconfirmed in this fixture.
