# Execution Modes

Use one of these operating modes explicitly when the task is ambiguous.

## `read-only`

Use for:
- research
- trend scans
- account inspection
- conversation mapping

Allowed:
- search
- read
- summarize
- draft nothing if the user only wants analysis

Forbidden:
- any public write action

## `draft-only`

Default mode for most writing tasks.

Use for:
- post drafting
- reply drafting
- visual briefs
- content planning

Allowed:
- produce candidate outputs
- produce final draft options

Forbidden:
- public write execution

## `review-ready`

Use when the user wants a near-final package to approve.

Allowed:
- final post text
- target-to-reply mapping
- execution checklist

Forbidden:
- execution before explicit approval

## `execute`

Use only when:
- preflight passed
- the exact approved scope is clear
- confirmation policy has been satisfied

Allowed:
- only the approved actions

Required output after running:
- exact actions attempted
- exact successes and failures
- any partial-success state
