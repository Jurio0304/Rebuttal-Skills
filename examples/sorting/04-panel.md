# Independent panel run • synthetic case

Three fresh reviewer agents received separate packets from this exercise. Each packet contained the fictional scale, one original score and review, the submitted claim and the corresponding draft. Agents did not see each other's answers, the author's evidence sheet, future discussion or a preferred rating. All judgements on this page are **simulated**.

| Simulated reviewer | Proposed rating | Comment and actionable feedback from the run |
|---|---|---|
| R1 | 2 → 3 | Equal warm-up, request order and the 100-to-82 ms comparison addressed the fairness question. Asked the author to qualify the deployment claim and carry the warm-up protocol into the paper. |
| R2 | 2 → 3 | The first-request results answered the short-job question. Suggested putting both figures in the deployment guidance and limiting the abstract's claim to the warm condition. |
| R3 | 3 → 3 | Checking original positions against a stable reference, especially across run boundaries, addressed the question about ties. Recommended reporting the comparison criterion and coverage. |

**R1's simulated forum reply**

> The matched warm-up answers my main concern. Both libraries receive the same ten untimed requests and the same timed sequence, and RunFold still reduces median latency from 100 to 82 ms. I would raise my rating to 3. Please state in the deployment claim that this result measures warm-service median latency, and include the warm-up protocol in the paper.

**R2's simulated forum reply**

> This answers my deployment question. For the one-shot jobs I described, RunFold took 111 ms on the first request versus 110 ms for MergeBase, so I would expect no latency benefit under the tested conditions. In a persistent service, after ten untimed requests, RunFold reduced latency from 100 to 82 ms. Please include both figures in the deployment guidance and qualify the abstract’s latency claim accordingly.

**R3's simulated forum reply**

> Thank you for checking ties that span run boundaries. Comparing the original positions within each equal-key group against a stable reference directly answers my question. All 24 fixtures preserved the reference order, which resolves my concern. I support including the comparison and its coverage in the correctness section.

## Author clarification and rework

The author accepted R1's request and added how the five traces were summarized, using the existing evidence. The same R1 agent received that clarification and responded:

> Yes. The proposed wording limits the claim to warm-service median latency, and the aggregation rule makes clear that each trace contributes one median. This addresses my requested revision. My proposed rating remains 3 (lean accept), with the manuscript edit still pending.

**Revised R1 body**

RunFold reduces warm-service median latency from 100 to 82 ms with equal warm-up and the same timed request sequence. Both libraries receive ten identical untimed requests on the same machine with a 1 GiB limit. We alternate implementation order across five fixed traces, compute the median within each trace and report the median of those five values. We will specify the warm-service scope in the abstract and document the warm-up and aggregation in the deployment paragraph.

The new detail and revision commitment answer R1. R2's body already gives both deployment conditions, and R3's body specifies the tie criterion. Their suggestions become manuscript commitments. The later AC exercise uses only the separately supplied [forum inputs](05-discussion-input.md).
