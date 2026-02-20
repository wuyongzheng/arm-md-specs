## F5.1.53 ESB

Error Synchronization Barrier is an error synchronization event that might also update DISR and VDISR. This instruction can be used at all Exception levels and in Debug state.

In Debug state, this instruction behaves as if SError interrupts are masked at all Exception levels. For more information, see RAS PE architecture and Arm ® Reliability, Availability, and Serviceability (RAS) System Architecture, for A-profile architecture (ARM IHI 0100).

If FEAT\_RAS is not implemented, this instruction executes as a NOP .

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

(FEAT\_RAS)

<!-- image -->

## Encoding

ESB{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_RAS) then ExecuteAsNOP(); end if cond != '1110' then UNPREDICTABLE; end // ESB must be encoded with AL condition

## CONSTRAINED UNPREDICTABLE behavior

If cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes unconditionally.
- The instruction executes conditionally.

T1

(FEAT\_RAS)

<!-- image -->

## Encoding

ESB{&lt;c&gt;}{&lt;q&gt;}

Listing F5-40

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_RAS) then ExecuteAsNOP(); end if InITBlock() then UNPREDICTABLE; end
```

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes unconditionally.
- The instruction executes conditionally.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); SynchronizeErrors(); AArch32.ESBOperation(); if PSTATE.EL IN {EL0, EL1} && EL2Enabled() then AArch32.vESBOperation(); elsif IsFeatureImplemented(FEAT_E3DSE) && PSTATE.EL != EL3 && !ELUsingAArch32(EL3) then AArch64.dESBOperation(); end TakeUnmaskedSErrorInterrupts(); end
```

Listing F5-42