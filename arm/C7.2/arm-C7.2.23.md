## C7.2.23 BIF

Bitwise insert if false

This instruction inserts each bit from the first source SIMD&amp;FP register into the destination SIMD&amp;FP register if the corresponding bit of the second source SIMD&amp;FP register is 0, otherwise leaves the bit in the destination register unchanged.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Three registers of the same type

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
BIF <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 64 << UInt(Q);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'Q':

&lt;T&gt;

&lt;Vn&gt;

|   Q | <T>   |
|-----|-------|
|   0 | 8B    |
|   1 | 16B   |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[d, datasize]; constant bits(datasize) operand2 = NOT(V[m, datasize]); constant bits(datasize) operand3 = V[n, datasize]; V[d, datasize] = operand1 EOR ((operand1 EOR operand3)
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
AND operand2);
```
