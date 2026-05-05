## C6.2.211 LDLARH

Load LOAcquire register halfword

This instruction loads a halfword from memory, zero-extends it, and writes it to a register.

If the destination register is not one of WZR or XZR , LDLARH loads from memory with Acquire semantics.

For more information about memory ordering semantics, see Load LOAcquire, Store LORelease and Load-Acquire, Load-AcquirePC, and Store-Release.

For information about addressing modes, see Load/Store addressing modes.

## No offset

(FEAT\_LOR)

<!-- image -->

## Encoding

```
LDLARH <Wt>, [<Xn|SP>{, #0}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_LOR) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean acquire = t != 31; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

&lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
bits(64) address; constant AccessDescriptor accdesc = CreateAccDescLOR(MemOp_LOAD, tagchecked, acquire, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant bits(16) data = Mem[address, 2, accdesc]; X[t, 32] = ZeroExtend(data, 32);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

o0
