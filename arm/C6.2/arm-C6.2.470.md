## C6.2.470 SWPT, SWPTA, SWPTAL, SWPTL

Swap unprivileged

This instruction atomically loads a 32-bit word or 64-bit doubleword from a memory location, and stores the value held in a register back to the same memory location. The value initially loaded from memory is returned in the destination register.

- If the destination register is not one of WZR or XZR , SWPTA and SWPTAL load from memory with acquire semantics.
- SWPTL and SWPTAL store to memory with release semantics.
- SWPT has neither acquire nor release semantics.

For more information about memory ordering semantics, see Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

Explicit Memory effects produced by the instruction behave as if the instruction was executed at EL0 if the Effective value of PSTATE.UAO is 0 and either:

- The instruction is executed at EL1.
- The instruction is executed at EL2 when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

Otherwise, the Explicit Memory effects operate with the restrictions determined by the Exception level at which the instruction is executed.

## Integer

(FEAT\_LSUI)

<!-- image -->

## Encoding for the 32-bit SWPT variant

```
Applies when (sz == 0 && A == 0 && R == 0)
```

```
SWPT <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 32-bit SWPTA variant

```
Applies when (sz == 0 && A == 1 && R == 0) SWPTA <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 32-bit SWPTAL variant

Applies when (sz == 0 &amp;&amp; A == 1 &amp;&amp; R ==

```
SWPTAL
```

```
1) <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 32-bit SWPTL variant

Applies when (sz == 0 &amp;&amp; A == 0 &amp;&amp; R == 1)

```
SWPTL <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 64-bit SWPT variant

Applies when (sz == 1 &amp;&amp; A == 0 &amp;&amp; R ==

```
SWPT
```

```
0) <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the 64-bit SWPTA variant

```
Applies when (sz == 1 && A == 1 && R ==
```

```
SWPTA <Xs>,
```

```
0) <Xt>, [<Xn|SP>]
```

## Encoding for the 64-bit SWPTAL variant

```
Applies when (sz == 1 && A == 1 && R == 1)
```

```
SWPTAL <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the 64-bit SWPTL variant

```
Applies when (sz == 1 && A == 0 && R == 1)
```

```
SWPTL <Xs>, <Xt>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LSUI) then constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer datasize = 32 << UInt(sz); constant integer regsize = if datasize == 64 then 64 else 32; constant boolean acquire = A == '1' && Rt != '11111'; constant boolean release = R == '1'; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Ws&gt;

Is the 32-bit name of the general-purpose register to be stored, encoded in the 'Rs' field.

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

&lt;Xs&gt;

- &lt;Xt&gt;

```
EndOfDecode(Decode_UNDEF);
```

Is the 64-bit name of the general-purpose register to be stored, encoded in the 'Rs' field.

Is the 64-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## Operation

```
bits(64) address; bits(datasize) data; bits(datasize) store_value; constant boolean privileged = AArch64.IsUnprivAccessPriv(); constant AccessDescriptor accdesc = CreateAccDescAtomicOp(MemAtomicOp_SWP, acquire, release, tagchecked, privileged, t, s); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; store_value = X[s, datasize]; constant bits(datasize) comparevalue = bits(datasize) UNKNOWN; // Irrelevant when not executing CAS data = MemAtomic(address, comparevalue, store_value, accdesc); X[t, regsize] = ZeroExtend(data, regsize);
```
