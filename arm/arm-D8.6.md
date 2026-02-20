## D8.6 Memory region attributes

ISGDKK

The memory region attributes in a descriptor define the memory type, Memory Tagging attributes, the XS attribute, Cacheability, and whether the memory region is Shareable. For translation regimes that support two translation stages, the stage 1 and stage 2 memory region attributes are combined to produce a resultant memory type and Cacheability, and Shareability.

IHJZQP

IGJJZB

ILHJDF

All of the following apply to the memory region attributes:

- The stage 1 OA attributes are derived from a combination of the Block descriptor and Page descriptor AttrIndx[3:0] field, and the MAIR\_ELx and MAIR2\_ELx register fields.
- The stage 1 translation table walk attributes are derived from the TCR\_ELx.{IRGN n , ORGN n , SH n } fields.
- The SCTLR\_ELx.{C, I} fields might override stage 1 attributes.
- The HCR\_EL2.PTW field might override stage 2 translation attributes of a stage 1 translation table walk.
- If EL2 is enabled, then for the EL1&amp;0 translation regime the HCR\_EL2.{CD, DC} fields might override stage 1 and stage 2 attributes.
- All of the following HCR\_EL2.FWB values affect the stage 2 attributes:
- -When the Effective value of HCR\_EL2.FWB is 0, stage 2 attributes are derived from the stage 2 MemAttr[3:2] descriptor bits, then combined with stage 1 attributes.
- -When the Effective value of HCR\_EL2.FWB is 1, stage 2 attributes are derived from the stage 2 MemAttr[2:0] descriptor bits.
- For Device memory and Normal Non-cacheable mappings from stage 1, normalization of the Shareability that is input to stage 2 is IMPLEMENTATION DEFINED.
- For Device memory and Normal Non-cacheable mappings from stage 2, Shareability is always normalized to Outer Shareable.

For a virtualization implementation, combining memory attributes from stage 1 and stage 2 translations support all of the following functions that are useful to a hypervisor executing at EL2:

- Reduce or increase the permitted Cacheability of a region.
- Increase the required Shareability of a region.

The effects of combining memory attributes defined by the hypervisor are expected to be functionally transparent to the Guest OS.

## D8.6.1 Stage 1 memory type and Cacheability attributes

RNWZCF

If FEAT\_AIE is implemented, then all of the following apply:

- If a stage 1 translation regime uses VMSAv9-128, then the Effective value of the stage 1 Attribute Index Extension (AIE) is 1.
- If a stage 1 translation regime uses VMSAv8-64, then the AIE value is determined by the following table:

## Table D8-94 Determination of AIE value

| Translation regime   | AIE value    |
|----------------------|--------------|
| EL1&0                | TCR2_EL1.AIE |
| EL2&0                | TCR2_EL2.AIE |
| EL2                  | TCR2_EL2.AIE |
| EL3                  | TCR_EL3.AIE  |

RSXRTL

If FEAT\_AIE is not implemented, then the Effective value of AIE is 0.

RHHGNL

If FEAT\_AIE is not implemented, all of the following apply:

- For a stage 1 translation, the Block descriptor and Page descriptor AttrIndx[2:0] field holds the value n used to select the 8-bit field MAIR\_ELx.Attr&lt; n &gt; that specifies the memory region attributes of the descriptor OA.

RYJLRL

RBXFVK

- It is IMPLEMENTATION DEFINED how AttrIndx[2:0] is used to index into AMAIR\_ELx.

If FEAT\_AIE is implemented, then all of the following apply to the Block descriptor and Page descriptor AttrIndx field:

- If AIE is disabled, or if AIE is enabled and AttrIndx[3] is 0, then AttrIndx[2:0] holds the value n used to select the 8-bit field in all of the following registers:
- -MAIR\_ELx.Attr&lt; n &gt; that specifies the memory region attributes of the descriptor OA.
- -AMAIR\_ELx.Attr&lt; n &gt; that specifies the IMPLEMENTATION DEFINED memory region attributes of the descriptor OA.
- If AIE is enabled and AttrIndx[3] is 1, then AttrIndx[2:0] holds the value n used to select the 8-bit field in all of the following registers:
- -MAIR2\_ELx.Attr&lt; n &gt; that specifies the memory region attributes of the descriptor OA.
- -AMAIR2\_ELx.Attr&lt; n &gt; that specifies the IMPLEMENTATION DEFINED memory region attributes of the descriptor OA.

If AIE is enabled, then AttrIndx[3:0] is used to index into AMAIR\_ELx as follows:

- When AttrIndx[3] is 0, stage 1 Auxiliary Memory Attributes are obtained from AMAIR\_ELx[AttrIndx[2:0]*8+7:AttrIndx[2:0]*8].
- When AttrIndx[3] is 1, stage 1 Auxiliary Memory Attributes are obtained from additional AMAIR2\_ELx[AttrIndx[2:0]*8+7:AttrIndx[2:0]*8].

IDKDPN FEAT\_AIE enables use of page based IMPLEMENTATION DEFINED memory attributes to select an 8-bit field from AMAIR\_ELx or AMAIR2\_ELx.

IFVLFZ

For the memory region specified by a Block descriptor and Page descriptor, the MAIR\_ELx.Attr&lt; n &gt; or MAIR2\_ELx.Attr&lt; n &gt; field selected by the descriptor AttrIndx[2:0] field defines all of the following:

- The Device or Normal memory type.
- For Device memory, all of the following:
- -One of the Device-nGnRnE, Device-nGnRE, Device-nGRE, or Device-GRE Device memory types.
- -If FEAT\_XS is implemented, then the XS attribute.
- For Normal memory, all of the following:
- -For both inner and outer Cacheability, one of the Non-cacheable, Write-Through, or Write-Back attributes.
- -For Write-Through Cacheable and Write-Back Cacheable regions, the Read-Allocate and Write-Allocate hints, each of which is Allocate or No Allocate, and the Transient allocation hints.
- -If FEAT\_MTE2 is implemented, then the Tagged attribute.
- -If FEAT\_XS is implemented, then the XS attribute.

For more information, see XS attribute modifier and Memory region tagging types.

| R QVNKY   | If FEAT_AIE is implemented, then the value 0x00 in AMAIR_ELx.Attr< n > or AMAIR2_ELx.Attr< n > does not give IMPLEMENTATION DEFINED memory region attributes for translations using that Attr< n > field at stage 1.   |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I NSVYS   | The memory attributes obtained from MAIR_ELx.Attr< n >, MAIR2_ELx.Attr< n >, AMAIR_ELx.Attr< n >, and AMAIR2_ELx.Attr< n > are permitted to be cached in a TLB.                                                        |
| I QNNGV   | For some translation regimes, the memory region attributes determined from translation tables, MAIR_ELx, and MAIR2_ELx values might be overridden by the configuration of SCTLR_ELx.{C, I} and HCR_EL2.DC.             |
| R MJGNV   | For stage 1 of a translation regime using VMSAv8-64, if AIE is enabled, then hierarchical permissions are disabled and                                                                                                 |

## D8.6.2 Stage 1 Shareability attributes

RZWYSH

For Normal Cacheable memory, if the Effective value of TCR\_ELx.DS is 0, then the SH[1:0] field in a stage 1 translation Block descriptor and Page descriptor encodes the Shareability attributes of the descriptor OA, as shown in the following table:

|   SH[1:0] | Normal memory                                                                                                                            |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------|
|        00 | Non-shareable                                                                                                                            |
|        01 | Reserved, CONSTRAINED UNPREDICTABLE as described in Reserved values in System and memory-mapped registers and translation table entries. |
|        10 | Outer Shareable                                                                                                                          |
|        11 | Inner Shareable                                                                                                                          |

RPYFVQ

If a region is mapped as Device memory or Normal Non-cacheable memory after all enabled translation stages, then the region has an effective Shareability attribute of Outer Shareable.

RNSCNC

If stage 2 translation is enabled and stage 1 maps a region as Device memory or Normal Non-cacheable memory, then it is IMPLEMENTATION DEFINED whether:

- The Shareability attribute configured for stage 1 is input into stage 2 translation.
- An effective Outer Shareable attribute is input into stage 2 translation.

IHRNGF If the Effective value of TCR\_ELx.DS is 1, then the stage 1 translation descriptor bits[9:8] are OA[51:50] instead of SH[1:0].

IGJPJW For Normal Cacheable memory, if the Effective value of TCR\_ELx.DS is 1, then the stage 1 translation Shareability is treated as being mapped by one of the following:

- For the EL3 translation regime, TCR\_EL3.SH0.
- For the EL2 translation regime, if the Effective value of HCR\_EL2.E2H is 0, then TCR\_EL2.SH0.
- For the EL2 and EL2&amp;0 translation regimes, if the Effective value of HCR\_EL2.E2H is 1 and the V A is an address that is translated using tables pointed to by TTBR0\_EL2, then TCR\_EL2.SH0.
- For the EL2 and EL2&amp;0 translation regimes, if the Effective value of HCR\_EL2.E2H is 1 and the V A is an address that is translated using tables pointed to by TTBR1\_EL2, then TCR\_EL2.SH1.
- For the EL1&amp;0 translation regime, if the V A is an address that is translated using tables pointed to by TTBR0\_EL1, then TCR\_EL1.SH0.
- For the EL1&amp;0 translation regime, if the V A is an address that is translated using tables pointed to by TTBR1\_EL1, then TCR\_EL1.SH1.

## D8.6.3 Stage 2 memory type and Cacheability attributes

RWYQVN

RKTSYP

IBBJDH

For any stage 2 translation, if the final memory type any is Normal Cacheable type, then all of the following apply:

- If the output of stage 1 specifies a Cacheable memory type, then the final cache allocation hints are the stage 1 cache allocation hints.
- If the output of stage 1 does not specify a Cacheable memory type, then the final cache allocation hints are Read Allocate, Write Allocate.
- Stage 2 translation configuration does not assign cache allocation hints.

If the memory type from a stage 2 translation causes a stage 1 translation table walk to a Device memory type, then one of the following occurs:

- If HCR\_EL2.PTW is 0, then the translation table walk occurs as if it is to Normal Non-cacheable memory, and the walk can be done speculatively.
- If HCR\_EL2.PTW is 1, then the memory access generates a stage 2 Permission fault.

## D8.6.4 Stage 2 Memory Tagging attributes

RKVBTQ

All statements in this section and subsections require implementation of FEAT\_MTE\_PERM.

IHKMRJ

IFWGDY

RXSYYN

IFYRCG

RYMSKV

If the stage 1 Tagged attribute is not defined for a memory region then the NoTagAccess attribute is not defined.

The NoTagAccess attribute is a permission and has no effect on the cacheability of Allocation Tags.

If all of the following are true, then a stage 2 Permission fault due to the NoTagAccess attribute is generated on a memory access:

- The access is an explicit Allocation Tag read, explicit Allocation Tag write or a Tag Checked access.
- The memory region tagging type for the access is Tagged. See Memory region tagging types.
- The combined stage 1 and stage 2 memory attributes specify the NoTagAccess attribute.

APermission fault due to the NoTagAccess attribute is not generated for a Tag Unchecked memory access.

On a stage 2 Permission fault due to the NoTagAccess attribute, all of the following are true:

- The fault is taken to EL2.
- The fault is reported as a Data Abort from a lower Exception level.
- ESR\_EL2.TagAccess is 1.
- The value of ESR\_EL2.WnR is set to one of the following:
- -If the fault is due to a Tag write effect, then 1.
- -If the fault is due to a Tag read effect, then 0.
- FAR\_EL2 is valid.

RPYQZB

For the purpose of determining whether a Permission fault due to the NoTagAccess attribute is generated for a Tag Checked access, if a Tag Check Fault is configured to have no effect on the PE due to SCTLR\_ELx.{TCF, TCF0}, then the access is treated as Tag Unchecked.

IXRKQK

For more information about the prioritization of a Permission fault due to the NoTagAccess attribute, see Prioritization of Permission faults.

## D8.6.5 Stage 2 memory type and Cacheability attributes when FWB is disabled

| R MFDHF   | All statements in this section and subsections require that the Effective value of HCR_EL2.FWB is 0.                                                                                                                      |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R QPHXK   | If the Effective value of HCR_EL2.FWB is 0, then the stage 1 and stage 2 memory type and Cacheability attributes are combined.                                                                                            |
| R HMNDG   | For stage 2 translations, the MemAttr[3:0] field in a Block descriptor and Page descriptor encodes the memory type and Cacheability of the memory region addressed by the descriptor OA, as shown in the following table: |

## Table D8-96 Stage 2 MemAttr[3:0] encoding

| MemAttr[3:0]   | Memory type        | Cacheability                                          | Condition                        |
|----------------|--------------------|-------------------------------------------------------|----------------------------------|
| 0000           | Device-nGnRnE      | Not applicable                                        | -                                |
| 0001           | Device-nGnRE       | Not applicable                                        | -                                |
| 0010           | Device-nGRE        | Not applicable                                        | -                                |
| 0011           | Device-GRE         | Not applicable                                        | -                                |
| 0100           | Normal NoTagAccess | Outer Write-Back Cacheable Inner Write-Back Cacheable | FEAT_MTE_PERM is implemented     |
|                | Reserved           | Reserved, CONSTRAINED UNPREDICTABLE                   | FEAT_MTE_PERM is not implemented |
| 0101           | Normal             | Outer Non-cacheable Inner Non-cacheable               | -                                |

|   MemAttr[3:0] | Memory type   | Cacheability                                                | Condition   |
|----------------|---------------|-------------------------------------------------------------|-------------|
|           0110 | Normal        | Outer Non-cacheable Inner Write-Through Cacheable           | -           |
|           0111 | Normal        | Outer Non-cacheable Inner Write-Back Cacheable              | -           |
|           1000 | Reserved      | Reserved, CONSTRAINED UNPREDICTABLE                         | -           |
|           1001 | Normal        | Outer Write-Through Cacheable Inner Non-cacheable           | -           |
|           1010 | Normal        | Outer Write-Through Cacheable Inner Write-Through Cacheable | -           |
|           1011 | Normal        | Outer Write-Through Cacheable Inner Write-Back Cacheable    | -           |
|           1100 | Normal        | Reserved, CONSTRAINED UNPREDICTABLE                         | -           |
|           1101 | Normal        | Outer Write-Back Cacheable Inner Non-cacheable              | -           |
|           1110 | Normal        | Outer Write-Back Cacheable Inner Write-Through Cacheable    | -           |
|           1111 | Normal        | Outer Write-Back Cacheable Inner Write-Back Cacheable       | -           |

## ILJCRP For more information, see:

- Reserved values in System and memory-mapped registers and translation table entries.
- Combining stage 1 and stage 2 memory type attributes.

## D8.6.5.1 Combining stage 1 and stage 2 memory type attributes

If the Effective value of HCR\_EL2.FWB is 0, then the stage 1 and stage 2 memory type attributes are combined as shown in the following table:

## Table D8-97 Combining stage 1 and stage 2 memory type attributes

| Rule                                                                   | If either translation stage assigns:   | Resultant memory type is:     |
|------------------------------------------------------------------------|----------------------------------------|-------------------------------|
| Device has precedence over Normal                                      | Any Device memory type                 | Any Device memory type        |
| Non-Gathering has precedence over Gathering                            | ADevice-nGxx memory type               | ADevice-nGxx memory type      |
| Non-Reordering has precedence over Reordering                          | ADevice-nGnRx memory type              | ADevice-nGnRx memory type     |
| No Early write acknowledge has precedence over Early write acknowledge | The Device-nGnRnE memory type          | The Device-nGnRnE memory type |

## D8.6.5.2 Combining stage 1 and stage 2 Cacheability attributes for Normal memory

If the Effective value of HCR\_EL2.FWB is 0, then the stage 1 and stage 2 Inner Cacheability and Outer Cacheability attributes are combined as shown in the following table:

RTNHFM

RGQFSF

Table D8-98 Combining stage 1 and stage 2 Cacheability attributes for Normal memory

| Assignment in stage 1   | Assignment in stage 2   | Resultant Cacheability   |
|-------------------------|-------------------------|--------------------------|
| Non-cacheable           | Any                     | Non-cacheable            |
| Any                     | Non-cacheable           | Non-cacheable            |
| Write-Through Cacheable | Write-Through Cacheable | Write-Through Cacheable  |
| Write-Through Cacheable | Write-Back Cacheable    | Write-Through Cacheable  |
| Write-Back Cacheable    | Write-Through Cacheable | Write-Through Cacheable  |
| Write-Back Cacheable    | Write-Back Cacheable    | Write-Back Cacheable     |

IMCQKW

For stage 2 translations, if the Effective value of HCR\_EL2.FWB is 0 and the stage 2 MemAttr[3:0] field is 0b1111 , then the combined memory type and Cacheability attributes are the output memory type and Cacheability attributes from stage 1.

RJSXRX

If FEAT\_MTE\_PERM is implemented, the stage 2 NoTagAccess attribute is determined by the following:

- If the stage 1 memory type is not Tagged, the stage 2 NoTagAccess attribute is ignored.
- If the stage 1 memory type is Tagged, the stage 1 and stage 2 attributes are combined as shown in Table D8-99:

Table D8-99 Combined stage 1 and stage 2 attributes if FEAT\_MTE\_PERM is implemented

| Stage 1 memory type and Cacheability attribute   | Stage 2 memory type and Cacheability attribute   | Resultant memory type and Cacheability attribute   |
|--------------------------------------------------|--------------------------------------------------|----------------------------------------------------|
| Normal Write-Back, Tagged                        | Normal Write-Back                                | Normal Write-Back, Tagged                          |
| Normal Write-Back, Tagged                        | Normal Write-back, NoTagAccess                   | Normal Write-back, Tagged, NoTagAccess             |

## D8.6.6 Stage 2 memory type and Cacheability attributes when FWB is enabled

RLNQJQ

All statements in this section and subsections require that the Effective value of HCR\_EL2.FWB is 1.

RZNGNK

RNQDNZ

RJXGKQ

RVRJSW

For stage 2 translations, if FEAT\_MTE\_PERM is not implemented, then FEAT\_S2FWB has all of the following effects on the MemAttr[3:2] bits:

- MemAttr[3] is RES0.
- The value of MemAttr[2] determines the interpretation of the MemAttr[1:0] bits.

For stage 2 translations, if FEAT\_MTE\_PERM is implemented, then MemAttr[3] is not RES0 and all bits of MemAttr[3:0] determine the memory region type and Cacheability attributes.

For stage 2 translations, if FEAT\_MTE\_PERM is implemented, then all of the following values of MemAttr[3:2] apply:

- 0b10 is Reserved.
- All other values determine the interpretation of the MemAttr[1:0] bits.

For stage 2 translations, if MemAttr[2] is 0, or if FEAT\_MTE\_PERM is implemented and MemAttr[3:2] is 0b00 , then the MemAttr[1:0] bits define Device memory attributes as shown in the following table:

## Table D8-100 Stage 2 MemAttr[1:0] encoding when MemAttr[2] is 0, FWB enabled

|   Stage 2 MemAttr[1:0] | Device Memory Attribute   |
|------------------------|---------------------------|
|                     00 | Device-nGnRnE             |
|                     01 | Device-nGnRE              |
|                     10 | Device-nGRE               |
|                     11 | Device-GRE                |

RRHWZM

For stage 2 translations, the MemAttr[1:0] bits affect the memory type and Cacheability as shown in the following table:

Table D8-101 Stage 2 MemAttr[1:0] encoding, FWB enabled

| Stage 2 MemAttr[3:2]   | Stage 1 memory type and Cacheability attribute   | Stage 2 MemAttr[1:0]   | Resultant memory type and Cacheability attribute   |
|------------------------|--------------------------------------------------|------------------------|----------------------------------------------------|
| 01                     | Device<attr>                                     | 01                     | Device<attr>                                       |
| 01                     | Normal Non-cacheable                             | 01                     | Normal Non-cacheable                               |
| 01                     | Normal Write-Through                             | 01                     | Normal Non-cacheable                               |
| 01                     | Normal Write-Back                                | 01                     | Normal Non-cacheable                               |
| 01                     | Normal Write-Back, Tagged                        | 01                     | Normal Non-cacheable                               |
| 01                     | Normal Write-Back, Tagged                        | 1x                     | Normal Write-Back, Tagged                          |
| 11                     | -                                                | 01                     | Reserved                                           |
| 11                     | Normal Write-Back, Tagged                        | 1x                     | Normal Write-Back, Tagged, NoTagAccess             |
| x1                     | -                                                | 00                     | Reserved                                           |
| x1                     | Device<attr>                                     | 10                     | Normal Write-Back                                  |
| x1                     | Normal Non-cacheable                             | 10                     | Normal Write-Back                                  |
| x1                     | Normal Write-Through                             | 10                     | Normal Write-Back                                  |
| x1                     | Device<attr>                                     | 11                     | Device<attr>                                       |
| x1                     | Normal Non-cacheable                             | 11                     | Normal Non-cacheable                               |
| x1                     | Normal Write-Through                             | 11                     | Normal Write-Through                               |
| x1                     | Normal Write-Back                                | 1x                     | Normal Write-Back                                  |

RGSDKZ If MemAttr[1:0] bits define Device memory attributes, then stage 2 Device memory attributes are combined with stage 1 memory attributes.

RTHYXB If the stage 1 translation specifies a cacheable memory type, then the stage 1 cache allocation hint is applied to the final cache allocation hint where the final memory type is cacheable.

- RTBQKG If the stage 1 translation does not specify a cacheable memory type, then if the final memory type is cacheable, it is treated as Read-Allocate, Write-Allocate, Non-Transient.

RRMTWN If the stage 1 translation specifies a Device memory type, and the stage 2 descriptor MemAttr[2:0] field is 0b110 , then all of the following apply:

- If an atomic memory access occurs, then it is IMPLEMENTATION DEFINED whether it is supported in the same way as accesses to memory locations with a resultant Device memory type.
- If an exclusive access occurs, then it is IMPLEMENTATION DEFINED whether it is supported in the same way as accesses to memory locations with a resultant Device memory type.

- If a misaligned access occurs, then it is CONSTRAINED UNPREDICTABLE whether the resultant stage 1 memory type generates a stage 1 Alignment fault.
- For a DC ZVA , DC GZVA , or DC GVA instruction, it is CONSTRAINED UNPREDICTABLE whether the resultant stage 1 memory type generates a stage 1 Alignment fault.
- If the translation applies to any Active element of an SVE Non-fault vector load instruction, or to an Active element that is not the First active element of an SVE First-fault vector load instruction, then it is CONSTRAINED UNPREDICTABLE whether the element access is performed, or is suppressed and reported in the FFR.

IRRDBK The architecture requires that CLIDR\_EL1.{LoUU, LoIUS} are {0, 0} so that no data cache levels need to be cleaned to manage coherency with instruction fetches.

RDPDXS

ILJRWR

If the stage 1 translation specifies a Normal memory type with Cacheability other than Write-Back Cacheable, and the stage 2 descriptor MemAttr[2:0] field is 0b110 , then it is CONSTRAINED UNPREDICTABLE whether accesses generated by the following instruction types follow the alignment requirements in the same way as accesses to a Normal memory type with Cacheability other than Write-Back Cacheable:

- Load-Exclusive, Store-Exclusive and Atomic instructions.
- Non-atomic Load-Acquire/Store-Release instructions.

For more information, see:

- XS attribute modifier.
- Reserved values in System and memory-mapped registers and translation table entries.
- Alignment of data accesses.

## D8.6.7 Stage 2 Shareability attributes

ICGGBV

The stage 2 Shareability attributes are not affected by the Effective value of HCR\_EL2.FWB.

RDNZJQ

For Normal Cacheable memory, if the Effective value of VTCR\_EL2.DS is 0, then the SH[1:0] field in a stage 2 translation Block descriptor and Page descriptor encodes the Shareability attributes of the descriptor OA, as shown in the following table:

## Table D8-102 Stage 2 Shareability attributes

|   SH[1:0] | Normal memory                       |
|-----------|-------------------------------------|
|        00 | Non-shareable                       |
|        01 | Reserved, CONSTRAINED UNPREDICTABLE |
|        10 | Outer Shareable                     |
|        11 | Inner Shareable                     |

| R HTSGQ   | For Normal Cacheable memory, if the Effective value of VTCR_EL2.DS is 1, then the stage 2 translation Shareability is determined by VTCR_EL2.SH0.      |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| R YHCTP   | For Device memory and Normal Non-cacheable memory, the Shareability attributes of the stage 2 translation descriptor OAare treated as Outer Shareable. |
| I LPRLS   | If the Effective value of VTCR_EL2.DS is 1, then the stage 2 translation descriptor bits[9:8] are OA[51:50] instead of SH[1:0].                        |
| I DPSTX   | For more information, see Reserved values in System and memory-mapped registers and translation table entries.                                         |

ILTFXF

RWLQYW

RZNLRJ

## D8.6.7.1 Combining the stage 1 and stage 2 Shareability attributes for Normal memory

The value of HCR\_EL2.FWB does not affect how Shareability attributes from stage 1 and stage 2 are combined.

If the resultant memory type from a stage 1 and stage 2 translation is one of the following, the memory region is treated as Outer Shareable:

- Any Device memory type.
- Normal Inner Non-cacheable, Outer Non-cacheable.

For a memory region with a resultant memory type of Normal that is not Inner Non-cacheable, Outer Non-cacheable, the stage 1 and stage 2 Shareability attributes can be combined as shown in the following table:

## Table D8-103 Combining stage 1 and stage 2 Shareability attributes

| Assignment in stage 1   | Assignment in stage 2   | Resultant Shareability   |
|-------------------------|-------------------------|--------------------------|
| Outer Shareable         | Any                     | Outer Shareable          |
| Inner Shareable         | Outer Shareable         | Outer Shareable          |
| Inner Shareable         | Inner Shareable         | Inner Shareable          |
| Inner Shareable         | Non-shareable           | Inner Shareable          |
| Non-shareable           | Outer Shareable         | Outer Shareable          |
| Non-shareable           | Inner Shareable         | Inner Shareable          |
| Non-shareable           | Non-shareable           | Non-shareable            |