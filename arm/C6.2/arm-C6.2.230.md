## C6.2.230 LDSET, LDSETA, LDSETAL, LDSETL

Atomic bit set on word or doubleword

This instruction atomically loads a 32-bit word or 64-bit doubleword from memory, performs a bitwise OR with the value held in a register on it, and stores the result back to memory. The value initially loaded from memory is returned in the destination register.

- If the destination register is not one of WZR or XZR , LDSETA and LDSETAL load from memory with acquire semantics.
- LDSETL and LDSETAL store to memory with release semantics.
- LDSET has neither acquire nor release semantics.

For more information about memory ordering semantics, see Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

This instruction is used by the alias STSET, STSETL.

## Integer

(FEAT\_LSE)

<!-- image -->

## Encoding for the 32-bit no memory ordering variant

Applies when

LDSET

&lt;Ws&gt;,

(size ==

10

&amp;&amp;

A

==

0 &amp;&amp;

&lt;Wt&gt;, [&lt;Xn|SP&gt;]

## Encoding for the 32-bit acquire variant

```
Applies when (size == 10 && A == 1 && R == 0) LDSETA <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 32-bit acquire-release variant

```
Applies when (size == 10 && A == 1 && R == 1) LDSETAL <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 32-bit release variant

```
Applies when (size == 10 && A == 0 && R == 1) LDSETL <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 64-bit no memory ordering variant

```
Applies when (size == 11 && A == 0 && R == 0)
```

```
LDSET <Xs>, <Xt>, [<Xn|SP>]
```

R ==

0)

## Encoding for the 64-bit acquire variant

```
Applies when (size == 11 && A == 1 && R ==
```

```
LDSETA
```

```
0) <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the 64-bit acquire-release variant

```
Applies when (size == 11 && A == 1 && R ==
```

```
LDSETAL
```

```
1) <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the 64-bit release variant

```
Applies when (size == 11 && A == 0 && R ==
```

```
LDSETL
```

```
1) <Xs>, <Xt>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LSE) then EndOfDecode(Decode_UNDEF);
```

```
constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer datasize = 8 << UInt(size); constant integer regsize = if datasize == 64 then 64 else 32; constant boolean acquire = A == '1' && Rt != '11111'; constant boolean release = R == '1'; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Ws&gt;

Is the 32-bit name of the general-purpose register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Xs&gt;

<!-- image -->

Is the 64-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## Alias Conditions

Is the 64-bit name of the general-purpose register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

| Alias         | Is preferred when         |
|---------------|---------------------------|
| STSET, STSETL | A == '0' && Rt == '11111' |

## Operation

```
bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescAtomicOp(MemAtomicOp_ORR, acquire, release, tagchecked, privileged, t, s); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant bits(datasize) comparevalue = bits(datasize) UNKNOWN; // Irrelevant when not executing CAS constant bits(datasize) value = X[s, datasize]; constant bits(datasize) data = MemAtomic(address, comparevalue, value, accdesc); if t != 31 then X[t, regsize] = ZeroExtend(data, regsize);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
