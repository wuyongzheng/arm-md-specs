## F6.1.149 VMULL (integer and polynomial)

Vector Multiply Long (integer and polynomial)

Vector Multiply Long multiplies corresponding elements in two vectors. The destination vector elements are twice as long as the elements that are multiplied.

For information about multiplying polynomials see Polynomial arithmetic over {0, 1}.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

size

## Encoding

```
VMULL{<c>}{<q>}.<dt> <Qd>, <Dn>, <Dm>
```

## Decode for this encoding

```
if size == '11' then SEE "Related encodings"; if op == '1' && (U == '1' || size == '01') then UNDEFINED; if op == '1' && size =='10' && !IsFeatureImplemented(FEAT_PMULL) then UNDEFINED; if Vd<0> == '1' then UNDEFINED; constant boolean unsigned = (U == '1'); constant boolean polynomial = (op == '1'); constant boolean long_destination = TRUE; constant integer esize = if polynomial && size == '10' then 64 else 8 << UInt(size); constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer elements = 64 DIV esize; constant integer regs = 1;
```

T1

<!-- image -->

## Encoding

```
VMULL{<c>}{<q>}.<dt> <Qd>, <Dn>, <Dm>
```

size

## Decode for this encoding

```
if size == '11' then SEE "Related encodings"; if op == '1' && (U == '1' || size == '01') then UNDEFINED; if op == '1' && size == '10' && InITBlock() then UNPREDICTABLE; if op == '1' && size == '10' && !IsFeatureImplemented(FEAT_PMULL) then UNPREDICTABLE; if Vd<0> == '1' then UNDEFINED; constant boolean unsigned = (U == '1'); constant boolean polynomial = (op == '1'); constant boolean long_destination = TRUE; constant integer esize = if polynomial && size == '10' then 64 else 8 << UInt(size); constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer elements = 64 DIV esize; constant integer regs = 1;
```

## CONSTRAINED UNPREDICTABLE behavior

If op == '1' &amp;&amp; size == '10' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

Related encodings: See Advanced SIMD data-processing for the T32 instruction set, or Advanced SIMD data-processing for the A32 instruction set.

## Assembler Symbols

<!-- image -->

For the 'A1' variant: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the operands, encoded in 'op:U:size':

|   op |   U |   size | <dt>   |
|------|-----|--------|--------|
|    0 |   0 |     00 | S8     |
|    0 |   0 |     01 | S16    |
|    0 |   0 |     10 | S32    |
|    0 |   1 |     00 | U8     |
|    0 |   1 |     01 | U16    |
|    0 |   1 |     10 | U32    |
|    1 |   0 |     00 | P8     |
|    1 |   0 |     10 | P64    |

<!-- image -->

<!-- image -->

&lt;dt&gt;

&lt;Qd&gt;

&lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for r = 0 to regs-1 for e = 0 to elements-1 constant bits(esize) op1elt = Elem[Din[n+r],e,esize]; constant bits(esize) op2elt = Elem[Din[m+r],e,esize]; bits(2 * esize) product; if polynomial then product = PolynomialMult(op1elt, op2elt); else constant integer element1 = if unsigned then UInt(op1elt) else SInt(op1elt); constant integer element2 = if unsigned then UInt(op2elt) else SInt(op2elt); product = (element1 * element2)<2*esize-1:0>; if long_destination then Elem[Q[d>>1],e,2*esize] = product; else Elem[D[d+r],e,esize] = product<esize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.