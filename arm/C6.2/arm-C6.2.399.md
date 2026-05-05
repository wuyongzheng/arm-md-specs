## C6.2.399 STLLRB

Store LORelease register byte

This instruction stores a byte from a 32-bit register to a memory location. The instruction also has memory ordering semantics as described in Load LOAcquire, Store LORelease. For information about addressing modes, see Load/Store addressing modes.

## No offset

(FEAT\_LOR)

<!-- image -->

## Encoding

```
STLLRB <Wt>, [<Xn|SP>{, #0}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_LOR) then EndOfDecode(Decode_UNDEF);
```

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean acquire = FALSE; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

&lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

<!-- image -->

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
bits(64) address; constant AccessDescriptor accdesc = CreateAccDescLOR(MemOp_STORE, tagchecked, acquire, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; Mem[address, 1, accdesc] = X[t, 8];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
