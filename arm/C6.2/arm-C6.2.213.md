## C6.2.213 LDP

## Load pair of registers

This instruction calculates an address from a base register value and an immediate offset, loads two 32-bit words or two 64-bit doublewords from memory, and writes them to two registers. For information about addressing modes, see Load/Store addressing modes.

It has encodings from 3 classes: Post-index, Pre-index, and Signed offset

## Post-index

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (opc == 00) LDP <Wt1>, <Wt2>, [<Xn|SP>], #<imm>
```

## Encoding for the 64-bit variant

```
Applies when (opc == 10) LDP <Xt1>, <Xt2>, [<Xn|SP>], #<imm>
```

## Decode for all variants of this encoding

```
boolean wback = TRUE; constant boolean postindex =
```

## Pre-index

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (opc == 00) LDP
```

```
<Wt1>, <Wt2>, [<Xn|SP>, #<imm>]!
```

## Encoding for the 64-bit variant

```
Applies when (opc == 10) LDP <Xt1>, <Xt2>, [<Xn|SP>, #<imm>]!
```

## Decode for all variants of this encoding

```
boolean wback = TRUE; constant boolean postindex =
```

```
FALSE;
```

```
TRUE;
```

## Signed offset

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (opc == 00) LDP
```

```
<Wt1>, <Wt2>, [<Xn|SP>{, #<imm>}]
```

## Encoding for the 64-bit variant

```
Applies when (opc == 10) LDP <Xt1>, <Xt2>, [<Xn|SP>{, #<imm>}]
```

## Decode for all variants of this encoding

```
boolean wback = FALSE; constant boolean postindex = FALSE;
```

For information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly LDP.

## Assembler Symbols

## &lt;Wt1&gt;

Is the 32-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Wt2&gt;

Is the 32-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;imm&gt;

For the 'Post-index 32-bit' and 'Pre-index 32-bit' variants: is the signed immediate byte offset, a multiple of 4 in the range -256 to 252, encoded in the 'imm7' field as &lt;imm&gt;/4.

For the 'Post-index 64-bit' and 'Pre-index 64-bit' variants: is the signed immediate byte offset, a multiple of 8 in the range -512 to 504, encoded in the 'imm7' field as &lt;imm&gt;/8.

For the 'Signed offset 32-bit' variant: is the optional signed immediate byte offset, a multiple of 4 in the range -256 to 252, defaulting to 0 and encoded in the 'imm7' field as &lt;imm&gt;/4.

For the 'Signed offset 64-bit' variant: is the optional signed immediate byte offset, a multiple of 8 in the range -512 to 504, defaulting to 0 and encoded in the 'imm7' field as &lt;imm&gt;/8.

## &lt;Xt1&gt;

Is the 64-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xt2&gt;

Is the 64-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant boolean nontemporal = FALSE; constant integer{} scale = 2 + UInt(opc<1>); constant integer{} datasize = 8 << scale; constant bits(64) offset = LSL(SignExtend(imm7, 64), scale); constant boolean tagchecked = wback || n != 31; boolean rt_unknown = FALSE; boolean wb_unknown = FALSE; if wback && (t == n || t2 == n) && n != 31 then constant Constraint c = ConstrainUnpredictable(Unpredictable_WBOVERLAPLD); assert c IN {Constraint_WBSUPPRESS, Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_WBSUPPRESS wback = FALSE; // Writeback is suppressed when Constraint_UNKNOWN wb_unknown = TRUE; // Writeback is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP); end end if t == t2 then constant Constraint c = ConstrainUnpredictable(Unpredictable_LDPOVERLAP); assert c IN {Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_UNKNOWN rt_unknown = TRUE; // Result is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP); end end
```

```
Operation bits(64) address; bits(datasize) data1; bits(datasize) data2; constant integer dbytes = datasize DIV 8; constant boolean privileged = PSTATE.EL != EL0; constant boolean ispair = TRUE; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked, ispair, t, t2); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; if !postindex then address = AddressAdd(address, offset, accdesc); constant bits(2*datasize) data = Mem[address, 2 * dbytes, accdesc]; if rt_unknown then data1 = bits(datasize) UNKNOWN; data2 = bits(datasize) UNKNOWN; elsif BigEndian(accdesc.acctype) then data2 = data<(datasize-1):0>; data1 = data<(2*datasize-1):datasize>; else data1 = data<(datasize-1):0>; data2 = data<(2*datasize-1):datasize>;
```

```
X[t, datasize] = data1; X[t2, datasize] = data2; if wback then if wb_unknown then address = bits(64) UNKNOWN; elsif postindex then address = AddressAdd(address, offset, if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
accdesc);
```
