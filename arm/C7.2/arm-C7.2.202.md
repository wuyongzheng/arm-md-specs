## C7.2.202 INS (element)

Insert vector element from another vector element

This instruction copies the vector element of the source SIMD&amp;FP register to the specified vector element of the destination SIMD&amp;FP register.

This instruction can insert data into individual elements within a SIMD&amp;FP register without clearing the remaining bits to zero.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

This instruction is used by the alias MOV (element).

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
INS <Vd>.<Ts>[<index1>], <Vn>.<Ts>[<index2>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if imm5 == 'x0000' then EndOfDecode(Decode_UNDEF); constant integer size = LowestSetBitNZ(imm5<3:0>); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer dst_index = UInt(imm5<4:size+1>); constant integer src_index = UInt(imm4<3:size>); constant integer idxdsize = 64 << UInt(imm4<3>); // imm4<size-1:0> is IGNORED constant integer esize = 8 << size;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an element size specifier, encoded in 'imm5':

<!-- image -->

&lt;Ts&gt;

| imm5   | <Ts>     |
|--------|----------|
| x0000  | RESERVED |
| xxxx1  | B        |
| xxx10  | H        |

## &lt;index1&gt;

Is the destination element index encoded in 'imm5':

## &lt;Vn&gt;

| imm5   | <Ts>   |
|--------|--------|
| xx100  | S      |
| x1000  | D      |

| imm5   | <index1>        |
|--------|-----------------|
| x0000  | RESERVED        |
| xxxx1  | UInt(imm5<4:1>) |
| xxx10  | UInt(imm5<4:2>) |
| xx100  | UInt(imm5<4:3>) |
| x1000  | UInt(imm5<4>)   |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;index2&gt;

Is the source element index encoded in 'imm5:imm4':

| imm5   | <index2>        |
|--------|-----------------|
| x0000  | RESERVED        |
| xxxx1  | UInt(imm4)      |
| xxx10  | UInt(imm4<3:1>) |
| xx100  | UInt(imm4<3:2>) |
| x1000  | UInt(imm4<3>)   |

Unspecified bits in 'imm4' are ignored but should be set to zero by an assembler.

## Alias Conditions

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(idxdsize) operand = V[n, idxdsize]; bits(128) result; result = V[d, 128]; Elem[result, dst_index, esize] = V[d, 128] = result;
```

| Alias         | Is preferred when   |
|---------------|---------------------|
| MOV (element) | Unconditionally     |

```
Elem[operand, src_index, esize];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
