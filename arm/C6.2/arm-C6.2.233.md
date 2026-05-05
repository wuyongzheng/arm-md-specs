## C6.2.233 LDSETP, LDSETPA, LDSETPAL, LDSETPL

Atomic bit set on quadword

This instruction atomically loads a 128-bit quadword from memory, performs a bitwise OR with the value held in a pair of registers on it, and stores the result back to memory. The value initially loaded from memory is returned in the same pair of registers.

- LDSETPA and LDSETPAL load from memory with acquire semantics.
- LDSETPL and LDSETPAL store to memory with release semantics.
- LDSETP has neither acquire nor release semantics.

## Integer

(FEAT\_LSE128)

<!-- image -->

## Encoding for the LDSETP variant

Applies when

(A == 0

&amp;&amp;

R

==

0)

```
LDSETP <Xt1>, <Xt2>, [<Xn|SP>]
```

## Encoding for the LDSETPA variant

```
0)
```

```
Applies when (A == 1 && R == LDSETPA <Xt1>, <Xt2>, [<Xn|SP>]
```

## Encoding for the LDSETPAL variant

```
Applies when (A == 1 && R == 1) LDSETPAL <Xt1>, <Xt2>, [<Xn|SP>]
```

## Encoding for the LDSETPL variant

```
1)
```

```
Applies when (A == 0 && R == LDSETPL <Xt1>, <Xt2>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LSE128) then EndOfDecode(Decode_UNDEF); if Rt == '11111' then EndOfDecode(Decode_UNDEF); if Rt2 == '11111' then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant boolean acquire = A == '1'; constant boolean release = R == '1'; constant boolean tagchecked = n != 31; boolean rt_unknown = FALSE; if t == t2 then constant Constraint c = ConstrainUnpredictable(Unpredictable_LSE128OVERLAP); assert c IN {Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP};
```

```
case c of when Constraint_UNKNOWN rt_unknown = TRUE; // result when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP);
```

```
is UNKNOWN
```

For information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly CONSTRAINED UNPREDICTABLE behavior for A64 instructions.

## Assembler Symbols

## &lt;Xt1&gt;

Is the 64-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xt2&gt;

Is the 64-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
bits(64) address; constant bits(64) value1 = X[t, 64]; constant bits(64) value2 = X[t2, 64]; bits(128) data; bits(128) store_value; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescAtomicOp(MemAtomicOp_ORR, acquire, release, tagchecked, privileged, t, t2, t, t2); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; store_value = if BigEndian(accdesc.acctype) then value1:value2 else value2:value1; constant bits(128) comparevalue = bits(128) UNKNOWN; // Irrelevant when not executing CAS data = MemAtomic(address, comparevalue, store_value, accdesc); if rt_unknown then data = bits(128) UNKNOWN; if BigEndian(accdesc.acctype) then X[t, 64] = data<127:64>; X[t2, 64] = data<63:0>; else X[t, 64] = data<63:0>; X[t2, 64] = data<127:64>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
