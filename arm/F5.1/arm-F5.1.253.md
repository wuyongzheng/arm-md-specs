## F5.1.253 SXTAB16

Signed Extend and Add Byte 16

Signed Extend and Add Byte 16 extracts two 8-bit values from a register, sign-extends them to 16 bits each, adds the results to two 16-bit values from another register, and writes the final results to the destination register. The instruction can specify a rotation by 0, 8, 16, or 24 bits before extracting the 8-bit values.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
SXTAB16{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, ROR #<amount>}
```

## Decode for this encoding

```
if Rn == '1111' then SEE "SXTB16"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer rotation = if d == 15 || m == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
SXTAB16{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, ROR #<amount>}
```

## Decode for this encoding

```
if Rn == '1111' then SEE "SXTB16"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer rotation = // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || m == 15 then UNPREDICTABLE;
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

## &lt;q&gt;

## &lt;Rd&gt;

## &lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field.

## &lt;amount&gt;

Is the rotate amount, encoded in 'rotate':

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) rotated = ROR(R[m], rotation); R[d]<15:0> = R[n]<15:0> + SignExtend(rotated<7:0>, 16); R[d]<31:16> = R[n]<31:16> + SignExtend(rotated<23:16>, 16);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

|   rotate | <amount>   |
|----------|------------|
|       00 | [absent]   |
|       01 | 8          |
|       10 | 16         |
|       11 | 24         |