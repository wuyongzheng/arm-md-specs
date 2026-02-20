## C9.2.158 LDR (table)

Load ZT0 register

This instruction loads the 64-byte ZT0 register from the memory address provided in the 64-bit scalar base register. This instruction is unpredicated.

The load is performed as contiguous byte accesses, with no endian conversion and no guarantee of single-copy atomicity larger than a byte. However, if alignment is checked, then the base register must be aligned to 16 bytes.

This instruction does not require the PE to be in Streaming SVE mode, and it is expected that this instruction will not experience a significant slowdown due to contention with other PEs that are executing in Streaming SVE mode.

## SME2

(FEAT\_SME2)

<!-- image -->

## Encoding

```
LDR ZT0, [<Xn|SP>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer n = UInt(Rn);
```

## Assembler Symbols

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
CheckSMEEnabled(); CheckSMEZT0Enabled(); constant integer elements = 512 DIV 8; bits(64) addr; bits(512) result; constant boolean contiguous = TRUE; constant boolean nontemporal = FALSE; constant boolean tagchecked = n != 31; constant AccessDescriptor accdesc = CreateAccDescSME(MemOp_LOAD, nontemporal, contiguous, tagchecked); if n == 31 then CheckSPAlignment(); addr = SP[64]; else addr = X[n, 64]; constant boolean aligned = IsAligned(addr, 16); if !aligned && AlignmentEnforced() then constant FaultRecord fault = AlignmentFault(accdesc, addr); AArch64.Abort(fault); for e = 0 to elements-1
```

```
EndOfDecode(Decode_UNDEF);
```

```
Elem[result, e, 8] = AArch64.MemSingle[addr, 1, accdesc, aligned]; addr = AddressIncrement(addr, 1, accdesc); ZT0[512] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.