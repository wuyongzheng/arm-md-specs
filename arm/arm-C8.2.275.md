## C8.2.275 FTMAD

Floating-point trigonometric multiply-add coefficient

This instruction multiplies each element of the first source vector by the absolute value of the corresponding element of the second source vector and performs a fused addition of each product with a value obtained from a table of hard-wired coefficients, and destructively places the results in the first source vector. This instruction is unpredicated.

The coefficients are selected by a combination of the sign bit in the second source element and an immediate index in the range 0 to 7.

FTMAD can be combined with FTSMUL and FTSSEL to compute values for sin(x) and cos(x). For more information, see FTSMUL . The coefficients are intended to provide accurate results for FTSMUL inputs in the range π /4 &lt; x ≤ π /4.

For double-precision operations, the coefficients are:

|   element2<63> |   Index | Hexadecimal         | Approximate value   |
|----------------|---------|---------------------|---------------------|
|              0 |       0 | 3ff0 0000 0000 0000 | 1                   |
|              0 |       1 | bfc5 5555 5555 5543 | -1/3!               |
|              0 |       2 | 3f81 1111 1110 f30c | 1/5!                |
|              0 |       3 | bf2a 01a0 19b9 2fc6 | -1/7!               |
|              0 |       4 | 3ec7 1de3 51f3 d22b | 1/9!                |
|              0 |       5 | be5a e5e2 b60f 7b91 | -1/11!              |
|              0 |       6 | 3de5 d840 8868 552f | 1/13!               |
|              0 |       7 | 0000 0000 0000 0000 | 0                   |
|              1 |       0 | 3ff0 0000 0000 0000 | 1                   |
|              1 |       1 | bfe0 0000 0000 0000 | -1/2!               |
|              1 |       2 | 3fa5 5555 5555 5536 | 1/4!                |
|              1 |       3 | bf56 c16c 16c1 3a0b | -1/6!               |
|              1 |       4 | 3efa 01a0 19b1 e8d8 | 1/8!                |
|              1 |       5 | be92 7e4f 7282 f468 | -1/10!              |
|              1 |       6 | 3e21 ee96 d264 1b13 | 1/12!               |
|              1 |       7 | bda8 f763 80fb b401 | -1/14!              |

For single-precision operations, the coefficients are:

|   element2<63> |   Index | Hexadecimal   | Approximate value   |
|----------------|---------|---------------|---------------------|
|              0 |       0 | 3f80 0000     | 1                   |
|              0 |       1 | be2a aaab     | -1/3!               |
|              0 |       2 | 3c08 8886     | 1/5!                |
|              0 |       3 | b950 08b9     | -1/7!               |
|              0 |       4 | 3636 9d6d     | 1/9!                |
|              0 |       5 | 0000 0000     | 0                   |
|              0 |       6 | 0000 0000     | 0                   |

|   element2<63> |   Index | Hexadecimal   | Approximate value   |
|----------------|---------|---------------|---------------------|
|              0 |       7 | 0000 0000     | 0                   |
|              1 |       0 | 3f80 0000     | 1                   |
|              1 |       1 | bf00 0000     | -1/2!               |
|              1 |       2 | 3d2a aaa6     | 1/4!                |
|              1 |       3 | bab6 0705     | -1/6!               |
|              1 |       4 | 37cd 37cc     | 1/8!                |
|              1 |       5 | 0000 0000     | 0                   |
|              1 |       6 | 0000 0000     | 0                   |
|              1 |       7 | 0000 0000     | 0                   |

For half-precision operations, the coefficients are:

|   element2<63> |   Index | Hexadecimal   | Approximate value   |
|----------------|---------|---------------|---------------------|
|              0 |       0 | 3c00          | 1                   |
|              0 |       1 | b155          | -1/3!               |
|              0 |       2 | 2030          | 1/5!                |
|              0 |       3 | 0000          | 0                   |
|              0 |       4 | 0000          | 0                   |
|              0 |       5 | 0000          | 0                   |
|              0 |       6 | 0000          | 0                   |
|              0 |       7 | 0000          | 0                   |
|              1 |       0 | 3c00          | 1                   |
|              1 |       1 | b800          | -1/2!               |
|              1 |       2 | 293a          | 1/4!                |
|              1 |       3 | 0000          | 0                   |
|              1 |       4 | 0000          | 0                   |
|              1 |       5 | 0000          | 0                   |
|              1 |       6 | 0000          | 0                   |
|              1 |       7 | 0000          | 0                   |

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

SVE

(FEAT\_SVE)

<!-- image -->

| 31 29 28 20              | 25 24 23 22 21 19 18 16 15 13 12 10 9 5 4   |
|--------------------------|---------------------------------------------|
| 0 1 1 0 0 1 0 1 size 0 1 | 0 imm3 1 0 0 0 0 0 Zm Zdn                   |

## Encoding

```
FTMAD <Zdn>.<T>, <Zdn>.<T>, <Zm>.<T>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) then EndOfDecode(Decode_UNDEF);
```

```
if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer dn = UInt(Zdn); constant integer m = UInt(Zm); constant integer imm = UInt(imm3);
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the first source and destination scalable vector register, encoded in the 'Zdn' field.

<!-- image -->

Is the size specifier, encoded in 'size':

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## &lt;imm&gt;

Is the unsigned immediate operand, in the range 0 to 7, encoded in the 'imm3' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[dn, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize) element1 = Elem[operand1, e, esize]; constant bits(esize) element2 = Elem[operand2, e, esize]; Elem[result, e, esize] = FPTrigMAdd(imm, element1, element2, FPCR); Z[dn, VL] = result;
```

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.