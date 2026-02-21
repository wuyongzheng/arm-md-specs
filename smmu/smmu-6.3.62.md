## 6.3.62 SMMU\_S\_INIT

The SMMU\_S\_INIT characteristics are:

## Purpose

Provides controls for the invalidation of all cache and TLB contents.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_INIT are RES0.

## Attributes

SMMU\_S\_INIT is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:1]

Reserved, RES0.

## INV\_ALL, bit [0]

Invalidate all cache and TLB contents.

- For writes:
- -0b0 : If INV\_ALL == 0, ignored.
- -0b1 : SMMU-global invalidation is performed for all configuration and translation caches for all translation regimes and Security states.
- For reads:
- -0b0 : There is no outstanding global invalidation operation.
- -0b1 : There is an outstanding global invalidation operation.
- Note: This field can be used to simplify Secure software that otherwise makes no use of the SMMU but must safely initialize the SMMU for use by Non-secure software. See section 3.11 Reset, Enable and initialization .
- Note: When SMMU\_S\_IDR1.SECURE\_IMPL == 1, but no Secure software exists, Arm strongly recommends this register is exposed for use by Non-secure initialization software.
- Note: If the system provides an IMPLEMENTATION DEFINED mechanism that allows Non-secure software to access this register, Secure software is expected to disable this mechanism after the SMMU is initialized.

If SMMU\_ROOT\_IDR0.REALM\_IMPL == 1, then SMMU\_S\_INIT.INV\_ALL has no effect if SMMU\_ROOT\_CR0.GPCEN == 1, and it is Root firmware's responsibility to write to INV\_ALL before enabling granule protection checks.

The reset behavior of this field is:

- This field resets to '0' .

## Additional Information

When observing the conditions in this section, a write of INV\_ALL to 1 causes an invalidation of all cache and TLB entries that are present before the write and on completion of the invalidation the SMMU resets INV\_ALL to 0, including when an invalidation operation was already underway before the write.

Note: If the conditions regarding SMMUEN are observed correctly, a write of 1 to INV\_ALL is guaranteed to invalidate the SMMU caches and reset INV\_ALL to 0 when complete.

The completion of an INV\_ALL invalidation is not required to depend on the completion of any outstanding transactions.

An INV\_ALL invalidation operation affects locked configuration and translation cache entries, if an implementation supports locking of cache entries.

Note: As GPT information is permitted to be cached in a TLB, an INV\_ALL operation also invalidates all GPT information cached in TLBs.

## Accessing SMMU\_S\_INIT

SMMU\_S\_INIT.INV\_ALL has no effect if SMMU\_ROOT\_CR0.GPCEN == 1.

If SMMU\_ROOT\_CR0.GPCEN == 0, a write of 1 to INV\_ALL when any SMMU\_(*\_)CR0.SMMUEN == 1, or an Update of any SMMUEN to 1 is in progress, or SMMU\_ROOT\_CR0.ACCESSEN == 1, or an Update of ACCESSEN to 1 is in progress, is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The write is IGNORED.
- The invalidation operation occurs and completes, with INV\_ALL reset to 0 on completion.

An Update of SMMUEN to 1 while an INV\_ALL invalidation operation is underway has a CONSTRAINED UNPREDICTABLE effect on the invalidation operation and has one of the following behaviors:

- The invalidation operation completes successfully, with INV\_ALL reset to 0 after completion.
- The invalidation operation might not affect any cache or TLB entries, and INV\_ALL is reset to 0 by the SMMU.

After INV\_ALL is written to 1, a write of 0 before the invalidation operation is observed to have completed is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The invalidation operation does not take place.
- The invalidation operation completes successfully but it cannot be determined when this completion occurs.

Note: It is Root firmware's responsibility to write to INV\_ALL before enabling SMMU\_ROOT\_CR0.{ACCESSEN, GPCEN}.

Accesses to this register use the following encodings:

Accessible at offset 0x803C from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.