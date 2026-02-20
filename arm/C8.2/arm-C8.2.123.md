## C8.2.123 CTERMEQ, CTERMNE

Compare and terminate loop

This instruction detects termination conditions in serialized vector loops by testing whether the comparison between the scalar source operands holds true. If the comparison is not successful, the instruction tests the state of the !Last condition flag (C), which indicates whether the previous flag-setting predicate instruction selected the last element of the vector partition.

The Z and C condition flags are preserved by this instruction. The N and V condition flags are set as a pair to generate one of the following conditions for a subsequent conditional instruction:

| Condition   |   N |   V | Meaning                                                      |
|-------------|-----|-----|--------------------------------------------------------------|
| GE          |   0 |   0 | Continue loop (compare failed and last element not selected) |
| LT          |   0 |   1 | Terminate loop (last element selected)                       |
| LT          |   1 |   0 | Terminate loop (compare succeeded)                           |
| GE          |   1 |   1 | Never generated                                              |

The scalar source operands are 32-bit or 64-bit general-purpose registers of the same size.

It has encodings from 2 classes: Equal and Not equal

## Equal

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CTERMEQ <R><n>, <R><m>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32 << UInt(sz); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant CmpOp cmp_op = Cmp_EQ;
```

## Not equal

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CTERMNE <R><n>, <R><m>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32 << UInt(sz); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant CmpOp cmp_op = Cmp_NE;
```

## Assembler Symbols

&lt;R&gt;

Is a width specifier, encoded in 'sz':

&lt;n&gt;

&lt;m&gt;

Is the number [0-30] of the source general-purpose register or the name ZR (31), encoded in the 'Rm' field.

## Operation

```
CheckSVEEnabled(); constant bits(esize) operand1 = X[n, esize]; constant bits(esize) operand2 = X[m, esize]; constant integer element1 = UInt(operand1); constant integer element2 = UInt(operand2); boolean term; case cmp_op of when Cmp_EQ term = element1 == element2; when Cmp_NE term = element1 != element2; if term then PSTATE.N = '1'; PSTATE.V = '0'; else PSTATE.N = '0'; PSTATE.V = (NOT PSTATE.C);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   sz | <R>   |
|------|-------|
|    0 | W     |
|    1 | X     |

Is the number [0-30] of the source general-purpose register or the name ZR (31), encoded in the 'Rn' field.