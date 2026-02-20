## F5.1.159 REVSH

Byte-Reverse Signed Halfword reverses the byte order in the lower 16-bit halfword of a 32-bit register, and sign-extends the result to 32 bits.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

```
REVSH{<c>}{<q>} <Rd>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); if d == 15 || m == 15 then UNPREDICTABLE;
```

T1

## Encoding

REVSH{&lt;c&gt;}{&lt;q&gt;}

&lt;Rd&gt;,

&lt;Rm&gt;

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm);
```

T2

<!-- image -->

## Encoding

REVSH{&lt;c&gt;}{&lt;q&gt;}

&lt;Rd&gt;,

&lt;Rm&gt;

```
REVSH{<c>}.W <Rd>, <Rm> // (<Rd>, <Rm> can be represented in T1)
```

<!-- image -->

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant integer n = UInt(Rn); // Armv8-A removes UNPREDICTABLE for R13 if m != n || d == 15 || m == 15 then
```

```
UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If m != n , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes with the additional decode: m = UInt(Rn);.
- The instruction executes with the additional decode: m = UInt(Rm);.
- The value in the destination register is UNKNOWN.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Rd&gt;

Is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Rm&gt;

For the 'A1' and 'T1' variants: is the general-purpose source register, encoded in the 'Rm' field.

For the 'T2' variant: is the general-purpose source register, encoded in the 'Rm' field. It must be encoded with an identical value in the 'Rn' field.

## Operation

```
SignExtend(R[m]<7:0>, 24);
```

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) result; result<31:8> = result<7:0> = R[m]<15:8>; R[d] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.