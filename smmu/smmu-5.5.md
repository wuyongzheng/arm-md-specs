## 5.5 Fault configuration (A, R, S bits)

The STE contains fault configuration for faults derived from stage 2 translations (S2R, S2S) and the CD contains fault configuration for faults derived from stage 1 translations (A, R, S).

A applies to CD.A, R applies to STE.S2R and CD.R, S applies to STE.S2S and CD.S.

The A, R and S flags control fault behavior for transactions experiencing the following Translation-related faults during stage1 or stage 2 translation, see section 3.12 Fault models, recording and reporting :

- F\_TRANSLATION.
- F\_ACCESS.
- F\_ADDR\_SIZE.
- F\_PERMISSION.

Transactions are terminated with an abort if they encounter any other fault or configuration error and attempt to record an event in the relevant Event queue. This case is unaffected by the A, R and S flags.

When a transaction encounters one of the four Translation-related faults, it might be immediately terminated or stalled (in which case it is later retried, or terminated, according to software command).

The following flags are used to configure fault behavior:

| A   | Abort behavior upon transaction termination   | When set and a transaction experiencing one of the faults listed in this section is terminated, an abort or bus error is returned to the client device. When clear, such a transaction is completed successfully with RAZ/WI behavior so that the client does not receive an error condition. This configuration exists only for stage 1. The termination behavior of stage 2 is abort, as though an implied A == 1. An SMMUmight only implement abort termination (with no RAZ/WI support) and indicate this behavior through the SMMU_IDR0.TERM_MODEL flag. For these implementations, configuring CD.A == 0 renders the CD ILLEGAL. The A flag has no effect on faults arising from ATS Translation Requests, which do not support RAZ/WI behavior.   |
|-----|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R   | Record event                                  | When set, the detection of the fault is recorded in the Event queue. When clear, the fault record is suppressed. This field only suppresses a fault record if S == 0 and if the fault is of one of the four Translation-related faults.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## S Stall upon fault

When set, an incoming transaction experiencing one of the four Translation-related faults is stalled. No response is given to the transaction until software issues a resume or terminate command, whereupon the transaction is either retried or terminated. The stall is always reported and the R bit is ignored.

Configuration or faults not arising during stage 1 or stage 2 translation cause the transaction to be terminated, regardless of the setting of this bit.

When clear, an incoming transaction experiencing a fault is terminated immediately in a manner according to A.

The CD.S flag has no effect on Translation-related faults arising from ATS Translation Requests, for which a R == W == 0 response is given, see section 3.9.1 ATS interface .

Some implementations might not support stalling of eligible transactions and immediately terminate the transaction (with behavior determined by the A bit). Other implementations might not support immediate termination of transactions (that fault in a manner eligible to stall). Such implementations indicate these behaviors through the SMMU\_(S\_)IDR0.STALL\_MODEL field.

When stage 1 translation is enabled (STE.Config[0] == 1), an STE is considered ILLEGAL if:

- SMMU\_(S\_)IDR0.STALL\_MODEL != 0b00 and STE.S1STALLD == 1. A CD (Stage 1 translation enabled) is considered ILLEGAL if one of the following applies:
- SMMU\_(S\_)IDR0.STALL\_MODEL == 0b00 and STE.S1STALLD == 1 and CD.S == 1.
- SMMU\_(S\_)IDR0.STALL\_MODEL == 0b01 and CD.S == 1.
- SMMU\_(S\_)IDR0.STALL\_MODEL == 0b10 and CD.S == 0.

When stage 2 translation is enabled (STE.Config[1] == 1), an STE is considered ILLEGAL if one of the following applies:

- SMMU\_IDR0.STALL\_MODEL == 0b01 and STE.S2S == 1.
- SMMU\_IDR0.STALL\_MODEL == 0b10 and STE.S2S == 0.
- Note: If SMMU\_S\_IDR1.SEL2 == 0, Stage 2-enabled STEs cannot also be Secure.

When STE.S1STALLD == 1, STE.Config[0] == 1, and

SMMU\_R\_IDR0.STALL\_MODEL == 0b01 , this is ILLEGAL for the Realm programming interface and results in C\_BAD\_STE.

When STE.S2S == 1, STE.Config[1] == 1, and SMMU\_R\_IDR0.STALL\_MODEL == 0b01 , this is ILLEGAL for the Realm programming interface and results in C\_BAD\_STE.

## ARS

- 0b000 Silently terminate transactions at the SMMU, with writes acknowledged successfully and reads returning zero, RAZ/WI.
- 0b010 Terminate transactions at the SMMU in a RAZ/WI manner, but record fault event as well.
- 0bxx1 Stall transaction and record fault event.

In this case, the effective value of R is assumed to be 1 so that it is impossible for transactions to stall without an event being recorded.

Only the stalled transaction is held and subsequent non-faulting transactions in the same stream or substream might complete (subject to interconnect ordering rules) before the stall is resolved, see section 3.12.2 Stall model .

Later receipt of a CMD\_RESUME or CMD\_STALL\_TERM ensures that the transaction will be retried or terminated (with termination behavior given by the CMD\_RESUME operation).

- 0b100 Transaction abort reported to client, silent.
- 0b110 Transaction abort reported to client, fault event recorded.

Figure 5.1: Fault configuration flow

<!-- image -->

These flags can be used, in the following combinations, to affect transactions experiencing one of the four Translation-related faults:

Note: Although the STE has no A flag, stage 2 behavior is as though an effective A flag is fixed at 1.

Note: ARS == 0bxx1 is ILLEGAL when the SMMU does not support Stall behavior, or when an STE has explicitly disabled stage 1 stall configuration but stage 1 is configured to use it:

- A CD with CD.S == 1 is considered ILLEGAL if either of the following is true:
- -SMMU\_(*\_)IDR0.STALL\_MODEL == 0b00 and the CD is reached through an STE with STE.S1STALLD == 1.
- -SMMU\_(*\_)IDR0.STALL\_MODEL == 0b01 .
- A STE with STE.S2S == 1 is considered ILLEGAL if SMMU\_(*\_)IDR0.STALL\_MODEL == 0b01 .

Note: ARS == 0bxx0 is ILLEGAL when the SMMU forces Stall behavior:

- A CD with CD.S == 0 is considered ILLEGAL if SMMU\_(*\_)IDR0.STALL\_MODEL == 0b10 .
- A STE with stage 2 translation enabled and STE.S2S == 0 is considered ILLEGAL if SMMU\_IDR0.STALL\_MODEL == 0b10 .

Note: There is no separate Hit Under Previous Context Fault configuration as in prior SMMU architectures because those contain a different concept of in-register context configuration being in a stall state, whereas in SMMUv3 it is only the transaction that is stalled, separate from the configuration in memory. The treatment of stalls is therefore a per-stream or per-transaction concept rather than a per-translation context concept.

Where interconnect ordering rules allow, later transactions might overtake a stalled transaction associated with the same StreamID (and SubstreamID, if supplied with all transactions). A device might restrict ordering further if required. See section 3.12.2 Stall model for more details.