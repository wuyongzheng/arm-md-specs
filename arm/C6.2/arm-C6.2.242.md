## C6.2.242 LDTNP

Load unprivileged pair of registers, with non-temporal hint

This instruction calculates an address from a base register value and an immediate offset, loads two 64-bit doublewords from memory, and writes them to two registers. For information about addressing modes, see Load/Store addressing modes. For information about non-temporal pair instructions, see Load/Store non-temporal pair.

Explicit Memory effects produced by the instruction behave as if the instruction was executed at EL0 if the Effective value of PSTATE.UAO is 0 and either:

- The instruction is executed at EL1.
- The instruction is executed at EL2 when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

Otherwise, the Explicit Memory effects operate with the restrictions determined by the Exception level at which the instruction is executed.

## Signed offset

(FEAT\_LSUI)

<!-- image -->

## Encoding

```
LDTNP <Xt1>, <Xt2>, [<Xn|SP>{, #<imm>}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_LSUI) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant boolean nontemporal = TRUE; constant integer datasize = 64; constant bits(64) offset = LSL(SignExtend(imm7, 64), 3); constant boolean tagchecked = n != 31; boolean rt_unknown = FALSE; if t == t2 then constant Constraint c = ConstrainUnpredictable(Unpredictable_LDPOVERLAP); assert c IN {Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_UNKNOWN rt_unknown = TRUE; // Result is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP);
```

LDTNP has the same CONSTRAINED UNPREDICTABLE behavior as LDNP . See Architectural Constraints on UNPREDICTABLE behaviors, and particularly LDNP.

## Assembler Symbols

&lt;Xt1&gt;

Is the 64-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

<!-- image -->

Is the 64-bit name of the second general-purpose register to be transferred, encoded in the 'Rt2' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;imm&gt;

Is the optional signed immediate byte offset, a multiple of 8 in the range -512 to 504, defaulting to 0 and encoded in the 'imm7' field as &lt;imm&gt;/8.

## Operation

```
bits(64) address; constant integer dbytes = datasize DIV 8; constant boolean privileged = AArch64.IsUnprivAccessPriv(); constant boolean ispair = TRUE; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked, ispair, t, t2); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); constant bits(2*datasize) data = Mem[address, 2 * dbytes, accdesc]; if rt_unknown then X[t, datasize] = bits(datasize) UNKNOWN; elsif BigEndian(accdesc.acctype) then X[t2, datasize] = data<(datasize-1):0>; X[t, datasize] = data<(2*datasize-1):datasize>; else X[t, datasize] = data<(datasize-1):0>; X[t2, datasize] = data<(2*datasize-1):datasize>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
