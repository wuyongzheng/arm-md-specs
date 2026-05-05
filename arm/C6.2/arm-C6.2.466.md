## C6.2.466 SWP, SWPA, SWPAL, SWPL

Swap word or doubleword in memory

This instruction atomically loads a 32-bit word or 64-bit doubleword from a memory location, and stores the value held in a register back to the same memory location. The value initially loaded from memory is returned in the destination register.

- If the destination register is not one of WZR or XZR , SWPA and SWPAL load from memory with acquire semantics.
- SWPL and SWPAL store to memory with release semantics.
- SWP has neither acquire nor release semantics.

For more information about memory ordering semantics, see Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

## Integer

(FEAT\_LSE)

<!-- image -->

## Encoding for the 32-bit SWP variant

```
Applies when (size == 10 && A == 0 && R == 0)
```

```
SWP <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 32-bit SWPA variant

```
Applies when (size == 10 && A == 1 && R == 0) SWPA <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 32-bit SWPAL variant

```
Applies when (size == 10 && A == 1 && R == 1) SWPAL <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 32-bit SWPL variant

Applies when (size == 10 &amp;&amp; A == 0 &amp;&amp; R == 1)

```
SWPL <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the 64-bit SWP variant

```
Applies when (size == 11 && A == 0 && R == 0)
```

```
SWP <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the 64-bit SWPA variant

```
Applies when (size == 11 && A == 1 && R == 0) SWPA <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the 64-bit SWPAL variant

Applies when (size == 11 &amp;&amp; A == 1 &amp;&amp; R ==

```
SWPAL <Xs>,
```

```
1) <Xt>, [<Xn|SP>]
```

## Encoding for the 64-bit SWPL variant

Applies when (size == 11 &amp;&amp; A == 0 &amp;&amp; R ==

```
SWPL
```

```
1) <Xs>, <Xt>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LSE) then EndOfDecode(Decode_UNDEF); constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer datasize = 8 << UInt(size); constant integer regsize = if datasize == 64 then 64 else 32; constant boolean acquire = A == '1' && Rt != '11111'; constant boolean release = R == '1'; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Ws&gt;

Is the 32-bit name of the general-purpose register to be stored, encoded in the 'Rs' field.

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Xs&gt;

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## Operation

```
bits(64) address; bits(datasize) data; bits(datasize) store_value; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescAtomicOp(MemAtomicOp_SWP, acquire, release, tagchecked, privileged, t, s); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; store_value = X[s, datasize];
```

Is the 64-bit name of the general-purpose register to be stored, encoded in the 'Rs' field.

```
constant bits(datasize) comparevalue = bits(datasize) UNKNOWN; // Irrelevant when not executing CAS data = MemAtomic(address, comparevalue, store_value, accdesc); X[t, regsize] = ZeroExtend(data, regsize);
```
