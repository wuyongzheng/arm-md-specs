## F5.1.256 SXTB16

Signed Extend Byte 16 extracts two 8-bit values from a register, sign-extends them to 16 bits each, and writes the results to the destination register. The instruction can specify a rotation by 0, 8, 16, or 24 bits before extracting the 8-bit values.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
SXTB16{<c>}{<q>} {<Rd>, }<Rm> {, ROR #<amount>}
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant integer rotation = UInt(rotate:'000'); if d == 15 || m == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
SXTB16{<c>}{<q>} {<Rd>, }<Rm> {, ROR #<amount>}
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant integer rotation = UInt(rotate:'000'); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || m == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Rd&gt;

Is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Rm&gt;

Is the general-purpose source register, encoded in the 'Rm' field.

## &lt;amount&gt;

Is the rotate amount, encoded in 'rotate':

## Operation

```
if
```

```
ConditionPassed() then EncodingSpecificOperations(); constant bits(32) rotated = ROR(R[m], R[d]<15:0> = SignExtend(rotated<7:0>, 16); R[d]<31:16> = SignExtend(rotated<23:16>, 16);
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