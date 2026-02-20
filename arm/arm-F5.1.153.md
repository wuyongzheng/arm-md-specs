## F5.1.153 QSUB

Saturating Subtract subtracts one register value from another register value, saturates the result to the 32-bit signed integer range -2 31 &lt;= x &lt;= 2 31 - 1, and writes the result to the destination register. If saturation occurs, it sets PSTATE.Q to 1.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
QSUB{<c>}{<q>} {<Rd>, }<Rm>, <Rn>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); if d == 15 || n == 15 || m == 15 then
```

T1

<!-- image -->

## Encoding

```
QSUB{<c>}{<q>} {<Rd>, }<Rm>, <Rn>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
UNPREDICTABLE;
```

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Rd&gt;

Is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Rm&gt;

Is the first general-purpose source register, encoded in the 'Rm' field.

&lt;Rn&gt;

Is the second general-purpose source register, encoded in the 'Rn' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) r; boolean sat; (r, sat) = SignedSatQ(SInt(R[m]) R[d] = r; if sat then PSTATE.Q = '1';
```

```
SInt(R[n]), 32);
```