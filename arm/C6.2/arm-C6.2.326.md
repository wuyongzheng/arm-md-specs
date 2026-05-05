## C6.2.326 RCWSCASP, RCWSCASPA, RCWSCASPAL, RCWSCASPL

Read check write software compare and swap quadword in memory

This instruction reads a 128-bit quadword from memory, and compares it against the value held in a pair of registers. If the comparison is equal, the value in a second pair of registers is conditionally written to memory. Storing back to memory is conditional on RCW Checks and RCWS Checks. If the compare fails, the RCW Checks fail, or the RCWS Checks fail, the architecture permits writing the value read from the location to memory. If the write is performed, the read and the write occur atomically such that no other modification of the memory location can take place between the read and the write. This instruction updates the condition flags based on the result of the update of memory.

- RCWSCASPA and RCWSCASPAL load from memory with acquire semantics.
- RCWSCASPL and RCWSCASPAL store to memory with release semantics.
- RCWSCASP has neither acquire nor release semantics.

## Note

This instruction is for performing atomic updates of translation table entries and not for general use.

## Integer

(FEAT\_D128 &amp;&amp; FEAT\_THE)

<!-- image -->

## Encoding for the RCWSCASP variant

```
Applies when (A == 0 && R == 0) RCWSCASP
```

```
<Xs>, <X(s+1)>, <Xt>, <X(t+1)>, [<Xn|SP>]
```

## Encoding for the RCWSCASPA variant

```
Applies when (A == 1 && R == 0) RCWSCASPA <Xs>, <X(s+1)>, <Xt>, <X(t+1)>, [<Xn|SP>]
```

## Encoding for the RCWSCASPAL variant

```
Applies when (A == 1 && R == 1) RCWSCASPAL <Xs>, <X(s+1)>, <Xt>, <X(t+1)>, [<Xn|SP>]
```

## Encoding for the RCWSCASPL variant

```
Applies when (A == 0 && R == 1)
```

```
RCWSCASPL <Xs>, <X(s+1)>, <Xt>, <X(t+1)>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_D128) || !IsFeatureImplemented(FEAT_THE) then EndOfDecode(Decode_UNDEF); if Rs<0> == '1' then EndOfDecode(Decode_UNDEF); if Rt<0> == '1' then EndOfDecode(Decode_UNDEF); constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean acquire = A == '1'; constant boolean release = R == '1'; constant boolean soft = TRUE; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Xs&gt;

Is the 64-bit name of the first general-purpose register to be compared and loaded, encoded in the 'Rs' field. &lt;Xs&gt; must be an even-numbered register.

## &lt;X(s+1)&gt;

Is the 64-bit name of the second general-purpose register to be compared and loaded.

## &lt;Xt&gt;

Is the 64-bit name of the first general-purpose register to be conditionally stored, encoded in the 'Rt' field. &lt;Xt&gt; must be an even-numbered register.

## &lt;X(t+1)&gt;

Is the 64-bit name of the second general-purpose register to be conditionally stored.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
if !IsD128Enabled(PSTATE.EL) then UNDEFINED; bits(64) address; bits(128) newdata; bits(128) compdata; bits(128) readdata; bits(4) nzcv; constant bits(64) s1 = X[s, 64]; constant bits(64) s2 = X[s+1, 64]; constant bits(64) t1 = X[t, 64]; constant bits(64) t2 = X[t+1, 64]; constant AccessDescriptor accdesc = CreateAccDescRCW(MemAtomicOp_CAS, soft, acquire, release, tagchecked, t, t+1, s, s+1); compdata = if BigEndian(accdesc.acctype) then s1:s2 else s2:s1; newdata = if BigEndian(accdesc.acctype) then t1:t2 else t2:t1; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; (nzcv, readdata) = MemAtomicRCW(address, compdata, newdata, accdesc);
```

```
PSTATE.<N,Z,C,V> = nzcv; if BigEndian(accdesc.acctype) then X[s, 64] = readdata<127:64>; X[s+1, 64] = readdata<63:0>; else X[s, 64] = readdata<63:0>; X[s+1, 64] = readdata<127:64>;
```
