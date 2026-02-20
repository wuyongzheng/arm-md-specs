## C8.2.650 SQINCP (vector)

Signed saturating increment vector by count of true predicate elements

This instruction counts the number of true elements in the source predicate and then uses the result to increment all destination vector elements. The results are saturated to the element signed integer range.

The predicate size specifier may be omitted in assembler source code, but this is deprecated and will be prohibited in a future release of the architecture.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
SQINCP <Zdn>.<T>, <Pm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer m = UInt(Pm); constant integer dn = UInt(Zdn); constant boolean unsigned = FALSE;
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the source and destination scalable vector register, encoded in the 'Zdn' field.

<!-- image -->

Is the size specifier, encoded in 'size':

## &lt;Pm&gt;

Is the name of the source scalable predicate register, encoded in the 'Pm' field.

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[dn, VL]; constant bits(PL) operand2 = P[m, PL]; bits(VL) result; integer count = 0; for e = 0 to elements-1 if ActivePredicateElement(operand2, e, esize) then count = count + 1; for e = 0 to elements-1 constant bits(esize) opelt = Elem[operand1, e, esize]; if unsigned then (Elem[result, e, esize], -) = UnsignedSatQ(UInt(opelt) + count, esize); else (Elem[result, e, esize], -) = SignedSatQ(SInt(opelt) + count, esize); Z[dn, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.