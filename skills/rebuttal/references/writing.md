# Write an answer the reviewer can assess

Lead with a sentence that settles the question as far as the evidence allows. Give the comparator, observation or proof step the reviewer would need to assess it. Then explain the implication for the paper. A revision location is useful when the reader will find a changed definition, claim, table or proof there.

Write in the authors' voice. Use a confident verb for an established fact, a conditional for an inference and future tense for a confirmed commitment. A compliment about the review takes up space that could answer its question. A brief acknowledgement earns its place when it identifies a substantive contribution, such as a reviewer supplying the missing counterexample.

For public examples of when issue labels, tables, manuscript pointers and local qualifications help, see [observed discussion patterns](discussion-patterns.md).

## Read the paragraph in the authors' voice

For an established result, use a precise affirmative verb such as *reduces*, *preserves* or *identifies*, followed by the condition and the actual comparison. Give the reader one clear reason to credit the contribution. Use *suggests* for an interpretation that depends on additional assumptions. If a reviewer correctly identifies an error, acknowledge it, make the correction and identify the verified impact on the main claim.

When a secondary setting shows no gain, state the observed result once in the answer about that setting. Retain its scope when summarizing the main result. Repeat the qualification in the AC summary only if it changes the decision or resolves a shared concern. Reviewing the final prose, look for successive sentences that restate the same caveat, generic apologies before the answer, or a stronger verb than the comparison supports. Replace them with the result, the condition or the action the reviewer actually asked about.

## Choose a response form

| Reviewer concern | What to include |
| --- | --- |
| A mechanism is hard to reconstruct | Show the order of operations or one worked input. Identify the definition or diagram that supplies the missing step. |
| A plausible alternative explains the gain | Name the changed factor, held-fixed conditions and resulting contrast. State the implications for that explanation. |
| A comparison has mismatched resources | Give the relevant budgets, measurement unit and selection protocol on both sides. Report a matched comparison or delimit the original finding. |
| The work overlaps with prior art | Acknowledge the shared idea, verify the closest prior method, identify the precise difference and show the consequence supported by the paper. |
| A theorem, number or attribution is wrong | State the correction, how the error arose if known, which conclusions it affects, and where it has been or will be corrected. |
| The result is mixed or unfinished | Put the favorable and unfavorable conditions in the same answer when both bear on the question. Give the surviving claim. Label unmeasured conditions and frame future steps as plans. |

## Worked sentences

The following excerpts use invented situations and results. Each illustrates the response to a different question.

**Mixed result.** A reviewer asks whether a file index speeds up all lookups. The authors repeated matched measurements and have approved a narrower claim.

> The index reduced median lookup time for timestamp ranges from 40 to 24 ms. Exact-key lookups took 8 ms with either implementation on the same files. We will limit the latency claim in Section 3 to timestamp-range queries.

The local null result belongs beside the positive one because it changes the scope of “all lookups.” If the question concerns a different claim, mention this condition only where it affects the interpretation.

**Correction.** A reviewer found an invalid proof step. The authors have checked the repaired statement and edited a local revision.

> You are right that the cancellation in Lemma 2 requires a nonzero denominator. We added that assumption to the lemma and checked every application in Theorem 1, where strict positivity already holds. The theorem therefore retains its stated domain.

**Unresolved attribution.** A reviewer asks which of two changes accounts for a speedup. Only the combined system was measured.

> Both changes were enabled in the reported timing experiment. The comparison establishes the runtime of the combined implementation. Isolating the scheduling change would require holding the memory layout fixed, so we will describe the measured gain at the system level.

**Concise follow-up.** A reviewer accepts the measurement but asks whether its scope includes initialization.

> The reported interval starts after initialization and ends when the last record is written. It measures steady-state processing. We have added those timing boundaries to the caption of Table 2.

Use the final example's past tense only when the cited edit exists. If the author has approved a future correction, name it as a commitment. Keep draft notes, missing inputs and source paths outside the response body.
