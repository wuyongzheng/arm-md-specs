## C8.2.39 BDEP

Scatter lower bits into positions selected by bitmask

This instruction scatters the lowest-numbered contiguous bits within each element of the first source vector to the bit positions indicated by non-zero bits in the corresponding mask element of the second source vector, preserving their order, and sets the bits corresponding to a zero mask bit to zero. This instruction is unpredicated.

ID\_AA64ZFR0\_EL1.BitPerm indicates whether this instruction is implemented.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled, or FEAT\_SSVE\_BitPerm is implemented.

## SVE2

(FEAT\_SVE\_BitPerm)

<!-- image -->

## Encoding

```
BDEP <Zd>.<T>, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE_BitPerm) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

## &lt;Zn&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
if IsFeatureImplemented(FEAT_SSVE_BitPerm) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) data = Z[n, VL]; constant bits(VL) mask = Z[m, VL]; bits(VL) result; for e = 0 to elements - 1 Elem[result, e, esize] = BitDeposit(Elem[data, e, esize], Elem[mask, e, esize]); Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.