## C7.2.257 PMUL

Polynomial multiply

This instruction multiplies corresponding elements in the vectors of the two source SIMD&amp;FP registers, places the results in a vector, and writes the vector to the destination SIMD&amp;FP register.

For information about multiplying polynomials see Polynomial arithmetic over {0, 1}.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Three registers of the same type

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
PMUL <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if U == '1' && size != '00' then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size:Q':

| size   | Q   | <T>      |
|--------|-----|----------|
| 00     | 0   | 8B       |
| 00     | 1   | 16B      |
| 01     | x   | RESERVED |
| 1x     | x   | RESERVED |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

<!-- image -->

&lt;Vn&gt;

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(datasize) operand2 = V[m, datasize]; bits(datasize) result; bits(esize) element1; bits(esize) element2; bits(esize) product; for e = 0 to elements-1 element1 = Elem[operand1, e, esize]; element2 = Elem[operand2, e, esize]; product = PolynomialMult(element1, Elem[result, e, esize] = product; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
element2)<esize-1:0>;
```
