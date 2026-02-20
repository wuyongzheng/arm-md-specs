## F5.1.301 WFI

Wait For Interrupt is a hint instruction that indicates that the PE can enter a low-power state and remain there until a wakeup event occurs. For more information, see Wait For Interrupt.

As described in Wait For Interrupt, the execution of a WFI instruction that would otherwise cause entry to a low-power state can be trapped to a higher Exception level, see HCR.TWI, SCR.TWI, and SCTLR.nTWI.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

WFI{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

// No additional

decoding

T1

## Encoding

WFI{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

// No additional decoding required

T2

<!-- image -->

## Encoding

WFI{&lt;c&gt;}.W

required

Listing F5-93

<!-- image -->

Listing F5-94

## Decode for this encoding

// No additional decoding required

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

<!-- image -->

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields.
```

## Operation

Listing F5-96

```
if ConditionPassed() then EncodingSpecificOperations(); if !AArch32.InterruptPending() then if HaveEL(EL3) && EL3SDDUndefPriority() then // Check for traps described by the Secure Monitor. // If the trap is enabled, the instruction will be UNDEFINED because EDSCR.SDD is 1. AArch32.CheckForWFxTrap(EL3, WFxType_WFI); end if PSTATE.EL == EL0 then // Check for traps described by the OS. AArch32.CheckForWFxTrap(EL1, WFxType_WFI); end if PSTATE.EL IN {EL0, EL1} && EL2Enabled() && !IsInHost() then // Check for traps described by the Hypervisor. AArch32.CheckForWFxTrap(EL2, WFxType_WFI); end if HaveEL(EL3) && PSTATE.M != M32_Monitor then // Check for traps described by the Secure Monitor. AArch32.CheckForWFxTrap(EL3, WFxType_WFI); end WaitForInterrupt(); end end
```