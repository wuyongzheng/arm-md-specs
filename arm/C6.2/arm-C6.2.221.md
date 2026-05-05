## C6.2.221 LDRH (immediate)

Load register halfword (immediate)

This instruction loads a halfword from memory, zero-extends it, and writes the result to a register. The address that is used for the load is calculated from a base register and an immediate offset. For information about addressing modes, see Load/Store addressing modes.

It has encodings from 3 classes: Post-index, Pre-index, and Unsigned offset

## Post-index

<!-- image -->

## Encoding

```
LDRH <Wt>, [<Xn|SP>], #<simm>
```

## Decode for this encoding

```
boolean wback = TRUE; constant boolean postindex = TRUE; constant bits(64) offset
```

## Pre-index

<!-- image -->

## Encoding

<!-- image -->

## Decode for this encoding

```
boolean wback = TRUE; constant boolean postindex = FALSE; constant bits(64) offset = SignExtend(imm9, 64);
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
boolean wback = FALSE; constant boolean postindex = FALSE; constant bits(64) offset
```

```
= LSL(ZeroExtend(imm12, 64), 1);
```

For information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly LDRH (immediate).

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;simm&gt;

Is the signed immediate byte offset, in the range -256 to 255, encoded in the 'imm9' field.

## &lt;pimm&gt;

Is the optional positive immediate byte offset, a multiple of 2 in the range 0 to 8190, defaulting to 0 and encoded in the 'imm12' field as &lt;pimm&gt;/2.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31; Constraint c; boolean wb_unknown = FALSE; if wback && n == t && n != 31 then c = ConstrainUnpredictable(Unpredictable_WBOVERLAPLD); assert c IN {Constraint_WBSUPPRESS, Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_WBSUPPRESS wback = FALSE; // Writeback is suppressed when Constraint_UNKNOWN wb_unknown = TRUE; // Writeback is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP); end end
```

## Operation

```
bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; if !postindex then address = AddressAdd(address, offset, accdesc); constant bits(16) data = Mem[address, 2, accdesc];
```

```
X[t, 32] = ZeroExtend(data, 32); if wback then if wb_unknown then address = bits(64) UNKNOWN; elsif postindex then address = AddressAdd(address, offset, if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
accdesc);
```
