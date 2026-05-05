## C6.2.358 SETGP, SETGM, SETGE

Memory set with tag setting

These instructions set a requested number of bytes in memory to the value in the least significant byte of the source data register and store an Allocation Tag to memory for each Tag Granule written. The Allocation Tag is calculated from the Logical Address Tag in the register that holds the first address to be set. The prologue, main, and epilogue instructions are expected to be run in succession and to appear consecutively in memory: SETGP, then SETGM, and then SETGE.

SETGP performs some preconditioning of the arguments suitable for using the SETGM instruction, and sets an IMPLEMENTATION DEFINED portion of the requested number of bytes. SETGM sets a further IMPLEMENTATION DEFINED portion of the remaining bytes. SETGE sets any final remaining bytes.

Note

The ability to set an IMPLEMENTATION DEFINED number of bytes allows an implementation to optimize how the bytes being set are divided between the different instructions.

For more information on exceptions specific to memory set instructions, see Memory Copy and Memory Set exceptions.

The architecture supports two algorithms for the memory set: option A and option B. Which algorithm is used is IMPLEMENTATION DEFINED.

Note

Portable software should not assume that the choice of algorithm is constant.

For SETGP:

- If Xn&lt;63&gt; == 1, the set size is saturated to 0x7FFFFFFFFFFFFFF0 .

On completion of SETGP, option A:

- Xn holds -1 times the number of bytes in the saturated set size remaining to be set.
- Xd holds the original Xd + saturated set size.
- PSTATE.{N,Z,C,V} are set to {0,0,0,0}.

On completion of SETGP, option B:

- Xn holds the number of bytes in the saturated set size remaining to be set.
- Xd holds the lowest address that has not been set.
- PSTATE.{N,Z,C,V} are set to {0,0,1,0}.

For SETGM, option A, when PSTATE.C = 0:

- Xn holds a signed 64-bit integer.
- Xn holds -1 times the number of bytes remaining to be set.
- Xd holds the lowest address to be set - Xn.
- On completion of the instruction, Xn holds -1 times the number of bytes remaining to be set.

For SETGM, option B, when PSTATE.C = 1:

- Xn holds the number of bytes remaining to be set.
- Xd holds the lowest address to be set.
- On completion of the instruction:
- Xn holds the number of bytes remaining to be set.
- Xd holds the lowest address that has not been set.

For SETGE, option A, when PSTATE.C = 0:

- Xn holds a signed 64-bit integer.
- Xn holds -1 times the number of bytes remaining to be set.
- Xd holds the lowest address to be set - Xn.

- On completion of the instruction, Xn holds 0.

For SETGE, option B, when PSTATE.C = 1:

- Xn holds the number of bytes remaining to be set.
- Xd holds the lowest address to be set.
- On completion of the instruction:
- Xn holds 0.
- Xd holds the lowest address that has not been set.

## Integer

(FEAT\_MOPS &amp;&amp; FEAT\_MTE)

<!-- image -->

## Encoding for the Prologue variant

Applies when (op2 == 0000)

```
SETGP [<Xd>]!, <Xn>!, <Xs>
```

## Encoding for the Main variant

```
Applies when (op2 == 0100) SETGM [<Xd>]!, <Xn>!, <Xs>
```

## Encoding for the Epilogue variant

Applies when 1000)

```
(op2 == SETGE [<Xd>]!, <Xn>!, <Xs>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_MOPS) || !IsFeatureImplemented(FEAT_MTE) || sz != '00' then EndOfDecode(Decode_UNDEF); SETParams memset; memset.d = UInt(Rd); memset.s = UInt(Rs); memset.n = UInt(Rn); constant bits(2) options = op2<1:0>; constant boolean nontemporal = options<1> == '1'; case op2<3:2> of when '00' memset.stage = MOPSStage_Prologue; when '01' memset.stage = MOPSStage_Main; when '10' memset.stage = MOPSStage_Epilogue; otherwise EndOfDecode(Decode_UNDEF);
```

For information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly Memory Copy and Memory Set SET* and Crossing a page boundary with different memory types or Shareability attributes.

## Assembler Symbols

## &lt;Xd&gt;

For the 'Prologue' variant: is the 64-bit name of the general-purpose register that holds an encoding of the destination address (an integer multiple of 16) and is updated by the instruction, encoded in the 'Rd' field.

For the 'Epilogue' and 'Main' variants: is the 64-bit name of the general-purpose register that holds an encoding of the destination address (an integer multiple of 16) and for option B is updated by the instruction, encoded in the 'Rd' field.

For the 'Prologue' variant: is the 64-bit name of the general-purpose register that holds the number of bytes to be set (an integer multiple of 16) and is updated by the instruction, encoded in the 'Rn' field.

For the 'Main' variant: is the 64-bit name of the general-purpose register that holds an encoding of the number of bytes to be set (an integer multiple of 16) and is updated by the instruction, encoded in the 'Rn' field.

For the 'Epilogue' variant: is the 64-bit name of the general-purpose register that holds an encoding of the number of bytes to be set (an integer multiple of 16) and is set to zero on completion of the instruction, encoded in the 'Rn' field.

For the 'Main' and 'Prologue' variants: is the 64-bit name of the general-purpose register that holds the source data in bits&lt;7:0&gt;, encoded in the 'Rs' field.

For the 'Epilogue' variant: is the 64-bit name of the general-purpose register that holds the source data, encoded in the 'Rs' field.

## Operation

```
CheckMOPSEnabled(); CheckSETConstrainedUnpredictable(memset.n, memset.d, memset.s); constant bits(8) data = X[memset.s, 8]; MOPSBlockSize B = 0; memset.is_setg = TRUE; memset.nzcv = PSTATE.<N,Z,C,V>; memset.toaddress = X[memset.d, 64]; if memset.stage == MOPSStage_Prologue then memset.setsize = UInt(X[memset.n, 64]); else memset.setsize = SInt(X[memset.n, 64]); memset.implements_option_a = SETGOptionA(); constant boolean privileged = (if options<0> == '1' then AArch64.IsUnprivAccessPriv() else PSTATE.EL != EL0); constant AccessDescriptor accdesc = CreateAccDescSTGMOPS(privileged, nontemporal); if memset.stage == MOPSStage_Prologue then if memset.setsize > ArchMaxMOPSSETGSize then memset.setsize = ArchMaxMOPSSETGSize; if ((memset.setsize != 0 && !IsAligned(memset.toaddress, TAG_GRANULE)) || !IsAligned(memset.setsize<63:0>, TAG_GRANULE)) then constant FaultRecord fault = AlignmentFault(accdesc, memset.toaddress); AArch64.Abort(fault); if memset.implements_option_a then memset.nzcv = '0000'; memset.toaddress = memset.toaddress + memset.setsize; memset.setsize = 0 -memset.setsize; else
```

<!-- image -->

## &lt;Xs&gt;

```
memset.nzcv = '0010'; memset.stagesetsize = MemSetStageSize(memset); if memset.stage != MOPSStage_Prologue then CheckMemSetParams(memset, options); bits(64) fault_address; if memset.implements_option_a then fault_address = memset.toaddress + memset.setsize; else fault_address = memset.toaddress; if (memset.setsize != 0 && (memset.stagesetsize != 0 || MemStageSetZeroSizeCheck()) && !IsAligned(memset.toaddress, TAG_GRANULE)) then constant FaultRecord fault = AlignmentFault(accdesc, fault_address); AArch64.Abort(fault); if ((memset.stagesetsize != 0 || MemStageSetZeroSizeCheck()) && !IsAligned(memset.setsize<63:0>, TAG_GRANULE)) then constant FaultRecord fault = AlignmentFault(accdesc, fault_address); AArch64.Abort(fault); integer tags_set; AddressDescriptor memaddrdesc; PhysMemRetStatus memstatus; AddressDescriptor tagmemaddrdesc; PhysMemRetStatus tagmemstatus; boolean fault = FALSE; boolean tagfault = FALSE; if memset.implements_option_a then while memset.stagesetsize < 0 && !fault && !tagfault do // IMP DEF selection of the block size that is worked on. While many // implementations might make this constant, that is not assumed. B = SETSizeChoice(memset, TAG_GRANULE); assert B <= -1 * memset.stagesetsize && B<3:0> == '0000'; (-, memaddrdesc, memstatus) = MemSetBytes(memset.toaddress + memset.setsize, data, B, accdesc); constant bits(4) tag = AArch64.AllocationTagFromAddress(memset.toaddress + memset.setsize); (tags_set, tagmemaddrdesc, tagmemstatus) = MemSetTags(memset.toaddress + memset.setsize, tag, B, accdesc); fault = IsFault(memaddrdesc) || IsFault(memstatus); tagfault = IsFault(tagmemaddrdesc) || IsFault(tagmemstatus); if !fault && !tagfault then memset.setsize = memset.setsize + B; memset.stagesetsize = memset.stagesetsize + B; else while memset.stagesetsize > 0 && !fault && !tagfault do // IMP DEF selection of the block size that is worked on. While many // implementations might make this constant, that is not assumed. B = SETSizeChoice(memset, TAG_GRANULE); assert B <= memset.stagesetsize && B<3:0> == '0000'; (-, memaddrdesc, memstatus) = MemSetBytes(memset.toaddress, data, B, accdesc); constant bits(4) tag = AArch64.AllocationTagFromAddress(memset.toaddress); (tags_set, tagmemaddrdesc, tagmemstatus) = MemSetTags(memset.toaddress, tag, B, accdesc); fault = IsFault(memaddrdesc) || IsFault(memstatus); tagfault = IsFault(tagmemaddrdesc) || IsFault(tagmemstatus); if !fault && !tagfault then memset.toaddress = memset.toaddress + B;
```

```
memset.setsize = memset.setsize -B; memset.stagesetsize = memset.stagesetsize -B; UpdateSetRegisters(memset, fault || tagfault, tags_set * TAG_GRANULE); if fault then if IsFault(memaddrdesc) then AArch64.Abort(memaddrdesc.fault); else constant boolean iswrite = TRUE; HandleExternalAbort(memstatus, iswrite, memaddrdesc, B, accdesc); elsif tagfault then if IsFault(tagmemaddrdesc) then AArch64.Abort(tagmemaddrdesc.fault); else constant boolean iswrite = TRUE; HandleExternalAbort(tagmemstatus, iswrite, tagmemaddrdesc, 1, accdesc); if memset.stage == MOPSStage_Prologue then PSTATE.<N,Z,C,V> = memset.nzcv;
```
