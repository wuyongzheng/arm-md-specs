## D13.8 Event threshold and edge counting

ICJGPM

When FEAT\_PMUv3\_TH is implemented, software can program an event counter to only count when the event described by PMEVTYPER&lt;n&gt;\_EL0 meets a threshold condition. The supported threshold conditions are:

- Less-than.
- Greater-than-or-equal-to.
- Not-equals.
- Equal-to.

INJMGF FEAT\_PMUv3\_EDGE is an optional extension to FEAT\_PMUv3\_TH that adds edge-detection logic to support counting threshold crossing events.

IVBVHX

FEAT\_PMUv3\_TH2 is an optional extension to FEAT\_PMUv3\_TH and FEAT\_PMUv3\_EDGE that adds additional controls for event counter linking.

RHVGCV

RQVYDV

RGWTCZ

When FEAT\_PMUv3\_TH is implemented:

- If PMEVTYPER&lt;n&gt;\_EL0.TC is not 0b000 or PMEVTYPER&lt;n&gt;\_EL0.TH is nonzero, then threshold counting for event counter &lt;n&gt; is enabled.
- If PMEVTYPER&lt;n&gt;\_EL0.TC is 0b000 and PMEVTYPER&lt;n&gt;\_EL0.TH is zero, then threshold counting for event counter &lt;n&gt; is disabled.

When FEAT\_PMUv3\_TH is not implemented, the Effective values of PMEVTYPER&lt;n&gt;\_EL0.{TC, TH} are { 0b000 , 0}.

When FEAT\_PMUv3\_EDGE is implemented:

- If PMEVTYPER&lt;n&gt;\_EL0.TE is 1, edge counting for event counter &lt;n&gt; is enabled.
- If PMEVTYPER&lt;n&gt;\_EL0.TE is 0, edge counting for event counter &lt;n&gt; is disabled.

RSGLNM When FEAT\_PMUv3\_EDGE is not implemented, the Effective value of PMEVTYPER&lt;n&gt;\_EL0.TE is 0.

RHXHZC

When FEAT\_PMUv3\_TH2 is implemented, for each odd-numbered event counter &lt;n&gt;, PMEVTYPER&lt;n&gt;\_EL0.TLC controls linking event counter &lt;n&gt; to event counter &lt;n-1&gt;.

RMRPVL

RJJRJQ

ILQXJZ

When FEAT\_PMUv3\_TH2 is not implemented or &lt;n&gt; is even, the Effective value of PMEVTYPER&lt;n&gt;\_EL0.TLC is zero.

The values V B [ n ] , C T [ n ] , V T [ n ] , C P [ n ] , C E [ n ] , V E [ n ] , and V [ n ] for an event counter &lt;n&gt; are defined as follows:

- V B [ n ] is the (base) value the counter increments by when threshold counting is disabled and edge counting is disabled for the event counter &lt;n&gt;.
- C T [ n ] is the result of evaluating the threshold condition. C T [ n ] is always one (TRUE) or zero (FALSE).
- V T [ n ] is the value that results from applying the threshold condition:
- -When FEAT\_PMUv3\_TH2 is not implemented or n is even, V T [ n ] is one of V B [ n ] , one, or zero.
- -When FEAT\_PMUv3\_TH2 is implemented and n is odd, V T [ n ] is one of V [ n -1] , V B [ n ] , one, or zero.
- C P [ n ] is the value C T [ n ] took on the previous cycle if counting the event was allowed on the previous cycle, and zero otherwise. C P [ n ] is always one (TRUE) or zero (FALSE).
- C E [ n ] is the result of evaluating the edge condition. C E [ n ] is always one (TRUE) or zero (FALSE).
- V E [ n ] is the value that results from applying the edge condition:
- -When FEAT\_PMUv3\_TH2 is not implemented or n is even, V E [ n ] is always C E [ n ] , that is, one (TRUE) or zero (FALSE).
- -When FEAT\_PMUv3\_TH2 is implemented and n is odd, V E [ n ] is one of V [ n -1] , one, or zero.
- V [ n ] is the value that results from applying both the threshold and edge conditions. V [ n ] is one of V E [ n ] , V T [ n ] , or V B [ n ] , depending on the configuration of counter &lt;n&gt;.

If an event counter &lt;m&gt; is disabled, then V B [ m ] , C T [ m ] , V T [ m ] , and V [ m ] are all zero.

For even-numbered event counters, PMEVTYPER&lt;n&gt;\_EL0.TLC is RES0. For odd-numbered event counters, the following combinations of values are reserved:

- PMEVTYPER&lt;n&gt;\_EL0.TLC[1:0] is 0b11 .

RWXVGN

IHNHNC

IQLJJP

RXFGYS

- PMEVTYPER&lt;n&gt;\_EL0.{TC[0], TE, TLC[1:0]} is {1, 0, 0b10 }.
- PMEVTYPER&lt;n&gt;\_EL0.{TE, TLC[1:0]} is {1, 0b01 }.

For all event counters, the following combination is reserved:

- PMEVTYPER&lt;n&gt;\_EL0.{TC[1:0], TE} is { 0b00 , 1}.

The effect of setting PMEVTYPER&lt;n&gt;\_EL0.{TC, TE, TLC} to reserved values is CONSTRAINED UNPREDICTABLE. See Reserved values in System and memory-mapped registers and translation table entries.

The threshold condition for event counter &lt;n&gt;, denoted by the value C T [ n ] , is controlled by PMEVTYPER&lt;n&gt;\_EL0.{TC, TH}.

C T [ n ] is defined as follows, where TC and TH are the Effective values of PMEVTYPER&lt;n&gt;\_EL0.{TC, TH} respectively:

̸

<!-- formula-not-decoded -->

Example D13-4 Incrementing event counter n by V B [ n ] when V B [ n ] meets the threshold condition When all of the following are true, the event counter n will increment by four:

- PMEVTYPER&lt;n&gt;\_EL0.TC is 0b010 , equals, meaning threshold counting for event counter n is enabled.
- PMEVTYPER&lt;n&gt;\_EL0.TH is 4.
- PMEVTYPER&lt;n&gt;.evtCount is 0x003F , STALL\_SLOT.
- There are exactly four operation Slots not occupied by an operation Attributable to the PE on the cycle.

Example D13-5 Incrementing event counter n by 1 when V B [ n ] meets the threshold condition

When all of the following are true, the event counter n will increment by one:

- PMEVTYPER&lt;n&gt;\_EL0.TC is 0b101 , greater-than-or-equal, count, meaning threshold counting for event counter n is enabled.
- PMEVTYPER&lt;n&gt;\_EL0.TH is 2.
- PMEVTYPER&lt;n&gt;.evtCount is 0x80C1 , FP\_FIXED\_OPS\_SPEC.
- At least two non-scalable floating-point operations are issued on the cycle. For example:
- -Two floating-point add instructions.
- -One floating-point multiply-add instruction

RNXPYM The edge condition for event counter &lt;n&gt;, denoted by the value C E [ n ] C [ n ] is defined as follows, where TC is the Effective value of PMEVTYPER&lt;n&gt;\_EL0.TC:

, is controlled by PMEVTYPER&lt;n&gt;\_EL0.TC[0]. E

̸

<!-- formula-not-decoded -->

̸

When &lt;n&gt; is odd, the result of applying the threshold condition for event counter &lt;n&gt;, denoted by the value V T [ n ] , is controlled by PMEVTYPER&lt;n&gt;\_EL0.{TC, TLC}.

V T [ n ] for an odd counter &lt;n&gt; is defined as follows, where TC and TLC are the Effective values of PMEVTYPER&lt;n&gt;\_EL0.{TC, TLC} respectively:

<!-- formula-not-decoded -->

RFLGYG

RYKFCB

IGNYJH

IXWZRM

When &lt;n&gt; is odd, the result of applying the edge condition for event counter &lt;n&gt;, denoted by the value V E [ n ] , is controlled by PMEVTYPER&lt;n&gt;\_EL0.TLC.

V E [ n ] for an odd counter &lt;n&gt; is defined as follows, where TLC is the Effective value of PMEVTYPER&lt;n&gt;\_EL0.TLC:

Note

<!-- formula-not-decoded -->

The input V [ n -1] from event counter &lt;n-1&gt; to the functions for event counter &lt;n&gt; in RXFGYS and RFLGYG is the result of applying the threshold and edge conditions to event counter &lt;n-1&gt; defined by RHBWBB, and not the base value for event counter &lt;n-1&gt;, V B [ n -1] .

When &lt;n&gt; is even, the result of applying the threshold condition for event counter &lt;n&gt;, denoted by value V T [ n ] , is controlled by PMEVTYPER&lt;n&gt;\_EL0.TC.

V T [ n ] for an even counter &lt;n&gt; is defined as follows, where TC is the value of PMEVTYPER&lt;n&gt;\_EL0.TC:

<!-- formula-not-decoded -->

RBGDTJ When &lt;n&gt; is even, the result of applying the edge condition for event counter &lt;n&gt;, denoted by the value V E [ n ] , is as defined as follows:

<!-- formula-not-decoded -->

IHZBBG RYKFCB and RBGDTJ are subsets of RXFGYS and RFLGYG, respectively, that apply when the Effective value of PMEVTYPER&lt;n&gt;\_EL0.TLC is zero, and therefore also apply when FEAT\_PMUv3\_TH2 is not implemented, regardless of whether &lt;n&gt; is even or odd.

RHBWBB The value of V [ n ] for event counter &lt;n&gt; is defined as follows, where TC , TH , and TE are the Effective values of PMEVTYPER&lt;n&gt;\_EL0.{TC, TH, TE} respectively:

̸

̸

The pseudocode function PMUCountValue() in A-profile Architecture Pseudocode describes this.

<!-- formula-not-decoded -->

## Example D13-6 Using edge counting without threshold counting

To use edge counting without threshold counting, for example for a single-bit event (that is, V B[n] is either 0 or 1):

- Set PMEVTYPER&lt;n&gt;\_EL0.TH to 0.
- Set PMEVTYPER&lt;n&gt;\_EL0.TE to 1.
- Set PMEVTYPER&lt;n&gt;\_EL0.TC to:
- -0b001 for a leading edge (zero to nonzero) count.
- -0b011 for a falling edge (nonzero to zero) count.
- -0b010 to count both edges.

RXFGYS and RFLGYG describe the following permitted combinations for an event counter &lt;n&gt; when FEAT\_PMUv3\_TH2 is implemented and &lt;n&gt; is odd:

IGBTTP

Table D13-5 Count value when PMEVTYPER&lt;n&gt;\_EL0.TE is 0, FEAT\_PMUv3\_TH2 is implemented, and &lt;n&gt; is odd

|     | TLC   |   TC[0] | If C T [ n ] is TRUE, count by   | If C T [ n ] is FALSE, count by   |
|-----|-------|---------|----------------------------------|-----------------------------------|
| (A) | 0b00  |       0 | V B [ n ]                        | 0                                 |
| (B) | 0b00  |       1 | 1                                | 0                                 |
| (C) | 0b01  |       0 | V B [ n ]                        | V [ n - 1]                        |
| (D) | 0b01  |       1 | 1                                | V [ n - 1]                        |
| (E) | 0b10  |       0 | V [ n - 1]                       | 0                                 |

Table D13-6 Count value when PMEVTYPER&lt;n&gt;\_EL0.TE is 1, FEAT\_PMUv3\_TH2 is implemented, and &lt;n&gt; is odd

|     | TLC   |   TC[0] | If C E [ n ] is TRUE, count by   |   If C E [ n ] is FALSE, count by |
|-----|-------|---------|----------------------------------|-----------------------------------|
| (F) | 0b00  |       1 | 1                                |                                 0 |
| (G) | 0b10  |       1 | V [ n - 1]                       |                                 0 |

RYKFCB and RBGDTJ describe the following permitted combinations for an event counter &lt;n&gt; when FEAT\_PMUv3\_TH2 is not implemented or &lt;n&gt; is even:

Table D13-7 Count value when PMEVTYPER&lt;n&gt;\_EL0.TE is 0, and FEAT\_PMUv3\_TH2 is not implemented or &lt;n&gt; is even

|     |   TC[0] | If C T [ n ] is TRUE, count by   |   If C T [ n ] is FALSE, count by |
|-----|---------|----------------------------------|-----------------------------------|
| (A) |       0 | V B [ n ]                        |                                 0 |
| (B) |       1 | 1                                |                                 0 |

Table D13-8 Count value when PMEVTYPER&lt;n&gt;\_EL0.TE is 1, and FEAT\_PMUv3\_TH2 is not implemented or &lt;n&gt; is even

|     |   TC[0] |   If C E [ n ] is TRUE, count by |   If C E [ n ] is FALSE, count by |
|-----|---------|----------------------------------|-----------------------------------|
| (F) |       1 |                                1 |                                 0 |

RMRLWN

IYTVPB

Example D13-7 Using linking to count the logical combination of the inputs to two other counters FEAT\_PMUv3\_TH2 allows the following linking functions to be defined, when using a threshold value of zero:

|      | Function                       | Equivalent function   | Equivalent function   |   Equivalent function | Equivalent function   | Equivalent function   | Equivalent function   | Equivalent function   | Use   |
|------|--------------------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-------|
| (1a) | V B [ n ] AND V B [ n - 1]     | if V_B[n]             | ==                    |                     0 | then                  | V[n-1]                | or                    | 0                     | (E)   |
| (1b) | V B [ n ] AND V B [ n - 1]     | if V_B[n]             | ==                    |                     0 | then                  | V_B[n]                | else                  | V[n-1]                | (C)   |
| (2)  | V B [ n ] OR V B [ n - 1]      | if V_B[n]             | !=                    |                     0 | then                  | 1 else                | V[n-1]                |                       | (D)   |
| (3)  | V B [ n ] OR V B [ n - 1]      | if V_B[n]             | !=                    |                     0 | then                  | V_B[n]                | else                  | V[n-1]                | (C)   |
| (4)  | NOT V B [ n ] AND V B [ n - 1] | if V_B[n]             | ==                    |                     0 | then                  | V[n-1]                | else                  | 0                     | (E)   |
| (5)  | NOT V B [ n ] OR V B [ n 1]    | if V_B[n]             | ==                    |                     0 | then                  | 1 else                | V[n-1]                |                       | (D)   |

-

How event counter &lt;n-1&gt; is configured also affects the output, as the results for (C), (D), and (E) depend on V [ n -1] , and not V B [ n -1] . For example:

- In examples (2) and (5), event counter &lt;n-1&gt; might need to be configured such that its threshold mechanism delivers V [ n -1] as zero or one. That is, using configuration (B).
- Event counter &lt;n-1&gt; might be configured so that V [ n -1] is zero when V B [ n -1] is nonzero, and one otherwise.
- Threshold counting might be disabled on event counter &lt;n-1&gt; meaning the counter counts the base value for event counter &lt;n-1&gt; is counted when the threshold condition on event counter &lt;n&gt; is not met.

Other threshold values can be used to define richer functions. For example, increment the counter by V B [ n -1] only if V B [ n ] ≥ X .

Two PMU events are coincident if they are synchronous in the implementation, meaning they are counted at the same time. It is IMPLEMENTATION DEFINED which events are coincident.

Note

An implementation typically includes a pipeline for executing instructions. An instruction might generate events at any stage in the pipeline. Unless the implementation explicitly synchronizes these events, which is unlikely in the general case due to the implementation cost, these events would not be coincident despite being generated by the same instruction. Two events generated by different instructions might be coincident due to instruction-level parallelism.

Linked PMU event counters can only be meaningfully used with coincident events.