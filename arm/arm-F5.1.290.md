## F5.1.290 USAT16

Unsigned Saturate 16 saturates two signed 16-bit values to a selected unsigned range.

This instruction sets PSTATE.Q to 1 if the operation saturates.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
USAT16{<c>}{<q>} <Rd>, #<imm>, <Rn>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer saturate_to = UInt(sat_imm); if d == 15 || n == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
USAT16{<c>}{<q>} <Rd>, #<imm>, <Rn>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer saturate_to = UInt(sat_imm); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Rd&gt;

Is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;imm&gt;

Is the bit position for saturation, in the range 0 to 15, encoded in the 'sat\_imm' field.

## &lt;Rn&gt;

Is the general-purpose source register, encoded in the 'Rn' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(saturate_to) result1; boolean sat1; (result1, sat1) = UnsignedSatQ(SInt(R[n]<15:0>), saturate_to); bits(saturate_to) result2; boolean sat2; (result2, sat2) = UnsignedSatQ(SInt(R[n]<31:16>), saturate_to); R[d]<15:0> = ZeroExtend(result1, 16); R[d]<31:16> = ZeroExtend(result2, 16); if sat1 || sat2 then PSTATE.Q = '1';
```