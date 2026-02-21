## 6.3.162 SMMU\_R\_GMECID

The SMMU\_R\_GMECID characteristics are:

## Purpose

Configures the MECID value for global SMMU-originated accesses to the Realm PA space.

## Configuration

This register is present only when SMMU\_R\_IDR3.MEC == 1. Otherwise, direct accesses to SMMU\_R\_GMECID are RES0.

## Attributes

SMMU\_R\_GMECID is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## GMECID, bits [15:0]

MECID for SMMU-originated access to Realm PA space for:

- Fetches of L1STD, STE and VMS structures.
- Access to Command queues, Event queue and PRI queue.
- SMMU-originated MSIs.
- Fetches of DPT information

Bits above the supported MECID size, indicated in SMMU\_R\_MECIDR.MECIDSIZE are RES0.

If MECIDSIZE is less than 0xF , the SMMU treats bits [15:MECIDSIZE+1] of this field as zero.

The reset behavior of this field is:

- This field resets to 0x0000 .

## Accessing SMMU\_R\_GMECID

Note: Accesses to SMMU\_R\_GMECID are not guarded by SMMU\_R\_CR0.PRIQEN or any of the SMMU\_R\_IRQ\_CTRL bits. PRIQEN has an Effective value of 0 if

SMMUEN is 0. Software must not change the global MECID value in situations where generation of an MSI with an unknown MECID value could

cause the target location contents to become UNKNOWN. For an MSI that targets a GIC ITS, the MECID might be IGNORED by the GIC and therefore

use of an unknown MECID would not lead to a loss of correctness.

Accesses to this register use the following encodings:

Accessible at offset 0x0228 from SMMUv3\_R\_PAGE\_0

- When ((((((SMMU\_R\_CR0.SMMUEN == '0') &amp;&amp; (SMMU\_R\_CR0.EVENTQEN == '0')) &amp;&amp; (SMMU\_R\_CR0.CMDQEN == '0')) &amp;&amp; (SMMU\_R\_CR0ACK.SMMUEN == '0'))

&amp;&amp; (SMMU\_R\_CR0ACK.EVENTQEN == '0')) &amp;&amp; (SMMU\_R\_CR0ACK.CMDQEN == '0')) &amp;&amp; ((SMMU\_R\_IDR0.ECMDQ == '0') || (((SMMU\_R\_IDR0.ECMDQ == '1') &amp;&amp; (SMMU\_R\_ECMDQ\_PROD&lt;n&gt;.EN == '0')) &amp;&amp; (SMMU\_R\_ECMDQ\_CONS&lt;n&gt;.ENACK == '0'))), accesses to this register are RW.

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.