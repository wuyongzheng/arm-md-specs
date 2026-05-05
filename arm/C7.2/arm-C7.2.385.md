## C7.2.385 STNP (SIMD&amp;FP)

Store pair of SIMD&amp;FP registers, with non-temporal hint

This instruction stores a pair of SIMD&amp;FP registers to memory, issuing a hint to the memory system that the access is non-temporal. The address used for the store is calculated from an address from a base register value and an immediate offset. For information about non-temporal pair instructions, see Load/Store SIMD and Floating-point non-temporal pair.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Signed offset

(FEAT\_FP)

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (opc == 00) STNP <St1>, <St2>, [<Xn|SP>{, #<imm>}]
```

## Encoding for the 64-bit variant

```
Applies when (opc == 01) STNP <Dt1>, <Dt2>, [<Xn|SP>{, #<imm>}]
```

## Encoding for the 128-bit variant

```
Applies when (opc == 10) STNP <Qt1>, <Qt2>, [<Xn|SP>{, #<imm>}]
```

## Decode for all variants of this encoding

// Empty.

## Assembler Symbols

&lt;St1&gt;

Is the 32-bit name of the first SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

&lt;St2&gt;

Is the 32-bit name of the second SIMD&amp;FP register to be transferred, encoded in the 'Rt2' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;imm&gt;

For the '32-bit' variant: is the optional signed immediate byte offset, a multiple of 4 in the range -256 to 252, defaulting to 0 and encoded in the 'imm7' field as &lt;imm&gt;/4.

For the '64-bit' variant: is the optional signed immediate byte offset, a multiple of 8 in the range -512 to 504, defaulting to 0 and encoded in the 'imm7' field as &lt;imm&gt;/8.

For the '128-bit' variant: is the optional signed immediate byte offset, a multiple of 16 in the range -1024 to 1008, defaulting to 0 and encoded in the 'imm7' field as &lt;imm&gt;/16.

## &lt;Dt1&gt;

Is the 64-bit name of the first SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

## &lt;Dt2&gt;

Is the 64-bit name of the second SIMD&amp;FP register to be transferred, encoded in the 'Rt2' field.

## &lt;Qt1&gt;

Is the 128-bit name of the first SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

## &lt;Qt2&gt;

Is the 128-bit name of the second SIMD&amp;FP register to be transferred, encoded in the 'Rt2' field.

## Shared Decode

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); end constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant boolean nontemporal = TRUE; constant integer{} scale = 2 + (UInt(opc) as integer{0..2}); constant integer{} datasize = 8 << scale; constant bits(64) offset = LSL(SignExtend(imm7, 64), scale); constant boolean tagchecked = n != 31;
```

## Operation

```
AArch64.CheckFPEnabled(); bits(64) address; constant integer dbytes = datasize DIV 8; constant boolean privileged = PSTATE.EL != EL0; constant boolean ispair = TRUE; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_STORE, nontemporal, tagchecked, privileged, ispair); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); bits(2*datasize) data; if BigEndian(accdesc.acctype) then data = V[t, datasize] : V[t2, datasize]; else data = V[t2, datasize] : V[t, datasize]; Mem[address, 2*dbytes, accdesc] = data;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
