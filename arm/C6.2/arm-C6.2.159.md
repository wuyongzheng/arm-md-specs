## C6.2.159 ESB

Error synchronization barrier

This instruction is an error synchronization event that might also update DISR\_EL1 and VDISR\_EL2.

This instruction can be used at all Exception levels and in Debug state.

In Debug state, this instruction behaves as if SError interrupts are masked at all Exception levels. For more information, see RAS PE architecture and Arm ® Reliability, Availability, and Serviceability (RAS) System Architecture, for A-profile architecture (ARM IHI 0100).

If FEAT\_RAS is not implemented, this instruction executes as a NOP .

## System

(FEAT\_RAS)

<!-- image -->

## Encoding

ESB

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_RAS) then EndOfDecode(Decode_NOP);
```

## Operation

```
SynchronizeErrors(); AArch64.ESBOperation(); if PSTATE.EL IN {EL0, EL1} && EL2Enabled() then AArch64.vESBOperation(); elsif IsFeatureImplemented(FEAT_E3DSE) && PSTATE.EL != EL3 then AArch64.dESBOperation(); TakeUnmaskedSErrorInterrupts();
```
