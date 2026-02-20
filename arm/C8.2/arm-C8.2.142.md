## C8.2.142 EORTB

Interleaving exclusive-OR (top, bottom)

This instruction performs an interleaving exclusive-OR between the odd-numbered elements of the first source vector register and the even-numbered elements of the second source vector register, placing the result in the odd-numbered elements of the destination vector, leaving the even-numbered elements unchanged. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
EORTB <Zd>.<T>, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer sel1 = 1; constant integer sel2 = 0;
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

&lt;Zn&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

<!-- image -->

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV (2 * esize); constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result = Z[d, VL]; for e = 0 to elements-1 constant bits(esize) element1 = Elem[operand1, 2*e + sel1, esize]; constant bits(esize) element2 = Elem[operand2, 2*e + sel2, esize]; Elem[result, 2*e + sel1, esize] = element1 EOR element2; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.