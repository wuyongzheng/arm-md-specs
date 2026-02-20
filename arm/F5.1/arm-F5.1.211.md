## F5.1.211 SSAT

Signed Saturate saturates an optionally-shifted signed value to a selectable signed range.

This instruction sets PSTATE.Q to 1 if the operation saturates.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Arithmetic shift right variant

Applies when (sh ==

```
SSAT{<c>}{<q>} <Rd>, #<imm>, <Rn>, ASR
```

```
1) #<amount>
```

## Encoding for the Logical shift left variant

Applies when (sh ==

```
0)
```

```
SSAT{<c>}{<q>} <Rd>, #<imm>, <Rn> {, LSL #<amount>}
```

## Decode for all variants of this encoding

```
imm5);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer saturate_to = UInt(sat_imm)+1; SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(sh:'0', if d == 15 || n == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding for the Arithmetic shift right variant

```
Applies when (sh == 1 && !(imm3 == 000 && imm2 == 00)) SSAT{<c>}{<q>} <Rd>, #<imm>, <Rn>, ASR #<amount>
```

## Encoding for the Logical shift left variant

```
Applies when (sh == 0) SSAT{<c>}{<q>} <Rd>, #<imm>, <Rn>
```

```
{, LSL #<amount>}
```

## Decode for all variants of this encoding

```
if sh == '1' && (imm3:imm2) == '00000' then SEE "SSAT16"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer saturate_to = UInt(sat_imm)+1; SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(sh:'0', imm3:imm2); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields.
```

## &lt;Rd&gt;

Is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;imm&gt;

Is the bit position for saturation, in the range 1 to 32, encoded in the 'sat\_imm' field as &lt;imm&gt;-1.

## &lt;Rn&gt;

Is the general-purpose source register, encoded in the 'Rn' field.

## &lt;amount&gt;

For the 'A1 Arithmetic shift right' variant: is the shift amount, in the range 1 to 32 encoded in the 'imm5' field as &lt;amount&gt; modulo 32.

For the 'A1 Logical shift left' variant: is the optional shift amount, in the range 0 to 31, defaulting to 0 and encoded in the 'imm5' field.

For the 'T1 Arithmetic shift right' variant: is the shift amount, in the range 1 to 31 encoded in the 'imm3:imm2' field as &lt;amount&gt;.

For the 'T1 Logical shift left' variant: is the optional shift amount, in the range 0 to 31, defaulting to 0 and encoded in the 'imm3:imm2' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) operand = Shift(R[n], shift_t, shift_n, PSTATE.C); // PSTATE.C ignored bits(saturate_to) result; boolean sat; (result, sat) = SignedSatQ(SInt(operand), saturate_to); R[d] = SignExtend(result, 32); if sat then PSTATE.Q = '1';
```