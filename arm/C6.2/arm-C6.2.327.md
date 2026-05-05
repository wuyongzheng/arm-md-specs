## C6.2.327 RCWSCLR, RCWSCLRA, RCWSCLRAL, RCWSCLRL

Read check write software atomic bit clear on doubleword in memory

This instruction atomically loads a 64-bit doubleword from memory, performs a bitwise AND with the complement of the value held in a register on it, and conditionally stores the result back to memory. Storing of the result back to memory is conditional on RCW Checks and RCWS Checks. The value initially loaded from memory is returned in the destination register. This instruction updates the condition flags based on the result of the update of memory.

- If the destination register is not XZR , RCWSCLRA and RCWSCLRAL load from memory with acquire semantics.
- RCWSCLRL and RCWSCLRAL store to memory with release semantics.
- RCWSCLR has neither acquire nor release semantics.

## Note

This instruction is for performing atomic updates of translation table entries and not for general use.

## Integer

(FEAT\_THE)

<!-- image -->

## Encoding for the RCWSCLR variant

Applies when

(A == 0

RCWSCLR

&amp;&amp;

R

==

0)

&lt;Xs&gt;, &lt;Xt&gt;, [&lt;Xn|SP&gt;]

## Encoding for the RCWSCLRA variant

```
Applies when (A == 1 && R == 0) RCWSCLRA <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the RCWSCLRAL variant

```
1)
```

```
Applies when (A == 1 && R == RCWSCLRAL <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the RCWSCLRL variant

```
Applies when (A == 0 && R == 1) RCWSCLRL <Xs>, <Xt>, [<Xn|SP>]
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
if IsD128Enabled(PSTATE.EL) then UNDEFINED; bits(64) address; constant bits(64) newdata = X[s, 64]; bits(64) readdata; bits(4) nzcv; constant AccessDescriptor accdesc = CreateAccDescRCW(MemAtomicOp_BIC, soft, acquire, release, tagchecked, t, s); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant bits(64) compdata = bits(64) UNKNOWN; // Irrelevant when not executing CAS (nzcv, readdata) = MemAtomicRCW(address, compdata, newdata, accdesc); PSTATE.<N,Z,C,V> = nzcv; X[t, 64] = readdata; // Return the old value when t!=31
```
