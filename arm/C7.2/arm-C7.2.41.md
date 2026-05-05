## C7.2.41 DUP (general)

Duplicate general-purpose register to vector

This instruction duplicates the contents of the source general-purpose register into a scalar or each element in a vector, and writes the result to the SIMD&amp;FP destination register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
DUP <Vd>.<T>, <R><n>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if imm5 == 'x0000' then EndOfDecode(Decode_UNDEF); if imm5 == 'x1000' && Q == '0' then EndOfDecode(Decode_UNDEF); constant integer size = LowestSetBitNZ(imm5<3:0>); constant integer d = UInt(Rd); constant integer n = UInt(Rn); // imm5<4:size+1> is IGNORED constant integer esize = 8 << size; constant integer datasize = 64 << UInt(Q);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'imm5:Q':

| imm5   | Q   | <T>      |
|--------|-----|----------|
| x0000  | x   | RESERVED |
| xxxx1  | 0   | 8B       |
| xxxx1  | 1   | 16B      |
| xxx10  | 0   | 4H       |
| xxx10  | 1   | 8H       |
| xx100  | 0   | 2S       |
| xx100  | 1   | 4S       |

<!-- image -->

&lt;T&gt;

<!-- image -->

&lt;R&gt;

<!-- image -->

Is the number [0-30] of the general-purpose source register or ZR (31), encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(esize) element = X[n, esize]; constant integer elements = datasize bits(datasize) result; for e = 0 to elements-1 Elem[result, e, esize] = element; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

| imm5   |   Q | <T>      |
|--------|-----|----------|
| x1000  |   0 | RESERVED |
| x1000  |   1 | 2D       |

Is the width specifier for the general-purpose source register, encoded in 'imm5':

| imm5   | <R>      |
|--------|----------|
| x0000  | RESERVED |
| xxxx1  | W        |
| xxx10  | W        |
| xx100  | W        |
| x1000  | X        |

Unspecified bits in 'imm5' are ignored but should be set to zero by an assembler.

```
DIV esize;
```
