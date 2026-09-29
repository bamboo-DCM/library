# Write hooks that do not trap the work

> **Public edition · version 1.0.1-share · 29 September 2026**  
> A practical manual for building AI-agent hooks that remain finite, authority-neutral and recoverable.

Published by [Bamboo DCM](https://bamboodcm.com).

This is the public edition of a method Bamboo maintains internally; the internal edition is canonical.

A hook runs at a boundary: before a tool call, after a write, when an agent stops,
or when a permission decision is about to be shown. That makes hooks useful. It
also gives a small script the power to delay valid work, hide an approval,
manufacture another model turn or make its own repair impossible.

The central rule is simple:

> A hook may enforce an authority that already exists. It may not become the
> authority, and it may not make itself indispensable to recovery.

This manual gives you a method, a worksheet and a test floor. It does not promise
perfect controls. It aims for something more practical: when a hook is wrong,
the system reaches a finite, visible and recoverable outcome instead of an
expensive loop.

## Who this is for

Use this manual if you write lifecycle hooks, tool guards, permission callbacks,
admission checks or agent stop conditions. The method is runtime-neutral. You
still need the current documentation for the product and version you use.

The examples use generic names and synthetic paths. Adapt them to your runtime;
do not copy event fields or exit codes without checking the runtime's contract.

## 1. Treat the registration as the unit

The audit unit is one live **registration**:

- runtime and version;
- registry address;
- event;
- matcher;
- ordered command and arguments;
- timeout;
- body path and body hash;
- trust state;
- delivery evidence.

The same body registered twice is two control points. Two byte-identical bodies
can behave differently because one is unwired, untrusted, mapped to another
event or receiving a different payload. Record each registration separately.

Give each registration one purpose. Shared code is fine; a registration that
mixes several unrelated policy decisions is hard to reason about and harder to
recover from.

## 2. Classify the consequence before choosing the tier

Do not begin with “fail open” or “fail closed.” Begin with the effect the hook
governs and the credible downside of getting it wrong.

| Consequence | Starting posture |
|---|---|
| Confidentiality, access, payment, destructive or irreversible action, public or named-recipient dispatch | Blocking may be justified when a named policy owner already requires it |
| Material repository or data-integrity risk | Block only when the exact predicate and recovery can be shown |
| Formatting, metadata, process quality, documentation hygiene | Advisory or recorded debt by default |
| Missing dependency, dependency timeout, broken parser, absent trust or delivery evidence | `UNAVAILABLE` or `ERROR`, not a counterfeit policy denial |

A broken checker is evidence about the checker. It is not evidence that the
underlying action lacks authority.

The typed state and the runtime adapter's disposition of that state are separate
decisions. For a registration whose own failure could destroy or disclose rather
than merely fail to advise, the policy owner must record how `UNAVAILABLE` and
`ERROR` are handled. The conforming default for that consequence class is to
refuse the effect while reporting `UNAVAILABLE` or `ERROR`—never a counterfeit
`DENY`—and to name an independently operable rescue. This is a consequence test,
not a universal fail-closed slogan.

Where the runtime rather than the hook disposes of a failure mode—for example,
when the hook is killed at its timeout, its body cannot start or its delivery is
not native—the owner records that mode as runtime-disposed, measures its actual
direction and carries the residue explicitly. A failure mode is runtime-disposed
only when no hook code can execute after it occurs; any mode in which hook code
can still run, including an uncaught internal fault, is the hook's own failure
and takes the §2 default and the paired fixtures. The worksheet may not claim
that the hook refused an effect it never had the opportunity to evaluate.

A registration that refuses on its own failure needs paired fixtures. Inject an
internal fault after parsing as well as removing a dependency, verify that the
adapter reports `UNAVAILABLE` or `ERROR` with the declared disposition, and
rerun the must-allow set under the same classifier. The refusal is not conforming
if it swallows the ordinary allow path.

Blocking has a delivery cost. State it. A five-second false block repeated fifty
times is not free, and a loop that creates new model turns can spend far more than
time. Use the least restrictive control that still protects the named downside.

## 3. Define a typed result before the runtime adapter

Keep the hook's semantic result separate from the runtime's exit-code or JSON
protocol. Use at least these states:

- `ALLOW`: policy permits the exact action.
- `DENY`: policy forbids the exact action for a named reason.
- `UNAVAILABLE`: the decision could not be evaluated because a dependency or
  evidence source was unavailable.
- `ERROR`: the hook itself failed.
- `ADVISORY`: the action may continue, with a visible finding.
- `DEBT`: a known weakness or missing control is recorded without blocking the
  current action.

Then write one adapter per supported runtime. The adapter maps the typed result
to the runtime's documented behavior. Do not let an unsupported field, timeout
or child exit code decide policy accidentally.

Every result carries:

```text
registration_id
rule_version
event_id or tool_use_id
normalized_target_identity
result
reason_code
evidence
authority_delta
budget_consumed
observed_effect
```

`authority_delta` defaults to `none`. A finding may point to an existing owner or
procedure. It cannot create a reviewer, recipient, repair project, publication,
archive or deletion obligation that the governing policy did not already create.

Treat every authorization input as a separate typed contract. An input that
upgrades `DENY` to `ALLOW`, clears a block or consumes an escape must declare its
actor class—principal, agent, automation or the hook itself—and the runtime field
from which that actor is established. Agent-emitted text and the hook's own prior
output are never principal authorization. If the runtime cannot attribute the
input, return `UNAVAILABLE`, never `ALLOW`. Test the design session's own
transcript as the worst-case mention corpus.

## 4. Match executable intent, not textual mention

Hooks often receive strings that contain commands, file paths, prose, examples,
logs and quoted test data. A substring match cannot distinguish these roles.

Use the runtime's actual event shape. Parse or normalize the grammar you claim to
understand. If you support only a bounded dialect, say so and test the boundary.
Exact matching is suitable for an exact-string invariant; it is not a substitute
for parsing a language.

At minimum, test:

- the action that must match;
- a quoted mention of that action;
- an example in documentation;
- a near-neighbour tool or path;
- relative and absolute forms where the runtime allows both;
- malformed and empty payloads;
- unsupported syntax.

Unsupported input becomes a typed evidence gap. Do not quietly call it safe or
forbidden.

## 5. Keep observation separate from mutation

A pre-action decision should be a pure function of declared inputs wherever
possible. Hidden writes are forbidden.

Declare three sets:

1. **Reads:** files, environment fields, registries, APIs and state.
2. **Writes:** files, counters, locks, caches and receipts.
3. **Outward effects:** messages, network calls, approvals, task creation,
   publication or another system change.

Audit and lifecycle detection are read-only by default. If a mutation is needed,
give it a separate owner, authorization, idempotency key and receipt. Sequence
dependent effects and verify the first effect before starting the second.

A post-action advisory may report a landed write. It does not retroactively own,
undo or authorize that write.

## 6. Make repetition finite at two levels

A hook can be locally bounded and still participate in an unbounded system. For
example, the model retries, the hook requests another turn, a helper retries and
an external service retries. Four modest retry policies can multiply one request
into dozens of attempts.

Define both:

- a **local budget** for one registration; and
- an **aggregate continuation budget** for the composed session or workflow.

There is no universal correct number. Derive each limit from the work it protects,
the expected recovery time and the cost of another attempt.

Every retry needs changed state or new evidence. The same request against the
same state consumes budget and moves toward a terminal typed result. Budget or
escape exhaustion returns `UNAVAILABLE` with a reason code such as
`budget_exhausted` and takes the §2 disposition for the registration's
consequence class. A counter-based escape therefore never becomes an `ALLOW`
for a destructive or disclosing gate; its escape must be a route outside the
registration as required by §7. For registrations outside the destroy/disclose
class, exhaustion takes the failure direction the owner recorded on the
worksheet, advisory by default per the §2 table. Timeouts must state whether
child work is cancelled, detached or still capable of producing an effect; the
registration's own timeout kill is runtime-disposed under §2.

The no-progress and budget signals must be derivable from state the hook can
observe in every context in which the registration fires. A signal persisted in
only some contexts is an escape that does not exist in the others. Whatever
carries the aggregate continuation budget is itself a registration with a
declared write set and rescue, subject to the mutation rules in §5 and the cycle
rule in §7, and it may not sit inside the strongly connected component it
bounds.

For stop/continuation hooks, require:

- an objective completion predicate;
- a next action available to the receiving actor;
- a re-entry or generation marker;
- a no-progress rule;
- an attempt and elapsed-time budget;
- a terminal outcome that returns control instead of creating another turn.

## 7. Draw the dependency graph and break blocking cycles

Map each blocking control to the services, files, runtimes and other hooks it
needs. Include its repair and disable paths.

A blocking strongly connected component is a warning: control A needs B, B needs
C, and C needs A. It is nonconformant unless an edge outside that component can
reach a safe finite state.

Every blocking hook therefore needs one of these:

- an independently operable rescue path; or
- a last-known-good route that does not consult the failed component.

Test the rescue with the primary control unavailable. A rescue instruction that
calls the broken route is not rescue. A kill switch hidden behind the hook it
disables is not a kill switch.

Rescue does not erase genuine safety boundaries. It restores a safe way to apply
the already-governing authority.

## 8. Bind decisions to immutable identity

The checked object can change before the effect. Bind consequential decisions to
the identifier the runtime guarantees it will execute, the normalized input,
target hash/version and policy version. Re-read at effect time or use a
transaction where the platform supports one. Where the runtime offers neither,
record the check-to-effect window on the target object as an accepted residual in
the worksheet and test the symlink/rename case under family 6.

If identity moves, return `UNAVAILABLE` with reason code `stale` and reevaluate
under the same budget. Do not apply an approval or review from one generation to
its successor.

If the hook can mutate, make invocation idempotent. Replaying the same event twice
must not append twice, send twice, create a second task or accumulate new blocking
state. Idempotency must also hold across the active set: hooks can be individually
idempotent and oscillate when composed.

"No second effect" applies to outward effects, mutations and blocking state. The
receipt that records a replay is keyed by `event_id` or `tool_use_id`; it is the
evidence that the replay consumed budget instead of producing another effect.

## 9. Test the system, not the script

Use the [conformance worksheet](conformance-worksheet.md) to build the packet.
The minimum families are:

1. must-deny and must-allow, with must-allow rerun under any classifier that
   refuses on the registration's own failure;
2. quotations, examples and near neighbours;
3. malformed, empty and missing-dependency input, including an injected internal
   fault after parsing for any registration that refuses on its own failure;
4. repeat, no-progress and escape exhaustion in each actor context exposed under
   family 5;
5. root-agent and subagent/provenance cases where exposed;
6. concurrency and time-of-check/time-of-use cases where applicable;
7. wiring, trust and native delivery, separate from body parity;
8. multi-hook ordering, permutations and cycles;
9. end-to-end required-route failure and rescue completion;
10. mutation tests that prove both the protection and escape are causally live.

Mutation testing matters because a green test can observe the right answer without
depending on the line or branch it claims to guard. Change the relevant condition
deliberately and confirm the test fails.

A test that proves interception does not prove system soundness. The route must
also complete when it should, fail visibly when it cannot and recover through the
declared external path.

## 10. Promote slowly and retire completely

Use an explicit lifecycle:

```text
proposed → shadow/observe → advisory → blocking → maintained → superseded/retired
```

Blocking is earned by consequence and measured evidence. A genuine pre-existing
safety boundary may require blocking from the start, but the implementation still
needs observation, tests and recovery proof.

Retirement covers the complete registration. Remove every live registry entry,
verify absence, preserve historical evidence and keep the decision trace. A body
left on disk but unwired is not live; a body deleted while a different installed
copy remains registered is not retired.

Where a registry keys identity or trust by position, any insertion, reordering or
removal re-identifies neighbouring registrations. After a registry edit,
re-verify trust and delivery for every registration in that registry, not only
the changed one, and record trust and delivery per host rather than per fleet.

## Four synthetic examples

### A formatting check

A post-write hook finds a missing heading. No confidentiality, authority or data
integrity consequence exists. The right result is `ADVISORY`, with the exact file
and a suggested fix. It must not undo the write or require a process audit before
the user can continue.

### A destructive command guard

A pre-tool hook identifies a recursive deletion against a resolved target. A
named safety policy already forbids the effect. Blocking is justified if the
matcher distinguishes the exact executable intent, the error names a reversible
alternative and the rescue/disable route remains operable when the hook is broken.

### A missing publication helper

A policy permits an internal publication, but the preferred helper is unavailable.
The hook reports `UNAVAILABLE`; it does not claim the publication is forbidden.
The caller follows a separately owned, bounded recovery route and verifies the
effect. Repairing the helper becomes debt, not a prerequisite invented by the
hook.

### A stop hook with an impossible condition

A stop hook asks the agent to create evidence that the current actor cannot
access. Each continuation sees the same state. Without a no-progress rule, this
is a cost loop. A conforming hook consumes one bounded attempt, reports the missing
capability and returns control with a terminal result.

## Auditing an existing fleet

Do not inherit an inventory count. Recompute the current population from every
declared registry and admitted host surface. Preserve:

- duplicate registrations;
- registered bodies that are missing;
- body files that are unregistered;
- divergent bodies or adapters;
- excluded surfaces and the reason for exclusion;
- unknown trust or delivery state.

Audit each registration against the worksheet without changing it. End every row
in exactly one disposition:

- `fix-now`: a separately authorized repair is needed before the stated control
  can be relied on;
- `follow-on`: a bounded owner, test and reopen trigger are recorded;
- `accepted-exception`: a competent owner accepts the priced risk until an expiry
  or review trigger;
- `no-change`: current evidence supports the registration.

An `accepted-exception` whose expiry passes without dated renewal by a competent
owner, and a `follow-on` whose reopen trigger fires without a recorded action,
revert to `UNKNOWN` at the next audit and cannot count as conformity. The
exception record carries the acceptance date, owner and priced risk so the lapse
is detectable from the record alone.

`UNKNOWN` is incomplete. It is not conformity. A fleet audit never silently
repairs the fleet or creates a project merely because it found a defect.

## What this manual does not do

This manual does not choose your organization's authority, threat model or risk
appetite. It does not make every hook portable, prove that a vendor will preserve
an event contract, or guarantee that a tested hook will never fail.

It does not prescribe one fleet-wide fail direction or one retry number; failure
direction follows the consequence test in §2. It does not make a local hook a
security boundary against an actor who can disable it. It cannot prove native
delivery from source code or registry bytes alone.

The method does not require a new control for every error. An imperfect
process with good detection and a bounded adequacy repair can be safer and cheaper
than a control stack that tries to prevent every failure and traps the work.

## Sources

- [OpenAI Hooks](https://learn.chatgpt.com/docs/hooks)
- [Claude Code hooks reference](https://code.claude.com/docs/en/hooks)
- [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/)
- [Kubernetes admission-webhook good practices](https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/)
- [Git hooks](https://git-scm.com/docs/githooks)
- [GitHub webhook best practices](https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks)
- [Google SRE: Addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/)
- [Azure Circuit Breaker pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker)
- [AWS: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)
- [OPA policy testing](https://www.openpolicyagent.org/docs/policy-testing), [decision logs](https://www.openpolicyagent.org/docs/management-decision-logs) and [philosophy](https://www.openpolicyagent.org/docs/philosophy)
- [MITRE CWE-367: Time-of-check Time-of-use race condition](https://cwe.mitre.org/data/definitions/367)
- [JSON Schema](https://json-schema.org/learn/getting-started-step-by-step)
- [OpenTelemetry observability primer](https://opentelemetry.io/docs/concepts/observability-primer/)

## About the author

Arthur O'Keefe is Founder and Chief AI Officer of Bamboo DCM. A computer engineer by training, he has operated a nuclear reactor as a U.S. Navy submarine officer, built financial systems and helped build Movile and iFood as Movile’s Group CFO and Chief Strategy Officer. He builds systems of iteration and writes about the engineering and operating judgment that make them useful. A system of iteration is AI you can push back on. You can run it flat out for a weekend or park it for a week, then find the work waiting where you left it.

## About Bamboo DCM

Bamboo DCM is an independent structurer and distributor of corporate and structured credit in Brazil. We turn mid-market companies' growth-capital needs into transactions institutional investors can fund. Since 2022 we have brought over R$900 million to market across 25+ transactions, ~60% of them with first-time institutional issuers. We hold CVM coordinator (Resolution 161) and securitization (Resolution 60) licenses, and we are ANBIMA-adherent.

Regulated activities are conducted by Bamboo Securitizadora S.A. (CNPJ 48.343.871/0001-34), which acts as coordinator of public offerings under its CVM Resolution 161 coordinator license and issues and services CRI, CRA and debentures under CVM Resolution 60. This content is informational and is not an offer, recommendation or promise of returns.

## Contact and license

- **Arthur O'Keefe:** [arthur@bamboodcm.com](mailto:arthur@bamboodcm.com)
- **Felipe Moraes:** [felipe@bamboodcm.com](mailto:felipe@bamboodcm.com)
- **Urian Inhauser:** [urian@bamboodcm.com](mailto:urian@bamboodcm.com)

Free to share and adapt under [CC BY 4.0](../LICENSE) with attribution to
[Bamboo DCM](https://bamboodcm.com).

*This manual is part of the knowledge-systems framework Bamboo DCM uses for
AI-assisted execution in regulated finance. If the broader framework is useful
to your work, get in touch.*
