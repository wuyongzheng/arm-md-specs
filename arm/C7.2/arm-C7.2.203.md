## C7.2.203 INS (general)

Insert vector element from general-purpose register

This instruction copies the contents of the source general-purpose register to the specified vector element in the destination SIMD&amp;FP register.

This instruction can insert data into individual elements within a SIMD&amp;FP register without clearing the remaining bits to zero.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

This instruction is used by the alias MOV (from general).

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
INS <Vd>.<Ts>[<index>], <R><n>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if imm5 == 'x0000' then EndOfDecode(Decode_UNDEF); constant integer size = LowestSetBitNZ(imm5<3:0>); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer index = UInt(imm5<4:size+1>); constant integer esize = 8 << size;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an element size specifier, encoded in 'imm5':

<!-- image -->

| imm5   | <Ts>     |
|--------|----------|
| x0000  | RESERVED |
| xxxx1  | B        |
| xxx10  | H        |
| xx100  | S        |
| x1000  | D        |

## &lt;index&gt;

Is the element index encoded in 'imm5':

<!-- image -->

<!-- image -->

Is the number [0-30] of the general-purpose source register or ZR (31), encoded in the 'Rn' field.

## Alias Conditions

## Operation

```
X[n, esize];
```

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(esize) element = bits(128) result = V[d, 128]; Elem[result, index, esize] = element; V[d, 128] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

| imm5   | <index>         |
|--------|-----------------|
| x0000  | RESERVED        |
| xxxx1  | UInt(imm5<4:1>) |
| xxx10  | UInt(imm5<4:2>) |
| xx100  | UInt(imm5<4:3>) |
| x1000  | UInt(imm5<4>)   |

Is the width specifier for the general-purpose source register, encoded in 'imm5':

| imm5   | <R>      |
|--------|----------|
| x0000  | RESERVED |
| xxxx1  | W        |
| xxx10  | W        |
| xx100  | W        |
| x1000  | X        |

| Alias              | Is preferred when   |
|--------------------|---------------------|
| MOV (from general) | Unconditionally     |
