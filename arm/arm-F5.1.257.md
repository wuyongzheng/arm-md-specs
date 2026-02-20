## F5.1.257 SXTH

Signed Extend Halfword extracts a 16-bit value from a register, sign-extends it to 32 bits, and writes the result to the destination register. The instruction can specify a rotation by 0, 8, 16, or 24 bits before extracting the 16-bit value.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

SXTH{&lt;c&gt;}{&lt;q&gt;}

{&lt;Rd&gt;, }&lt;Rm&gt;

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant integer rotation = UInt(rotate:'000'); if d == 15 || m == 15 then UNPREDICTABLE;
```

T1

## Encoding

SXTH{&lt;c&gt;}{&lt;q&gt;}

{&lt;Rd&gt;, }&lt;Rm&gt;

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant integer rotation = 0;
```

<!-- image -->

## Encoding

U

{, ROR #&lt;amount&gt;}

<!-- image -->

```
SXTH{<c>}{<q>} {<Rd>, }<Rm> {, ROR #<amount>} SXTH{<c>}.W {<Rd>, }<Rm> // (<Rd>, <Rm> can be represented in T1)
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant integer rotation = // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || m == 15 then UNPREDICTABLE;
```

```
UInt(rotate:'000');
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
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) rotated = ROR(R[m], R[d] = SignExtend(rotated<15:0>, 32);
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