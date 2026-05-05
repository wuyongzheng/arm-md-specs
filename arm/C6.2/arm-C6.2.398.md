## C6.2.398 STLLR

## Store LORelease register

This instruction stores a 32-bit word or a 64-bit doubleword to a memory location, from a register. The instruction also has memory ordering semantics as described in Load LOAcquire, Store LORelease. For information about addressing modes, see Load/Store addressing modes.

## No offset

(FEAT\_LOR)

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (size == 10) STLLR <Wt>, [<Xn|SP>{, #0}]
```

## Encoding for the 64-bit variant

```
Applies when (size == 11) STLLR <Xt>, [<Xn|SP>{, #0}]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LOR) then EndOfDecode(Decode_UNDEF);
```

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer elsize = 8 << UInt(size); constant boolean acquire = FALSE; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

&lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## Operation

```
bits(64) address; constant integer dbytes = elsize DIV 8; constant AccessDescriptor accdesc = CreateAccDescLOR(MemOp_STORE, tagchecked, acquire, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; Mem[address, dbytes, accdesc] = X[t, elsize];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
