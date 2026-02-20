## F5.1.300 WFE

Wait For Event is a hint instruction that indicates that the PE can enter a low-power state and remain there until a wakeup event occurs. Wakeup events include the event signaled as a result of executing the SEV instruction on any PE in the multiprocessor system. For more information, see Wait For Event and Send Event.

As described in Wait For Event and Send Event, the execution of a WFE instruction that would otherwise cause entry to a low-power state can be trapped to a higher Exception level, see HCR.TWE, SCR.TWE, and SCTLR.nTWE.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

WFE{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

// No additional decoding required

T1

## Encoding

WFE{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

// No additional decoding required

T2

<!-- image -->

## Encoding

WFE{&lt;c&gt;}.W

Listing F5-89

<!-- image -->

Listing F5-90

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

Listing F5-92

```
if ConditionPassed() then EncodingSpecificOperations(); if IsEventRegisterSet() then ClearEventRegister(); else if HaveEL(EL3) && EL3SDDUndefPriority() then // Check for traps described by the Secure Monitor. // If the trap is enabled, the instruction will be UNDEFINED because EDSCR.SDD is 1. AArch32.CheckForWFxTrap(EL3, WFxType_WFE); end if PSTATE.EL == EL0 then // Check for traps described by the OS. AArch32.CheckForWFxTrap(EL1, WFxType_WFE); end if PSTATE.EL IN {EL0, EL1} && EL2Enabled() && !IsInHost() then // Check for traps described by the Hypervisor. AArch32.CheckForWFxTrap(EL2, WFxType_WFE); end if HaveEL(EL3) && PSTATE.M != M32_Monitor then // Check for traps described by the Secure Monitor. AArch32.CheckForWFxTrap(EL3, WFxType_WFE); end WaitForEvent(); end end
```