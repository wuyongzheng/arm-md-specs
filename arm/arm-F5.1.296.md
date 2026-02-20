## F5.1.296 UXTAH

Unsigned Extend and Add Halfword

Unsigned Extend and Add Halfword extracts a 16-bit value from a register, zero-extends it to 32 bits, adds the result to a value from another register, and writes the final result to the destination register. The instruction can specify a rotation by 0, 8, 16, or 24 bits before extracting the 16-bit value.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
UXTAH{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, ROR #<amount>}
```

## Decode for this encoding

```
if Rn == '1111' then SEE "UXTH"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer rotation = if d == 15 || m == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
UXTAH{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, ROR #<amount>}
```

## Decode for this encoding

```
if Rn == '1111' then SEE "UXTH"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer rotation = // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || m == 15 then UNPREDICTABLE;
```

```
UInt(rotate:'000');
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
UInt(rotate:'000');
```

U

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rd' field.

&lt;q&gt;

## &lt;Rd&gt;

## &lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field.

## &lt;amount&gt;

Is the rotate amount, encoded in 'rotate':

## Operation

```
if
```

```
ConditionPassed() then EncodingSpecificOperations(); constant bits(32) rotated = ROR(R[m], R[d] = R[n] + ZeroExtend(rotated<15:0>, 32);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

|   rotate | <amount>   |
|----------|------------|
|       00 | [absent]   |
|       01 | 8          |
|       10 | 16         |
|       11 | 24         |

```
rotation);
```