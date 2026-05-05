## C6.2.240 LDTADD, LDTADDA, LDTADDAL, LDTADDL

Atomic add unprivileged

This instruction atomically loads a 32-bit word or 64-bit doubleword from memory, adds the value held in a register to it, and stores the result back to memory. The value initially loaded from memory is returned in the destination register.

- If the destination register is not one of WZR , or XZR , LDTADDA and LDTADDAL load from memory with acquire semantics.
- LDTADDL and LDTADDAL store to memory with release semantics.
- LDTADD has neither acquire nor release semantics.

For more information about memory ordering semantics, see Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

Explicit Memory effects produced by the instruction behave as if the instruction was executed at EL0 if the Effective value of PSTATE.UAO is 0 and either:

- The instruction is executed at EL1.
- The instruction is executed at EL2 when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

Otherwise, the Explicit Memory effects operate with the restrictions determined by the Exception level at which the instruction is executed.

This instruction is used by the alias STTADD, STTADDL.

## Integer

(FEAT\_LSUI)

<!-- image -->

## Encoding for the 32-bit no memory ordering variant

```
Applies when (sz == 0 && A == 0 && R == 0) LDTADD <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 32-bit acquire variant

```
Applies when (sz == 0 && A == 1 && R == 0) LDTADDA <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 32-bit acquire-release variant

```
Applies when (sz == 0 && A == 1 && R == 1) LDTADDAL <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 32-bit release variant

```
Applies when (sz == 0 && A == 0 && R == 1) LDTADDL <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 64-bit no memory ordering variant

```
Applies when (sz == 1 && A == 0 && R ==
```

```
LDTADD
```

```
0) <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the 64-bit acquire variant

```
Applies when (sz == 1 && A == 1 && R ==
```

```
LDTADDA
```

```
0) <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the 64-bit acquire-release variant

```
Applies when (sz == 1 && A == 1 && R ==
```

```
LDTADDAL
```

```
1) <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the 64-bit release variant

```
Applies when (sz == 1 && A == 0 && R ==
```

```
LDTADDL
```

```
1) <Xs>, <Xt>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_LSUI) then constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer datasize = 32 << UInt(sz); constant integer regsize = if datasize == 64 then 64 else 32; constant boolean acquire = A == '1' && Rt != '11111'; constant boolean release = R == '1'; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Ws&gt;

Is the 32-bit name of the general-purpose register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Xs&gt;

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

Is the 64-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## Alias Conditions

## Operation

```
bits(64) address; constant boolean privileged = AArch64.IsUnprivAccessPriv(); constant AccessDescriptor accdesc = CreateAccDescAtomicOp(MemAtomicOp_ADD, acquire, release, tagchecked, privileged, t, s); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant bits(datasize) comparevalue = bits(datasize) UNKNOWN; // Irrelevant when not executing CAS constant bits(datasize) value = X[s, datasize]; constant bits(datasize) data = MemAtomic(address, comparevalue, value, accdesc); if t != 31 then X[t, regsize] = ZeroExtend(data, regsize);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

## Alias

STTADD, STTADDL

## Is preferred when

A == '0' &amp;&amp; Rt == '11111'
