## C6.2.363 SETPN, SETMN, SETEN

Memory set, non-temporal

These instructions set a required number of bytes in memory to the value in the least significant byte of the source data register. The prologue, main, and epilogue instructions are expected to be run in succession and to appear consecutively in memory: SETPN, then SETMN, and then SETEN.

SETPN performs some preconditioning of the arguments suitable for using the SETMN instruction, and sets an IMPLEMENTATION DEFINED portion of the requested number of bytes. SETMN sets a further IMPLEMENTATION DEFINED portion of the remaining bytes. SETEN sets any final remaining bytes.

Note

The ability to set an IMPLEMENTATION DEFINED number of bytes allows an implementation to optimize how the bytes being set are divided between the different instructions.

For more information on exceptions specific to memory set instructions, see Memory Copy and Memory Set exceptions.

The architecture supports two algorithms for the memory set: option A and option B. Which algorithm is used is IMPLEMENTATION DEFINED.

Note

Portable software should not assume that the choice of algorithm is constant.

For SETPN:

- If Xn&lt;63&gt; == 1, the set size is saturated to 0x7FFFFFFFFFFFFFFF .

On completion of SETPN, option A:

- Xn holds -1 times the number of bytes in the saturated set size remaining to be set.
- Xd holds the original Xd + saturated set size.
- PSTATE.{N,Z,C,V} are set to {0,0,0,0}.

On completion of SETPN, option B:

- Xn holds the number of bytes in the saturated set size remaining to be set.
- Xd holds the lowest address that has not been set.
- PSTATE.{N,Z,C,V} are set to {0,0,1,0}.

For SETMN, option A, when PSTATE.C = 0:

- Xn holds a signed 64-bit integer.
- Xn holds -1 times the number of bytes remaining to be set.
- Xd holds the lowest address to be set - Xn.
- On completion of the instruction, Xn holds -1 times the number of bytes remaining to be set.

For SETMN, option B, when PSTATE.C = 1:

- Xn holds the number of bytes remaining to be set.
- Xd holds the lowest address to be set.
- On completion of the instruction:
- Xn holds the number of bytes remaining to be set.
- Xd holds the lowest address that has not been set.

For SETEN, option A, when PSTATE.C = 0:

- Xn holds a signed 64-bit integer.
- Xn holds -1 times the number of bytes remaining to be set.
- Xd holds the lowest address to be set - Xn.
- On completion of the instruction, Xn holds 0.

For SETEN, option B, when PSTATE.C = 1:

- Xn holds the number of bytes remaining to be set.
- Xd holds the lowest address to be set.
- On completion of the instruction:
- Xn holds 0.
- Xd holds the lowest address that has not been set.

## Integer

(FEAT\_MOPS)

<!-- image -->

## Encoding for the Prologue variant

Applies when 0010)

```
(op2 == SETPN [<Xd>]!, <Xn>!, <Xs>
```

## Encoding for the Main variant

```
Applies when (op2 == 0110) SETMN [<Xd>]!, <Xn>!, <Xs>
```

## Encoding for the Epilogue variant

```
Applies when (op2 == 1010) SETEN [<Xd>]!, <Xn>!, <Xs>
```

## Decode for all variants of this encoding

```
'00' then EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_MOPS) || sz != SETParams memset; memset.d = UInt(Rd); memset.s = UInt(Rs); memset.n = UInt(Rn); constant bits(2) options = op2<1:0>; constant boolean nontemporal = options<1> == '1'; case op2<3:2> of when '00' memset.stage = MOPSStage_Prologue; when '01' memset.stage = MOPSStage_Main; when '10' memset.stage = MOPSStage_Epilogue; otherwise EndOfDecode(Decode_UNDEF);
```

For information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly Memory Copy and Memory Set SET* and Crossing a page boundary with different memory types or Shareability attributes.

## Assembler Symbols

## &lt;Xd&gt;

For the 'Prologue' variant: is the 64-bit name of the general-purpose register that holds the destination address and is updated by the instruction, encoded in the 'Rd' field.

For the 'Epilogue' and 'Main' variants: is the 64-bit name of the general-purpose register that holds an encoding of the destination address and for option B is updated by the instruction, encoded in the 'Rd' field.

For the 'Prologue' variant: is the 64-bit name of the general-purpose register that holds the number of bytes to be set and is updated by the instruction, encoded in the 'Rn' field.

For the 'Main' variant: is the 64-bit name of the general-purpose register that holds an encoding of the number of bytes to be set and is updated by the instruction, encoded in the 'Rn' field.

For the 'Epilogue' variant: is the 64-bit name of the general-purpose register that holds the number of bytes to be set and is set to zero on completion of the instruction, encoded in the 'Rn' field.

## &lt;Xn&gt;

<!-- image -->

Is the 64-bit name of the general-purpose register that holds the source data, encoded in the 'Rs' field.

## Operation

```
CheckMOPSEnabled(); CheckSETConstrainedUnpredictable(memset.n, memset.d, memset.s); constant bits(8) data = X[memset.s, 8]; MOPSBlockSize B = 0; memset.is_setg = FALSE; memset.nzcv = PSTATE.<N,Z,C,V>; memset.toaddress = X[memset.d, 64]; if memset.stage == MOPSStage_Prologue then memset.setsize = UInt(X[memset.n, 64]); else memset.setsize = SInt(X[memset.n, 64]); memset.implements_option_a = SETOptionA(); constant boolean privileged = (if options<0> == '1' then AArch64.IsUnprivAccessPriv() else PSTATE.EL != EL0); constant AccessDescriptor accdesc = CreateAccDescMOPS(MemOp_STORE, privileged, nontemporal); if memset.stage == MOPSStage_Prologue then if memset.setsize > ArchMaxMOPSBlockSize then memset.setsize = ArchMaxMOPSBlockSize; if memset.implements_option_a then memset.nzcv = '0000'; memset.toaddress = memset.toaddress + memset.setsize; memset.setsize = 0 -memset.setsize; else memset.nzcv = '0010'; memset.stagesetsize = MemSetStageSize(memset); if memset.stage != MOPSStage_Prologue then CheckMemSetParams(memset, options); AddressDescriptor memaddrdesc; PhysMemRetStatus memstatus; integer memory_set; boolean fault = FALSE;
```

```
if memset.implements_option_a then while memset.stagesetsize < 0 && !fault do // IMP DEF selection of the block size that is worked on. While many // implementations might make this constant, that is not assumed. B = SETSizeChoice(memset, 1); assert B <= -1 * memset.stagesetsize; (memory_set, memaddrdesc, memstatus) = MemSetBytes(memset.toaddress + memset.setsize, data, B, accdesc); if memory_set != B then fault = TRUE; else memset.setsize = memset.setsize + B; memset.stagesetsize = memset.stagesetsize + B; else while memset.stagesetsize > 0 && !fault do // IMP DEF selection of the block size that is worked on. While many // implementations might make this constant, that is not assumed. B = SETSizeChoice(memset, 1); assert B <= memset.stagesetsize; (memory_set, memaddrdesc, memstatus) = MemSetBytes(memset.toaddress, data, B, accdesc); if memory_set != B then fault = TRUE; else memset.toaddress = memset.toaddress + B; memset.setsize = memset.setsize -B; memset.stagesetsize = memset.stagesetsize -B; UpdateSetRegisters(memset, fault, memory_set); if fault then if IsFault(memaddrdesc) then AArch64.Abort(memaddrdesc.fault); else constant boolean iswrite = TRUE; HandleExternalAbort(memstatus, iswrite, memaddrdesc, B, accdesc); if memset.stage == MOPSStage_Prologue then PSTATE.<N,Z,C,V> = memset.nzcv;
```
