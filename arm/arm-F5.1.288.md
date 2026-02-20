## F5.1.288 USADA8

Unsigned Sum of Absolute Differences and Accumulate

Unsigned Sum of Absolute Differences and Accumulate performs four unsigned 8-bit subtractions, and adds the absolute values of the differences to a 32-bit accumulate operand.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
USADA8{<c>}{<q>} <Rd>, <Rn>, <Rm>, <Ra>
```

## Decode for this encoding

```
if Ra == '1111' then SEE "USAD8"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra); if d == 15 || n == 15 || m == 15 then
```

T1

<!-- image -->

## Encoding

```
USADA8{<c>}{<q>} <Rd>, <Rn>, <Rm>, <Ra>
```

## Decode for this encoding

```
if Ra == '1111' then SEE "USAD8"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 then
```

```
UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
UNPREDICTABLE;
```

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rd' field.

&lt;q&gt;

&lt;Rd&gt;

&lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field.

&lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field.

&lt;Ra&gt;

Is the third general-purpose source register holding the addend, encoded in the 'Ra' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant integer absdiff1 = Abs(UInt(R[n]<7:0>) -UInt(R[m]<7:0>)); constant integer absdiff2 = Abs(UInt(R[n]<15:8>) -UInt(R[m]<15:8>)); constant integer absdiff3 = Abs(UInt(R[n]<23:16>) UInt(R[m]<23:16>)); constant integer absdiff4 = Abs(UInt(R[n]<31:24>) UInt(R[m]<31:24>)); constant integer result = UInt(R[a]) + absdiff1 + absdiff2 + absdiff3 + absdiff4; R[d] = result<31:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.