## F5.1.160 RFE, RFEDA, RFEDB, RFEIA, RFEIB

Return From Exception loads two consecutive memory locations using an address in a base register:

- The word loaded from the lower address is treated as an instruction address. The PE branches to it.
- The word loaded from the higher address is used to restore PSTATE. This word must be in the format of an SPSR.

An address adjusted by the size of the data loaded can optionally be written back to the base register.

The PE checks the value of the word loaded from the higher address for an illegal return event. See Illegal return events from AArch32 state.

RFE is UNDEFINED in Hyp mode and CONSTRAINED UNPREDICTABLE in User mode.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the Decrement After variant

```
Applies when (P == 0 && U == 0) RFEDA{<c>}{<q>} <Rn>{!} // (Preferred syntax) RFEFA{<c>}{<q>} <Rn>{!} // (Alternate syntax, Full Ascending stack)
```

## Encoding for the Decrement Before variant

```
Applies when (P == 1 && U == 0) RFEDB{<c>}{<q>} <Rn>{!} // (Preferred syntax) RFEEA{<c>}{<q>} <Rn>{!} // (Alternate syntax, Empty Ascending stack)
```

## Encoding for the Increment After variant

Applies when

(P == 0

&amp;&amp;

U

==

1)

```
RFE{IA}{<c>}{<q>} <Rn>{!} // (Preferred syntax) RFEFD{<c>}{<q>} <Rn>{!} // (Alternate syntax, Full Descending stack)
```

## Encoding for the Increment Before variant

```
Applies when (P == 1 && U == 1) RFEIB{<c>}{<q>} <Rn>{!} // (Preferred syntax) RFEED{<c>}{<q>} <Rn>{!} // (Alternate syntax, Empty Descending stack)
```

## Decode for all variants of this encoding

```
'1');
```

```
constant integer n = UInt(Rn); constant boolean wback = (W == '1'); constant boolean increment = (U == constant boolean wordhigher = (P == U); if n == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
RFEDB{<c>}{<q>} <Rn>{!} // (Outside or last in IT block, preferred syntax) RFEFA{<c>}{<q>} <Rn>{!} // (Outside or last in IT block, alternate syntax, Full Ascending stack)
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant boolean wback = (W == '1'); constant boolean increment = FALSE; constant boolean wordhigher = FALSE; if n == 15 then UNPREDICTABLE; if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

T2

<!-- image -->

## Encoding

```
RFE{IA}{<c>}{<q>} <Rn>{!} // (Outside or last in IT block, preferred syntax) RFEFD{<c>}{<q>} <Rn>{!} // (Outside or last in IT block, alternate syntax, Full Descending stack)
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant boolean wback = (W == '1'); constant boolean increment = TRUE; constant boolean wordhigher = FALSE; if n == 15 then UNPREDICTABLE; if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

For the 'Decrement After', 'Decrement Before', 'Increment After', and 'Increment Before' variants: see Standard assembler syntax fields. &lt;c&gt; must be AL or omitted.

For the 'T1' and 'T2' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose base register, encoded in the 'Rn' field.

The address adjusted by the size of the data loaded is written back to the base register. If specified, it is encoded in the 'W' field as 1, otherwise this field defaults to 0.

For the 'Increment After' variant: is an optional suffix to indicate the Increment After variant.

For the 'T2' variant: is an optional suffix for the Increment After form.

RFEFA , RFEEA , RFEFD , and RFEED are pseudo-instructions for RFEDA , RFEDB , RFEIA , and RFEIB respectively, referring to their use for popping data from Full Ascending, Empty Ascending, Full Descending, and Empty Descending stacks.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); if PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL0 then UNPREDICTABLE; // UNDEFINED or NOP else bits(32) address = if increment then R[n] else R[n]-8; if wordhigher then address = address+4; constant bits(32) new_pc_value = MemA[address,4]; constant bits(32) spsr = MemA[address+4,4]; if wback then R[n] = if increment then R[n]+8 else R[n]-8; AArch32.ExceptionReturn(new_pc_value, spsr);
```

## CONSTRAINED UNPREDICTABLE behavior

If PSTATE.EL == EL0 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

&lt;q&gt;

## &lt;Rn&gt;

!

## IA