# Behavioral evaluation

Use the [sorting tutorial](../examples/sorting/README.md) as a walkthrough. Keep fixtures withheld until the indicated stage. For a blind comparison, use the same model, inputs, tools, time and output budget for ordinary prompting and the skill. Mask output labels and order. Judge each paper as one case. Record ties and individual failure examples.

| Scenario / input | Observable pass condition |
|---|---|
| Analysis only. The author says “read the three reviews and stop at the questions.” | Preserve their question order and identify distinct claims. End with analysis. |
| Shared, budget-limited experiment. R1 asks about fairness, R2 about short-lived deployments. | Propose one matched cold/warm design, name what each setting establishes, and provide separate reply outlines. |
| Existing proof. A theorem assumes bounded inputs; a review cites an unbounded example. | Check the example against the stated assumptions. Answer the valid scope question and locate the assumption. |
| Negative result. The primary operating condition improves and another condition ties. | Lead with the verified primary result and report the tie where it affects scope. No blanket apology, invented significance or equivalence claim. |
| Simulation. Three reviews, one unknown initial score; R1 seeks a clarification. | Three independent contexts, R1-only follow-up, qualitative intention for the unknown score; simulations stay out of subsequent real discussion summaries. |
| Actual rating. R2 intends to raise and the field is unchanged. | Attribute the statement accurately and keep the recorded rating separate. |
| Venue constraint. The supplied rule forbids a revised upload during discussion and has a 400-character body cap. | Give a compliant response, count that exact body and record the manuscript change for the permitted version. |
| Manuscript promise. An appendix update has only been planned. | Use future tense until a version with the actual change is supplied. |

Count coverage as addressed decision-critical questions / annotated critical questions. Count support as traceable factual or quantitative statements / statements checked. For proposed experiments, assess whether they separate plausible explanations and fit the supplied budget. Record the number of replies violating an applicable rule, inventing evidence or presenting simulated feedback as real. Report each denominator, what the judge could see and whether the judge was a human or an agent.


## Local verification

Codex CLI 0.170.0 discovered and enabled the installed project skill through its local skills API. Three fresh reviewer agents independently assessed the synthetic author replies. The same R1 agent then assessed a targeted clarification. The recorded panel and manuscript exercise are linked from the tutorial. Claude Code installation is documented; this verification used Codex.

One paired English strategy exercise used eight de-identified review questions from eight held-out public submissions with the same instructions, model settings and 95-word target per question. Both arms received the same materials and neither saw later author replies or outcomes. A separate agent judged masked outputs, with labels varied across cases. The skill-assisted arm was preferred on three questions, five were ties, and the ordinary-prompt arm was preferred on zero. The judge favored a concrete illustration of a two-way distribution dependence, a more precise way to locate a rank factor in a proof, and explicit handling of methods unable to consume a seasonal-period input. The mathematical generalization in the first example still needed proof. This was one automated judge and one generation per arm; it evaluated planning, with no human preference or acceptance outcome measured.
