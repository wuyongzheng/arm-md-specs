## 6.3.57 SMMU\_S\_CR0

The SMMU\_S\_CR0 characteristics are:

## Purpose

Secure SMMU programming interface control and configuration register.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_CR0 are RES0.

## Attributes

SMMU\_S\_CR0 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:10]

Reserved, RES0.

## NSSTALLD, bit [9]

Non-secure stall disable.

| NSSTALLD   | Meaning                                                             |
|------------|---------------------------------------------------------------------|
| 0b0        | Non-secure programming interface might use Stall model.             |
| 0b1        | Non-secure programming interface prohibited from using Stall model. |

- When SMMU\_S\_IDR0.STALL\_MODEL == 0b00 , setting this bit modifies the Non-secure behavior so that only the Terminate model is available for Non-secure streams and SMMU\_IDR0.STALL\_MODEL reads as 0b01 . Otherwise, if NSSTALLD == 0, SMMU\_IDR0.STALL\_MODEL == SMMU\_S\_IDR0.STALL\_MODEL.
- When SMMU\_S\_IDR0.STALL\_MODEL != 0b00 , this bit is RES0 and SMMU\_IDR0.STALL\_MODEL == SMMU\_S\_IDR0.STALL\_MODEL.
- -Note: A reserved SMMU\_S\_CR0 bit is not reflected into SMMU\_S\_CR0ACK.

The reset behavior of this field is:

- This field resets to '0' .

## VMW, bits [8:6]

## When SMMU\_IDR0.VMW == 1:

Secure VMID Wildcard.

| VMW   | Meaning                                    |
|-------|--------------------------------------------|
| 0b000 | TLB invalidations match VMID tags exactly. |
| 0b001 | TLB invalidations match VMID[N:1].         |
| 0b010 | TLB invalidations match VMID[N:2].         |
| 0b011 | TLB invalidations match VMID[N:3].         |
| 0b100 | TLB invalidations match VMID[N:4].         |

- The VMW field is defined in the same way as SMMU\_CR0.VMW, but affects Secure VMID matching on invalidation.
- All other values are reserved, and behave as 0b000 .
- -N == upper bit of VMID as determined by SMMU\_IDR0.VMID16.
- This field has no effect on VMID matching on translation lookup.

The reset behavior of this field is:

- This field resets to '000' .

## Otherwise:

Reserved, RES0.

## SIF, bit [5]

Secure Instruction Fetch.

| SIF   | Meaning                                                                                              |
|-------|------------------------------------------------------------------------------------------------------|
| 0b0   | Secure transactions might exit the SMMUas a Non-secure instruction fetch.                            |
| 0b1   | Secure transactions determined to be Non-secure instruction fetch are treated as a Permission fault. |

This field causes transactions from a Secure stream that are determined to be an instruction fetch, after INSTCFG fields are applied, to experience a Permission fault if their effective stage 1 output NS attribute is Non-secure.

- When translation is disabled because SMMUEN == 0, the transaction is terminated with abort and no F\_PERMISSION is recorded.
- When SMMUEN is set, one of the following occurs and, if the Event queue is writable, a stage 1 F\_PERMISSION is recorded:
- -If stage 1 translation is disabled (STE.Config selects bypass, including the case where Config == 0b1x1 and STE.S1DSS causes stage 1 to be skipped, behaving as though Config == 0b1x0 ) the faulting transaction is terminated with abort.
- -If stage 1 translation is applied (STE.Config enables stage 1 and STE.S1DSS does not cause stage 1 translation to be skipped), CD.{A,R,S} govern stall and terminate behavior of the transaction.
- -The F\_PERMISSION event is reported with CLASS = IN and S2 = 0.

The SIF field is permitted to be cached in a TLB or configuration cache and an Update of this field requires invalidation of all Secure TLB entries and configuration caches.

The reset behavior of this field is:

- This field resets to '0' .

## Bit [4]

Reserved, RES0.

## CMDQEN, bit [3]

Enable Secure Command queue processing.

| CMDQEN   | Meaning                                                           |
|----------|-------------------------------------------------------------------|
| 0b0      | Processing of commands from the Secure Command queue is disabled. |
| 0b1      | Processing of commands from the Secure Command queue is enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## EVENTQEN, bit [2]

Enable Secure Event queue writes.

| EVENTQEN   | Meaning                                        |
|------------|------------------------------------------------|
| 0b0        | Writes to the Secure Event queue are disabled. |
| 0b1        | Writes to the Secure Event queue are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## Bit [1]

Reserved, RES0.

## SMMUEN, bit [0]

Secure SMMU enable.

| SMMUEN   | Meaning                                                                                         |
|----------|-------------------------------------------------------------------------------------------------|
| 0b0      | All Secure streams bypass the SMMU, with attributes determined from SMMU_S_GBPA.                |
| 0b1      | All Secure streams are checked against configuration structures, and might undergo translation. |

The reset behavior of this field is:

- This field resets to '0' .

## Additional Information

The Update procedure, with respect to flags reflected into SMMU\_S\_CR0ACK, is the same as for SMMU\_CR0.

The Update side effects of CMDQEN, EVENTQEN, and SMMUEN fields are similar to their respective equivalents in SMMU\_CR0.

## Accessing SMMU\_S\_CR0

Accesses to this register use the following encodings:

Accessible at offset 0x8020 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## Additional information

For more information, see the additional information section in SMMU\_CR0.

## 6.3.57.1 NSSTALLD

This bit has no Update side effects. NSSTALLD prevents Non-secure configuration from using the Stall model, therefore stall-related commands are unavailable and use of STE and CD stall configuration renders the structures ILLEGAL.

This bit is permitted to be cached in configuration caches.

This bit must not be modified when any of the following could occur:

- Non-secure CMD\_STALL\_TERM or CMD\_RESUME commands have been submitted to the Non-secure Command queue, therefore might be processed.
- Non-secure transactions are being translated through structures configured to stall faults.

A change to this bit takes effect at an UNPREDICTABLE point prior to Update completion. If changed while the above stall-related activities are occurring, it is UNPREDICTABLE whether transactions and commands behave in manner corresponding to either value of this bit, until Update of this bit completes.

Update completes when it is guaranteed that all of the following are observable:

- Any subsequent fetch of an STE or CD will behave in a manner relating to the new value of this bit.
- Any subsequently consumed command will behave in a manner relating to the new value of this bit.
- The value of SMMU\_IDR0.STALL\_MODEL reflects the new value of this bit.

Note: After Update is completed, client transactions might be affected by stall configuration previously cached in a Configuration cache, until completion of an appropriate invalidation operation.

Note: Secure software is expected to Update this bit before Non-secure software can access the SMMU.

## 6.3.57.2 SIF

This bit has no Update side effects.

For a transaction that bypasses translation, a change to SIF is guaranteed to be visible with respect to that transaction after the new value of SIF is acknowledged in SMMU\_S\_CR0ACK.SIF.

For a transaction that undergoes translation, a change to SIF is guaranteed to be visible with respect to that transaction only after the completion of a TLB invalidation of a scope related to that transaction, where the TLB invalidation is made visible to the SMMU after the new value of SIF is acknowledged in SMMU\_S\_CR0ACK.SIF.