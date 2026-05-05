## C6.2.331 RCWSSET, RCWSSETA, RCWSSETAL, RCWSSETL

Read check write software atomic bit set on doubleword in memory

This instruction atomically loads a 64-bit doubleword from memory, performs a bitwise OR with the complement of the value held in a register on it, and conditionally stores the result back to memory. Storing of the result back to memory is conditional on RCW Checks and RCWS Checks. The value initially loaded from memory is returned in the destination register. This instruction updates the condition flags based on the result of the update of memory.

- If the destination register is not XZR , RCWSSETA and RCWSSETAL load from memory with acquire semantics.
- RCWSSETL and RCWSSETAL store to memory with release semantics.
- RCWSSET has neither acquire nor release semantics.

## Note

This instruction is for performing atomic updates of translation table entries and not for general use.

## Integer

(FEAT\_THE)

<!-- image -->

## Encoding for the RCWSSET variant

```
Applies when (A == 0 && R == 0)
```

```
RCWSSET <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the RCWSSETA variant

```
Applies when (A == 1 && R == 0) RCWSSETA <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the RCWSSETAL variant

```
1)
```

```
Applies when (A == 1 && R == RCWSSETAL <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the RCWSSETL variant

```
Applies when (A == 0 && R == 1) RCWSSETL <Xs>, <Xt>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_THE) then EndOfDecode(Decode_UNDEF); constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean soft = TRUE; constant boolean acquire = A == '1' && t != 31; constant boolean release = R == '1'; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Xs&gt;

Is the 64-bit name of the general-purpose register to be stored, encoded in the 'Rs' field.

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be loaded, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
if IsD128Enabled(PSTATE.EL) then UNDEFINED; bits(64) address; constant bits(64) newdata = X[s, 64]; bits(64) readdata; bits(4) nzcv; constant AccessDescriptor accdesc = CreateAccDescRCW(MemAtomicOp_ORR, soft, acquire, release, tagchecked, t, s); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant bits(64) compdata = bits(64) UNKNOWN; // Irrelevant when not executing CAS (nzcv, readdata) = MemAtomicRCW(address, compdata, newdata, accdesc); PSTATE.<N,Z,C,V> = nzcv; X[t, 64] = readdata; // Return the old value when t!=31
```
