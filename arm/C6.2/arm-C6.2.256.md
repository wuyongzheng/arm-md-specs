## C6.2.256 LDUMINB, LDUMINAB, LDUMINALB, LDUMINLB

Atomic unsigned minimum on byte

This instruction atomically loads an 8-bit byte from memory, compares it against the value held in a register, and stores the smaller value back to memory, treating the values as unsigned numbers. The value initially loaded from memory is returned in the destination register.

- If the destination register is not WZR , LDUMINAB and LDUMINALB load from memory with acquire semantics.
- LDUMINLB and LDUMINALB store to memory with release semantics.
- LDUMINB has neither acquire nor release semantics.

For more information about memory ordering semantics, see Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

This instruction is used by the alias STUMINB, STUMINLB.

## Integer

(FEAT\_LSE)

<!-- image -->

## Encoding for the No memory ordering variant

```
Applies when (A == 0 && R == 0)
```

```
LDUMINB <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the Acquire variant

```
Applies when (A == 1 && R == 0) LDUMINAB <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the Acquire-release variant

```
1)
```

```
Applies when (A == 1 && R == LDUMINALB <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the Release variant

```
Applies when (A == 0 && R == 1) LDUMINLB <Ws>, <Wt>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LSE) then EndOfDecode(Decode_UNDEF); constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean acquire = A == '1' && Rt != '11111'; constant boolean release = R == '1'; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Ws&gt;

Is the 32-bit name of the general-purpose register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Alias Conditions

## Operation

```
bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescAtomicOp(MemAtomicOp_UMIN, acquire, release, tagchecked, privileged, t, s); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant bits(8) comparevalue = bits(8) UNKNOWN; // Irrelevant when not executing CAS constant bits(8) value = X[s, 8]; constant bits(8) data = MemAtomic(address, comparevalue, value, accdesc); if t != 31 then X[t, 32] = ZeroExtend(data, 32);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

## Alias

STUMINB, STUMINLB

## Is preferred when

A == '0' &amp;&amp; Rt == '11111'
