## C6.2.55 CASPT, CASPAT, CASPALT, CASPLT

Compare and swap pair unprivileged

This instruction reads a pair of 64-bit doublewords from memory, and compares them against the values held in the first pair of registers. If the comparison is equal, the values in the second pair of registers are written to memory. If the comparison is not equal, the architecture permits writing the value read from the location to memory. If the writes are performed, the reads and writes occur atomically such that no other modification of the memory location can take place between the reads and writes.

- CASPAT and CASPALT load from memory with acquire semantics.
- CASPLT and CASPALT store to memory with release semantics.
- CASPT has neither acquire nor release semantics.

The architecture permits that the data read clears any exclusive monitors associated with that location, even if the compare subsequently fails.

If the instruction generates a synchronous Data Abort, the registers which are compared and loaded, that is &lt;Xs&gt; and &lt;X(s+1)&gt; , are restored to the values held in the registers before the instruction was executed.

Explicit Memory effects produced by the instruction behave as if the instruction was executed at EL0 if the Effective value of PSTATE.UAO is 0 and either:

- The instruction is executed at EL1.
- The instruction is executed at EL2 when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

Otherwise, the Explicit Memory effects operate with the restrictions determined by the Exception level at which the instruction is executed.

For a CASPT or CASPAT instruction, when &lt;Ws&gt; or &lt;Xs&gt; specifies the same register as &lt;Wt&gt; or &lt;Xt&gt; , this signals to the memory system that an additional subsequent CASPT , CASPAT , CASPALT , or CASPLT access to the specified location is likely to occur in the near future. The memory system can respond by taking actions that are expected to enable the subsequent CASPT , CASPAT , CASPALT , or CASPLT access to succeed when it does occur.

Acode sequence starting with a CASPT or CASPAT instruction for which &lt;Ws&gt; or &lt;Xs&gt; specifies the same register as &lt;Wt&gt; or &lt;Xt&gt; , and ending with a subsequent CASPT , CASPAT , CASPALT , or CASPLT to the same location, exhibits the following properties for best performance when the location may be accessed concurrently, on one or more other PEs:

- The sequence does not contain any direct system register writes, address translation instructions, cache or TLB maintenance operations, exception producing instructions, exception returns, or ISB barriers.
- The execution of the sequence includes 32 or fewer instructions.
- The value provided in &lt;Ws&gt; or &lt;Xs&gt; of the first CASPT or CASPAT is a value likely to result in the comparison failing. A failing comparison result may lead to better performance due to the hardware not performing a write to memory.

Note

For a CASPT or CASPAT instruction, when &lt;Ws&gt; or &lt;Xs&gt; specifies the same register as &lt;Wt&gt; or &lt;Xt&gt; , the value in memory is not modified, because the CASPT or CASPAT either fails its compare or writes the same value back to memory.

For more information about memory ordering semantics, see Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

No offset

(FEAT\_LSUI)

<!-- image -->

## Encoding for the CASPT variant

Applies when

```
(L == 0 && o0 == 0) CASPT <Xs>, <X(s+1)>, <Xt>, <X(t+1)>, [<Xn|SP>{, #0}]
```

## Encoding for the CASPAT variant

```
Applies when (L == 1 && o0 == 0) CASPAT <Xs>, <X(s+1)>, <Xt>, <X(t+1)>, [<Xn|SP>{, #0}]
```

## Encoding for the CASPALT variant

```
Applies when (L == 1 && o0 == 1) CASPALT <Xs>, <X(s+1)>, <Xt>, <X(t+1)>, [<Xn|SP>{, #0}]
```

## Encoding for the CASPLT variant

```
Applies when (L == 0 && o0 == 1) CASPLT <Xs>, <X(s+1)>, <Xt>, <X(t+1)>, [<Xn|SP>{, #0}]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LSUI) then EndOfDecode(Decode_UNDEF); if Rs<0> == '1' || Rt<0> == '1' then EndOfDecode(Decode_UNDEF); constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer datasize = 64; constant boolean acquire = L == '1'; constant boolean release = o0 == '1'; constant boolean tagchecked = n != 31;
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
bits(64) address; bits(2*datasize) comparevalue; bits(2*datasize) newvalue; bits(2*datasize) data; constant bits(datasize) s1 = X[s, datasize]; constant bits(datasize) s2 = X[s+1, datasize]; constant bits(datasize) t1 = X[t, datasize]; constant bits(datasize) t2 = X[t+1, datasize]; constant boolean privileged = AArch64.IsUnprivAccessPriv(); constant AccessDescriptor accdesc = CreateAccDescAtomicOp(MemAtomicOp_CAS, acquire, release, tagchecked, privileged, t, t+1, s, s+1); comparevalue = if BigEndian(accdesc.acctype) then s1:s2 else s2:s1; newvalue = if BigEndian(accdesc.acctype) then t1:t2 else t2:t1; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; data = MemAtomic(address, comparevalue, newvalue, accdesc); if BigEndian(accdesc.acctype) then X[s, datasize] = data<2*datasize-1:datasize>; X[s+1, datasize] = data<datasize-1:0>; else X[s, datasize] = data<datasize-1:0>; X[s+1, datasize] = data<2*datasize-1:datasize>;
```
