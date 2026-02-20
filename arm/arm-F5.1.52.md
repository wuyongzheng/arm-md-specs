## F5.1.52 ERET

Exception Return.

The PE branches to the address held in the register holding the preferred return address, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.

The register holding the preferred return address is:

- ELR\_hyp, when executing in Hyp mode.
- LR, when executing in a mode other than Hyp mode, User mode, or System mode.

The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.

Exception Return is CONSTRAINED UNPREDICTABLE in User mode and System mode.

In Debug state, the T1 encoding of ERET executes the DRPS operation.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

ERET{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

// No additional decoding required

T1

<!-- image -->

## Encoding

ERET{&lt;c&gt;}{&lt;q&gt;}

## Decode for this encoding

if InITBlock() &amp;&amp; !LastInITBlock() then UNPREDICTABLE; end

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

Listing F5-37

Listing F5-38

## Assembler Symbols

<!-- image -->

<!-- image -->

```
<c> See Standard assembler syntax fields. <q>
```

See Standard assembler syntax fields.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); if !Halted() then if PSTATE.M IN {M32_User,M32_System} then UNPREDICTABLE; // UNDEFINED or NOP else constant bits(32) new_pc_value = if PSTATE.EL == EL2 then ELR_hyp else R[14]; AArch32.ExceptionReturn(new_pc_value, SPSR_curr[]); end else // Perform DRPS operation in Debug state if PSTATE.M == M32_User then UNDEFINED; elsif PSTATE.M == M32_System then UNPREDICTABLE; // UNDEFINED or NOP else SynchronizeContext(); DebugRestorePSR(); end end end
```

## CONSTRAINED UNPREDICTABLE behavior

If PSTATE.M IN {M32\_User,M32\_System} , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

Listing F5-39