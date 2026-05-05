## C6.2.54 CASP, CASPA, CASPAL, CASPL

Compare and swap pair of words or doublewords in memory

This instruction reads a pair of 32-bit words or 64-bit doublewords from memory, and compares them against the values held in the first pair of registers. If the comparison is equal, the values in the second pair of registers are written to memory. If the comparison is not equal, the architecture permits writing the value read from the location to memory. If the writes are performed, the reads and writes occur atomically such that no other modification of the memory location can take place between the reads and writes.

- CASPA and CASPAL load from memory with acquire semantics.
- CASPL and CASPAL store to memory with release semantics.
- CASP has neither acquire nor release semantics.

The architecture permits that the data read clears any exclusive monitors associated with that location, even if the compare subsequently fails.

If the instruction generates a synchronous Data Abort, the registers which are compared and loaded, that is &lt;Ws&gt; and &lt;W(s+1)&gt; , or &lt;Xs&gt; and &lt;X(s+1)&gt; , are restored to the values held in the registers before the instruction was executed.

For a CASP or CASPA instruction, when &lt;Ws&gt; or &lt;Xs&gt; specifies the same register as &lt;Wt&gt; or &lt;Xt&gt; , this signals to the memory system that an additional subsequent CASP , CASPA , CASPAL , or CASPL access to the specified location is likely to occur in the near future. The memory system can respond by taking actions that are expected to enable the subsequent CASP , CASPA , CASPAL , or CASPL access to succeed when it does occur.

Acode sequence starting with a CASP or CASPA instruction for which &lt;Ws&gt; or &lt;Xs&gt; specifies the same register as &lt;Wt&gt; or &lt;Xt&gt; , and ending with a subsequent CASP , CASPA , CASPAL , or CASPL to the same location, exhibits the following properties for best performance when the location may be accessed concurrently, on one or more other PEs:

- The sequence does not contain any direct system register writes, address translation instructions, cache or TLB maintenance operations, exception producing instructions, exception returns, or ISB barriers.
- The execution of the sequence includes 32 or fewer instructions.
- The value provided in &lt;Ws&gt; or &lt;Xs&gt; of the first CASP or CASPA is a value likely to result in the comparison failing. Afailing comparison result may lead to better performance due to the hardware not performing a write to memory.

Note

For a CASP or CASPA instruction, when &lt;Ws&gt; or &lt;Xs&gt; specifies the same register as &lt;Wt&gt; or &lt;Xt&gt; , the value in memory is not modified, because the CASP or CASPA either fails its compare or writes the same value back to memory.

For more information about memory ordering semantics, see Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

## No offset

(FEAT\_LSE)

<!-- image -->

## Encoding for the 32-bit CASP variant

Applies when (sz == 0 &amp;&amp; L == 0 &amp;&amp; o0 == 0) CASP &lt;Ws&gt;, &lt;W(s+1)&gt;, &lt;Wt&gt;, &lt;W(t+1)&gt;, [&lt;Xn|SP&gt;{, #0}]

## Encoding for the 32-bit CASPA variant

```
Applies when (sz == 0 && L == 1 && o0 == 0) CASPA <Ws>, <W(s+1)>, <Wt>, <W(t+1)>, [<Xn|SP>{, #0}]
```

## Encoding for the 32-bit CASPAL variant

```
Applies when (sz == 0 && L == 1 && o0 == 1)
```

```
CASPAL <Ws>, <W(s+1)>, <Wt>, <W(t+1)>, [<Xn|SP>{, #0}]
```

## Encoding for the 32-bit CASPL variant

```
Applies when (sz == 0 && L == 0 && o0 == 1)
```

```
CASPL <Ws>, <W(s+1)>, <Wt>, <W(t+1)>, [<Xn|SP>{, #0}]
```

## Encoding for the 64-bit CASP variant

```
Applies when (sz == 1 && L == 0 && o0 == 0) CASP <Xs>, <X(s+1)>, <Xt>, <X(t+1)>, [<Xn|SP>{, #0}]
```

## Encoding for the 64-bit CASPA variant

```
Applies when (sz == 1 && L == 1 && o0 == 0) CASPA <Xs>, <X(s+1)>, <Xt>, <X(t+1)>, [<Xn|SP>{, #0}]
```

## Encoding for the 64-bit CASPAL variant

```
Applies when (sz == 1 && L == 1 && o0 == 1) CASPAL <Xs>, <X(s+1)>, <Xt>, <X(t+1)>, [<Xn|SP>{, #0}]
```

## Encoding for the 64-bit CASPL variant

```
Applies when (sz == 1 && L == 0 && o0 == 1) CASPL <Xs>, <X(s+1)>, <Xt>, <X(t+1)>, [<Xn|SP>{, #0}]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LSE) then EndOfDecode(Decode_UNDEF);
```

```
if Rs<0> == '1' || Rt<0> == '1' then EndOfDecode(Decode_UNDEF); constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer datasize = 32 << UInt(sz); constant boolean acquire = L == '1'; constant boolean release = o0 == '1'; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Ws&gt;

Is the 32-bit name of the first general-purpose register to be compared and loaded, encoded in the 'Rs' field. &lt;Ws&gt; must be an even-numbered register.

## &lt;W(s+1)&gt;

Is the 32-bit name of the second general-purpose register to be compared and loaded.

## &lt;Wt&gt;

Is the 32-bit name of the first general-purpose register to be conditionally stored, encoded in the 'Rt' field. &lt;Wt&gt; must be an even-numbered register.

## &lt;W(t+1)&gt;

Is the 32-bit name of the second general-purpose register to be conditionally stored.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Xs&gt;

Is the 64-bit name of the first general-purpose register to be compared and loaded, encoded in the 'Rs' field. &lt;Xs&gt; must be an even-numbered register.

## &lt;X(s+1)&gt;

Is the 64-bit name of the second general-purpose register to be compared and loaded.

## &lt;Xt&gt;

Is the 64-bit name of the first general-purpose register to be conditionally stored, encoded in the 'Rt' field. &lt;Xt&gt; must be an even-numbered register.

## &lt;X(t+1)&gt;

Is the 64-bit name of the second general-purpose register to be conditionally stored.

## Operation

```
bits(64) address; bits(2*datasize) comparevalue; bits(2*datasize) newvalue; bits(2*datasize) data; constant bits(datasize) s1 = X[s, datasize]; constant bits(datasize) s2 = X[s+1, datasize]; constant bits(datasize) t1 = X[t, datasize]; constant bits(datasize) t2 = X[t+1, datasize]; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescAtomicOp(MemAtomicOp_CAS, acquire, release, tagchecked, privileged, t, t+1, s, s+1); comparevalue = if BigEndian(accdesc.acctype) then s1:s2 else s2:s1; newvalue = if BigEndian(accdesc.acctype) then t1:t2 else t2:t1; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; data = MemAtomic(address, comparevalue, newvalue, accdesc);
```

```
if BigEndian(accdesc.acctype) then X[s, datasize] = data<2*datasize-1:datasize>; X[s+1, datasize] = data<datasize-1:0>; else X[s, datasize] = data<datasize-1:0>; X[s+1, datasize] = data<2*datasize-1:datasize>;
```
