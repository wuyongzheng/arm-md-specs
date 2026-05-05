## C5.5.28 TLBI RPAOS, TLB Range Invalidate GPT Information by PA, Outer Shareable

The TLBI RPAOS characteristics are:

## Purpose

Invalidates cached copies of GPT entries from TLBs. Details:

- The invalidation applies to TLB entries containing GPT information that relates to a physical address.
- The invalidation affects all TLBs in the Outer Shareable domain.
- Invalidates TLB entries containing GPT information from all levels of the GPT walk that relates to the supplied physical address.
- Invalidations are range-based, invalidating TLB entries starting from the address in BaseADDR, within the range as specified by SIZE.

The full set of TLB maintenance instructions that invalidate cached GPT entries is: TLBI PAALL, TLBI PAALLOS, TLBI RPALOS, and TLBI RPAOS.

These instructions have the same ordering, observability, and completion behavior as all other TLBI instructions.

## Configuration

This system instruction is present only when FEAT\_RME is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TLBI RPAOS are UNDEFINED.

## Attributes

TLBI RPAOS is a 64-bit System instruction.

## Field descriptions

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## SIZE, bits [47:44]

Size of the range for invalidation.

If SIZE is a reserved value, no TLB entries are required to be invalidated.

| SIZE   | Meaning   |
|--------|-----------|
| 0b0000 | 4KB.      |
| 0b0001 | 16KB.     |
| 0b0010 | 64KB.     |
| 0b0011 | 2MB.      |

All other values are reserved.

If SIZE gives a range smaller than the configured physical granule size in GPCCR\_EL3.PGS, then the Effective value of SIZE is taken to be the size configured by GPCCR\_EL3.PGS.

If GPCCR\_EL3.PGS is configured to a reserved value, no TLB entries are required to be invalidated.

If GPCCR\_EL3.PGS is configured to different values at the broadcasting PE and receiving PE, no TLB entries are required to be invalidated at the receiving PE.

## Address[55:52], bits [43:40]

## When FEAT\_D128 is implemented:

Extension to Address. For more information, see Address.

## Otherwise:

Reserved, RES0.

## Address, bits [39:0]

The starting address for the range of the maintenance instruction.

This field is decoded with reference to the value of GPCCR\_EL3.PGS to give BaseADDR as follows:

| GPCCR_EL3.PGS   | BaseADDR                   |
|-----------------|----------------------------|
| 0b00 (4KB)      | BaseADDR[51:12] = Xt[39:0] |
| 0b10 (16KB)     | BaseADDR[51:14] = Xt[39:2] |
| 0b01 (64KB)     | BaseADDR[51:16] = Xt[39:4] |

Other bits of BaseADDR are treated as zero, to give the Effective value of BaseADDR.

If the Effective value of BaseADDR is not aligned to the size of the Effective value of SIZE, no TLB entries are required to be invalidated.

If the Effective value of BaseADDR targets an address above the implemented PA range that ID\_AA64MMFR0\_EL1.PARange indicates, no TLB entries are required to be invalidated.

If ID\_AA64MMFR0\_EL1.PARange is 0b0111 , Address[55:52] form the upper part of the BaseADDR value. Otherwise, Address[55:52] are RES0.

## Executing TLBI RPAOS

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

| SIZE   | Meaning   |
|--------|-----------|
| 0b0100 | 32MB.     |
| 0b0101 | 512MB.    |
| 0b0110 | 1GB.      |
| 0b0111 | 16GB.     |
| 0b1000 | 64GB.     |
| 0b1001 | 512GB.    |

TLBI RPAOS{, &lt;Xt&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b110 | 0b1000 | 0b0100 | 0b011 |

if !(IsFeatureImplemented(FEAT\_RME) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

UNDEFINED;

elsif PSTATE.EL == EL2 then

UNDEFINED;

elsif PSTATE.EL == EL3 then

AArch64.TLBI\_RPA(TLBILevel\_Any, X[t, 64], Broadcast\_OSH);
