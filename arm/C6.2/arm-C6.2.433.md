## C6.2.433 STTP

Store unprivileged pair of registers

This instruction calculates an address from a base register value and an immediate offset, and stores two 64-bit doublewords to the calculated address, from two registers.

Explicit Memory effects produced by the instruction behave as if the instruction was executed at EL0 if the Effective value of PSTATE.UAO is 0 and either:

- The instruction is executed at EL1.
- The instruction is executed at EL2 when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

Otherwise, the Explicit Memory effects operate with the restrictions determined by the Exception level at which the instruction is executed.

For information about addressing modes, see Load/Store addressing modes.

It has encodings from 3 classes: Post-index, Pre-index, and Signed offset

## Post-index

(FEAT\_LSUI)

<!-- image -->

## Encoding

```
STTP <Xt1>, <Xt2>, [<Xn|SP>], #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_LSUI) then constant boolean wback = TRUE; constant boolean postindex = TRUE;
```

## Pre-index

(FEAT\_LSUI)

<!-- image -->

## Encoding

```
STTP <Xt1>, <Xt2>, [<Xn|SP>, #<imm>]!
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_LSUI) then constant boolean wback = TRUE; constant boolean postindex = FALSE;
```

```
EndOfDecode(Decode_UNDEF);
```

```
EndOfDecode(Decode_UNDEF);
```

## Signed offset

(FEAT\_LSUI)

<!-- image -->

## Encoding

```
STTP <Xt1>, <Xt2>, [<Xn|SP>{, #<imm>}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_LSUI) then constant boolean wback = FALSE; constant boolean postindex = FALSE;
```

```
EndOfDecode(Decode_UNDEF);
```

STTP has the same CONSTRAINED UNPREDICTABLE behavior as STP . See Architectural Constraints on UNPREDICTABLE behaviors, and particularly STP.

## Assembler Symbols

## &lt;Xt1&gt;

Is the 64-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xt2&gt;

Is the 64-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;imm&gt;

For the 'Load/store register pair (post-indexed)' and 'Load/store register pair (pre-indexed)' variants: is the signed immediate byte offset, a multiple of 8 in the range -512 to 504, encoded in the 'imm7' field as &lt;imm&gt;/8.

For the 'Load/store register pair (offset)' variant: is the optional signed immediate byte offset, a multiple of 8 in the range -512 to 504, defaulting to 0 and encoded in the 'imm7' field as &lt;imm&gt;/8.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant boolean nontemporal = FALSE; constant integer{} scale = 2 + UInt(opc<1>); constant integer{} datasize = 64; constant bits(64) offset = LSL(SignExtend(imm7, 64), scale); constant boolean tagchecked = wback || n != 31; boolean rt_unknown = FALSE; if wback && (t == n || t2 == n) && n != 31 then constant Constraint c = ConstrainUnpredictable(Unpredictable_WBOVERLAPST); assert c IN {Constraint_NONE, Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_NONE rt_unknown = FALSE; // Value stored is pre-writeback when Constraint_UNKNOWN rt_unknown = TRUE; // Value stored is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF);
```

```
when end end
```

## Operation

```
bits(64) address; bits(datasize) data1; bits(datasize) data2; constant integer dbytes = datasize DIV 8; constant boolean privileged = AArch64.IsUnprivAccessPriv(); constant boolean ispair = TRUE; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_STORE, nontemporal, privileged, tagchecked, ispair, t, t2); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; if !postindex then address = AddressAdd(address, offset, accdesc); if rt_unknown && t == n then data1 = bits(datasize) UNKNOWN; else data1 = X[t, datasize]; if rt_unknown && t2 == n then data2 = bits(datasize) UNKNOWN; else data2 = X[t2, datasize]; constant bits(2*datasize) data = (if BigEndian(accdesc.acctype) then data1:data2 else data2:data1); Mem[address, 2 * dbytes, accdesc] = data; if wback then if postindex then address = AddressAdd(address, offset, accdesc); if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
Constraint_NOP EndOfDecode(Decode_NOP);
```
