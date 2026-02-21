## 6.3.112 SMMU\_ROOT\_CR0

The SMMU\_ROOT\_CR0 characteristics are:

## Purpose

Root Control Register

## Configuration

Each field in this register has a corresponding field in SMMU\_ROOT\_CR0ACK, with the same Update observability semantics as fields in SMMU\_CR0 versus SMMU\_CR0ACK.

## Attributes

SMMU\_ROOT\_CR0 is a 32-bit register.

This register is part of the SMMUv3\_ROOT block.

## Field descriptions

<!-- image -->

## Bits [31:2]

Reserved, RES0.

## GPCEN, bit [1]

Enable Granule Protection Checks.

| GPCEN   | Meaning                                                                                                  |
|---------|----------------------------------------------------------------------------------------------------------|
| 0b0     | All accesses bypass granule protection checks.                                                           |
| 0b1     | All client and SMMU-originated accesses, except for GPT walks, are subject to granule protection checks. |

When this bit is changed, the SMMU updates SMMU\_ROOT\_CR0ACK.GPCEN to match, once the following observability requirements are satisfied. This is referred to as completion of an Update.

Completion of an Update of GPCEN from 0 to 1 guarantees that:

- All future client-originated and SMMU-originated transactions are subject to granule protection checks.
- All previous transactions that were issued without a granule protection check have completed.

Completion of an Update of GPCEN from 1 to 0 guarantees that:

- All future client-originated and SMMU-originated transactions will bypass granule protection checks.
- All prior faults to be reported in SMMU\_ROOT\_GPF\_FAR and SMMU\_ROOT\_GPT\_CFG\_FAR have been reported.
- The SMMU has completed all outstanding fetches of GPT information.

Note: Completion of an Update of GPCEN from 1 to 0 does not guarantee that outstanding accesses using the previous GPT configuration have completed. However, completion of a TLBI by PA with scope PAALL after the completion of the Update of GPCEN does guarantee this, including for Non-secure accesses made to Locations above the range configured in SMMU\_ROOT\_GPT\_BASE\_CFG.PPS.

The reset behavior of this field is:

- This field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is RO if any of the following are true:
- -SMMU\_ROOT\_CR0.ACCESSEN != SMMU\_ROOT\_CR0ACK.ACCESSEN
- -SMMU\_ROOT\_CR0.GPCEN != SMMU\_ROOT\_CR0ACK.GPCEN
- Otherwise, access to this field is RW.

## ACCESSEN, bit [0]

Enable accesses from the SMMU and client devices.

| ACCESSEN   | Meaning                                                                                       |
|------------|-----------------------------------------------------------------------------------------------|
| 0b0        | SMMU-originated accesses and client-originated accesses do not become observable.             |
| 0b1        | SMMU-originated accesses and client-originated accesses are not terminated by this mechanism. |

This bit has higher priority than GPCEN.

When this bit is changed, the SMMU updates SMMU\_ROOT\_CR0ACK.ACCESSEN to match, once the observability requirements below are satisfied. This is referred to as completion of an Update.

Completion of an Update of ACCESSEN from 0 to 1 guarantees that:

- Previous accesses that were to be terminated by this mechanism have been marked to be terminated.
- Future client-originated and SMMU-originated accesses might succeed, according to other architectural checks.

Note: It is Root firmware's responsibility to set ACCESSEN to 1 only after an Update of GPCEN to 1 has successfully completed, in order to guarantee a consistent update order.

Completion of an Update of ACCESSEN from 1 to 0 guarantees that:

- Previous client-originated accesses not terminated by this mechanism are observable to their Shareability domain.
- Previous SMMU-originated accesses, including GPT fetches, have completed.
- The SMMU will not issue GPT fetches.
- Future SMMU-originated accesses will be terminated as though experiencing a GPF as-reported in SMMU\_ROOT\_GPF\_FAR.
- Future client-originated accesses will be processed in a manner consistent with any access to a physical address experiencing a GPF. This includes:
- -An access is terminated with an external abort as a result of a configuration structure or translation table access experiencing a GPF.
- -An access is terminated with an external abort as a result of a GPF on the output address of that access.
- -If cached configuration information and information cached in TLBs would permit the access to be stalled, it is stalled.
- -If cached configuration information and information cached in TLBs would permit the access to be completed as RAZ/WI, it is completed as RAZ/WI.

Note: For an SMMU that supports stall model, advertised in SMMU\_(S\_)IDR0.STALL\_MODEL, there may be outstanding transactions affected by stall configuration if ACCESSEN is programmed to 0 while SMMU\_(S\_)CR0.SMMUEN == 1. Configuration of SMMU\_(S\_)CR0.SMMUEN to 0 guarantees termination of stalled transactions.

The reset behavior of this field is:

- This field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is RO if any of the following are true:
- -SMMU\_ROOT\_CR0.ACCESSEN != SMMU\_ROOT\_CR0ACK.ACCESSEN
- -SMMU\_ROOT\_CR0.GPCEN != SMMU\_ROOT\_CR0ACK.GPCEN
- Otherwise, access to this field is RW.

## Accessing SMMU\_ROOT\_CR0

Accesses to this register use the following encodings:

Accessible at offset 0x0020 from SMMUv3\_ROOT

- When an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.