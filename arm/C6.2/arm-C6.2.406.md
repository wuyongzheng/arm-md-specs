## C6.2.406 STLURB

Store-release register byte (unscaled)

This instruction calculates an address from a base register value and an immediate offset, and stores a byte to the calculated address, from a 32-bit register.

The instruction has memory ordering semantics as described in Load-Acquire, Load-AcquirePC, and Store-Release For information about addressing modes, see Load/Store addressing modes.

## Unscaled offset (FEAT\_LRCPC2)

<!-- image -->

## Encoding

```
STLURB <Wt>, [<Xn|SP>{, #<simm>}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_LRCPC2) then EndOfDecode(Decode_UNDEF); constant bits(64) offset = SignExtend(imm9, 64); constant integer n = UInt(Rn); constant integer t = UInt(Rt); constant integer datasize = 8; constant boolean acquire = FALSE; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;simm&gt;

Is the optional signed immediate byte offset, in the range -256 to 255, defaulting to 0 and encoded in the 'imm9' field.

## Operation

```
bits(64) address; constant AccessDescriptor accdesc = CreateAccDescAcqRel(MemOp_STORE, tagchecked, acquire, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc);
```

Mem[address, datasize DIV 8, accdesc] = X[t, datasize];

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
