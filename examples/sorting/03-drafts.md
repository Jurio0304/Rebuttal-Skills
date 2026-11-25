# Initial author responses • synthetic

These three bodies form the initial panel input. The aggregation detail in E1 is available to the author for follow-up.

## R1

RunFold reduces median latency from 100 to 82 ms in the matched warm condition. Both libraries receive the same ten untimed requests, followed by the same timed request sequence, on the same machine with a 1 GiB limit. Implementation order alternates across five fixed traces. The comparison therefore retains the warm-service gain when the baseline receives equal warm-up.

## R2

The gain applies to a persistent service. After the same ten untimed requests, RunFold takes 82 ms versus 100 ms for MergeBase. On the first request in a fresh process the figures are 111 and 110 ms, respectively. We will specify these operating conditions in the abstract and deployment guidance.

## R3

RunFold preserves the reference order of equal keys in all 24 duplicate-key fixtures. We compared original positions within each equal-key group against a stable reference, including cases in which ties span run boundaries. We will report the check and its coverage in the correctness section.
