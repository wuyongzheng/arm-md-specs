## C8.2.96 CLASTA (scalar)

Conditionally extract element after last to general-purpose register

This instruction extracts, from the source vector register, the element after the Last active element, or if the Last active element is the final element it extracts element zero, and then zero-extends that element to destructively place in the destination and first source general-purpose register. If there are no Active elements, the least significant element-size bits of the destination and first source general-purpose register are destructively zero-extended.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CLASTA <R><dn>, <Pg>, <R><dn>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then
```

```
EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer dn = UInt(Rdn); constant integer m = UInt(Zm); constant integer csize = if esize < 64 then 32 else 64; constant boolean isBefore = FALSE;
```

## Assembler Symbols

<!-- image -->

Is a width specifier, encoded in 'size':

&lt;dn&gt;

<!-- image -->

B

|   size | <R>   |
|--------|-------|
|     00 | W     |
|     01 | W     |
|     10 | W     |
|     11 | X     |

Is the number [0-30] of the source and destination general-purpose register or the name ZR (31), encoded in the 'Rdn' field.

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

## &lt;Zm&gt;

Is the name of the source scalable vector register, encoded in the 'Zm' field.

<!-- image -->

Is the size specifier, encoded in 'size':

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

```
last, esize], csize);
```

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(esize) operand1 = X[dn, esize]; constant bits(VL) operand2 = Z[m, VL]; bits(csize) result; integer last = LastActiveElement(mask, esize); if last < 0 then result = ZeroExtend(operand1, csize); else if !isBefore then last = last + 1; if last >= elements then last = 0; result = ZeroExtend(Elem[operand2, X[dn, csize] = result;
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the general-purpose register written by this instruction might be significantly delayed.