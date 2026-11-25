# Intake • synthetic teaching case

In a fictional sorting-library submission, RunFold reuses an index of sorted runs across requests. The submitted text says “RunFold reduces sorting latency in service deployments.” A default configuration reached 80 ms median latency for RunFold versus 100 ms for MergeBase in one persistent service. The paper did not document each library's warm-up or how ties are handled. The target is a long-running service. Peak memory and tail latency have not been measured.

The fictional venue provides a 1–4 overall scale (1 reject, 2 lean reject, 3 lean accept, 4 accept), 1,000 Unicode code points per review body, anonymous text-only Markdown, and a discussion-period revision window. This exercise rule card is independent of actual conference rules.

| Reviewer | Original rating | Original review |
|---|---:|---|
| R1 | 2 | Your library caches prior work. How was the competing implementation warmed? I would reconsider if the result holds under the same warm-up and request order. |
| R2 | 2 | Our short-lived jobs run once and exit. Do the gains extend to cold starts? Please explain what a user deploying either way should expect. |
| R3 | 3 | The index might change the ordering of equal keys. Can you show what happens to ties? I would value a concrete test of the stability claim. |

First, decide who needs a fair baseline, who needs an operating condition, and who needs a correctness check. There is time for one latency experiment and inspection of the existing correctness suite.
