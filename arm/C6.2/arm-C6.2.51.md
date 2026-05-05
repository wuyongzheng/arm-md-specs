## C6.2.51 CAS, CASA, CASAL, CASL

Compare and swap word or doubleword in memory

This instruction reads a 32-bit word or 64-bit doubleword from memory, and compares it against the value held in a first register. If the comparison is equal, the value in a second register is written to memory. If the comparison is not equal, the architecture permits writing the value read from the location to memory. If the write is performed, the read and write occur atomically such that no other modification of the memory location can take place between the read and write.

- If the destination register is not one of WZR or XZR , CASA and CASAL load from memory with acquire semantics.
- CASL and CASAL store to memory with release semantics.
- CAS has neither acquire nor release semantics.

The architecture permits that the data read clears any exclusive monitors associated with that location, even if the compare subsequently fails.

If the instruction generates a synchronous Data Abort, the register which is compared and loaded, that is &lt;Ws&gt; , or &lt;Xs&gt; , is restored to the value held in the register before the instruction was executed.

For a CAS or CASA instruction, when &lt;Ws&gt; or &lt;Xs&gt; specifies the same register as &lt;Wt&gt; or &lt;Xt&gt; , this signals to the memory system that an additional subsequent CAS , CASA , CASAL , or CASL access to the specified location is likely to occur in the near future. The memory system can respond by taking actions that are expected to enable the subsequent CAS , CASA , CASAL , or CASL access to succeed when it does occur.

Acode sequence starting with a CAS or CASA instruction for which &lt;Ws&gt; or &lt;Xs&gt; specifies the same register as &lt;Wt&gt; or &lt;Xt&gt; , and ending with a subsequent CAS , CASA , CASAL , or CASL to the same location, exhibits the following properties for best performance when the location may be accessed concurrently, on one or more other PEs:

- The sequence does not contain any direct system register writes, address translation instructions, cache or TLB maintenance operations, exception producing instructions, exception returns, or ISB barriers.
- The execution of the sequence includes 32 or fewer instructions.
- The value provided in &lt;Ws&gt; or &lt;Xs&gt; of the first CAS or CASA is a value likely to result in the comparison failing. A failing comparison result may lead to better performance due to the hardware not performing a write to memory.

Note

For a CAS or CASA instruction, when &lt;Ws&gt; or &lt;Xs&gt; specifies the same register as &lt;Wt&gt; or &lt;Xt&gt; , the value in memory is not modified, because the CAS or CASA either fails its compare or writes the same value back to memory.

For more information about memory ordering semantics, see Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

## No offset

(FEAT\_LSE)

<!-- image -->

## Encoding for the 32-bit CAS variant

Applies when (size == 10 &amp;&amp; L == 0 &amp;&amp; o0 == 0)

CAS

&lt;Ws&gt;, &lt;Wt&gt;, [&lt;Xn|SP&gt;{, #0}]

## Encoding for the 32-bit CASA variant

Applies when (size == 10 &amp;&amp; L == 1 &amp;&amp; o0 == 0)

CASA

&lt;Ws&gt;, &lt;Wt&gt;, [&lt;Xn|SP&gt;{, #0}]

## Encoding for the 32-bit CASAL variant

Applies when (size == 10 &amp;&amp; L == 1 &amp;&amp; o0 ==

```
CASAL <Ws>,
```

```
1) <Wt>, [<Xn|SP>{, #0}]
```

## Encoding for the 32-bit CASL variant

Applies when (size == 10 &amp;&amp; L == 0 &amp;&amp; o0 ==

```
CASL
```

```
1) <Ws>, <Wt>, [<Xn|SP>{, #0}]
```

## Encoding for the 64-bit CAS variant

```
Applies when (size == 11 && L == 0 && o0 ==
```

```
CAS
```

```
0) <Xs>, <Xt>, [<Xn|SP>{, #0}]
```

## Encoding for the 64-bit CASA variant

```
Applies when (size == 11 && L == 1 && o0 == 0) CASA <Xs>, <Xt>, [<Xn|SP>{, #0}]
```

## Encoding for the 64-bit CASAL variant

Applies when (size == 11 &amp;&amp; L == 1 &amp;&amp; o0 ==

```
CASAL <Xs>,
```

```
1) <Xt>, [<Xn|SP>{, #0}]
```

## Encoding for the 64-bit CASL variant

```
Applies when (size == 11 && L == 0 && o0 ==
```

```
CASL
```

```
1) <Xs>, <Xt>, [<Xn|SP>{, #0}]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LSE) then EndOfDecode(Decode_UNDEF);
```

```
constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer datasize = 8 << UInt(size); constant integer regsize = if datasize == 64 then 64 else 32; constant boolean acquire = L == '1' && t != 31; constant boolean release = o0 == '1'; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Ws&gt;

Is the 32-bit name of the general-purpose register to be compared and loaded, encoded in the 'Rs' field.

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be conditionally stored, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

&lt;Xs&gt;

Is the 64-bit name of the general-purpose register to be compared and loaded, encoded in the 'Rs' field.

<!-- image -->

Is the 64-bit name of the general-purpose register to be conditionally stored, encoded in the 'Rt' field.

## Operation

```
bits(64) address; bits(datasize) comparevalue; bits(datasize) newvalue; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescAtomicOp(MemAtomicOp_CAS, acquire, release, tagchecked, privileged, t, s); comparevalue = X[s, datasize]; newvalue = X[t, datasize]; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant bits(datasize) data = MemAtomic(address, comparevalue, newvalue, accdesc); X[s, regsize] = ZeroExtend(data, regsize);
```
