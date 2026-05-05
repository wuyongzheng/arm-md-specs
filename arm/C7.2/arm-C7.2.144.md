## C7.2.144 FMLAL, FMLAL2 (vector)

Floating-point fused multiply-add long to accumulator (vector)

This instruction multiplies corresponding half-precision floating-point values in the vectors in the two source SIMD&amp;FP registers, and accumulates the intermediate product without rounding to the corresponding single-precision vector element of the destination SIMD&amp;FP register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

In Armv8.2 and Armv8.3, this is an OPTIONAL instruction. From Armv8.4, it is mandatory for all implementations to support it.

## Note

ID\_AA64ISAR0\_EL1.FHM indicates whether this instruction is supported.

It has encodings from 2 classes: FMLAL and FMLAL2

## FMLAL

(FEAT\_FHM)

<!-- image -->

## Encoding

```
FMLAL <Vd>.<Ta>, <Vn>.<Tb>, <Vm>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_FHM) then EndOfDecode(Decode_UNDEF); if sz == '1' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 32; constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant integer part = 0;
```

## FMLAL2

(FEAT\_FHM)

<!-- image -->

## Encoding

```
FMLAL2 <Vd>.<Ta>, <Vn>.<Tb>, <Vm>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_FHM) then EndOfDecode(Decode_UNDEF); if sz == '1' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 32; constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant integer part = 1;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'Q':

&lt;Ta&gt;

&lt;Vn&gt;

&lt;Tb&gt;

|   Q | <Ta>   |
|-----|--------|
|   0 | 2S     |
|   1 | 4S     |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'Q':

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize DIV 2) operand1 = Vpart[n, part, datasize DIV 2]; constant bits(datasize DIV 2) operand2 = Vpart[m, part, datasize DIV 2]; constant bits(datasize) operand3 = V[d, datasize]; bits(datasize) result; bits(esize DIV 2) element1; bits(esize DIV 2) element2;
```

|   Q | <Tb>   |
|-----|--------|
|   0 | 2H     |
|   1 | 4H     |

```
for e = 0 to elements-1 element1 = Elem[operand1, e, esize DIV 2]; element2 = Elem[operand2, e, esize DIV 2]; Elem[result, e, esize] = FPMulAddH(Elem[operand3, e, esize], element1, element2, FPCR); V[d, datasize] = result;
```
