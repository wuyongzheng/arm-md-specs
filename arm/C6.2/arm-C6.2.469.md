## C6.2.469 SWPP, SWPPA, SWPPAL, SWPPL

Swap quadword in memory

This instruction atomically loads a 128-bit quadword from a memory location, and stores the value held in a pair of registers back to the same memory location. The value initially loaded from memory is returned in the same pair of registers.

- SWPPA and SWPPAL load from memory with acquire semantics.
- SWPPL and SWPPAL store to memory with release semantics.
- SWPP has neither acquire nor release semantics.

## Integer

(FEAT\_LSE128)

<!-- image -->

## Encoding for the SWPP variant

Applies when

(A == 0

&amp;&amp;

R

==

```
SWPP <Xt1>, <Xt2>, [<Xn|SP>]
```

## Encoding for the SWPPA variant

```
Applies when (A == 1 && R == 0) SWPPA <Xt1>, <Xt2>, [<Xn|SP>]
```

## Encoding for the SWPPAL variant

```
Applies when (A == 1 && R == 1) SWPPAL <Xt1>, <Xt2>, [<Xn|SP>]
```

## Encoding for the SWPPL variant

```
Applies when (A == 0 && R == 1) SWPPL <Xt1>, <Xt2>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LSE128) then EndOfDecode(Decode_UNDEF); if Rt == '11111' then EndOfDecode(Decode_UNDEF); if Rt2 == '11111' then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant boolean acquire = A == '1'; constant boolean release = R == '1'; constant boolean tagchecked = n != 31; boolean rt_unknown = FALSE; if t == t2 then
```

0)

```
constant Constraint c = ConstrainUnpredictable(Unpredictable_LSE128OVERLAP); assert c IN {Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_UNKNOWN rt_unknown = TRUE; // result is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP);
```

For information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly CONSTRAINED UNPREDICTABLE behavior for A64 instructions.

## Assembler Symbols

&lt;Xt1&gt;

Is the 64-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xt2&gt;

Is the 64-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
bits(64) address; constant bits(64) value1 = X[t, 64]; constant bits(64) value2 = X[t2, 64]; bits(128) data; bits(128) store_value; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescAtomicOp(MemAtomicOp_SWP, acquire, release, tagchecked, privileged, t, t2, t, t2); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; store_value = if BigEndian(accdesc.acctype) then value1:value2 else value2:value1; constant bits(128) comparevalue = bits(128) UNKNOWN; // Irrelevant when not executing CAS data = MemAtomic(address, comparevalue, store_value, accdesc); if rt_unknown then data = bits(128) UNKNOWN; if BigEndian(accdesc.acctype) then X[t, 64] = data<127:64>; X[t2, 64] = data<63:0>; else X[t, 64] = data<63:0>; X[t2, 64] = data<127:64>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
