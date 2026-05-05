## C6.2.117 CPYFPWTRN, CPYFMWTRN, CPYFEWTRN

Memory copy forward-only, writes unprivileged, reads non-temporal

These instructions copy a requested number of bytes in memory from a source address to a destination address in a forward direction. The prologue, main, and epilogue instructions are expected to be run in succession and to appear consecutively in memory: CPYFPWTRN, then CPYFMWTRN, and then CPYFEWTRN.

CPYFPWTRNperforms some preconditioning of the arguments suitable for using the CPYFMWTRN instruction, and copies an IMPLEMENTATION DEFINED portion of the requested number of bytes. CPYFMWTRN copies a further IMPLEMENTATION DEFINED portion of the remaining bytes. CPYFEWTRN copies any final remaining bytes.

Note

The ability to copy an IMPLEMENTATION DEFINED number of bytes allows an implementation to optimize how the bytes being copied are divided between the different instructions.

For more information on exceptions specific to memory copy instructions, see Memory Copy and Memory Set exceptions.

The memory copy performed by these instructions is in the forward direction only, so the instructions are suitable for a memory copy only where there is no overlap between the source and destination locations, or where the source address is greater than or equal to the destination address.

The architecture supports two algorithms for the memory copy: option A and option B. Which algorithm is used is IMPLEMENTATION DEFINED.

Note

Portable software should not assume that the choice of algorithm is constant.

## For CPYFPWTRN:

- If Xn&lt;63&gt; == 1, the copy size is saturated to 0x7FFFFFFFFFFFFFFF .

On completion of CPYFPWTRN, option A:

- Xn holds -1 times the number of bytes in the saturated copy size remaining to be copied.
- Xs holds the original Xs + saturated copy size.
- Xd holds the original Xd + saturated copy size.
- PSTATE.{N,Z,C,V} are set to {0,0,0,0}.

On completion of CPYFPWTRN, option B:

- Xn holds the number of bytes in the saturated copy size remaining to be copied.
- Xs holds the lowest address that has not been copied from.
- Xd holds the lowest address that has not been copied to.
- PSTATE.{N,Z,C,V} are set to {0,0,1,0}.

For CPYFMWTRN, option A, when PSTATE.C = 0:

- Xn holds a signed 64-bit integer.
- Xn holds -1 times the number of bytes remaining to be copied.
- Xs holds the lowest address to be copied from - Xn.
- Xd holds the lowest address to be copied to - Xn.
- On completion of the instruction, Xn holds -1 times the number of bytes remaining to be copied.

For CPYFMWTRN, option B, when PSTATE.C = 1:

- Xn holds the number of bytes remaining to be copied.
- Xs holds the lowest address to be copied from.
- Xd holds the lowest address to be copied to.
- On completion of the instruction:
- Xn holds the number of bytes remaining to be copied.

- Xs holds the lowest address that has not been copied from.
- Xd holds the lowest address that has not been copied to.

For CPYFEWTRN, option A, when PSTATE.C = 0:

- Xn holds a signed 64-bit integer.
- Xn holds -1 times the number of bytes remaining to be copied.
- Xs holds the lowest address to be copied from - Xn.
- Xd holds the lowest address to be copied to - Xn.
- On completion of the instruction, Xn holds 0.

For CPYFEWTRN, option B, when PSTATE.C = 1:

- Xn holds the number of bytes remaining to be copied.
- Xs holds the lowest address to be copied from.
- Xd holds the lowest address to be copied to.
- On completion of the instruction:
- Xn holds 0.
- Xs holds the lowest address that has not been copied from.
- Xd holds the lowest address that has not been copied to.

Explicit Memory Write effects produced by the instruction behave as if the instruction was executed at EL0 if the Effective value of PSTATE.UAO is 0 and either:

- The instruction is executed at EL1.
- The instruction is executed at EL2 when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

Otherwise, the Explicit Memory Write effects operate with the restrictions determined by the Exception level at which the instruction is executed.

## Integer

(FEAT\_MOPS)

<!-- image -->

## Encoding for the Prologue variant

```
Applies when (op1 == 00) CPYFPWTRN [<Xd>]!, [<Xs>]!, <Xn>!
```

## Encoding for the Main variant

```
Applies when (op1 == 01) CPYFMWTRN [<Xd>]!, [<Xs>]!, <Xn>!
```

## Encoding for the Epilogue variant

```
Applies when (op1 == 10) CPYFEWTRN [<Xd>]!, [<Xs>]!, <Xn>!
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_MOPS) || sz != '00' then EndOfDecode(Decode_UNDEF); CPYParams memcpy; memcpy.d = UInt(Rd); memcpy.s = UInt(Rs); memcpy.n = UInt(Rn); constant bits(4) options = op2; constant boolean rnontemporal = options<3> == '1'; constant boolean wnontemporal = options<2> == '1'; case op1 of when '00' memcpy.stage = MOPSStage_Prologue; when '01' memcpy.stage = MOPSStage_Main; when '10' memcpy.stage = MOPSStage_Epilogue;
```

For information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly Memory Copy and Memory Set CPY* and Crossing a page boundary with different memory types or Shareability attributes.

## Assembler Symbols

&lt;Xd&gt;

For the 'Prologue' variant: is the 64-bit name of the general-purpose register that holds the destination address and is updated by the instruction, encoded in the 'Rd' field.

For the 'Epilogue' and 'Main' variants: is the 64-bit name of the general-purpose register that holds an encoding of the destination address, encoded in the 'Rd' field.

For the 'Prologue' variant: is the 64-bit name of the general-purpose register that holds the source address and is updated by the instruction, encoded in the 'Rs' field.

For the 'Epilogue' and 'Main' variants: is the 64-bit name of the general-purpose register that holds an encoding of the source address, encoded in the 'Rs' field.

For the 'Prologue' variant: is the 64-bit name of the general-purpose register that holds the number of bytes to be transferred and is updated by the instruction to encode the remaining size and destination, encoded in the 'Rn' field.

For the 'Main' variant: is the 64-bit name of the general-purpose register that holds an encoding of the number of bytes to be transferred, encoded in the 'Rn' field.

For the 'Epilogue' variant: is the 64-bit name of the general-purpose register that holds an encoding of the number of bytes to be transferred and is set to zero on completion of the instruction, encoded in the 'Rn' field.

## Operation

```
CheckMOPSEnabled(); CheckCPYConstrainedUnpredictable(memcpy.n, memcpy.d, memcpy.s); memcpy.nzcv = PSTATE.<N,Z,C,V>; memcpy.toaddress = X[memcpy.d, 64]; memcpy.fromaddress = X[memcpy.s, 64]; memcpy.cpysize = SInt(X[memcpy.n, 64]); memcpy.implements_option_a = CPYFOptionA(); constant boolean rprivileged = (if options<1> == '1' then AArch64.IsUnprivAccessPriv() else PSTATE.EL != EL0); constant boolean wprivileged = (if options<0> == '1' then AArch64.IsUnprivAccessPriv() else PSTATE.EL != EL0);
```

## &lt;Xs&gt;

## &lt;Xn&gt;

```
constant AccessDescriptor raccdesc = CreateAccDescMOPS(MemOp_LOAD, rprivileged, rnontemporal); constant AccessDescriptor waccdesc = CreateAccDescMOPS(MemOp_STORE, wprivileged, wnontemporal); if memcpy.stage == MOPSStage_Prologue then if memcpy.cpysize<63> == '1' then memcpy.cpysize = ArchMaxMOPSBlockSize; if memcpy.implements_option_a then memcpy.nzcv = '0000'; // Copy in the forward direction offsets the arguments. memcpy.toaddress = memcpy.toaddress + memcpy.cpysize; memcpy.fromaddress = memcpy.fromaddress + memcpy.cpysize; memcpy.cpysize = 0 -memcpy.cpysize; else memcpy.nzcv = '0010'; memcpy.stagecpysize = MemCpyStageSize(memcpy); if memcpy.stage != MOPSStage_Prologue then CheckMemCpyParams(memcpy, options); integer copied; boolean iswrite; AddressDescriptor memaddrdesc; PhysMemRetStatus memstatus; memcpy.forward = TRUE; boolean fault = FALSE; MOPSBlockSize B = 0; if memcpy.implements_option_a then while memcpy.stagecpysize != 0 && !fault do // IMP DEF selection of the block size that is worked on. While many // implementations might make this constant, that is not assumed. B = CPYSizeChoice(memcpy); assert B <= -1 * memcpy.stagecpysize; (copied, iswrite, memaddrdesc, memstatus) = MemCpyBytes(memcpy.toaddress + memcpy.cpysize, memcpy.fromaddress + memcpy.cpysize, memcpy.forward, B, raccdesc, waccdesc); if copied != B then fault = TRUE; else memcpy.cpysize = memcpy.cpysize + B; memcpy.stagecpysize = memcpy.stagecpysize + B; else while memcpy.stagecpysize > 0 && !fault do // IMP DEF selection of the block size that is worked on. While many // implementations might make this constant, that is not assumed. B = CPYSizeChoice(memcpy); assert B <= memcpy.stagecpysize; (copied, iswrite, memaddrdesc, memstatus) = MemCpyBytes(memcpy.toaddress, memcpy.fromaddress, memcpy.forward, B, raccdesc, waccdesc); if copied != B then fault = TRUE; else memcpy.fromaddress = memcpy.fromaddress + B; memcpy.toaddress = memcpy.toaddress + B; memcpy.cpysize = memcpy.cpysize -B; memcpy.stagecpysize = memcpy.stagecpysize -B; UpdateCpyRegisters(memcpy, fault, copied); if fault then
```

```
if IsFault(memaddrdesc) then AArch64.Abort(memaddrdesc.fault); if IsFault(memstatus) then constant AccessDescriptor accdesc = if iswrite then waccdesc else raccdesc; HandleExternalAbort(memstatus, iswrite, memaddrdesc, B, accdesc); if memcpy.stage == MOPSStage_Prologue then PSTATE.<N,Z,C,V> = memcpy.nzcv;
```
