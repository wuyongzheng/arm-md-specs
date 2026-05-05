## C7.2.430 UMOV

Unsigned move vector element to general-purpose register

This instruction reads the unsigned integer from the source SIMD&amp;FP register, zero-extends it to form a 32-bit or 64-bit value, and writes the result to the destination general-purpose register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

This instruction is used by the alias MOV (to general).

## Advanced SIMD (FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the 32-bit variant

Applies when

```
(Q == 0)
```

```
UMOV
```

```
<Wd>, <Vn>.<Ts>[<index>]
```

## Encoding for the 64-bit variant

Applies when

```
(Q == 1 && imm5 == x1000) UMOV <Xd>, <Vn>.D[<index>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
if imm5 == 'x0000' then EndOfDecode(Decode_UNDEF); constant integer size = LowestSetBitNZ(imm5<3:0>); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << size; constant integer datasize = 32 << UInt(Q); if datasize == 64 && esize < 64 then EndOfDecode(Decode_UNDEF); if datasize == 32 && esize >= 64 then EndOfDecode(Decode_UNDEF); constant integer index = UInt(imm5<4:size+1>); constant integer idxdsize = 64 << UInt(imm5<4>);
```

## Assembler Symbols

&lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

<!-- image -->

Is an element size specifier, encoded in 'imm5':

## &lt;index&gt;

For the '32-bit' variant: is the element index encoded in 'imm5':

| imm5   | <index>         |
|--------|-----------------|
| xx000  | RESERVED        |
| xxxx1  | UInt(imm5<4:1>) |
| xxx10  | UInt(imm5<4:2>) |
| xx100  | UInt(imm5<4:3>) |

For the '64-bit' variant: is the element index encoded in 'imm5&lt;4&gt;'.

<!-- image -->

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Alias Conditions

## Operation

```
if index == 0 then AArch64.CheckFPEnabled(); else AArch64.CheckFPAdvSIMDEnabled(); constant bits(idxdsize) operand = V[n, idxdsize]; X[d, datasize] = ZeroExtend(Elem[operand, index, esize], datasize);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

| imm5   | <Ts>     |
|--------|----------|
| xx000  | RESERVED |
| xxxx1  | B        |
| xxx10  | H        |
| xx100  | S        |

| Alias            | Of variant   | Is preferred when   |
|------------------|--------------|---------------------|
| MOV (to general) | 32-bit       | imm5 IN {'xx100'}   |
| MOV (to general) | 64-bit       | imm5 IN {'x1000'}   |
