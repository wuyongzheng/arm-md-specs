## C6.2.63 CB&lt;cc&gt; (register)

Compare registers and branch

This instruction compares the values in two registers, and conditionally branches to a label at a PC-relative offset if the condition is true. This instruction provides a hint that this is not a subroutine call or return. This instruction does not affect the condition flags.

This instruction is used by the pseudo-instructions CBLE (register), CBLO (register), CBLS (register), and CBLT (register).

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

&lt;Wt&gt;, &lt;Wm&gt;, &lt;label&gt;

## Encoding for the 32-bit greater than or equal variant

Applies when

CBGE

(sf

==

0

&amp;&amp;

cc

== 001)

&lt;Wt&gt;, &lt;Wm&gt;, &lt;label&gt;

## Encoding for the 32-bit higher variant

Applies when

(sf

==

0

CBHI

&amp;&amp;

cc

== 010)

&lt;Wt&gt;, &lt;Wm&gt;, &lt;label&gt;

## Encoding for the 32-bit higher or same variant

Applies when

CBHS

(sf

==

0

&amp;&amp;

cc

== 011)

&lt;Wt&gt;, &lt;Wm&gt;, &lt;label&gt;

## Encoding for the 32-bit equal variant

Applies when

(sf

==

0

CBEQ

&amp;&amp;

cc

== 110)

&lt;Wt&gt;, &lt;Wm&gt;, &lt;label&gt;

## Encoding for the 32-bit not equal variant

```
Applies when (sf == 0 && cc == 111) CBNE <Wt>, <Wm>, <label>
```

## Encoding for the 64-bit greater than variant

```
Applies when (sf == 1 && cc == 000) CBGT <Xt>, <Xm>, <label>
```

cc

== 000)

## Encoding for the 64-bit greater than or equal variant

Applies when (sf == 1 &amp;&amp; cc == 001)

```
CBGE <Xt>, <Xm>, <label>
```

## Encoding for the 64-bit higher variant

```
Applies when (sf == 1 && cc
```

```
CBHI
```

```
== 010) <Xt>, <Xm>, <label>
```

## Encoding for the 64-bit higher or same variant

```
Applies when (sf == 1 && cc == 011)
```

```
CBHS
```

```
<Xt>, <Xm>, <label>
```

## Encoding for the 64-bit equal variant

```
Applies when (sf == 1 && cc == 110)
```

```
CBEQ <Xt>, <Xm>, <label>
```

## Encoding for the 64-bit not equal variant

```
Applies when (sf == 1 && cc == 111)
```

```
CBNE <Xt>, <Xm>, <label>
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_CMPBR) then constant integer datasize = 32 << UInt(sf); constant integer t = UInt(Rt); constant integer m = UInt(Rm); constant bits(64) offset = SignExtend(imm9:'00', 64); CmpOp op; boolean unsigned; case cc of when '000' op = Cmp_GT; unsigned = FALSE; when '001' op = Cmp_GE; unsigned = FALSE; when '010' op = Cmp_GT; unsigned = TRUE; when '011' op = Cmp_GE; unsigned = TRUE; when '110' op = Cmp_EQ; unsigned = TRUE; when '111' op = Cmp_NE; unsigned = TRUE; otherwise EndOfDecode(Decode_UNDEF);
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be tested, encoded in the 'Rt' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## &lt;label&gt;

Is the program label to be conditionally branched to. Its offset from the address of this instruction, in the range -1024 to 1020, is encoded as 'imm9' times 4.

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be tested, encoded in the 'Rt' field.

<!-- image -->

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## Operation

```
constant bits(datasize) operand1 = X[t, datasize]; constant bits(datasize) operand2 = X[m, datasize]; constant boolean branch_conditional = TRUE; constant integer value1 = if unsigned then UInt(operand1) else SInt(operand1); constant integer value2 = if unsigned then UInt(operand2) else SInt(operand2); boolean cond; case op of when Cmp_EQ cond = value1 == value2; when Cmp_NE cond = value1 != value2; when Cmp_GE cond = value1 >= value2; when Cmp_GT cond = value1 > value2; if cond then BranchTo(PC64 + offset, BranchType_DIR, branch_conditional); else BranchNotTaken(BranchType_DIR, branch_conditional);
```
