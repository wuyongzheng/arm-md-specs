## F5.1.210 SRS, SRSDA, SRSDB, SRSIA, SRSIB

Store Return State stores the LR\_&lt;current\_mode&gt; and SPSR\_&lt;current\_mode&gt; to the stack of a specified mode. For information about memory accesses see Memory accesses.

SRS is UNDEFINED in Hyp mode.

SRS is CONSTRAINED UNPREDICTABLE if it is executed in User or System mode, or if the specified mode is any of the following:

- Not implemented.
- Amode that AArch32 PE modes does not show.
- Hyp mode.
- Monitor mode, if the SRS instruction is executed in Non-secure state.

If EL3 is using AArch64 and an SRS instruction that is executed in a Secure EL1 mode specifies Monitor mode, it is trapped to EL3.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the Decrement After variant

```
Applies when (P == 0 && U == 0) SRSDA{<c>}{<q>} SP{!}, #<mode>
```

## Encoding for the Decrement Before variant

```
Applies when (P == 1 && U == 0) SRSDB{<c>}{<q>} SP{!}, #<mode>
```

## Encoding for the Increment After variant

```
Applies when (P == 0 && U == 1) SRS{IA}{<c>}{<q>} SP{!}, #<mode>
```

## Encoding for the Increment Before variant

```
Applies when (P == 1 && U == 1) SRSIB{<c>}{<q>} SP{!}, #<mode>
```

## Decode for all variants of this encoding

```
constant boolean wback = (W == '1'); constant boolean increment = (U == '1'); constant boolean wordhigher = (P == U);
```

T1

<!-- image -->

## Encoding

```
SRSDB{<c>}{<q>} SP{!}, #<mode>
```

## Decode for this encoding

```
constant boolean wback = (W == '1'); constant boolean increment = FALSE; constant boolean wordhigher = FALSE;
```

T2

<!-- image -->

## Encoding

```
SRS{IA}{<c>}{<q>} SP{!}, #<mode>
```

## Decode for this encoding

```
constant boolean wback = (W == '1'); constant boolean increment = TRUE; constant boolean wordhigher = FALSE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly SRS (T32) and SRS (A32).

## Assembler Symbols

<!-- image -->

For the 'Decrement After', 'Decrement Before', 'Increment After', and 'Increment Before' variants: see Standard assembler syntax fields. &lt;c&gt; must be AL or omitted.

For the 'T1' and 'T2' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

The address adjusted by the size of the data loaded is written back to the base register. If specified, it is encoded in the 'W' field as 1, otherwise this field defaults to 0.

<!-- image -->

!

## &lt;mode&gt;

Is the number of the mode whose Banked SP is used as the base register, encoded in the 'mode' field. For details of PE modes and their numbers see AArch32 state PE modes.

## IA

For the 'Increment After' variant: is an optional suffix to indicate the Increment After variant.

For the 'T2' variant: is an optional suffix for the Increment After form.

SRSFA , SRSEA , SRSFD , and SRSED are pseudo-instructions for SRSIB , SRSIA , SRSDB , and SRSDA respectively, referring to their use for pushing data onto Full Ascending, Empty Ascending, Full Descending, and Empty Descending stacks.

## Operation

```
if CurrentInstrSet() == InstrSet_A32 then if ConditionPassed() then EncodingSpecificOperations(); if PSTATE.EL == EL2 then // UNDEFINED at EL2 UNDEFINED; // Check for UNPREDICTABLE cases. The definition of UNPREDICTABLE does not permit these // to be security holes if PSTATE.M IN {M32_User,M32_System} then UNPREDICTABLE; elsif mode == M32_Hyp then // Check for attempt to access Hyp mode SP UNPREDICTABLE; elsif mode == M32_Monitor then // Check for attempt to access Monitor mode SP if !HaveEL(EL3) || CurrentSecurityState() != SS_Secure then UNPREDICTABLE; elsif !ELUsingAArch32(EL3) then AArch64.MonitorModeTrap(); elsif BadMode(mode) then UNPREDICTABLE; constant bits(32) base = Rmode[13,mode]; bits(32) address = if increment then base else base-8; if wordhigher then address = address+4; MemA[address,4] = LR; MemA[address+4,4] = SPSR_curr[]; if wback then Rmode[13,mode] = if increment then base+8 else base-8; else if ConditionPassed() then EncodingSpecificOperations(); if PSTATE.EL == EL2 then // UNDEFINED at EL2 UNDEFINED; // Check for UNPREDICTABLE cases. The definition of UNPREDICTABLE does not permit these // to be security holes if PSTATE.M IN {M32_User,M32_System} then UNPREDICTABLE; elsif mode == M32_Hyp then // Check for attempt to access Hyp mode SP UNPREDICTABLE; elsif mode == M32_Monitor then // Check for attempt to access Monitor mode SP if !HaveEL(EL3) || CurrentSecurityState() != SS_Secure then UNPREDICTABLE; elsif !ELUsingAArch32(EL3) then AArch64.MonitorModeTrap(); elsif BadMode(mode) then UNPREDICTABLE; constant bits(32) base = Rmode[13,mode]; bits(32) address = if increment then base else base-8; if wordhigher then address = address+4; MemA[address,4] = LR;
```

```
MemA[address+4,4] = SPSR_curr[]; if wback then Rmode[13,mode] = if increment then base+8 else base-8;
```

## CONSTRAINED UNPREDICTABLE behavior

If PSTATE.M IN {M32\_User,M32\_System} , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

If mode == M32\_Hyp , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

If mode == M32\_Monitor &amp;&amp; (!HaveEL(EL3) || CurrentSecurityState() != SS\_Secure) , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

If BadMode(mode) , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction stores to the stack of the mode in which it is executed.
- The instruction stores to an UNKNOWN address, and if the instruction specifies writeback then any general-purpose register that can be accessed from the current Exception level without a privilege violation becomes UNKNOWN.