## C6.2.402 STLRB

Store-release register byte

This instruction stores a byte from a 32-bit register to a memory location. The instruction also has memory ordering semantics as described in Load-Acquire, Store-Release. For information about addressing modes, see Load/Store addressing modes.

<!-- image -->

## Encoding

STLRB

&lt;Wt&gt;, [&lt;Xn|SP&gt;{, #0}]

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean acquire = FALSE; constant boolean tagchecked =
```

```
n != 31;
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
bits(64) address; constant AccessDescriptor accdesc = CreateAccDescAcqRel(MemOp_STORE, tagchecked, acquire, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; Mem[address, 1, accdesc] = X[t, 8];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
