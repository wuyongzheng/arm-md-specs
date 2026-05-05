## C6.2.405 STLUR

Store-release register (unscaled)

This instruction calculates an address from a base register value and an immediate offset, and stores a 32-bit word or a 64-bit doubleword to the calculated address, from a register.

The instruction has memory ordering semantics as described in Load-Acquire, Load-AcquirePC, and Store-Release

For information about addressing modes, see Load/Store addressing modes.

## Unscaled offset (FEAT\_LRCPC2)

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (size == 10) STLUR
```

```
<Wt>, [<Xn|SP>{, #<simm>}]
```

## Encoding for the 64-bit variant

Applies when

```
STLUR
```

```
(size == 11) <Xt>, [<Xn|SP>{, #<simm>}]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LRCPC2) then EndOfDecode(Decode_UNDEF); constant integer scale = UInt(size); constant bits(64) offset = SignExtend(imm9, 64); constant integer n = UInt(Rn); constant integer t = UInt(Rt); constant integer datasize = 8 << scale; constant boolean acquire = FALSE; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;simm&gt;

Is the optional signed immediate byte offset, in the range -256 to 255, defaulting to 0 and encoded in the 'imm9' field.

<!-- image -->

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## Operation

```
bits(64) address; constant AccessDescriptor accdesc = CreateAccDescAcqRel(MemOp_STORE, tagchecked, acquire, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); Mem[address, datasize DIV 8, accdesc] = X[t, datasize];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
