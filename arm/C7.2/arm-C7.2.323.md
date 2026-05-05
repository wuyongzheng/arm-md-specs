## C7.2.323 SMOV

Signed move vector element to general-purpose register

This instruction reads the signed integer from the source SIMD&amp;FP register, sign-extends it to form a 32-bit or 64-bit value, and writes the result to destination general-purpose register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the 32-bit variant

Applies when

```
(Q == 0)
```

```
SMOV
```

```
<Wd>, <Vn>.<Ts>[<index>]
```

## Encoding for the 64-bit variant

```
Applies when (Q == 1) SMOV <Xd>, <Vn>.<Ts>[<index>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if imm5 == 'xx000' then EndOfDecode(Decode_UNDEF); constant integer size = LowestSetBitNZ(imm5<2:0>); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << size; constant integer datasize = 32 << UInt(Q); if datasize <= esize then EndOfDecode(Decode_UNDEF); constant integer index = UInt(imm5<4:size+1>); constant integer idxdsize = 64 << UInt(imm5<4>);
```

## Assembler Symbols

&lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

&lt;Ts&gt;

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

For the '32-bit' variant: is an element size specifier, encoded in 'imm5':

## &lt;index&gt;

For the '32-bit' variant: is the element index encoded in 'imm5':

| imm5   | <index>         |
|--------|-----------------|
| xxx00  | RESERVED        |
| xxxx1  | UInt(imm5<4:1>) |
| xxx10  | UInt(imm5<4:2>) |

For the '64-bit' variant: is the element index encoded in 'imm5':

| imm5   | <index>         |
|--------|-----------------|
| xx000  | RESERVED        |
| xxxx1  | UInt(imm5<4:1>) |
| xxx10  | UInt(imm5<4:2>) |
| xx100  | UInt(imm5<4:3>) |

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Operation

```
if index == 0 then AArch64.CheckFPEnabled(); else AArch64.CheckFPAdvSIMDEnabled(); constant bits(idxdsize) operand = V[n, idxdsize]; X[d, datasize] = SignExtend(Elem[operand, index, esize], datasize);
```

## &lt;Xd&gt;

| imm5   | <Ts>     |
|--------|----------|
| xxx00  | RESERVED |
| xxxx1  | B        |
| xxx10  | H        |

For the '64-bit' variant: is an element size specifier, encoded in 'imm5':

| imm5   | <Ts>     |
|--------|----------|
| xx000  | RESERVED |
| xxxx1  | B        |
| xxx10  | H        |
| xx100  | S        |

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
