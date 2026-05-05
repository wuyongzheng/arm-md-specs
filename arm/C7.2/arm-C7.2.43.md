## C7.2.43 EOR (vector)

Bitwise exclusive-OR (vector)

This instruction performs a bitwise exclusive-OR operation between the two source SIMD&amp;FP registers, and places the result in the destination SIMD&amp;FP register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Three registers of the same type (FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
EOR <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 64 << UInt(Q);
```

## Assembler Symbols

## &lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'Q':

&lt;T&gt;

## &lt;Vn&gt;

|   Q | <T>   |
|-----|-------|
|   0 | 8B    |
|   1 | 16B   |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[m, datasize]; constant bits(datasize) operand2 = Zeros(datasize); constant bits(datasize) operand3 = Ones(datasize); constant bits(datasize) operand4 = V[n, datasize]; V[d, datasize] = operand1 EOR ((operand2 EOR operand4) AND operand3);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
