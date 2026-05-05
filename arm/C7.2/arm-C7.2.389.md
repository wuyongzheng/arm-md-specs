## C7.2.389 STTNP (SIMD&amp;FP)

Store unprivileged pair of SIMD&amp;FP registers, with non-temporal hint

This instruction stores a pair of SIMD&amp;FP registers to memory, issuing a hint to the memory system that the access is non-temporal. The address used for the store is calculated from an address from a base register value and an immediate offset. For information about non-temporal pair instructions, see Load/Store SIMD and Floating-point non-temporal pair.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

Explicit Memory effects produced by the instruction behave as if the instruction was executed at EL0 if the Effective value of PSTATE.UAO is 0 and either:

- The instruction is executed at EL1.
- The instruction is executed at EL2 when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

Otherwise, the Explicit Memory effects operate with the restrictions determined by the Exception level at which the instruction is executed.

## Signed offset

(FEAT\_FP &amp;&amp; FEAT\_LSUI)

<!-- image -->

## Encoding

```
STTNP <Qt1>, <Qt2>, [<Xn|SP>{, #<imm>}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_FP) || !IsFeatureImplemented(FEAT_LSUI) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); constant boolean nontemporal = TRUE; constant integer datasize = 128; constant bits(64) offset = LSL(SignExtend(imm7, 64), 4); constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Qt1&gt;

Is the 128-bit name of the first SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

## &lt;Qt2&gt;

Is the 128-bit name of the second SIMD&amp;FP register to be transferred, encoded in the 'Rt2' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;imm&gt;

Is the optional signed immediate byte offset, a multiple of 16 in the range -1024 to 1008, defaulting to 0 and encoded in the 'imm7' field as &lt;imm&gt;/16.

## Operation

```
AArch64.CheckFPEnabled(); bits(64) address; constant integer dbytes = datasize DIV 8; constant boolean privileged = AArch64.IsUnprivAccessPriv(); constant boolean ispair = TRUE; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_STORE, nontemporal, tagchecked, privileged, ispair); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); bits(2*datasize) data; if BigEndian(accdesc.acctype) then data = V[t, datasize] : V[t2, datasize]; else data = V[t2, datasize] : V[t, datasize]; Mem[address, 2*dbytes, accdesc] = data;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
