## C6.2.62 CB&lt;cc&gt; (immediate)

Compare register with immediate and branch

This instruction compares the value in a register with an immediate, and conditionally branches to a label at a PC-relative offset if the comparison is true. This instruction provides a hint that this is not a subroutine call or return. This instruction does not affect the condition flags.

This instruction is used by the pseudo-instructions CBGE (immediate), CBHS (immediate), CBLE (immediate), and CBLS (immediate).

## Branch

(FEAT\_CMPBR)

<!-- image -->

## Encoding for the 32-bit greater than variant

Applies when

0

CBGT

(sf

==

&amp;&amp;

cc

== 000)

&lt;Wt&gt;, #&lt;imm&gt;,

&lt;label&gt;

## Encoding for the 32-bit less than variant

Applies when

==

0

CBLT

(sf

&amp;&amp;

cc

== 001)

&lt;Wt&gt;, #&lt;imm&gt;,

&lt;label&gt;

## Encoding for the 32-bit higher variant

```
Applies when (sf == 0 && cc == 010) CBHI <Wt>, #<imm>, <label>
```

## Encoding for the 32-bit lower variant

```
Applies when (sf == 0 && cc == 011) CBLO <Wt>, #<imm>, <label>
```

## Encoding for the 32-bit equal variant

```
Applies when (sf == 0 && cc == 110) CBEQ <Wt>, #<imm>, <label>
```

## Encoding for the 32-bit not equal variant

```
Applies when (sf == 0 && cc == 111) CBNE <Wt>, #<imm>, <label>
```

## Encoding for the 64-bit greater than variant

```
Applies when (sf == 1 && cc == 000) CBGT <Xt>, #<imm>, <label>
```

## Encoding for the 64-bit less than variant

Applies when (sf == 1 &amp;&amp; cc

```
== 001) CBLT <Xt>, #<imm>, <label>
```

## Encoding for the 64-bit higher variant

Applies when (sf == 1 &amp;&amp; cc

```
CBHI <Xt>, #<imm>,
```

```
== 010) <label>
```

## Encoding for the 64-bit lower variant

Applies when (sf == 1 &amp;&amp; cc

```
== 011) CBLO <Xt>, #<imm>, <label>
```

## Encoding for the 64-bit equal variant

```
Applies when (sf == 1 && cc
```

```
CBEQ <Xt>, #<imm>,
```

```
== 110) <label>
```

## Encoding for the 64-bit not equal variant

Applies when (sf == 1 &amp;&amp; cc

```
CBNE <Xt>, #<imm>,
```

```
== 111) <label>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_CMPBR) then EndOfDecode(Decode_UNDEF); constant integer datasize = 32 << UInt(sf); constant integer t = UInt(Rt); constant bits(64) offset = SignExtend(imm9:'00', 64); CmpOp op; boolean unsigned; case cc of when '000' op = Cmp_GT; unsigned = FALSE; when '001' op = Cmp_LT; unsigned = FALSE; when '010' op = Cmp_GT; unsigned = TRUE; when '011' op = Cmp_LT; unsigned = TRUE; when '110' op = Cmp_EQ; unsigned = TRUE; when '111' op = Cmp_NE; unsigned = TRUE; otherwise EndOfDecode(Decode_UNDEF); constant integer value2 = UInt(imm6);
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be tested, encoded in the 'Rt' field.

## &lt;imm&gt;

Is an unsigned immediate, in the range 0 to 63, encoded in the 'imm6' field.

## &lt;label&gt;

Is the program label to be conditionally branched to. Its offset from the address of this instruction, in the range -1024 to 1020, is encoded as 'imm9' times 4.

&lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be tested, encoded in the 'Rt' field.

## Operation

```
constant bits(datasize) operand1 = X[t, datasize]; constant boolean branch_conditional = TRUE; constant integer value1 = if unsigned then UInt(operand1) boolean cond; case op of when Cmp_EQ cond = value1 == value2; when Cmp_NE cond = value1 != value2; when Cmp_LT cond = value1 < value2; when Cmp_GT cond = value1 > value2; if cond then BranchTo(PC64 + offset, BranchType_DIR, branch_conditional); else BranchNotTaken(BranchType_DIR, branch_conditional);
```

```
else SInt(operand1);
```
