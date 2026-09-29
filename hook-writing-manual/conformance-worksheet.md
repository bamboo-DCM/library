# Hook registration conformance worksheet

Complete one worksheet per live registration. Do not merge byte-identical
registrations or inherit an old inventory count.

## Identity

| Field | Value | Evidence |
|---|---|---|
| Registration ID |  |  |
| Runtime and version |  |  |
| Registry address |  |  |
| Event |  |  |
| Matcher |  |  |
| Ordered command and arguments |  |  |
| Timeout |  |  |
| Body path and hash |  |  |
| Trust state |  |  |
| Native delivery evidence |  |  |

## Policy and effects

| Question | Answer | Evidence |
|---|---|---|
| What single purpose does this registration have? |  |  |
| What exact effect and credible downside justify its tier? |  |  |
| Which named source owns the policy? |  |  |
| Typed results supported |  |  |
| `authority_delta` |  |  |
| Declared reads |  |  |
| Declared writes |  |  |
| Declared outward effects |  |  |
| Failure direction by failure mode, including the hook's own failure |  |  |
| Authorization inputs and attributed actor |  |  |

## Matching and evidence

| Question | Answer | Evidence |
|---|---|---|
| What grammar or event schema is parsed? |  |  |
| What syntax is unsupported? |  |  |
| How are paths and target identities normalized? |  |  |
| How are root agents, subagents and other actors distinguished? |  |  |
| How is the decision bound to the effect-time identity? |  |  |

## Liveness and recovery

| Question | Answer | Evidence |
|---|---|---|
| Local attempt/continuation budget, counting signal and every context in which it is observable |  |  |
| Aggregate session/workflow budget and its carrier registration |  |  |
| No-progress rule |  |  |
| Timeout and child-cancellation behavior |  |  |
| Failure modes disposed by the runtime rather than the hook, and their measured direction, per host and runtime version; an unmeasured mode is UNKNOWN, not a direction |  |  |
| Dependency-graph cycle status |  |  |
| Independent rescue or last-known-good route |  |  |
| Rescue test with primary control unavailable |  |  |
| Idempotency key and duplicate-invocation result |  |  |

## Required test families

Mark a row `PASS`, `FAIL` or `INAPPLICABLE` with a reason. A case count is not
branch-reachability evidence.

| Family | Result | Receipt or reason |
|---|---|---|
| Must-deny |  |  |
| Must-allow, rerun under any refuse-on-own-failure classifier |  |  |
| Quotation/example/near-neighbour negatives |  |  |
| Malformed and empty input |  |  |
| Missing dependency, including the hook's own internal fault for refuse-on-failure registrations |  |  |
| Repeat, no-progress and escape exhaustion, including the typed result at exhaustion |  |  |
| Actor/provenance |  |  |
| Concurrency and TOCTOU |  |  |
| Wiring and trust |  |  |
| Native delivery |  |  |
| Multi-hook order and cycle |  |  |
| Required-route failure |  |  |
| Rescue completion |  |  |
| Mutation proof for protection |  |  |
| Mutation proof for escape |  |  |
| Zero hidden writes/effects |  |  |

## Lifecycle and disposition

| Field | Value | Evidence |
|---|---|---|
| Lifecycle state | proposed / shadow / advisory / blocking / maintained / superseded / retired |  |
| Promotion evidence |  |  |
| Retirement registration census |  |  |
| Current audit disposition | fix-now / follow-on / accepted-exception / no-change / UNKNOWN |  |
| Disposition owner |  |  |
| Risk and expiry/reopen trigger |  |  |
| Exception acceptance date, competent owner and priced risk |  |  |
| Separately authorized repair receipt, if any |  |  |

`UNKNOWN` means the audit is incomplete. The worksheet does not authorize a
repair, a new project or an outward effect.
