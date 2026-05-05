## C6.2.321 RCWCAS, RCWCASA, RCWCASAL, RCWCASL

Read check write compare and swap doubleword in memory

This instruction reads a 64-bit doubleword from memory, and compares it against the value held in a register. If the comparison is equal, the value in a second register is conditionally written to memory. Storing back to memory is conditional on RCW Checks. If the compare fails or the RCW Checks fail, the architecture permits writing the value read from the location to memory. If the write is performed, the read and the write occur atomically such that no other modification of the memory location can take place between the read and the write. This instruction updates the condition flags based on the result of the update of memory.

- If the destination register is not XZR , RCWCASA and RCWCASAL load from memory with acquire semantics.
- RCWCASL and RCWCASAL store to memory with release semantics.
- RCWCAS has neither acquire nor release semantics.

## Note

This instruction is for performing atomic updates of translation table entries and not for general use.

## Integer

(FEAT\_THE)

<!-- image -->

## Encoding for the RCWCAS variant

```
Applies when (A == 0 && R == 0) RCWCAS <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the RCWCASA variant

```
Applies when (A == 1 && R == 0) RCWCASA <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the RCWCASAL variant

```
Applies when (A == 1 && R == 1) RCWCASAL <Xs>, <Xt>, [<Xn|SP>]
```

## Encoding for the RCWCASL variant

```
Applies when
```

```
RCWCASL
```

```
(A == 0 && R == 1) <Xs>, <Xt>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_THE) then EndOfDecode(Decode_UNDEF); constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean soft = FALSE; constant boolean acquire = A == '1' && t != 31; constant boolean release = R == '1'; constant boolean tagchecked = n != 31;
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
if IsD128Enabled(PSTATE.EL) then UNDEFINED; bits(64) address; constant bits(64) newdata = X[t, 64]; constant bits(64) compdata = X[s, 64]; bits(64) readdata; bits(4) nzcv; constant AccessDescriptor accdesc = CreateAccDescRCW(MemAtomicOp_CAS, soft, acquire, release, tagchecked, t, s); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; (nzcv, readdata) = MemAtomicRCW(address, compdata, newdata, accdesc); PSTATE.<N,Z,C,V> = nzcv; X[s, 64] = readdata; // Return the old value when s!=31
```
