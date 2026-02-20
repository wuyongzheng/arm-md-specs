## C8.2.116 CNTP (predicate)

Set scalar to count of true predicate elements

This instruction counts the number of active and true elements in the source predicate and places the scalar result in the destination general-purpose register. Inactive predicate elements are not counted.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CNTP <Xd>, <Pg>, <Pn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Pn); constant integer d = UInt(Rd);
```

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the destination general-purpose register, encoded in the 'Rd' field.

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

Is the size specifier, encoded in 'size':

## &lt;Pg&gt;

## &lt;Pn&gt;

&lt;T&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(PL) operand = P[n, PL]; bits(64) sum = Zeros(64); for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) && ActivePredicateElement(operand, e, esize) then sum = sum + 1; X[d, 64] = sum;
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the general-purpose register written by this instruction might be significantly delayed.