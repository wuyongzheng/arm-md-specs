## F6.1.174 VQDMLSL

Vector Saturating Doubling Multiply Subtract Long multiplies corresponding elements in two doubleword vectors, subtracts double the products from corresponding elements of a quadword vector, and places the results in the same quadword vector.

The second operand can be a scalar instead of a vector. For more information about scalars see Advanced SIMD scalars.

If any of the results overflow, they are saturated. The cumulative saturation bit, FPSCR.QC, is set if saturation occurs. For details see Pseudocode details of saturation.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

```
VQDMLSL{<c>}{<q>}.<dt> <Qd>, <Dn>, <Dm>
```

## Decode for this encoding

```
UNDEFINED;
```

```
if size == '11' then SEE "Related encodings"; if size == '00' || Vd<0> == '1' then constant boolean add = (op == '0'); constant boolean scalar_form = FALSE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer index = integer UNKNOWN;
```

A2

<!-- image -->

## Encoding

```
VQDMLSL{<c>}{<q>}.<dt> <Qd>, <Dn>, <Dm>[<index>]
```

## Decode for this encoding

```
if size == '11' then SEE "Related encodings"; if size == '00' || Vd<0> == '1' then UNDEFINED; constant boolean add = (op == '0'); constant boolean scalar_form = TRUE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = if size == '01' then UInt(Vm<2:0>) else UInt(Vm); constant integer index = if size == '01' then UInt(M:Vm<3>) else UInt(M); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize;
```

T1

<!-- image -->

## Encoding

```
VQDMLSL{<c>}{<q>}.<dt> <Qd>, <Dn>, <Dm>
```

## Decode for this encoding

```
if size == '11' then SEE "Related encodings"; if size == '00' || Vd<0> == '1' then UNDEFINED; constant boolean add = (op == '0'); constant boolean scalar_form = FALSE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer index = integer UNKNOWN;
```

T2

<!-- image -->

## Encoding

```
VQDMLSL{<c>}{<q>}.<dt> <Qd>, <Dn>, <Dm>[<index>]
```

## Decode for this encoding

```
if size == '11' then SEE "Related encodings"; if size == '00' || Vd<0> == '1' then UNDEFINED; constant boolean add = (op == '0'); constant boolean scalar_form = TRUE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = if size == '01' then UInt(Vm<2:0>) else UInt(Vm); constant integer index = if size == '01' then UInt(M:Vm<3>) else UInt(M); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize;
```

Related encodings: See Advanced SIMD data-processing for the T32 instruction set, or Advanced SIMD data-processing for the A32 instruction set.

## Assembler Symbols

&lt;c&gt;

For the 'A1' and 'A2' variants: see Standard assembler syntax fields. This encoding must be unconditional. For the 'T1' and 'T2' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the operands, encoded in 'size':

|   size | <dt>   |
|--------|--------|
|     01 | S16    |
|     10 | S32    |

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

&lt;q&gt;

&lt;dt&gt;

## &lt;Qd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

For the 'A1' and 'T1' variants: is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

For the 'A2' and 'T2' variants: is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'Vm&lt;2:0&gt;' field when &lt;dt&gt; is S16, otherwise the 'Vm' field.

## &lt;index&gt;

Is the element index in the range 0 to 3, encoded in the 'M:Vm&lt;3&gt;' field when &lt;dt&gt; is S16, otherwise in range 0 to 1, encoded in the 'M' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); integer op2; if scalar_form then op2 = SInt(Elem[Din[m],index,esize]); for e = 0 to elements-1 if !scalar_form then op2 = SInt(Elem[Din[m],e,esize]); constant integer op1 = SInt(Elem[Din[n],e,esize]); // The following only saturates if both op1 and op2 equal bits(2*esize) product; boolean sat1; (product, sat1) = SignedSatQ(2*op1*op2, 2*esize); integer result; if add then result = SInt(Elem[Qin[d>>1],e,2*esize]) + SInt(product); else result = SInt(Elem[Qin[d>>1],e,2*esize]) SInt(product); bits(2*esize) res; boolean sat2; (res, sat2) = SignedSatQ(result, 2*esize); Elem[Q[d>>1],e,2*esize] = res; if sat1 || sat2 then FPSCR.QC = '1';
```

```
-(2^(esize-1))
```