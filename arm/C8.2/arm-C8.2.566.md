## C8.2.566 SBCLT

Subtract with carry long (top)

This instruction subtracts the odd-numbered elements of the first source vector and the inverted 1-bit carry from the least-significant bit of the odd-numbered elements of the second source vector from the even-numbered elements of the destination and accumulator vector. The 1-bit carry output is placed in the corresponding odd-numbered element of the destination vector.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SBCLT <Zda>.<T>, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32 << UInt(sz); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

## &lt;T&gt;

## &lt;Zn&gt;

Is the size specifier, encoded in 'sz':

|   sz | <T>   |
|------|-------|
|    0 | S     |
|    1 | D     |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer pairs = VL DIV (esize * 2); constant bits(VL) operand = Z[n, VL]; constant bits(VL) carries = Z[m, VL]; bits(VL) result = Z[da, VL]; for p = 0 to pairs-1 constant bits(esize) element1 = Elem[result, 2*p + 0, esize]; constant bits(esize) element2 = Elem[operand, 2*p + 1, esize]; constant bit carry_in = Elem[carries, 2*p + 1, esize]<0>; constant (res, nzcv) = AddWithCarry(element1, NOT(element2), constant bit carry_out = nzcv<1>; Elem[result, 2*p + 0, esize] = res; Elem[result, 2*p + 1, esize] = ZeroExtend(carry_out, esize); Z[da, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

```
carry_in);
```