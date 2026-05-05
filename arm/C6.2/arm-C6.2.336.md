## C6.2.336 RCWSWPP, RCWSWPPA, RCWSWPPAL, RCWSWPPL

Read check write swap quadword in memory

This instruction atomically loads a 128-bit quadword from a memory location, and conditionally stores the value held in a pair of registers back to the same memory location. Storing back to memory is conditional on RCW Checks. The value initially loaded from memory is returned in the same pair of registers. This instruction updates the condition flags based on the result of the update of memory.

- RCWSWPPA and RCWSWPPAL load from memory with acquire semantics.
- RCWSWPPL and RCWSWPPAL store to memory with release semantics.
- RCWSWPP has neither acquire nor release semantics.

## Note

This instruction is for performing atomic updates of translation table entries and not for general use.

## Integer

(FEAT\_D128 &amp;&amp; FEAT\_THE)

<!-- image -->

## Encoding for the RCWSWPP variant

```
Applies when (A == 0 && R == 0) RCWSWPP <Xt1>, <Xt2>, [<Xn|SP>]
```

## Encoding for the RCWSWPPA variant

```
Applies when (A == 1 && R == 0) RCWSWPPA <Xt1>, <Xt2>, [<Xn|SP>]
```

## Encoding for the RCWSWPPAL variant

```
Applies when (A == 1 && R == 1) RCWSWPPAL <Xt1>, <Xt2>, [<Xn|SP>]
```

## Encoding for the RCWSWPPL variant

1)

```
Applies when (A == 0 && R == RCWSWPPL <Xt1>, <Xt2>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_D128) || !IsFeatureImplemented(FEAT_THE) then EndOfDecode(Decode_UNDEF); if Rt == '11111' then EndOfDecode(Decode_UNDEF); if Rt2 == '11111' then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant boolean soft = FALSE; constant boolean acquire = A == '1'; constant boolean release = R == '1'; constant boolean tagchecked = n != 31; boolean rt_unknown = FALSE; if t == t2 then constant Constraint c = ConstrainUnpredictable(Unpredictable_LSE128OVERLAP); assert c IN {Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_UNKNOWN rt_unknown = TRUE; // result is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP);
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
if !IsD128Enabled(PSTATE.EL) then UNDEFINED; bits(64) address; bits(64) value1; bits(64) value2; bits(128) newdata; bits(128) readdata; bits(4) nzcv; constant AccessDescriptor accdesc = CreateAccDescRCW(MemAtomicOp_SWP, soft, acquire, release, tagchecked, t, t2, t, t2); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; value1 = X[t, 64]; value2 = X[t2, 64]; newdata = if BigEndian(accdesc.acctype) then value1:value2 else value2:value1; constant bits(128) compdata = bits(128) UNKNOWN; // Irrelevant when not executing CAS
```

```
(nzcv, readdata) = MemAtomicRCW(address, compdata, newdata, accdesc); PSTATE.<N,Z,C,V> = nzcv; if rt_unknown then readdata = bits(128) UNKNOWN; if BigEndian(accdesc.acctype) then X[t, 64] = readdata<127:64>; X[t2, 64] = readdata<63:0>; else X[t, 64] = readdata<63:0>; X[t2, 64] = readdata<127:64>;
```
