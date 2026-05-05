## C6.2.467 SWPB, SWPAB, SWPALB, SWPLB

Swap byte in memory

This instruction atomically loads an 8-bit byte from a memory location, and stores the value held in a register back to the same memory location. The value initially loaded from memory is returned in the destination register.

- If the destination register is not WZR , SWPAB and SWPALB load from memory with acquire semantics.
- SWPLB and SWPALB store to memory with release semantics.
- SWPB has neither acquire nor release semantics.

For more information about memory ordering semantics, see Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

## Integer

(FEAT\_LSE)

<!-- image -->

## Encoding for the SWPB variant

```
Applies when (A == 0 && R == 0) SWPB <Ws>, <Wt>, [<Xn|SP>]
```

## Encoding for the SWPAB variant

```
Applies when (A == 1 && R == SWPAB <Ws>, <Wt>, [<Xn|SP>]
```

```
0)
```

## Encoding for the SWPALB variant

```
Applies when (A == 1 && R == SWPALB <Ws>, <Wt>, [<Xn|SP>]
```

```
1)
```

## Encoding for the SWPLB variant

```
Applies when (A == 0 && R == 1) SWPLB <Ws>, <Wt>, [<Xn|SP>]
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
bits(64) address; bits(8) data; bits(8) store_value; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescAtomicOp(MemAtomicOp_SWP, acquire, release, tagchecked, privileged, t, s); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; store_value = X[s, 8]; constant bits(8) comparevalue = bits(8) UNKNOWN; // Irrelevant when not executing CAS data = MemAtomic(address, comparevalue, store_value, accdesc); X[t, 32] = ZeroExtend(data, 32);
```
