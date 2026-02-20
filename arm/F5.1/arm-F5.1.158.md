## F5.1.158 REV

Byte-Reverse Word reverses the byte order in a 32-bit register.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

```
REV{<c>}{<q>} <Rd>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); if d == 15 || m == 15 then UNPREDICTABLE; end
```

T1

## Encoding

REV{&lt;c&gt;}{&lt;q&gt;}

&lt;Rd&gt;, &lt;Rm&gt;

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm);
```

T2

<!-- image -->

## Encoding

REV{&lt;c&gt;}{&lt;q&gt;}

&lt;Rd&gt;, &lt;Rm&gt;

<!-- image -->

```
REV{<c>}.W <Rd>, <Rm> // (<Rd>, <Rm> can be represented in T1)
```

Listing F5-59

<!-- image -->

Listing F5-60

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant integer n = UInt(Rn); // Armv8-A removes UNPREDICTABLE for R13 if m != n || d == 15 || m == 15 then UNPREDICTABLE; end
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

<!-- image -->

&lt;Rd&gt;

Is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Rm&gt;

For the 'A1' and 'T1' variants: is the general-purpose source register, encoded in the 'Rm' field.

For the 'T2' variant: is the general-purpose source register, encoded in the 'Rm' field. It must be encoded with an identical value in the 'Rn' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) result; result<31:24> = R[m]<7:0>; result<23:16> = R[m]<15:8>; result<15:8> = R[m]<23:16>; result<7:0> = R[m]<31:24>; R[d] = result; end
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

Listing F5-62