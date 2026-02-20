## C8.2.292 LASTB (scalar)

Extract last element to general-purpose register

This instruction extracts the Last active element to a general-purpose register. If there is an Active element, the Last active element from the final source vector register is extracted. If there are no Active elements, the highest-numbered element is extracted. Then the extracted element is zero-extended and placed in the destination general-purpose register.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
LASTB
```

```
<R><d>, <Pg>, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer rsize = if esize < 64 then 32 else 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Rd); constant boolean isBefore = TRUE;
```

## Assembler Symbols

<!-- image -->

Is a width specifier, encoded in 'size':

<!-- image -->

<!-- image -->

<!-- image -->

&lt;Zn&gt;

|   size | <R>   |
|--------|-------|
|     00 | W     |
|     01 | W     |
|     10 | W     |
|     11 | X     |

Is the number [0-30] of the destination general-purpose register or the name ZR (31), encoded in the 'Rd' field.

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

Is the name of the source scalable vector register, encoded in the 'Zn' field.

&lt;T&gt;

Is the size specifier, encoded in 'size':

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

```
last, esize], rsize);
```

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = Z[n, VL]; bits(rsize) result; integer last = LastActiveElement(mask, esize); if isBefore then if last < 0 then last = elements - 1; else last = last + 1; if last >= elements then last = 0; result = ZeroExtend(Elem[operand, X[d, rsize] = result;
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the general-purpose register written by this instruction might be significantly delayed.