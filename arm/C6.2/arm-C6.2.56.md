## C6.2.56 CAST, CASAT, CASALT, CASLT

Compare and swap unprivileged

This instruction reads a 64-bit doubleword from memory, and compares it against the value held in a first register. If the comparison is equal, the value in a second register is written to memory. If the comparison is not equal, the architecture permits writing the value read from the location to memory. If the write is performed, the read and write occur atomically such that no other modification of the memory location can take place between the read and write.

- If the destination register is not one of WZR or XZR , CASAT and CASALT load from memory with acquire semantics.
- CASLT and CASALT store to memory with release semantics.
- CAST has neither acquire nor release semantics.

The architecture permits that the data read clears any exclusive monitors associated with that location, even if the compare subsequently fails.

If the instruction generates a synchronous Data Abort, the register which is compared and loaded, that is &lt;Xs&gt; , is restored to the value held in the register before the instruction was executed.

Explicit Memory effects produced by the instruction behave as if the instruction was executed at EL0 if the Effective value of PSTATE.UAO is 0 and either:

- The instruction is executed at EL1.
- The instruction is executed at EL2 when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

Otherwise, the Explicit Memory effects operate with the restrictions determined by the Exception level at which the instruction is executed.

For a CAST or CASAT instruction, when &lt;Ws&gt; or &lt;Xs&gt; specifies the same register as &lt;Wt&gt; or &lt;Xt&gt; , this signals to the memory system that an additional subsequent CAST , CASAT , CASALT , or CASLT access to the specified location is likely to occur in the near future. The memory system can respond by taking actions that are expected to enable the subsequent CAST , CASAT , CASALT , or CASLT access to succeed when it does occur.

Acode sequence starting with a CAST or CASAT instruction for which &lt;Ws&gt; or &lt;Xs&gt; specifies the same register as &lt;Wt&gt; or &lt;Xt&gt; , and ending with a subsequent CAST , CASAT , CASALT , or CASLT to the same location, exhibits the following properties for best performance when the location may be accessed concurrently, on one or more other PEs:

- The sequence does not contain any direct system register writes, address translation instructions, cache or TLB maintenance operations, exception producing instructions, exception returns, or ISB barriers.
- The execution of the sequence includes 32 or fewer instructions.
- The value provided in &lt;Ws&gt; or &lt;Xs&gt; of the first CAST or CASAT is a value likely to result in the comparison failing. Afailing comparison result may lead to better performance due to the hardware not performing a write to memory.

Note

For a CAST or CASAT instruction, when &lt;Ws&gt; or &lt;Xs&gt; specifies the same register as &lt;Wt&gt; or &lt;Xt&gt; , the value in memory is not modified, because the CAST or CASAT either fails its compare or writes the same value back to memory.

For more information about memory ordering semantics, see Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

## No offset

(FEAT\_LSUI)

<!-- image -->

## Encoding for the CAST variant

```
Applies when (L == 0 && o0 == 0) CAST <Xs>, <Xt>, [<Xn|SP>{, #0}]
```

## Encoding for the CASAT variant

```
Applies when (L == 1 && o0 == 0) CASAT <Xs>, <Xt>, [<Xn|SP>{, #0}]
```

## Encoding for the CASALT variant

```
Applies when (L == 1 && o0 == 1) CASALT <Xs>, <Xt>, [<Xn|SP>{, #0}]
```

## Encoding for the CASLT variant

```
Applies when (L == 0 && o0 == 1) CASLT <Xs>, <Xt>, [<Xn|SP>{, #0}]
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_LSUI) then constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean acquire = L == '1' && t != 31; constant boolean release = o0 == '1'; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Xs&gt;

Is the 64-bit name of the general-purpose register to be compared and loaded, encoded in the 'Rs' field.

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be conditionally stored, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
bits(64) address; bits(64) comparevalue; bits(64) newvalue; constant boolean privileged = AArch64.IsUnprivAccessPriv(); constant AccessDescriptor accdesc = CreateAccDescAtomicOp(MemAtomicOp_CAS, acquire, release, tagchecked, privileged, t, s); comparevalue = X[s, 64]; newvalue = X[t, 64]; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; X[s, 64] = MemAtomic(address, comparevalue, newvalue, accdesc);
```
