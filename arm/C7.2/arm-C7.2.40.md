## C7.2.40 DUP (element)

Duplicate vector element to vector or scalar

This instruction duplicates the vector element at the specified element index in the source SIMD&amp;FP register into a scalar or each element in a vector, and writes the result to the destination SIMD&amp;FP register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

This instruction is used by the alias MOV (scalar).

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
DUP <V><d>, <Vn>.<T>[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if imm5 == 'x0000' then EndOfDecode(Decode_UNDEF); constant integer size = LowestSetBitNZ(imm5<3:0>); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer index = UInt(imm5<4:size+1>); constant integer idxdsize = 64 << UInt(imm5<4>); constant integer esize = 8 << size; constant integer datasize = esize; constant integer elements = 1;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
DUP <Vd>.<T>, <Vn>.<Ts>[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if imm5 == 'x0000' then EndOfDecode(Decode_UNDEF); if imm5 == 'x1000' && Q == '0' then EndOfDecode(Decode_UNDEF); constant integer size = LowestSetBitNZ(imm5<3:0>); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer index = UInt(imm5<4:size+1>); constant integer idxdsize = 64 << UInt(imm5<4>); constant integer esize = 8 << size; constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

&lt;V&gt;

Is the destination width specifier, encoded in 'imm5':

| imm5   | <V>      |
|--------|----------|
| x0000  | RESERVED |
| xxxx1  | B        |
| xxx10  | H        |
| xx100  | S        |
| x1000  | D        |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

For the 'Scalar' variant: is the element width specifier, encoded in 'imm5':

| imm5   | <T>      |
|--------|----------|
| x0000  | RESERVED |
| xxxx1  | B        |
| xxx10  | H        |
| xx100  | S        |
| x1000  | D        |

For the 'Vector' variant: is an arrangement specifier, encoded in 'imm5:Q':

&lt;d&gt;

&lt;Vn&gt;

&lt;T&gt;

## &lt;index&gt;

Is the element index encoded in 'imm5':

## &lt;Vd&gt;

## &lt;Ts&gt;

| imm5   | Q   | <T>      |
|--------|-----|----------|
| x0000  | x   | RESERVED |
| xxxx1  | 0   | 8B       |
| xxxx1  | 1   | 16B      |
| xxx10  | 0   | 4H       |
| xxx10  | 1   | 8H       |
| xx100  | 0   | 2S       |
| xx100  | 1   | 4S       |
| x1000  | 0   | RESERVED |
| x1000  | 1   | 2D       |

| imm5   | <index>         |
|--------|-----------------|
| x0000  | RESERVED        |
| xxxx1  | UInt(imm5<4:1>) |
| xxx10  | UInt(imm5<4:2>) |
| xx100  | UInt(imm5<4:3>) |
| x1000  | UInt(imm5<4>)   |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an element size specifier, encoded in 'imm5':

Alias Conditions

| imm5   | <Ts>     |
|--------|----------|
| x0000  | RESERVED |
| xxxx1  | B        |
| xxx10  | H        |
| xx100  | S        |
| x1000  | D        |

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(idxdsize) operand = bits(datasize) result; bits(esize) element; element = Elem[operand, index, esize]; for e = 0 to elements-1 Elem[result, e, esize] = element; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
V[n, idxdsize];
```

| Alias        | Is preferred when   |
|--------------|---------------------|
| MOV (scalar) | Unconditionally     |
