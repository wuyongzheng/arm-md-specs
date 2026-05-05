## C7.2.248 MUL (by element)

Multiply (vector, by element)

This instruction multiplies the vector elements in the first source SIMD&amp;FP register by the specified value in the second source SIMD&amp;FP register, places the results in a vector, and writes the vector to the destination SIMD&amp;FP register. All the values in this instruction are unsigned integer values.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
MUL <Vd>.<T>, <Vn>.<T>, V<m>.<Ts>[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
constant integer idxdsize = 64 << UInt(H); integer index; bit Rmhi; case size of when '01' index = UInt(H:L:M); Rmhi = '0'; when '10' index = UInt(H:L); Rmhi = M; otherwise EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rmhi:Rm); constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size | Q   | <T>      |
|--------|-----|----------|
|     00 | x   | RESERVED |
|     01 | 0   | 4H       |
|     01 | 1   | 8H       |

&lt;T&gt;

## &lt;Vn&gt;

&lt;m&gt;

&lt;Ts&gt;

Is an element size specifier, encoded in 'size':

## &lt;index&gt;

Is the element index, encoded in 'size:H:L:M':

|   size | Q   | <T>      |
|--------|-----|----------|
|     10 | 0   | 2S       |
|     10 | 1   | 4S       |
|     11 | x   | RESERVED |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the number of the second SIMD&amp;FP source register, encoded in 'size:M:Rm':

|   size | <m>          |
|--------|--------------|
|     00 | RESERVED     |
|     01 | UInt('0':Rm) |
|     10 | UInt(M:Rm)   |
|     11 | RESERVED     |

|   size | <Ts>     |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | RESERVED |

|   size | <index>     |
|--------|-------------|
|     00 | RESERVED    |
|     01 | UInt(H:L:M) |
|     10 | UInt(H:L)   |
|     11 | RESERVED    |

Restricted to 0-15 when element size &lt;Ts&gt; is H.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = constant bits(idxdsize) operand2 = bits(datasize) result; integer element1; integer element2; bits(esize) product; element2 = UInt(Elem[operand2, index, esize]); for e = 0 to elements-1 element1 = UInt(Elem[operand1, e, esize]); product = (element1 * element2)<esize-1:0>; Elem[result, e, esize] = product; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
V[n, datasize]; V[m, idxdsize];
```
