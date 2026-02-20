## F5.1.39 CPS, CPSID, CPSIE

Change PE State changes one or more of the PSTATE.{A, I, F} interrupt mask bits and, optionally, the PSTATE.M mode field, without changing any other PSTATE bits.

CPS is treated as NOP if executed in User mode unless it is defined as being CONSTRAINED UNPREDICTABLE elsewhere in this section.

The PE checks whether the value being written to PSTATE.M is legal. See Illegal changes to PSTATE.M.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the Change mode variant

```
Applies when
```

```
(imod == 00 && M == 1) CPS{<q>} #<mode> // (Cannot be conditional)
```

## Encoding for the Interrupt disable variant

```
Applies when (imod == 11 && M == 0) CPSID{<q>} <iflags> // (Cannot be conditional)
```

## Encoding for the Interrupt disable and change mode variant

```
Applies when (imod == 11 && M == 1) CPSID{<q>} <iflags> , #<mode> // (Cannot
```

```
be conditional)
```

## Encoding for the Interrupt enable variant

```
Applies when (imod == 10 && M == 0) CPSIE{<q>} <iflags> // (Cannot be conditional)
```

## Encoding for the Interrupt enable and change mode variant

```
Applies when (imod == 10 && M == 1) CPSIE{<q>} <iflags> , #<mode> // (Cannot be conditional)
```

## Decode for all variants of this encoding

```
if mode != '00000' && M == '0' then UNPREDICTABLE; if (imod<1> == '1' && A:I:F == '000') || (imod<1> == '0' && A:I:F != '000') then UNPREDICTABLE; constant boolean enable = (imod == '10'); constant boolean disable = (imod == '11'); constant boolean changemode = (M == '1'); constant bits(5) pemode = mode; constant boolean affectA = (A == '1'); constant boolean affectI = (I == '1'); constant boolean affectF = (F == '1'); if (imod == '00' && M == '0') || imod == '01' then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If imod == '01' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

If imod == '00' &amp;&amp; M == '0' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

If mode != '00000' &amp;&amp; M == '0' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes with the additional decode: changemode = TRUE.
- The instruction executes as described, and the value specified by mode is ignored. There are no additional side-effects.

If imod&lt;1&gt; == '1' &amp;&amp; A:I:F == '000' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction behaves as if imod&lt;1&gt; == '0'.
- The instruction behaves as if A:I:F has an UNKNOWN nonzero value.

If imod&lt;1&gt; == '0' &amp;&amp; A:I:F != '000' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction behaves as if imod&lt;1&gt; == '1'.
- The instruction behaves as if A:I:F == '000'.

<!-- image -->

## Encoding for the Interrupt disable variant

```
Applies when (im == 1) CPSID{<q>} <iflags> // (Not permitted in IT block)
```

## Encoding for the Interrupt enable variant

```
Applies when (im == 0) CPSIE{<q>} <iflags> // (Not permitted in IT block)
```

T1

## Decode for all variants of this encoding

```
UNKNOWN;
```

```
if A:I:F == '000' then UNPREDICTABLE; constant boolean enable = (im == '0'); constant boolean disable = (im == '1'); constant boolean changemode = FALSE; constant boolean affectA = (A == '1'); constant boolean affectI = (I == '1'); constant boolean affectF = (F == '1'); constant bits(5) pemode = bits(5) if InITBlock() then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If A:I:F == '000' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

T2

```
111100111010(1)(1)(1)(1)10(0)0(0) 15 11 imod 10 9 M 8 A 7 I 6 F 5 mode 4 0
```

## Encoding for the Change mode variant

Applies when (imod == 00 &amp;&amp; M ==

```
1)
```

```
CPS{<q>} #<mode> // (Not permitted in IT block)
```

## Encoding for the Interrupt disable variant

```
Applies when (imod == 11 && M == 0) CPSID.W <iflags> // (Not permitted in IT block)
```

## Encoding for the Interrupt disable and change mode variant

```
Applies when (imod == 11 && M == 1) CPSID{<q>} <iflags>, #<mode> // (Not permitted in IT block)
```

## Encoding for the Interrupt enable variant

Applies when (imod == 10 &amp;&amp; M == 0)

```
CPSIE.W <iflags> // (Not permitted in IT block)
```

## Encoding for the Interrupt enable and change mode variant

Applies when (imod == 10 &amp;&amp; M ==

```
1)
```

```
CPSIE{<q>} <iflags>, #<mode> // (Not permitted in IT block)
```

## Decode for all variants of this encoding

```
if imod == '00' && M == '0' then SEE "Hint instructions"; if mode != '00000' && M == '0' then UNPREDICTABLE; if (imod<1> == '1' && A:I:F == '000') || (imod<1> == '0' && A:I:F != '000') then UNPREDICTABLE; constant boolean enable = (imod == '10'); constant boolean disable = (imod == '11'); constant boolean changemode = (M == '1'); constant bits(5) pemode = mode; constant boolean affectA = (A == '1'); constant boolean affectI = (I == '1'); constant boolean affectF = (F == '1'); if imod == '01' || InITBlock() then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If imod == '01' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

If mode != '00000' &amp;&amp; M == '0' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes with the additional decode: changemode = TRUE.
- The instruction executes as described, and the value specified by mode is ignored. There are no additional side-effects.

If imod&lt;1&gt; == '1' &amp;&amp; A:I:F == '000' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction behaves as if imod&lt;1&gt; == '0'.
- The instruction behaves as if A:I:F has an UNKNOWN nonzero value.

If imod&lt;1&gt; == '0' &amp;&amp; A:I:F != '000' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction behaves as if imod&lt;1&gt; == '1'.
- The instruction behaves as if A:I:F == '000'.

Hint instructions: In encoding T2, if the imod field is 0b00 and the M bit is 0b0 , a hint instruction is encoded. To determine which hint instruction, see Branches and miscellaneous control.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;mode&gt;

Is the number of the mode to change to, in the range 0 to 31, encoded in the 'mode' field.

## &lt;iflags&gt;

Is a sequence of one or more of the following, specifying which interrupt mask bits are affected:

- a Sets the A bit in the instruction, causing the specified effect on PSTATE.A, the SError interrupt mask bit.
- i Sets the I bit in the instruction, causing the specified effect on PSTATE.I, the IRQ interrupt mask bit.
- f Sets the F bit in the instruction, causing the specified effect on PSTATE.F, the FIQ interrupt mask bit.

## Operation

```
if CurrentInstrSet() == InstrSet_A32 then EncodingSpecificOperations(); if PSTATE.EL != EL0 then if enable then if affectA then PSTATE.A = '0'; if affectI then PSTATE.I = '0'; if affectF then PSTATE.F = '0'; if disable then if affectA then PSTATE.A = '1'; if affectI then PSTATE.I = '1'; if affectF then PSTATE.F = '1'; if changemode then // AArch32.WriteModeByInstr() sets PSTATE.IL to 1 if this is an illegal mode change. AArch32.WriteModeByInstr(pemode); else EncodingSpecificOperations(); if PSTATE.EL != EL0 then if enable then if affectA then PSTATE.A = '0'; if affectI then PSTATE.I = '0'; if affectF then PSTATE.F = '0'; if disable then if affectA then PSTATE.A = '1'; if affectI then PSTATE.I = '1'; if affectF then PSTATE.F = '1'; if changemode then // AArch32.WriteModeByInstr() sets PSTATE.IL to 1 if this is an illegal mode change. AArch32.WriteModeByInstr(pemode);
```