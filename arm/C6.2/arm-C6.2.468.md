## C6.2.468 SWPH, SWPAH, SWPALH, SWPLH

Swap halfword in memory

This instruction atomically loads a 16-bit halfword from a memory location, and stores the value held in a register back to the same memory location. The value initially loaded from memory is returned in the destination register.

- If the destination register is not WZR , SWPAH and SWPALH load from memory with acquire semantics.
- SWPLH and SWPALH store to memory with release semantics.
- SWPH has neither acquire nor release semantics.

For more information about memory ordering semantics, see Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

## Integer

(FEAT\_LSE)

<!-- image -->

## Encoding for the SWPH variant

```
Applies when (A == 0 && R == 0) SWPH <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the SWPAH variant

```
Applies when (A == 1 && R == 0) SWPAH <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the SWPALH variant

```
Applies when (A == 1 && R == SWPALH <Ws>, <Wt>, [<Xn|SP>]
```

```
1)
```

## Encoding for the SWPLH variant

```
Applies when (A == 0 && R == 1) SWPLH <Ws>, <Wt>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LSE) then EndOfDecode(Decode_UNDEF); constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean acquire = A == '1' && Rt != '11111'; constant boolean release = R == '1'; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Ws&gt;

Is the 32-bit name of the general-purpose register to be stored, encoded in the 'Rs' field.

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
bits(64) address; bits(16) data; bits(16) store_value; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescAtomicOp(MemAtomicOp_SWP, acquire, release, tagchecked, privileged, t, s); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; store_value = X[s, 16]; constant bits(16) comparevalue = bits(16) UNKNOWN; // Irrelevant when not executing CAS data = MemAtomic(address, comparevalue, store_value, accdesc); X[t, 32] = ZeroExtend(data, 32);
```
