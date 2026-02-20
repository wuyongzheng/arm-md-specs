## C8.2.611 SPLICE

Splice two vectors under predicate control

This instruction selects a region from the first source vector and copies it to the lowest-numbered elements of the result. Any remaining elements of the result are set to a copy of the lowest-numbered elements from the second source vector. The region is selected using the first and last true elements in the vector select predicate register. The result is destructively placed in the destination and first source vector, or constructively placed in the destination vector.

It has encodings from 2 classes: Constructive and Destructive

## Constructive

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SPLICE <Zd>.<T>, <Pv>, { <Zn1>.<T>, <Zn2>.<T> }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer v = UInt(Pv); constant integer dst = UInt(Zd); constant integer s1 = UInt(Zn); constant integer s2 = (s1 + 1) MOD 32;
```

## Destructive

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

|   31 | 29 28   | 25 24 23 22 21 20 19 17 16 15 14 13 12 10 9 5 4   |
|------|---------|---------------------------------------------------|
|    0 | 0 0 0 0 | 0 1 size 1 0 1 1 0 0 1 0 0 Pv Zm Zdn              |

## Encoding

```
SPLICE <Zdn>.<T>, <Pv>, <Zdn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer v = UInt(Pv); constant integer dst = UInt(Zdn); constant integer s1 = dst; constant integer s2 = UInt(Zm);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

&lt;T&gt;

## &lt;Pv&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the vector select predicate register P0-P7, encoded in the 'Pv' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded in the 'Zn' field.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the source multi-vector group, encoded in the 'Zn' field.

## &lt;Zdn&gt;

Is the name of the first source and destination scalable vector register, encoded in the 'Zdn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[v, PL]; constant bits(VL) operand1 = if AnyActiveElement(mask, esize) then Z[s1, VL] else Zeros(VL); constant bits(VL) operand2 = Z[s2, VL]; bits(VL) result; integer x = 0; boolean active = FALSE; constant integer lastnum = LastActiveElement(mask, esize); if lastnum >= 0 then for e = 0 to lastnum active = active || ActivePredicateElement(mask, e, esize); if active then Elem[result, x, esize] = Elem[operand1, e, esize]; x = x + 1; constant integer nelements = (elements -x) - 1; for e = 0 to nelements Elem[result, x, esize] = Elem[operand2, e, esize]; x = x + 1;
```

```
Z[dst, VL] = result;
```

## Operational Information

For the Destructive variant:

The destructive variant of this instruction might be immediately preceded in program order by a MOVPRFX The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and the destructive variant of this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

instruction.