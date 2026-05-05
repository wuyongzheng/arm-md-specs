## C6.2.190 LDAPURSW

Load-acquire RCpc register signed word (unscaled)

This instruction calculates an address from a base register and an immediate offset, loads a signed word from memory, sign-extends it, and writes it to a register.

If the destination register is not one of WZR or XZR , LDAPURSW loads from memory with AcquirePC semantics.

For more information about memory ordering semantics, see Load-Acquire, Load-AcquirePC, and Store-Release.

For information about addressing modes, see Load/Store addressing modes.

## Unscaled offset

(FEAT\_LRCPC2)

<!-- image -->

## Encoding

```
LDAPURSW <Xt>, [<Xn|SP>{, #<simm>}]
```

## Decode for this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_LRCPC2) then constant bits(64) offset = SignExtend(imm9, 64);
```

## Assembler Symbols

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;simm&gt;

Is the optional signed immediate byte offset, in the range -256 to 255, defaulting to 0 and encoded in the 'imm9' field.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer{} datasize = 32; constant boolean acquirepc = t != 31; constant boolean tagchecked = n != 31;
```

## Operation

```
bits(64) address; constant AccessDescriptor accdesc = if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); constant bits(datasize) data = Mem[address, datasize DIV 8, accdesc]; X[t, 64] = SignExtend(data, 64);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
CreateAccDescLDAcqPC(tagchecked, acquirepc, t);
```
