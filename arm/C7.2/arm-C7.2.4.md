## C7.2.4 ADDP (scalar)

Add pair of elements (scalar)

This instruction adds two vector elements in the source SIMD&amp;FP register and writes the scalar result into the destination SIMD&amp;FP register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
ADDP D<d>, <Vn>.2D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 64; constant integer datasize = 128;
```

## Assembler Symbols

&lt;d&gt;

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; V[d, esize] = IntReduce(ReduceOp_ADD, operand, esize);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
