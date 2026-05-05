## C6.2.416 STRB (immediate)

Store register byte (immediate)

This instruction stores the least significant byte of a 32-bit register to memory. The address that is used for the store is calculated from a base register and an immediate offset. For information about addressing modes, see Load/Store addressing modes.

It has encodings from 3 classes: Post-index, Pre-index, and Unsigned offset

## Post-index

<!-- image -->

## Encoding

STRB

&lt;Wt&gt;, [&lt;Xn|SP&gt;], #&lt;simm&gt;

## Decode for this encoding

```
constant boolean wback = TRUE; constant boolean postindex = TRUE; constant bits(64) offset
```

## Pre-index

<!-- image -->

## Encoding

STRB

&lt;Wt&gt;, [&lt;Xn|SP&gt;, #&lt;simm&gt;]!

## Decode for this encoding

```
constant boolean wback = TRUE; constant boolean postindex = FALSE; constant bits(64) offset = SignExtend(imm9, 64);
```

## Unsigned offset

<!-- image -->

## Encoding

<!-- image -->

```
= SignExtend(imm9, 64);
```

## Decode for this encoding

```
constant boolean wback = FALSE; constant boolean postindex = FALSE; constant bits(64) offset
```

```
= LSL(ZeroExtend(imm12, 64), 0);
```

For information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly STRB (immediate).

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;simm&gt;

Is the signed immediate byte offset, in the range -256 to 255, encoded in the 'imm9' field.

## &lt;pimm&gt;

Is the optional positive immediate byte offset, in the range 0 to 4095, defaulting to 0 and encoded in the 'imm12' field.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31; Constraint c; boolean rt_unknown = FALSE; if wback && n == t && n != 31 then c = ConstrainUnpredictable(Unpredictable_WBOVERLAPST); assert c IN {Constraint_NONE, Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_NONE rt_unknown = FALSE; // Value stored is original value when Constraint_UNKNOWN rt_unknown = TRUE; // Value stored is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP); end end
```

## Operation

```
bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_STORE, nontemporal, privileged, tagchecked, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; if !postindex then address = AddressAdd(address, offset, accdesc); bits(8) data;
```

```
if rt_unknown then data = bits(8) UNKNOWN; else data = X[t, 8]; Mem[address, 1, accdesc] = data; if wback then if postindex then address = AddressAdd(address, offset, if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
accdesc);
```
