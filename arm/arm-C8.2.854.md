## C8.2.854 UQDECP (scalar)

Unsigned saturating decrement scalar by count of true predicate elements

This instruction counts the number of true elements in the source predicate and then uses the result to decrement the scalar destination. The result is saturated to the general-purpose register's unsigned integer range.

It has encodings from 2 classes: 32-bit and 64-bit

## 32-bit

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UQDECP <Wdn>, <Pm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer m = UInt(Pm); constant integer dn = UInt(Rdn); constant boolean unsigned = TRUE; constant integer ssize = 32;
```

## 64-bit

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UQDECP <Xdn>, <Pm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer m = UInt(Pm); constant integer dn = UInt(Rdn); constant boolean unsigned = TRUE; constant integer ssize = 64;
```

## Assembler Symbols

## &lt;Wdn&gt;

Is the 32-bit name of the source and destination general-purpose register, encoded in the 'Rdn' field.

## &lt;Pm&gt;

Is the name of the source scalable predicate register, encoded in the 'Pm' field.

&lt;T&gt;

Is the size specifier, encoded in 'size':

## &lt;Xdn&gt;

Is the 64-bit name of the source and destination general-purpose register, encoded in the 'Rdn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(ssize) operand1 = X[dn, ssize]; constant bits(PL) operand2 = P[m, PL]; bits(ssize) result; integer count = 0; for e = 0 to elements-1 if ActivePredicateElement(operand2, e, esize) then count = count + 1; if unsigned then (result, -) = UnsignedSatQ(UInt(operand1) count, ssize); X[dn, 64] = ZeroExtend(result, 64); else (result, -) = SignedSatQ(SInt(operand1) count, ssize); X[dn, 64] = SignExtend(result, 64);
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the general-purpose register written by this instruction might be significantly delayed.

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |