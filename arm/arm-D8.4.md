## D8.4 Memory access control

ISHRMH

RMNKWG

RXRLBM

RSHZSG

Fields in the descriptors, PSTATE, and system registers determine the permissions used to control access to memory and instruction execution.

Direct permissions use one or more of the following to determine the base permissions that control whether or not a location can be accessed, the type of access that is permitted, and the privilege level necessary to access the location:

- The access permissions in Block descriptors and Page descriptors.
- If enabled, then the hierarchical access permissions in Table descriptors.

Indirect permissions use all of the following to determine the base permissions that control whether or not a location can be accessed, the type of access that is permitted, and the privilege level necessary to access the location:

- The Permission Indirection Index (PIIndex) field in Block descriptors and Page descriptors.
- For each translation regime, a Permission Indirection Register (PIR) indexed by PIIndex.

If enabled, Overlay permissions use all of the following to further restrict permissions from what is configured for the base permissions:

- The Permission Overlay Index (POIndex) field in Block descriptors and Page descriptors.
- For each Exception level, a Permission Overlay Register (POR) indexed by POIndex.

Note

Overlay permissions allow permissions to be progressively restricted by processes running at EL0 while reducing the number of calls to supervisory software at more privileged Exception levels, and without the cost of TLB maintenance.

## D8.4.1 Stage 1 permissions

| R TDNYB   | All statements in this section apply when stage 1 uses VMSAv8-64 or VMSAv9-128.                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R WBLJK   | The following table lists the stage 1 permissions and the access type that is permitted when that permission is present. If the stage 1 permission is not present, that access type is not permitted. |

## Table D8-61 Stage 1 permissions

| Stage 1 permission   | Access type permitted                                                                   |
|----------------------|-----------------------------------------------------------------------------------------|
| UnprivRead           | Unprivileged data read in the EL1&0 and EL2&0 translation regimes.                      |
| UnprivWrite          | Unprivileged data write in the EL1&0 and EL2&0 translation regimes.                     |
| PrivRead             | Privileged data read in the EL1&0, EL2&0, EL2, and EL3 translation regimes.             |
| PrivWrite            | Privileged data write in the EL1&0, EL2&0, EL2, and EL3 translation regimes.            |
| UnprivGCS            | Unprivileged GCS access in the EL1&0 and EL2&0 translation regimes.                     |
| PrivGCS              | Privileged GCS access in the EL1&0, EL2&0, EL2, and EL3 translation regimes.            |
| UnprivExecute        | Unprivileged instruction execution in the EL1&0 and EL2&0 translation regimes.          |
| PrivExecute          | Privileged instruction execution in the EL1&0, EL2&0, EL2, and EL3 translation regimes. |

IXFDFY

All of the following controls can ensure that memory locations are not both writable and executable:

- For privileged accesses in all translation regimes, PrivWXN.

- For unprivileged accesses in the EL1&amp;0 and EL2&amp;0 translation regimes, UnprivWXN.

IKWYWX

UnprivRead, UnprivWrite, UnprivGCS, UnprivExecute, and UnprivWXN do not apply to the EL2 and EL3 translation regimes.

RVBBBJ

If stage 1 translation is disabled, then stage 1 permits all data accesses, instruction executions, and GCS accesses.

IMTSDS

If stage 1 translation is enabled, then stage 1 permissions are determined by all of the following:

- Stage 1 Base permissions. For more information, see Stage 1 Base permissions.

- Stage 1 Overlay permissions. For more information, see Stage 1 Overlay permissions.

## D8.4.1.1 Stage 1 Base permissions

IPJNLQ

Stage 1 Base permissions can be determined by one of the following:

- Stage 1 Direct permissions. For more information, see Stage 1 Direct permissions.

- Stage 1 Indirect permissions. For more information, see Stage 1 Indirect permissions.

ISXTJD

If FEAT\_S1PIE is not implemented, then stage 1 Direct permissions are used.

IVYHZC

If stage 1 translation uses VMSAv8-64, then the choice between Direct and Indirect permissions is determined by one of the following:

- If the Exception level is not EL3, then TCR2\_ELx.PIE.

- If the Exception level is EL3, then TCR\_EL3.PIE.

IBSXJT

Stage 1 Direct permissions are not supported by VMSAv9-128. If stage 1 translation uses VMSAv9-128, then it uses Indirect permissions and the Effective value of the PIE field is 1.

## D8.4.1.2 Stage 1 Direct permissions

## D8.4.1.2.1 Stage 1 data accesses using Direct permissions

RCBNKR

For a stage 1 translation that supports one Exception level, the following table shows the possible data access

permissions.

## Table D8-62 Data access permissions for a stage 1 translation supporting one Exception level

|   AP[2] | Permissions         |
|---------|---------------------|
|       0 | PrivRead, PrivWrite |
|       1 | PrivRead            |

RMGGZM

For a stage 1 translation that supports one Exception level, AP[1] is RES1.

RRNGJG

For a stage 1 translation that supports two Exception levels, the following table shows the possible data access permissions at EL0 and the corresponding higher Exception level.

## Table D8-63 Data access permissions for a stage 1 translation supporting two Exception levels

|   AP[2:1] | Permissions                                  |
|-----------|----------------------------------------------|
|        00 | PrivRead, PrivWrite                          |
|        01 | PrivRead, PrivWrite, UnprivRead, UnprivWrite |
|        10 | PrivRead                                     |
|        11 | PrivRead, UnprivRead                         |

RPSZJJ

If stage 1 is enabled and stage 1 Base permissions use Direct permissions, then GCS access is not permitted and UnprivGCS and PrivGCS are not present.

IZRMQJ

For the EL1&amp;0 translation regime in the current Security state, if the Effective value of HCR\_EL2.{NV , NV1} is {1, 1},

then AP[1] is treated as 0 regardless of the actual value.

For more information, see Additional behavior when HCR\_EL2.NV is 1 and HCR\_EL2.NV1 is 1.

| I BVWWD   | If hardware management of dirty state is enabled at stage 1, then the AP[2] bit can be cleared by hardware in some situations. For more information, see Hardware management of the dirty state.                                                                                                |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I VZXYY   | Translation table entries at a given lookup level can limit data access Direct permissions at subsequent lookup levels.                                                                                                                                                                         |
| I VWPGP   | For a translation regime, if Overlay permissions are enabled, then hierarchical data access Direct permissions are disabled. See Stage 1 Overlay permissions.                                                                                                                                   |
| R YTXKB   | For a stage 1 translation, when hierarchical control is enabled, the Table descriptor APTable[1:0] field limits the data access permissions of subsequent stage 1 translation lookup levels, regardless of the Direct permissions in subsequent lookup levels, as shown in the following table: |

## Table D8-64 Effect of APTable[1:0] on subsequent lookup levels

|   APTable[1:0] | Effect at subsequent lookup levels              |
|----------------|-------------------------------------------------|
|             00 | No effect on data access permissions.           |
|             01 | Removes UnprivRead and UnprivWrite.             |
|             10 | Removes UnprivWrite and PrivWrite.              |
|             11 | Removes UnprivRead, UnprivWrite, and PrivWrite. |

- IGQYCH For a Permission fault, the level of the Block descriptor or Page descriptor is reported regardless of whether the lack of permissions was caused by configuration of the APTable or AP fields.
- IPCLHM For translation regimes that support one Exception level, APTable[0] is RES0.
- ITPCPS The APTable[1:0] settings are combined with the descriptor access permissions in subsequent lookup levels. They do not change the values entered in those descriptors, nor restrict what values can be entered.
- IPKGJC For the translation regime controlled by a TCR\_ELx, one or more of the following can be used to disable the Table descriptor APTable[1:0] field so that it is IGNORED by the PE and the behavior is as if the value is 0:
- If the Effective value of TCR\_ELx.HPD{0} is 1, hierarchical data access permission is disabled in the translation tables pointed to by TTBR0\_ELx.
- If the Effective value of TCR\_ELx.HPD1 is 1, hierarchical data access permission is disabled in the translation tables pointed to by TTBR1\_ELx.
- IYQWJF The descriptor APTable field affects all subsequent lookup levels. When an APTable field is changed, software is required to use a break-before-make sequence, including TLB maintenance for all lookup levels for the V A range translated by the descriptor.

## D8.4.1.2.3 Stage 1 instruction execution using Direct permissions

- IDXKST The instruction Execute-never, Unprivileged execute-never, and Privileged execute-never fields in a Block descriptor and Page descriptor are used to control instruction execution permissions under the Direct permissions scheme by a stage 1 translation.
- RTRZVM For a stage 1 translation that supports one Exception level, the XN field in the Block descriptor and Page descriptor has all of the following properties:
- If the Effective value of XN is 0, then PrivExecute is not removed by this bit.
- If the Effective value of XN is 1, then PrivExecute is removed.

For a stage 1 translation that supports two Exception levels, the UXN field in the Block descriptor and Page descriptor has all of the following properties:

- If the Effective value of UXN is 0, then UnprivExecute is not removed by this bit.

RRBDFT

- If the Effective value of UXN is 1, then UnprivExecute is removed.

| R LWPVL   | For a stage 1 translation that supports two Exception levels, the PXNfield in the Block descriptor and Page descriptor has all of the following properties: • If the Effective value of PXNis 0, then PrivExecute is not removed by this bit. • If the Effective value of PXNis 1, then PrivExecute is removed.                                                                                                                                                                                                                         |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R VWLLR   | For stage 1 translations that support two Exception levels, if UnprivWrite is present, then PrivExecute is removed.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| I KDRYB   | There are register control fields that can be used to force writable memory to be treated as XN, PXN, or UXN, regardless of the value of the corresponding descriptor fields.                                                                                                                                                                                                                                                                                                                                                           |
| R FYMXJ   | For unprivileged accesses in the EL1&0 and EL2&0 translation regimes, if SCTLR_ELx.WXN is 1, UnprivWrite is present, and UnprivExecute is present, then UnprivWXN is applied. Otherwise, UnprivWXN is removed.                                                                                                                                                                                                                                                                                                                          |
| R SYMMB   | For privileged accesses in all translation regimes, if SCTLR_ELx.WXN is 1, PrivWrite is present, and PrivExecute is present, then PrivWXN is applied. Otherwise, PrivWXN is removed.                                                                                                                                                                                                                                                                                                                                                    |
| I TBVCH   | For a stage 1 translation in a translation regime that supports two Exception levels, the corresponding SCTLR_ELx.WXN field does all of the following:                                                                                                                                                                                                                                                                                                                                                                                  |
| I FQVWM   | For a stage 1 translation in a translation regime that applies to a single Exception level, the corresponding SCTLR_ELx.WXN field does all of the following: • If the value is 0, then there is no effect on access permissions. • If the value is 1 and if the memory region is PrivWrite, then PrivExecute is removed, regardless of the value of                                                                                                                                                                                     |
|           | the Block descriptor or Page descriptor XNfield. The SCTLR_ELx.WXN field reduces the memory footprint available for code injection attacks by introducing an invariant that writable memory regions are not executable.                                                                                                                                                                                                                                                                                                                 |
| I XLDPQ   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|           | operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| I PNSFD   | SCTLR_ELx.WXN is permitted to be cached in a TLB.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| I JCPHF   | Stage 1 translation table entries at a given lookup level can limit instruction execution controls expressed using Direct permissions at subsequent lookup levels.                                                                                                                                                                                                                                                                                                                                                                      |
| I XMMSD   | For a translation regime, if Overlay permissions are enabled, then hierarchical instruction execution controls expressed using Direct permissions are disabled. See Stage 1 Overlay permissions.                                                                                                                                                                                                                                                                                                                                        |
| R RLQFP   | For a stage 1 translation, the value of the XNTable Table descriptor field has one of the following effects: • If the Effective value of the XNTable field is 0, then the field has no effect. • If the Effective value of the XNTable field is 1, then all of the following apply: - The XNfield in Block descriptors and Page descriptors is treated as 1 in subsequent lookup levels, regardless of the actual value of XN. - The value and interpretation of the XNTable and XNfields in all subsequent lookup levels are otherwise |

RNJJNG

- IZGSNV
- If the Effective value of the UXNTable field is 0, then the field has no effect.
- If the Effective value of the UXNTable field is 1, then all of the following apply:
- -The UXN field in Block descriptors and Page descriptors is treated as 1 in subsequent lookup levels, regardless of the actual value of UXN.
- -The value and interpretation of the UXNTable and UXN fields in all subsequent lookup levels are otherwise unaffected.

For a stage 1 translation, the value of the PXNTable Table descriptor field has one of the following effects:

- If the Effective value of the PXNTable field is 0, then the field has no effect.
- If the Effective value of the PXNTable field is 1, then all of the following apply:
- -The PXN field in Block descriptors and Page descriptors is treated as 1 in subsequent lookup levels, regardless of the actual value of PXN.
- -The value and interpretation of the PXNTable and PXN fields all subsequent lookup levels are otherwise unaffected.

ISRRJF The UXNTable, XNTable, and PXNTable Table descriptor fields control stage 1 translations. The corresponding bit positions are RES0 in the stage 2 Table descriptors.

INYWHQ For the translation regime controlled by a TCR\_ELx, one or more of the following can be used to disable the Table descriptor XNTable, UXNTable, and PXNTable fields so they are IGNORED by the PE and the system behavior is as if the values are zero:

- If the Effective value of TCR\_ELx.HPD{0} is 1, then hierarchical instruction execution permission is disabled in the translation tables pointed to by TTBR0\_ELx.
- If the Effective value of TCR\_ELx.HPD1 is 1, then hierarchical instruction execution permission is disabled in the translation tables pointed to by TTBR1\_ELx.

The Table descriptor UXNTable, XNTable, and PXNTable fields affect all subsequent lookup levels, including stage 1 translation output. When a UXNTable, XNTable, or PXNTable field is changed, software is required to use a break-before-make sequence, including TLB maintenance for all lookup levels for the V A range translated by the descriptor.

## D8.4.1.2.6 Summary of Direct permissions for stage 1 translations

- IWXKKQ If a translation regime applies to EL0 and a higher Exception level, then the following table shows the possible stage 1

memory access permissions, using all of the following notations:

- PXNand UXN are the Effective values of PXN and UXN after the effects of PXNTable and UXNTable, respectively.
- AP[2:1] is the Effective value of AP[2:1] after the effects of APTable are applied.
- If hardware update of dirty state is enabled, then AP[2] is considered to be 0 for the purposes of computing execute permission in some situations.
- WXNis in the SCTLR\_ELx register at the higher Exception level to which the translation regime applies.

## Table D8-65 Summary of possible memory access permissions using Direct permissions for a stage 1 translation supporting two Exception levels

|   UXN |   PXN |   AP[2:1] | WXN   | Permission                                                  |
|-------|-------|-----------|-------|-------------------------------------------------------------|
|     0 |     0 |        00 | 0     | PrivRead, PrivWrite, PrivExecute, UnprivExecute             |
|     0 |     0 |        00 | 1     | PrivRead, PrivWrite, PrivWXN, UnprivExecute                 |
|     0 |     0 |        01 | 0     | PrivRead, PrivWrite, UnprivRead, UnprivWrite, UnprivExecute |
|     0 |     0 |        01 | 1     | PrivRead, PrivWrite, UnprivRead, UnprivWrite, UnprivWXN     |
|     0 |     0 |        10 | x     | PrivRead, PrivExecute, UnprivExecute                        |
|     0 |     0 |        11 | x     | PrivRead, PrivExecute, UnprivRead, UnprivExecute            |
|     0 |     1 |        00 | x     | PrivRead, PrivWrite, UnprivExecute                          |

|   UXN |   PXN |   AP[2:1] | WXN   | Permission                                                  |
|-------|-------|-----------|-------|-------------------------------------------------------------|
|     0 |     1 |        01 | 0     | PrivRead, PrivWrite, UnprivRead, UnprivWrite, UnprivExecute |
|     0 |     1 |        01 | 1     | PrivRead, PrivWrite, UnprivRead, UnprivWrite, UnprivWXN     |
|     0 |     1 |        10 | x     | PrivRead, UnprivExecute                                     |
|     0 |     1 |        11 | x     | PrivRead, UnprivRead, UnprivExecute                         |
|     1 |     0 |        00 | 0     | PrivRead, PrivWrite, PrivExecute                            |
|     1 |     0 |        00 | 1     | PrivRead, PrivWrite, PrivWXN                                |
|     1 |     0 |        01 | x     | PrivRead, PrivWrite, UnprivRead, UnprivWrite                |
|     1 |     0 |        10 | x     | PrivRead, PrivExecute                                       |
|     1 |     0 |        11 | x     | PrivRead, PrivExecute, UnprivRead                           |
|     1 |     1 |        00 | x     | PrivRead, PrivWrite                                         |
|     1 |     1 |        01 | x     | PrivRead, PrivWrite, UnprivRead, UnprivWrite                |
|     1 |     1 |        10 | x     | PrivRead                                                    |
|     1 |     1 |        11 | x     | PrivRead, UnprivRead                                        |

ILJHZZ

For a memory location, if a translation regime applies to a single Exception level, then the following table shows the stage 1 access Direct permissions, using all of the following notations:

- WXNis in the SCTLR\_ELx register at the higher Exception level to which the translation regime applies.
- AP[2] is the effective value of AP[2] after the effects of APTable are applied.
- If hardware update of dirty state is enabled, then AP[2] is considered to be 0 for the purposes of computing execute permission in some situations.

## Table D8-66 Summary of possible memory access permissions using Direct permissions for a stage 1 translation supporting one Exception level

|   XN |   AP[2] | WXN   | Access permission                |
|------|---------|-------|----------------------------------|
|    0 |       0 | 0     | PrivRead, PrivWrite, PrivExecute |
|    0 |       0 | 1     | PrivRead, PrivWrite, PrivWXN     |
|    0 |       1 | x     | PrivRead, PrivExecute            |
|    1 |       0 | x     | PrivRead, PrivWrite              |
|    1 |       1 | x     | PrivRead                         |

IJZPHK

For more information, see Implications of enabling the dirty state management mechanism.

## D8.4.1.3 Stage 1 Indirect permissions

RJJWXH

All statements in this section require implementation of FEAT\_S1PIE.

ILYWDV

For the EL1&amp;0 and EL2&amp;0 translation regimes, the following Permission Indirection Registers determine unprivileged stage 1 Base permissions, S1UnprivBasePerm :

- PIRE0\_EL1.

- PIRE0\_EL2.

RDJZHM

For all purposes other than a direct read of the register, if the Effective value of HCR\_EL2.{NV , NV1} is {1, 1}, then the value of PIRE0\_EL1 is treated as 0.

IBSMJB

For all translation regimes, the following Permission Indirection Registers determine privileged stage 1 Base permissions, S1PrivBasePerm :

RBCPGD

- PIR\_EL1.
- PIR\_EL2.
- PIR\_EL3.

The following table shows how the 4-bit PIIndex field in stage 1 Block descriptors and Page descriptors is used to index into the Permission Indirection Registers to obtain S1UnprivBasePerm and S1PrivBasePerm:

Table D8-67 Using PIIndex to determine stage 1 Base permissions

| Translation regime   | S1UnprivBasePerm                      | S1PrivBasePerm                      |
|----------------------|---------------------------------------|-------------------------------------|
| EL1&0                | PIRE0_EL1[(PIIndex*4 + 3): PIIndex*4] | PIR_EL1[(PIIndex*4 + 3): PIIndex*4] |
| EL2&0                | PIRE0_EL2[(PIIndex*4 + 3): PIIndex*4] | PIR_EL2[(PIIndex*4 + 3): PIIndex*4] |
| EL2                  |                                       | PIR_EL2[(PIIndex*4 + 3): PIIndex*4] |
| EL3                  |                                       | PIR_EL3[(PIIndex*4 + 3): PIIndex*4] |

IMYXBN

RLLZDZ

Stage 1 Base permissions are computed using the following steps:

1. Stage 1 Base permissions are decoded from the PIR\_ELx register.
2. If PrivExecute or PrivGCS is present, and UnprivWrite or UnprivGCS is additionally present, then all Base permissions are removed. See RVFPJF.
3. For the translation, if an inappropriate OA space is selected, then each of PrivExecute, UnprivExecute, PrivGCS, UnprivGCS are removed. See RCYSKB and RYBDFF.
4. The effects of PSTATE.PAN are applied. It is IMPLEMENTATION DEFINED whether this is prioritized here or above step 3. See RTBKKB.

The following table shows the privileged and unprivileged stage 1 Base permissions that are applied as determined by the corresponding S1PrivBasePerm and S1UnprivBasePerm values, and whether stage 1 Overlay permissions are applied to those stage 1 Base permissions:

Table D8-68 Determination of stage 1 Base permissions and Overlay application

| S1PrivBasePerm / S1UnprivBasePerm   | Stage 1 Base Permissions                                                    | Stage 1 Overlay applied   |
|-------------------------------------|-----------------------------------------------------------------------------|---------------------------|
| 0b0000                              | -                                                                           | Yes                       |
| 0b0001                              | PrivRead / UnprivRead                                                       | Yes                       |
| 0b0010                              | PrivExecute / UnprivExecute                                                 | Yes                       |
| 0b0011                              | PrivRead / UnprivRead, PrivExecute / UnprivExecute                          | Yes                       |
| 0b0100                              | Reserved, treated as No access                                              | Yes                       |
| 0b0101                              | PrivRead / UnprivRead, PrivWrite / UnprivWrite                              | Yes                       |
| 0b0110                              | PrivRead / UnprivRead, PrivWrite / UnprivWrite, PrivExecute / UnprivExecute | Yes                       |
| 0b0111                              | PrivRead / UnprivRead, PrivWrite / UnprivWrite, PrivExecute / UnprivExecute | Yes                       |
| 0b1000                              | PrivRead / UnprivRead                                                       | No                        |

| S1PrivBasePerm / S1UnprivBasePerm   | Stage 1 Base Permissions                                                    | Stage 1 Overlay applied   |
|-------------------------------------|-----------------------------------------------------------------------------|---------------------------|
| 0b1001                              | PrivRead / UnprivRead, PrivGCS / UnprivGCS                                  | No                        |
| 0b1010                              | PrivRead / UnprivRead, PrivExecute / UnprivExecute                          | No                        |
| 0b1011                              | Reserved, treated as No access                                              | No                        |
| 0b1100                              | PrivRead / UnprivRead, PrivWrite / UnprivWrite                              | No                        |
| 0b1101                              | Reserved, treated as No access                                              | No                        |
| 0b1110                              | PrivRead / UnprivRead, PrivWrite / UnprivWrite, PrivExecute / UnprivExecute | No                        |
| 0b1111                              | Reserved, treated as No access                                              | No                        |

Note

For each row in Table D8-68, stage 1 Base permissions are removed unless stated in the table. Bit [3] in S1PrivBasePerm and S1UnprivBasePerm determines whether stage 1 Overlay permissions are applied to the corresponding stage 1 privileged and unprivileged permissions.

The following table shows how the PrivWXN and UnprivWXN controls are determined by the corresponding S1PrivBasePerm and S1UnprivBasePerm values.

Table D8-69 Determination of PrivWXN and UnprivWXN

| S1PrivBasePerm / S1UnprivBasePerm   | PrivWXN / UnprivWXN control   |
|-------------------------------------|-------------------------------|
| 0b0110                              | Applied                       |
| Others                              | Removed                       |

IPMKFB

IKDZDQ

RRSXJG

RVFPJF

If stage 1 Indirect permissions are used, then SCTLR\_ELx.WXN has no effect and is RES0.

PrivWXN and UnprivWXN are not permissions, but controls that affect the computation of Write and Execute permissions at stage 1. For the details of how this is computed, see Combining stage 1 Base permissions and Overlay permissions.

If stage 1 translation is using Indirect permissions, then a memory region is execute-never at stage 1 if PrivExecute and UnprivExecute are not present.

For the EL1&amp;0 and EL2&amp;0 translation regimes, all of the following combinations of S1PrivBasePerm and S1UnprivBasePerm are reserved, and the stage 1 Base permissions are removed:

- S1PrivBasePerm is one of { 0b0010 , 0b0011 , 0b0110 , 0b0111 , 0b1001 , 0b1010 , 0b1110 }, which apply PrivExecute or PrivGCS.
- S1UnprivBasePerm is one of { 0b0101 , 0b0110 , 0b0111 , 0b1001 , 0b1100 , 0b1110 }, which apply UnprivWrite or UnprivGCS.

Note

The combination of unprivileged write or unprivileged GCS access to memory locations that are also privileged executable or privileged GCS accessible is considered unsafe and should never be used by software. As a safety mechanism, all access permissions are removed. This is different than the mechanism used by Direct permissions. In that case, if unprivileged write permission to a memory location is permitted, then privileged execute permission is removed, but other permissions are retained.

This behavior is independent of stage 1 Overlay permissions.

RHJYGR

| R CYSKB   | If any of the following are true, then the stage 1 Base permissions, PrivGCS and UnprivGCS, are removed: • For Secure translation regimes, the stage 1 OAresides in the Non-secure address space. • For Root state, the stage 1 OAdoes not reside in the Root address space.                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R YBDFF   | If any of the following are true, then the stage 1 Base permissions, PrivExecute and UnprivExecute, are removed: • For Secure translation regimes when SCR_EL3.SIF is set to 1, the stage 1 OAresides in the Non-secure address space. • For Root state, the stage 1 OAdoes not reside in the Root address space. • For the Realm EL2 and Realm EL2&0 translation regimes, the stage 1 OAdoes not reside in the Realm address space.                                                                                                                                                                                                                          |
| R TBKKB   | For the EL1&0 and EL2&0 translation regimes, if the Effective value of PSTATE.PAN is 1 and S1UnprivBasePerm is not 0b0000 , then the stage 1 Base permissions, PrivRead and PrivWrite, are removed. It is IMPLEMENTATION DEFINED whether this applies when the S1UnprivBasePerm is a reserved value, which is therefore treated as 0b0000 . It is IMPLEMENTATION DEFINED whether this applies when the effect of SCR_EL3.SIF and the PA space, as described in R YBDFF , results in removal of all unprivileged stage 1 base permissions. Note The effect of PSTATE.PAN does not depend on the value of SCTLR_ELx.EPAN. If stage 1 uses Indirect permissions, |
| I LSZBZ   | When the Effective value of PSTATE.PAN is 1,R TBKKB ensures that memory with any form of user permissions is not accessible by privileged data accesses.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| R FBQWG   | Except for the impact of PSTATE.PAN, the Effective value of the stage 1 Base permissions are permitted to be cached in a TLB.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| R JHSVW   | If Indirect permissions are used, then hierarchical permissions are disabled and TCR_ELx.HPD n are RES1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| R         | D8.4.1.4 Stage 1 Overlay permissions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| R RSKVR   | All remaining statements in this section require implementation of FEAT_S1POE.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| R RQWXN   | The stage 1 Permission Overlay Enable (POE) is determined by the following table:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Table D8-70 Determination of stage 1 POE value

| Translation Regime   | Field        |
|----------------------|--------------|
| EL1&0                | TCR2_EL1.POE |
| EL2&0                | TCR2_EL2.POE |
| EL2                  | TCR2_EL2.POE |
| EL3                  | TCR_EL3.POE  |

| I KPGBV   | The POE field is not permitted to be cached in a TLB.                                                                                                                                                                          |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R TMNYQ   | For the EL1&0 translation regime, if the Effective value of HCR_EL2.{NV, NV1} is {1, 1}, the value of the stage 1 EL0 Permission Overlay Enable (E0POE) is 0. Otherwise, the E0POE field is determined by the following table: |

| Translation Regime   | Field          |
|----------------------|----------------|
| EL1&0                | TCR2_EL1.E0POE |
| EL2&0                | TCR2_EL2.E0POE |

| I SDBKH   | The E0POE field is not permitted to be cached in a TLB.                                                                                                                                                                                                                                                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R BVXDG   | For a translation regime, if one or more of the following apply, then hierarchical permissions are disabled and the corresponding TCR_ELx.HPD n are RES1: • For any translation regime, POE is 1. • For the EL1&0 and EL2&0 translation regimes, E0POE is 1.                                                       |
| R GDVJK   | If E0POE is 1 and one of the following applies, then stage 1 unprivileged overlay, S1UnprivOverlay , is enabled, otherwise it is disabled: • Stage 1 uses Direct permissions. • Stage 1 uses Indirect permissions and the Unprivileged Base permission configuration selects a value for which Overlay is applied. |
| R DPZHF   | If POE is 1 and one of the following applies, then stage 1 privilege overlay, S1PrivOverlay , is enabled, otherwise it is disabled: • Stage 1 uses Direct permissions. • Stage 1 uses Indirect permissions and the Privileged Base permission configuration selects a value for which                              |
| I SXYLW   | For the EL1&0 and EL2&0 translation regimes, the POR_EL0 Permission Overlay register determines the unprivileged stage 1 overlay permissions, S1UnprivOverlayPerm .                                                                                                                                                |
| I YQTQJ   | For all translation regimes, the following Permission Overlay registers determine privileged stage 1 overlay permissions, S1PrivOverlayPerm : • POR_EL1. • POR_EL2. • POR_EL3.                                                                                                                                     |
| I JGCLT   | The size of the POIndex field in Block descriptors and Page descriptors is one of the following: • In VMSAv8-64, 3-bits. • In VMSAv9-128, 4-bits.                                                                                                                                                                  |
| R BXJBV   | The following table shows how the POIndex field in stage 1 Block descriptors and Page descriptors is used to index into the Permission Overlay registers to obtain S1UnprivOverlayPerm and S1PrivOverlayPerm:                                                                                                      |

## Table D8-72 Using POIndex to determine stage 1 overlay permissions

| Translation Regime   | S1UnprivOverlayPerm                 | S1PrivOverlayPerm                   |
|----------------------|-------------------------------------|-------------------------------------|
| EL1&0                | POR_EL0[(POIndex*4 + 3): POIndex*4] | POR_EL1[(POIndex*4 + 3): POIndex*4] |
| EL2&0                | POR_EL0[(POIndex*4 + 3): POIndex*4] | POR_EL2[(POIndex*4 + 3): POIndex*4] |
| EL2                  |                                     | POR_EL2[(POIndex*4 + 3): POIndex*4] |
| EL3                  |                                     | POR_EL3[(POIndex*4 + 3): POIndex*4] |

RPGLZR

The following table shows the effect of applying stage 1 Overlay permissions to restrict stage 1 permissions:

## Table D8-73 Effect of stage 1 Overlay permissions

| Stage 1 Overlay permission   | Effect when permission is 0                                                                                                                                    |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UnprivRead                   | Restricts read permissions for unprivileged data accesses in the EL1&0 and EL2&0 translation regimes. Not Applicable in the EL2 and EL3 translation regimes.   |
| UnprivWrite                  | Restricts write permissions for unprivileged data accesses in the EL1&0 and EL2&0 translation regimes. Not Applicable in the EL2 and EL3 translation regimes.  |
| PrivRead                     | Restricts read permissions for privileged data accesses in the EL1&0, EL2&0, EL2, and EL3 translation regimes.                                                 |
| PrivWrite                    | Restricts write permissions for privileged data accesses in the EL1&0, EL2&0, EL2, and EL3 translation regimes.                                                |
| UnprivExecute                | Restricts permission for unprivileged instruction execution in the EL1&0 and EL2&0 translation regimes. Not Applicable in the EL2 and EL3 translation regimes. |
| PrivExecute                  | Restricts permission for privileged instruction execution in the EL1&0, EL2&0, EL2, and EL3 translation regimes.                                               |

Note

GCS permissions are not affected by stage 1 Overlay permissions.

RWDCGP

The following table shows the privileged and unprivileged stage 1 overlay permissions that are applied as determined by the corresponding S1PrivOverlayPerm and S1UnprivOverlayPerm values:

Table D8-74 Determination of stage 1 Overlay permissions

| S1PrivOverlayPerm / S1UnprivOverlayPerm   | Stage 1 Overlay permissions                                               |
|-------------------------------------------|---------------------------------------------------------------------------|
| 0b0000                                    | -                                                                         |
| 0b0001                                    | PrivRead / UnprivRead                                                     |
| 0b0010                                    | PrivExecute / UnprivExecute                                               |
| 0b0011                                    | PrivRead / UnprivRead PrivExecute / UnprivExecute                         |
| 0b0100                                    | PrivWrite / UnprivWrite                                                   |
| 0b0101                                    | PrivRead / UnprivRead PrivWrite / UnprivWrite                             |
| 0b0110                                    | PrivWrite / UnprivWrite PrivExecute / UnprivExecute                       |
| 0b0111                                    | PrivRead / UnprivRead PrivWrite / UnprivWrite PrivExecute / UnprivExecute |
| 0b1xxx                                    | Reserved, treated as 0b0000                                               |

Note

For each row in Table D8-74, stage 1 Overlay permissions are 0 unless stated in the table.

| I SKPNZ   | Stage 1 Overlay permissions are not permitted to be cached in a TLB. POIndex is permitted to be cached in a TLB.                                                                                                                                                                                                                                                                                                                           |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I VCQZV   | For a translation regime using VMSAv8-64 that is in-context, when TCR(2)_ELx.{HPD n , POE} or TCR(2)_ELx.{HPD n , E0P0E} transition from {0, 0} to {0, 1} or to {1, 1}, or vice-versa, the resulting stage 1 permissions are CONSTRAINED UNPREDICTABLE, as described in CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values.                                                                                      |
| I VRTYL   | For a translation regime using VMSAv8-64 that is in-context, when TCR(2)_ELx.{HWU nn , POE} or TCR(2)_ELx.{HWU nn , E0P0E} transition from {1, 0} to {0, 1} or to {1,1}, or vice-versa, the resulting stage1PBHA attributes and stage 1 permissions are CONSTRAINED UNPREDICTABLE, as described in CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values.                                                           |
| R QXXPC   | If PrivWXN is present, then all of the following apply to stage 1 Base permissions and stage 1 Overlay permissions: • If S1PrivOverlay is disabled and the decoded stage 1 Base permission PrivWrite is present, then the stage 1 Base permission PrivExecute is removed. • If S1PrivOverlay is enabled and the stage 1 Overlay permission PrivExecute is present, then the stage 1 Overlay permission PrivWrite is removed.               |
| R HQCYT   | If PrivWXN is removed, then it has no effect on stage 1 Base permissions and stage 1 Overlay permissions.                                                                                                                                                                                                                                                                                                                                  |
| R NPBXC   | If UnprivWXN is present, then all of the following apply to stage 1 Base permissions and stage 1 Overlay permissions: • If S1UnprivOverlay is disabled and the decoded stage 1 Base permission UnprivWrite is present, then the stage 1 Base permission UnprivExecute is removed. • If S1UnprivOverlay is enabled and the stage 1 Overlay permission UnprivExecute is present, then the stage 1 Overlay permission UnprivWrite is removed. |
| R GZLXV   | If UnprivWXN is removed, then it has no effect on stage 1 Base permissions and stage 1 Overlay permissions.                                                                                                                                                                                                                                                                                                                                |
| R NHNQC   | PrivWXN and UnprivWXN are permitted to be cached in a TLB.                                                                                                                                                                                                                                                                                                                                                                                 |
| I XGFTP   | Before applying PSTATE.PAN, stage 1 Base permissions are permitted to be cached in a TLB, therefore the effect of PrivWXN and UnprivWXN on stage 1 Base permissions is also permitted to be cached in a TLB. Stage 1 Overlay permissions are not permitted to be cached in a TLB, therefore the effect of PrivWXN and UnprivWXN on stage 1 Overlay permissions is also not permitted to be cached in a TLB.                                |
| R CZCYQ   | All of the following determine whether stage 1 permissions are present or removed: • For PrivGCS and UnprivGCS, if the corresponding Effective stage 1 Base permission is present, then the permission is present. Otherwise, it is removed.                                                                                                                                                                                               |
| R RPXZR   | If any of the following applies, then a stage 1 Permission fault due to Overlay is generated: • S1PrivOverlay is enabled and a privileged access is removed by the Effective value of the stage 1 Overlay permission. • S1UnprivOverlay is enabled and an unprivileged access is removed by the Effective value of the stage 1                                                                                                             |
|           | Overlay permission.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| I DWBGP   | For information on the priority of a stage 1 Permission fault due to Overlay, see Prioritization of Permission faults.                                                                                                                                                                                                                                                                                                                     |

## D8.4.2 Stage 2 permissions

RVHFGB

All statements in this section apply when stage 2 uses VMSAv8-64 or VMSAv9-128.

RBHXHT

The following table lists the stage 2 permissions and the access type that is permitted when the value of that permission is 1.

Table D8-75 Stage 2 permissions

| Stage 2 permission   | Permitted access                                                                      |
|----------------------|---------------------------------------------------------------------------------------|
| RO                   | Read only, including Data Read, RCWRead,MMURead                                       |
| WO                   | Write only, including Data Write, RCWWrite, MMUWrite                                  |
| RW                   | Read and write, including Data Read, Data Write, RCWRead, RCWWrite, MMURead, MMUWrite |
| MRO                  | Mostly read only, including Data Read, RCWRead, RCWWrite, MMURead, MMUWrite           |
| uX                   | Unprivileged Execute                                                                  |
| pX                   | Privileged Execute                                                                    |
| puX                  | Privileged Execute, Unprivileged Execute                                              |

| R BBLJH   | If stage 2 translation is disabled, then stage 2 permits all data accesses, instruction executions, and MMUaccesses.                                                                                                                                                                                                          |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R ZRSPR   | Stage 2 permissions are determined by one of the following: • Stage 2 Direct permissions. For more information, see Stage 2 Direct permissions. • Stage 2 Indirect permissions, which combine stage 2 Base permissions with, if enabled, stage 2 Overlay permissions. For more information, see Stage 2 Indirect permissions. |
| R KXXWX   | If FEAT_S2PIE is not implemented, then stage 2 Direct permissions are used.                                                                                                                                                                                                                                                   |
| R JMGVS   | If stage 2 translation uses VMSAv9-128, then the Effective value of the stage 2 Permission Indirection Enable (S2PIE) is 1. If the translation regime uses VMSAv8-64, then the stage 2 S2PIE value is determined by VTCR_EL2.S2PIE.                                                                                           |
| I JGTWJ   | Stage 2 Direct permissions are not combined with stage 2 Overlay permissions described in Stage 2 Overlay permissions. This is different from stage 1 Base permissions where stage 1 Direct permissions are combined with stage 1 Overlay permissions.                                                                        |
|           | D8.4.2.1 Stage 2 Direct permissions                                                                                                                                                                                                                                                                                           |
| I HHYYW   | Stage 2 Direct permissions are not supported by VMSAv9-128.                                                                                                                                                                                                                                                                   |
| R TVZYF   | For stage 2 Direct permissions, then: • Read permission implies MMUReadand RCW(S) Read permissions. • Write permission implies MMUWrite and RCW(S) Write permissions.                                                                                                                                                         |
|           | D8.4.2.1.1 Stage 2 data accesses using Direct permissions                                                                                                                                                                                                                                                                     |
| R YLJXV   | For the EL1&0 translation regime, if stage 2 translation is enabled, then the S2AP descriptor field determines the stage 2 data access permissions.                                                                                                                                                                           |
| R HBFHL   | The following table shows encoding of the S2AP descriptor field:                                                                                                                                                                                                                                                              |

## Table D8-76 Data access permissions for a stage 2 translation

|   S2AP[1:0] | Access permission from EL1&0   |
|-------------|--------------------------------|
|          00 | No data access                 |
|          01 | RO                             |
|          10 | WO                             |
|          11 | RW                             |

| I HXWLL   | The S2AP data access permissions do not distinguish between EL1 accesses and EL0 accesses.                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R FQNDX   | If an attempt is made to access memory that is not permitted by the value of the S2AP field, then a stage 2 Permission fault is generated.                                                          |
| I NTJRL   | If hardware management of dirty state is enabled at stage 2, then the S2AP[1] bit can be set to 1 by hardware in some situations.                                                                   |
| I GNDQQ   | The instruction Execute-never field in a Block descriptor and Page descriptor is used to control instruction execution permissions by a stage 2 translation.                                        |
| R PRCFD   | For a stage 2 translation, if FEAT_XNX is not implemented, then the XNfield in the Block descriptor and Page descriptor controls instruction execution permissions as shown in the following table: |

## Table D8-77 Stage 2 instruction access permissions, FEAT\_XNX not implemented

|   XN | Access                                                        |
|------|---------------------------------------------------------------|
|    0 | The stage 2 control does not forbid execution at EL1 and EL0. |
|    1 | The stage 2 control does not permit execution at EL1 or EL0.  |

RSTCTY

For a stage 2 translation, if FEAT\_XNX is implemented, then the XN[1:0] field in the Block descriptor and Page descriptor controls instruction execution permissions as shown in the following table:

## Table D8-78 Stage 2 instruction access permissions, FEAT\_XNX implemented

|   XN[1] |   XN[0] | Access                                                                                      |
|---------|---------|---------------------------------------------------------------------------------------------|
|       0 |       0 | The stage 2 control does not forbid execution at EL1 and EL0.                               |
|       0 |       1 | The stage 2 control does not permit execution at EL1, but does not forbid execution at EL0. |
|       1 |       0 | The stage 2 control does not permit execution at EL1 or EL0.                                |
|       1 |       1 | The stage 2 control does not forbid execution at EL1, but does not permit execution at EL0. |

## D8.4.2.2 Stage 2 Indirect permissions

RWCPLC

All statements in this section require implementation of FEAT\_S2PIE.

IWJDFF

Stage 2 Indirect permissions determine the stage 2 permissions by combining all of the following:

- Stage 2 Base permissions. For more information, see Stage 2 Base permissions.

- Stage 2 Overlay permissions. For more information, see Stage 2 Overlay permissions.

RWKZJP

RWLVPJ

<!-- image -->

<!-- image -->

## D8.4.2.2.1 Stage 2 Base permissions

Stage 2 Base permissions are determined by all of the following:

- Stage 2 General permissions.
- Stage 2 Special permissions.

The following table shows the stage 2 General permissions and the permitted accesses:

## Table D8-79 Accesses permitted by stage 2 General permissions

| General permission   | Permitted access                                                |
|----------------------|-----------------------------------------------------------------|
| NoAccess             | No Access                                                       |
| RO                   | Data Read, RCWRead, andMMURead                                  |
| RW                   | Data Read, Data Write, RCWRead, RCWWrite, MMURead, and MMUWrite |
| uX                   | Unprivileged Execute                                            |
| pX                   | Privileged Execute                                              |
| puX                  | Privileged Execute and Unprivileged Execute                     |

RWRFCR

The following table shows the stage 2 Special permissions and the permitted accesses:

## Table D8-80 Accesses permitted by stage 2 Special permissions

| Permission                 | Permitted Access                                                            |
|----------------------------|-----------------------------------------------------------------------------|
| WO                         | Data Write                                                                  |
| MRO                        | Mostly read only, including Data Read, RCWRead, RCWWrite,MMU Read, MMUWrite |
| MRO-TL0, MRO-TL1, MRO-TL01 | Data Read, RCWRead, RCWWrite, MMURead, MMUWrite                             |

Note

The stage 2 MRO* permissions do not provide data write permission.

The Mostly Read Only (MRO) permission prevents explicit write accesses from the EL1&amp;0 translation regime to EL1 translation tables while permitting hardware updates to the Access flag, dirty state, and the writes due to RCW and RCWS instructions.

If an IPA is marked as MRO in stage 2, then it has the following MROaccess permissions :

- Awrite to that IPA from an RCW instruction at EL1 or EL0 is permitted by stage 2.
- Awrite to that IPA from a stage 1 translation table walk as part of an Access flag or dirty state update is permitted by stage 2.
- Any other write to that IPA is not permitted by stage 2 and generates a stage 2 Permission fault.

All of the following TopLevel permissions determine the outcome of the TopLevel checks:

- For a VA translated by TTBR0\_EL1, when TopLevel0 is 1, the IPA is permitted to be used by the first level of the translation table walk.
- For a VA translated by TTBR1\_EL1, when TopLevel1 is 1, the IPA is permitted to be used by the first level of the translation table walk.

For more information, see Stage 2 TopLevel checks.

IBPBBQ

RBQJWZ

IHHBFN

RCWZCV

The following table shows how the stage 2 MRO TopLevel permissions are determined:

## Table D8-81 Stage 2 MRO TopLevel permissions

| MRO TopLevel permission   | TopLevel attributes              |
|---------------------------|----------------------------------|
| MRO-TL0                   | {TopLevel0, TopLevel1} is {1, 0} |
| MRO-TL1                   | {TopLevel0, TopLevel1} is {0, 1} |
| MRO-TL01                  | {TopLevel0, TopLevel1} is {1, 1} |
| Otherwise                 | {TopLevel0, TopLevel1} is {0, 0} |

| R JDVSM   | For stage 2 permissions not affected by VTCR_EL2.GCSH, all of the following apply:                                                                                                                                                                                             |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I WMGMR   | The stage 2 Base permissions, S2BasePerm, are determined by S2PIR_EL2.                                                                                                                                                                                                         |
| R CYQGN   | The following shows how the 4-bit PIIndex field in stage 2 Block descriptors and Page descriptors is used to index into S2PIR_EL2 to obtain S2BasePerm: • S2BasePerm is S2PIR_EL2[(PIIndex*4 + 3): PIIndex*4]                                                                  |
| I XLRNP   | For information on the S2BasePerm encodings, see Table D8-82.                                                                                                                                                                                                                  |
| R ZCKWH   | S2PIR_EL2 is permitted to be cached in a TLB, and therefore so is S2BasePerm.                                                                                                                                                                                                  |
| R QNYFF   | If FEAT_S2POE is not implemented, then stage 2 Overlay permissions are disabled.                                                                                                                                                                                               |
| R MMYHQ   | If stage 2 Indirect permissions are disabled, then stage 2 Overlay permissions are disabled.                                                                                                                                                                                   |
| I XFWQD   | If FEAT_S2POE is implemented and stage 2 uses Indirect permissions, then VTCR_EL2.S2POE determines whether stage 2 Overlay permissions are enabled.                                                                                                                            |
| I SXTQD   | The value of VTCR_EL2.S2POE is not permitted to be cached in a TLB. However, the effect of this field is permitted to be cached in a TLB to a limited extent, as described later in this section. The stage 2 Overlay permissions, S2OverlayPerm, are determined by S2POR_EL1. |
| I WWPGP   |                                                                                                                                                                                                                                                                                |
| R QPQFD   | The following shows how the 4-bit POIndex field in stage 2 Block descriptors and Page descriptors is used to index into S2POR_EL1 to obtain S2OverlayPerm:                                                                                                                     |
| I LCWFG   | For information on the S2OverlayPerm encodings, see Table D8-82.                                                                                                                                                                                                               |
| R LJKKX   | S2OverlayPerm is not permitted to be cached in a TLB, other than in the following limited case. If all of the following apply, then the effect of S2OverlayPerm is permitted to be cached in a TLB to a limited extent:                                                        |

- The limited extent is that a subsequent change to S2POR\_EL1 is not required to affect the use of that stage 1 translation table entry unless it has been explicitly invalidated from the TLB. This applies to each stage 1 translation table entry of a multi-level translation table walk.

| I SRYDP   | POIndex is permitted to be cached in a TLB.                                                                                                                                                                                                                                                                                                    |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I XHYZM   | When VTCR_EL2.{HWU nn , S2POE} transitions from {1, 0} to {0, 1} or to {1,1}, or vice-versa, without a change of VMIDor appropriate TLB maintenance, the resulting stage 2 PBHAattributes and stage 2 permissions are CONSTRAINED UNPREDICTABLE, as described in CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values. |
| R CXFCS   | The following table shows the stage 2 Base permissions and Overlay permissions that are applied as determined by the corresponding other S2BasePerm and S2OverlayPerm values:                                                                                                                                                                  |

## Table D8-82 Determination of stage 2 Base permissions and Overlay permissions

| S2BasePerm / S2OverlayPerm   | Stage 2 permissions           |
|------------------------------|-------------------------------|
| 0b0000                       | NoAccess                      |
| 0b0001                       | Reserved, treated as NoAccess |
| 0b0010                       | MRO                           |
| 0b0011                       | MRO-TL1                       |
| 0b0100                       | WO                            |
| 0b0101                       | Reserved, treated as NoAccess |
| 0b0110                       | MRO-TL0                       |
| 0b0111                       | MRO-TL01                      |
| 0b1000                       | RO                            |
| 0b1001                       | ROand uX                      |
| 0b1010                       | ROand pX                      |
| 0b1011                       | ROand puX                     |
| 0b1100                       | RW                            |
| 0b1101                       | RWand uX                      |
| 0b1110                       | RWand pX                      |
| 0b1111                       | RWand puX                     |

## D8.4.2.2.4 Combining stage 2 Base permissions and Overlay permissions

| I YHPCG   | S2BasePerm and S2OverlayPerm are combined to produce the stage 2 permissions, S2Perm.                                                                                                                   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R HPVST   | If all of the following apply, then S2Perm gets the value of S2BasePerm: • Stage 2 Indirect permissions are enabled. • Stage 2 Overlay permissions are disabled.                                        |
| R XLNQX   | If all of the following apply, then the stage 2 permission attributes, {TopLevel0, TopLevel1} are {0, 0}, and S2Perm is determined by the bitwise-AND of the encodings of S2BasePerm and S2OverlayPerm: |

RSPGVL

If all of the following apply, then S2Perm is determined by S2BasePerm and the corresponding S2OverlayPerm, as shown in Table D8-83:

- Stage 2 Indirect permissions are enabled.
- Stage 2 Overlay permissions are enabled.
- S2BasePerm are stage 2 Special permissions.
- S2OverlayPerm are stage 2 Special permissions.

## Table D8-83 Determination of stage 2 permissions from Special permissions

| S2BasePerm / S2OverlayPerm   | S2OverlayPerm / S2BasePerm         | S2Perm   |
|------------------------------|------------------------------------|----------|
| WO                           | WO                                 | WO       |
| WO                           | MRO, MRO-TL0, MRO-TL1, or MRO-TL01 | NoAccess |
| MRO                          | MRO                                | MRO      |
| MRO-TL0                      | MROorMRO-TL0                       | MRO-TL0  |
| MRO-TL1                      | MROorMRO-TL1                       | MRO-TL1  |
| MRO-TL0                      | MRO-TL1                            | MRO-TL01 |
| MRO-TL01                     | MRO, MRO-TL0, MRO-TL1, or MRO-TL01 | MRO-TL01 |

RGZNFT

If all of the following apply, then S2Perm is determined by S2BasePerm and the corresponding S2OverlayPerm, as shown in Table D8-84:

- Stage 2 Indirect permissions are enabled.
- Stage 2 Overlay permissions are enabled.
- Only one of S2BasePerm or S2OverlayPerm are stage 2 General permissions.
- The corresponding other S2BasePerm or S2OverlayPerm are stage 2 Special permissions.

## Table D8-84 Determination of stage 2 permissions from General and Special permissions

| S2BasePerm / S2OverlayPerm          | S2OverlayPerm / S2BasePerm             | S2Perm   |
|-------------------------------------|----------------------------------------|----------|
| MRO, MRO-TL0, MRO-TL1, and MRO-TL01 | NoAccess                               | NoAccess |
| WO                                  | NoAccess                               | NoAccess |
| MRO, MRO-TL0, MRO-TL1, and MRO-TL01 | RO, optionally with any of uX, pX, puX | RO       |
| MRO                                 | RW, optionally with any of uX, pX, puX | MRO      |
| MRO-TL0                             | RW, optionally with any of uX, pX, puX | MRO-TL0  |
| MRO-TL1                             | RW, optionally with any of uX, pX, puX | MRO-TL1  |
| MRO-TL01                            | RW, optionally with any of uX, pX, puX | MRO-TL01 |
| WO                                  | RO, optionally with any of uX, pX, puX | NoAccess |
| WO                                  | RW, optionally with any of uX, pX, puX | WO       |

RSYLGW

If S2BasePerm does not permit Privileged Execute and does not permit Unprivileged Execute, then stage 2 Indirect permissions are execute-never.

RZBXQM

For stage 2 Realm EL1&amp;0 translations, if the stage 2 OA is not in the Realm PA space, then the Effective value of S2BasePerm removes MMU read, MMU write, and execute permissions.

IPRXVM

For any stage 2 translation, if all of the following apply, then the Effective value of S2BasePerm removes MMU read and MMUwrite permissions:

- The combined memory attributes result in the Device memory type.
- HCR\_EL2.PTW is 1, enabling Protected Table Walk.

IPDJWZ

For the cases described in RZBXQM and IPRXVM, the Effective value of S2BasePerm can be determined by removing these permissions from the Stage 2 Base permissions and caching the result in a TLB, and combining the result with the Stage 2 Overlay permissions, if enabled.

RRRNDT

If all of the following are true, then a stage 2 Permission fault due to Overlay is generated:

- Stage 2 Overlay permissions are enabled and an access is not permitted by S2OverlayPerm,

- The access does not generate a Permission fault due to the Stage 2 TopLevel checks,

IDLDFD

For more information on the priority of a stage 2 Permission fault due to Overlay with respect to other Permission faults, see Prioritization of Permission faults.

## D8.4.3 Effect of both stage 1 and stage 2 on data access permissions

IQGWYR

The combination of both the stage 1 and stage 2 permissions determine the final data access permissions.

RKKXMY

IJYHLR

IBLVHL

IFNZDL

ISZJGX

ISMZSR

If both stage 1 and stage 2 translations are enabled, then in the absence of other higher-priority MMU faults, the data access permissions are combined in one of the following ways:

1. If data access to memory is not permitted by the stage 1 permissions, then a stage 1 Permission fault is generated, regardless of the stage 2 permissions.
2. If data access to memory is permitted by the stage 1 permissions, but is not permitted by the stage 2 permissions, then a stage 2 Permission fault is generated.
3. If data access to memory is permitted by both the stage 1 permissions and the stage 2 permissions, then a Permission fault is not generated.

For more information, see MMU fault prioritization from a single address translation stage.

If EL2 is enabled, then all of the following apply to the EL1&amp;0 translation regime:

- For stage 1 translations, all of the following apply:
- -The stage 1 translation is configured and controlled from EL1.
- -Stage 1 MMU faults are taken to EL1.
- For enabled stage 2 translations, all of the following apply:
- -The stage 2 translation is configured and controlled from EL2.
- -The stage 2 data access permissions do not differentiate between accesses at EL1 or EL0.
- -Software executing at EL2 can assign a write-only permission to a memory region.
- -Stage 2 MMU faults are taken to EL2.

Stage 1 Permission faults are reported with a higher priority than stage 2 Permission faults.

For a virtualization implementation, a hypervisor can define the stage 2 translation permissions to be more restrictive than the stage 1 translation permissions defined by a Guest OS. The final access permissions are the more restrictive of the permissions defined by:

- The Guest OS, in the stage 1 translation tables.
- The hypervisor, in the stage 2 translation tables.

The effects of combining access permissions defined by the hypervisor are expected to be functionally transparent to the Guest OS.

For more information, see MMU fault prioritization from a single address translation stage.

## D8.4.4 Effects on instruction execution permissions and restrictions on instruction fetch

| I CSNFS                 | The descriptors contain fields used to control instruction execution permissions in stage 1 and stage 2 translations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R SKGLB                 | If instruction execution is not permitted by one of the following, then the memory region is execute-never: • Stage 1 Direct permissions are in use, and XNis 1, or both UXNand PXNare 1.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| R BFDZQ                 | If a memory region is execute-never at the current Exception level, then speculative instruction fetch from that memory region is prohibited.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| R DYKWD                 | If a memory region is execute-never at the current Exception level, then when an attempt to execute from that memory region occurs, a Permission fault is generated at the first translation stage that determines the region is execute-never.                                                                                                                                                                                                                                                                                                                                                                          |
| I PTMPK                 | If Device memory is not execute-never, then speculative instruction fetch from that memory region is permitted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| I ZZSZZ                 | For all Exception levels from which a read-sensitive memory region can be accessed, to avoid the possibility of a speculative fetch affecting that memory region, software is expected to define that memory region as execute-never.                                                                                                                                                                                                                                                                                                                                                                                    |
| R WRCYB                 | Except for the purposes of PSTATE.PAN, the descriptor execute-never fields do not prevent data accesses to the memory region translated by the descriptor.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                         | D8.4.4.1 Effect of both stage 1 and stage 2 on instruction access permissions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                         | If both stage 1 and stage 2 translations are enabled, then in the absence of other higher-priority MMUfaults, the instruction execution permissions are combined in one of the following ways: 1. If instruction execution is not permitted by the stage 1 permissions, then a stage 1 Permission fault is generated,                                                                                                                                                                                                                                                                                                    |
| I NYXWS I SBXWZ         | regardless of the stage 2 permissions. 2. If instruction execution is permitted by the stage 1 permissions, but is not permitted by the stage 2 permissions, then a stage 2 Permission fault is generated. 3. If instruction execution is permitted by both the stage 1 permissions and the stage 2 permissions, then a Permission fault is not generated. For more information, see MMUfault prioritization from a single address translation stage. D8.4.4.2 Restriction on Secure instruction fetch The SCR_EL3.SIF bit can be used to prevent instruction execution from Non-secure memory at stage 1 when the PE is |
|                         | executing in Secure state. If all of the following apply, then an attempt to execute an instruction fetched from memory defined by the stage 1 translation as Non-secure generates a Permission fault:                                                                                                                                                                                                                                                                                                                                                                                                                   |
| R FNVTF R WWBFB R ZWRVD | • The Effective value of SCR_EL3.SIF is 1. • Execution is in Secure state. If FEAT_RME is implemented, then the SCR_EL3.SIF bit has no effect on execution in EL3. During execution at EL3, if FEAT_RME is implemented, then any attempt to execute an instruction fetched from                                                                                                                                                                                                                                                                                                                                          |
| I LNCZM                 | fetch from a memory region, including Non-secure mappings of that region, then that software needs to define the region as Device, XN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                         | SCR_EL3.SIF does not prevent speculative instruction fetch. If Secure software wants to prevent speculative instruction                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| I SQGVJ                 | SCR_EL3.SIF is permitted to be cached in a TLB.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

| I KYSPD   | TLB entries might reflect the value of SCR_EL3.SIF, therefore any change to the value of that bit requires synchronization and TLB invalidation.                                                                                           |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R JDPXL   | For an implementation that does not implement EL3, the Effective value of SCR_EL3.SIF is 0.                                                                                                                                                |
| R PKTDS   | If execution is using the Realm EL2 or Realm EL2&0 translation regime, then an attempt to execute an instruction fetched from physical memory other than the Realm PA space generates a stage 1 Permission fault.                          |
| R HGXXY   | For the purpose of PAN, if FEAT_PAN3 is implemented, then it is IMPLEMENTATION DEFINED whether a stage 1 translation in the Realm EL2&0 translation regime that resolves to a Non-secure address is treated as Unprivileged execute-never. |
| R YMCSL   | If execution is using the Realm EL1&0 translation regime, then any attempt to execute an instruction fetched from physical memory other than the Realm PA space generates a stage 2 Permission fault.                                      |
| I MQQXW   | If stage 2 translation is disabled in the Realm EL1&0 translation regime, then all OAs are in the Realm PA space and Permission faults due toR YMCSL can never occur.                                                                      |

## D8.4.5 Effect of PSTATE on access permission

| I LGNSH   | PSTATE.PAN affects memory access permissions decoded from memory access control fields in the descriptors. PSTATE.UAO affects the privilege level of a memory access. The PSTATE.BTYPE field is part of the determination of whether a branch access to a guarded memory region generates a Branch Target exception. For more information on PSTATE, see Process state, PSTATE.   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I KTCFZ   | PSTATE.PAN is used to prevent privileged data accesses to virtual memory addresses that are accessible from EL0.                                                                                                                                                                                                                                                                  |
| R NCMTC   | All statements in this section require implementation of FEAT_PAN.                                                                                                                                                                                                                                                                                                                |
| R TBYDZ   | For a translation regime, if one or more of the following apply, then the PSTATE.PAN bit has no effect in that regime: • Stage 1 translation is disabled. • Stage 1 translation supports a single privilege level.                                                                                                                                                                |
| R XTSQH   | If the Effective value of PSTATE.PAN is 1, then a privileged data access from any of the following Exception levels to a virtual memory address that is accessible to data accesses at EL0 generates a stage 1 Permission fault:                                                                                                                                                  |
| R DGQQK   | If the value of PSTATE.PAN is 0, then a privileged data access is permitted from the corresponding privileged Exception level to a virtual memory address that is accessible at EL0.                                                                                                                                                                                              |
| I ZBRBM   | When taking an exception from an EL in AArch64 state to an ELx, PSTATE.PAN is saved to and restored from SPSR_ELx.PAN.                                                                                                                                                                                                                                                            |
| I PWXVY   | When taking an exception from an EL in AArch32 state to an ELx in AArch64 state, CPSR.PAN is saved to and restored from SPSR_ELx.PAN.                                                                                                                                                                                                                                             |
| I FNLWP   | When entering and exiting Debug state, PSTATE.PAN is saved to and restored from DSPSR_EL0.PAN.                                                                                                                                                                                                                                                                                    |
| I RTHGD   | When an exception occurs, one of the following determines whether PSTATE.PAN is set to 1 or the value of PSTATE.PAN is unchanged: • When taking an exception to EL1, SCTLR_EL1.SPAN.                                                                                                                                                                                              |

RZGCNT

ICVRWF

If FEAT\_PAN3 is implemented, PSTATE.PAN is 1, and unprivileged instruction execution is permitted to a V A, then all of the following prevent privileged data accesses to that V A:

- For a data access from EL1, when SCTLR\_EL1.EPAN is 1, a Permission fault is generated.
- For a data access from EL2, when the Effective value of HCR\_EL2.E2H is 1 and SCTLR\_EL2.EPAN is 1, a Permission fault is generated.

RWHHYZ For the purpose of PAN, if FEAT\_PAN3 is implemented, then it is IMPLEMENTATION DEFINED whether SCR\_EL3.SIF is used to determine instruction execution permission.

IHKGQP

If FEAT\_PAN3 is implemented, then the SCTLR\_EL1.EPAN and SCTLR\_EL2.EPAN bits affect the AT S1E1RP and AT S1E1WP instructions, consistent with those instructions using PSTATE.PAN to determine whether the memory access generates a Permission fault.

RPMTWB

The PSTATE.PAN bit has no effect on all of the following:

- Instruction fetches.
- Data cache instructions, except DC ZV A, DC GZVA, and DC GVA.
- If FEAT\_PAN2 is not implemented, then address translation instructions.
- If FEAT\_PAN2 is implemented, then the address translation instructions other than AT S1E1RP and AT S1E1WP.

IYMLJD If the current Exception level is EL1 and the Effective value of HCR\_EL2.{NV , NV1} is {1, 1}, then PSTATE.PAN is treated as 0 for all purposes except reading the bit value.

IZRSWJ Software can access PSTATE.PAN using all of the following instructions:

- Software can use MSR (immediate) PAN, #Imm4 to modify PSTATE.PAN.
- Software can use MSR (register) PAN, Xt to modify PSTATE.PAN.
- Software can use MRS Xt, PAN to read PSTATE.PAN.

IGYGGV If the PE is in Debug state, then a debugger can use the DRPS instruction to modify PSTATE.PAN.

## D8.4.5.2 PSTATE.UAO

IWZGDY PSTATE.UAO is used to control whether, for unprivileged memory access instructions, memory accesses described as unprivileged by the instruction are treated as privileged or unprivileged.

RNMGWS All statements in this section require implementation of FEAT\_UAO.

RZVNJS Unprivileged memory access instructions are all of the following:

- The instructions described in Load/store unprivileged.
- If FEAT\_LSUI is implemented, the instructions described in the following sections:
- -Unprivileged atomic memory operations.
- -Swap unprivileged.
- -Compare and Swap unprivileged.
- -Load-Acquire/Store-Release unprivileged.
- -Load-Exclusive/Store-Exclusive unprivileged.
- -Load/store non-temporal pair unprivileged.
- -Load/store pair unprivileged.
- -Load/store unprivileged SIMD and floating-point register pair.
- -Load/store unprivileged SIMD and floating-point non-temporal pair.
- If FEAT\_MOPS is implemented, the instructions described as generating either unprivileged reads or unprivileged writes or both in Memory Copy and Memory Set instructions.
- If FEAT\_GCS is implemented, GCSSTTR .

When an exception occurs, all of the following apply to PSTATE.UAO:

- When taking an exception to ELx, PSTATE.UAO is saved to SPSR\_ELx.UAO and then set to 0.
- When returning from an exception at ELx, PSTATE.UAO is restored from SPSR\_ELx.UAO.

IPHDNT

If the PE is in AArch32 state, then when an exception occurs and the exception is taken to AArch64 state, all of the following occur:

- PSTATE.UAO is set to 0.

- The corresponding SPSR\_ELx.UA0 is set to 0.

IQWJDP

When entering and exiting Debug state, PSTATE.UAO is saved to and restored from DSPSR\_EL0.UAO.

IJQRCG

Software can access PSTATE.UAO using all of the following instructions:

- Software can use MSR (immediate) UAO, #Imm4 to modify PSTATE.UAO.

- Software can use MSR (register) UAO, Xt to modify PSTATE.UAO.

- Software can use MRS Xt, UAO to read PSTATE.UAO.

IVCMLT

If the PE is in Debug state, a debugger can use the DRPS instruction to modify PSTATE.UAO.

## D8.4.5.3 PSTATE.BTYPE

IYYZDP

PSTATE.BTYPE is part of a mechanism used to guard memory pages against executing instructions that are not the intended target of a branch. See also Restrictions on the effects of speculation from Armv9.5.

RJJMBN

All statements in this section require implementation of FEAT\_BTI.

RYWFHD

When an instruction completes execution, the value of the PSTATE.BTYPE field is determined by all of the following, as shown in the following table:

- The instruction that was executed.
- Whether or not the memory region is guarded.
- The register accessed by the instruction.

## Table D8-85 Values taken by PSTATE.BTYPE on execution of an instruction

| Instruction executed                  | Memory region   | Register accessed              | PSTATE.BTYPE   |
|---------------------------------------|-----------------|--------------------------------|----------------|
| BR , BRAA , BRAAZ , BRAB , BRABZ      | Guarded         | Any register except X16 or X17 | 0b11           |
| BLR , BLRAA , BLRAAZ , BLRAB , BLRABZ | Any             | Any register                   | 0b10           |
| BR , BRAA , BRAAZ , BRAB , BRABZ      | Guarded         | X16 or X17                     | 0b01           |
| BR , BRAA , BRAAZ , BRAB , BRABZ      | Non-guarded     | Any register                   | 0b01           |
| ERET , ERETAA , ERETAB , and DRPS     | Any             | Any register                   | SPSR_ELx.BTYPE |
| Any other instruction                 | Any             | Any register                   | 0b00           |

When the BTI instruction is executed, the &lt;targets&gt; operand determines the compatibility between the BTI instruction and different PSTATE.BTYPE values as shown in the following table:

## Table D8-86 Compatibility of BTI instruction to different PSTATE.BTYPE values

| <targets>   | PSTATE.BTYPE value   | PSTATE.BTYPE value   |                |                |
|-------------|----------------------|----------------------|----------------|----------------|
|             | 0b00                 | 0b01                 | 0b10           | 0b11           |
| (omitted)   | N/A                  | Not compatible       | Not compatible | Not compatible |
| c           | N/A                  | Compatible           | Compatible     | Not compatible |
| j           | N/A                  | Compatible           | Not compatible | Compatible     |

ICNBPL

| <targets>   | PSTATE.BTYPE value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | PSTATE.BTYPE value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | PSTATE.BTYPE value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | PSTATE.BTYPE value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|             | 0b00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 0b01                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 0b10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 0b11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| jc          | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Compatible                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Compatible                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Compatible                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| I JRBGR     | If stage 1 translation is enabled, the GP bit in Block and Page descriptors indicates whether the memory region is guarded. For more information, see FEAT_BTI. If stage 1 translation is disabled, no memory regions are guarded. For more information, see Behavior when stage 1 address translation is disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | If stage 1 translation is enabled, the GP bit in Block and Page descriptors indicates whether the memory region is guarded. For more information, see FEAT_BTI. If stage 1 translation is disabled, no memory regions are guarded. For more information, see Behavior when stage 1 address translation is disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | If stage 1 translation is enabled, the GP bit in Block and Page descriptors indicates whether the memory region is guarded. For more information, see FEAT_BTI. If stage 1 translation is disabled, no memory regions are guarded. For more information, see Behavior when stage 1 address translation is disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | If stage 1 translation is enabled, the GP bit in Block and Page descriptors indicates whether the memory region is guarded. For more information, see FEAT_BTI. If stage 1 translation is disabled, no memory regions are guarded. For more information, see Behavior when stage 1 address translation is disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| R LJHCL     | If the PSTATE.BTYPE field is not 0b00 and an attempt is made to execute an instruction within a guarded page, a Branch Target exception is generated unless the instruction is one of the following: • ABTI instruction that is compatible with the PSTATE.BTYPE field. • A PACIASP , PACIBSP , PACIASPPC , or PACIBSPPC instruction, and PSTATE.BTYPE is consistent with implicit BTI behavior of these instructions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | If the PSTATE.BTYPE field is not 0b00 and an attempt is made to execute an instruction within a guarded page, a Branch Target exception is generated unless the instruction is one of the following: • ABTI instruction that is compatible with the PSTATE.BTYPE field. • A PACIASP , PACIBSP , PACIASPPC , or PACIBSPPC instruction, and PSTATE.BTYPE is consistent with implicit BTI behavior of these instructions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | If the PSTATE.BTYPE field is not 0b00 and an attempt is made to execute an instruction within a guarded page, a Branch Target exception is generated unless the instruction is one of the following: • ABTI instruction that is compatible with the PSTATE.BTYPE field. • A PACIASP , PACIBSP , PACIASPPC , or PACIBSPPC instruction, and PSTATE.BTYPE is consistent with implicit BTI behavior of these instructions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | If the PSTATE.BTYPE field is not 0b00 and an attempt is made to execute an instruction within a guarded page, a Branch Target exception is generated unless the instruction is one of the following: • ABTI instruction that is compatible with the PSTATE.BTYPE field. • A PACIASP , PACIBSP , PACIASPPC , or PACIBSPPC instruction, and PSTATE.BTYPE is consistent with implicit BTI behavior of these instructions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| I ZJQDF     | The Software Breakpoint instruction and, if Halting is enabled and allowed, the Halt instruction always generate a higher priority exception or debug event than a Branch Target exception.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The Software Breakpoint instruction and, if Halting is enabled and allowed, the Halt instruction always generate a higher priority exception or debug event than a Branch Target exception.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The Software Breakpoint instruction and, if Halting is enabled and allowed, the Halt instruction always generate a higher priority exception or debug event than a Branch Target exception.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The Software Breakpoint instruction and, if Halting is enabled and allowed, the Halt instruction always generate a higher priority exception or debug event than a Branch Target exception.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| R VWTMW     | When a Branch Target exception occurs, it is taken to one of the following: • When executing at EL0 and HCR_EL2.TGE is 0, the Branch Target exception is taken to EL1. • When executing at EL0 and HCR_EL2.TGE is 1, the Branch Target exception is taken to EL2. • When executing at ELx, where x is 1, 2, or 3, the Branch Target exception is taken to ELx.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | When a Branch Target exception occurs, it is taken to one of the following: • When executing at EL0 and HCR_EL2.TGE is 0, the Branch Target exception is taken to EL1. • When executing at EL0 and HCR_EL2.TGE is 1, the Branch Target exception is taken to EL2. • When executing at ELx, where x is 1, 2, or 3, the Branch Target exception is taken to ELx.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | When a Branch Target exception occurs, it is taken to one of the following: • When executing at EL0 and HCR_EL2.TGE is 0, the Branch Target exception is taken to EL1. • When executing at EL0 and HCR_EL2.TGE is 1, the Branch Target exception is taken to EL2. • When executing at ELx, where x is 1, 2, or 3, the Branch Target exception is taken to ELx.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | When a Branch Target exception occurs, it is taken to one of the following: • When executing at EL0 and HCR_EL2.TGE is 0, the Branch Target exception is taken to EL1. • When executing at EL0 and HCR_EL2.TGE is 1, the Branch Target exception is taken to EL2. • When executing at ELx, where x is 1, 2, or 3, the Branch Target exception is taken to ELx.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| I VWNCG     | When a Branch Target exception occurs, ESR_ELx.EC is 0x0D . For more information, see ISS encoding for an exception from Branch Target Identification instruction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | When a Branch Target exception occurs, ESR_ELx.EC is 0x0D . For more information, see ISS encoding for an exception from Branch Target Identification instruction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | When a Branch Target exception occurs, ESR_ELx.EC is 0x0D . For more information, see ISS encoding for an exception from Branch Target Identification instruction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | When a Branch Target exception occurs, ESR_ELx.EC is 0x0D . For more information, see ISS encoding for an exception from Branch Target Identification instruction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| I GMGRS     | When any of the following are true, the PACIASP , PACIBSP , PACIASPPC , and PACIBSPPC instructions have an implicit BTI behavior that is compatible with the same PSTATE.BTYPE values as a BTI.jc instruction: • The PE is executing at EL0, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and SCTLR_EL1.BT0 is 0. • The PE is executing at EL0, the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, and SCTLR_EL2.BT0 is 0. • The PE is executing at EL1, and SCTLR_EL1.BT1 is 0. • The PE is executing at EL2, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and SCTLR_EL2.BT is 0. • The PE is executing at EL2, the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, and SCTLR_EL2.BT1 is 0. • The PE is executing at EL3, and SCTLR_EL3.BT is 0. Otherwise, these instructions have an implicit BTI behavior that is compatible with the same PSTATE.BTYPE values as BTI.c. The implicit branch target identification property of PACIASP , PACIBSP , PACIASPPC , and PACIBSPPC is independent | When any of the following are true, the PACIASP , PACIBSP , PACIASPPC , and PACIBSPPC instructions have an implicit BTI behavior that is compatible with the same PSTATE.BTYPE values as a BTI.jc instruction: • The PE is executing at EL0, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and SCTLR_EL1.BT0 is 0. • The PE is executing at EL0, the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, and SCTLR_EL2.BT0 is 0. • The PE is executing at EL1, and SCTLR_EL1.BT1 is 0. • The PE is executing at EL2, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and SCTLR_EL2.BT is 0. • The PE is executing at EL2, the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, and SCTLR_EL2.BT1 is 0. • The PE is executing at EL3, and SCTLR_EL3.BT is 0. Otherwise, these instructions have an implicit BTI behavior that is compatible with the same PSTATE.BTYPE values as BTI.c. The implicit branch target identification property of PACIASP , PACIBSP , PACIASPPC , and PACIBSPPC is independent | When any of the following are true, the PACIASP , PACIBSP , PACIASPPC , and PACIBSPPC instructions have an implicit BTI behavior that is compatible with the same PSTATE.BTYPE values as a BTI.jc instruction: • The PE is executing at EL0, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and SCTLR_EL1.BT0 is 0. • The PE is executing at EL0, the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, and SCTLR_EL2.BT0 is 0. • The PE is executing at EL1, and SCTLR_EL1.BT1 is 0. • The PE is executing at EL2, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and SCTLR_EL2.BT is 0. • The PE is executing at EL2, the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, and SCTLR_EL2.BT1 is 0. • The PE is executing at EL3, and SCTLR_EL3.BT is 0. Otherwise, these instructions have an implicit BTI behavior that is compatible with the same PSTATE.BTYPE values as BTI.c. The implicit branch target identification property of PACIASP , PACIBSP , PACIASPPC , and PACIBSPPC is independent | When any of the following are true, the PACIASP , PACIBSP , PACIASPPC , and PACIBSPPC instructions have an implicit BTI behavior that is compatible with the same PSTATE.BTYPE values as a BTI.jc instruction: • The PE is executing at EL0, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and SCTLR_EL1.BT0 is 0. • The PE is executing at EL0, the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, and SCTLR_EL2.BT0 is 0. • The PE is executing at EL1, and SCTLR_EL1.BT1 is 0. • The PE is executing at EL2, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and SCTLR_EL2.BT is 0. • The PE is executing at EL2, the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, and SCTLR_EL2.BT1 is 0. • The PE is executing at EL3, and SCTLR_EL3.BT is 0. Otherwise, these instructions have an implicit BTI behavior that is compatible with the same PSTATE.BTYPE values as BTI.c. The implicit branch target identification property of PACIASP , PACIBSP , PACIASPPC , and PACIBSPPC is independent |
| R DFHDM     | of the setting of the SCTLR_ELx.{EnIA, EnIB} bits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | of the setting of the SCTLR_ELx.{EnIA, EnIB} bits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | of the setting of the SCTLR_ELx.{EnIA, EnIB} bits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | of the setting of the SCTLR_ELx.{EnIA, EnIB} bits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| I CKJFH     | In a non-guarded page, the BTI instruction executes as a NOP .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | In a non-guarded page, the BTI instruction executes as a NOP .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | In a non-guarded page, the BTI instruction executes as a NOP .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | In a non-guarded page, the BTI instruction executes as a NOP .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| I WCDBN     | The effect of a NOP on PSTATE.BTYPE is described inR YWFHD .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The effect of a NOP on PSTATE.BTYPE is described inR YWFHD .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The effect of a NOP on PSTATE.BTYPE is described inR YWFHD .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The effect of a NOP on PSTATE.BTYPE is described inR YWFHD .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| I CPYQW     | There is no mechanism for direct reads or direct writes of the PSTATE.BTYPE field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | There is no mechanism for direct reads or direct writes of the PSTATE.BTYPE field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | There is no mechanism for direct reads or direct writes of the PSTATE.BTYPE field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | There is no mechanism for direct reads or direct writes of the PSTATE.BTYPE field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|             | Controlling memory access Security state                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Controlling memory access Security state                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Controlling memory access Security state                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Controlling memory access Security state                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| D8.4.6      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| R PRTVS     | In this section and subsections, IPA or PA space refers to the OAspace of stage 1 translations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | In this section and subsections, IPA or PA space refers to the OAspace of stage 1 translations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | In this section and subsections, IPA or PA space refers to the OAspace of stage 1 translations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | In this section and subsections, IPA or PA space refers to the OAspace of stage 1 translations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

| R KZLVM   | For a Secure translation regime, if the translation table entry is in Secure IPA or PA space, then the Block descriptor and Page descriptor NS determines all of the following: • If NS is 0, an access to the OAspecified by the descriptor is to Secure IPA or PA space.                                                         |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R LXLSC   | For all of the following, if a Block or Page descriptor has NS set to 1, then the OAis in the Non-secure PA space. Otherwise, the OAis in the Realm PA space: • Stage 1 translation in the Realm EL2 translation regime. • Stage 1 translation in the Realm EL2&0 translation regime.                                              |
| R QMLYQ   | If the stage 2 translation for a Realm stage 1 translation table walk resolves to an address not in the Realm PA space, it causes a stage 2 Permission fault.                                                                                                                                                                      |
| R VZYQL   | For a Non-secure translation regime, the NS and NSTable bits are RES0 and the OAor next-level table base address is in Non-secure IPA or PA space.                                                                                                                                                                                 |
| R FKJXR   | For a Secure translation regime, when the descriptor is fetched from Non-secure IPA or PA space, all of the following apply to the descriptor: • The descriptor NS and NSTable bits exist but they are SBZ instead of RES0. • The OAor next-level table base address specified by the descriptor is in Non-secure IPA or PA space. |
| R QSJJS   | For the EL3 stage 1 translation regime, if FEAT_RME is not implemented, then the NS field in a Block descriptor or Page descriptor determines the output PA space as shown in the following table:                                                                                                                                 |

## Table D8-87 Output PA space

|   NS | Output PA space   |
|------|-------------------|
|    0 | Secure.           |
|    1 | Non-secure.       |

RXTYPW

For the EL3 stage 1 translation regime, if FEAT\_RME is implemented, then the NSE and NS fields in a Block descriptor or Page descriptor determine the output PA space as shown in the following table:

## Table D8-88 Output PA space

|   NSE |   NS | Output PA space                                                  |
|-------|------|------------------------------------------------------------------|
|     0 |    0 | If FEAT_SEL2 is implemented, then Secure. Otherwise, Non-secure. |
|     0 |    1 | Non-secure.                                                      |
|     1 |    0 | Root.                                                            |
|     1 |    1 | Realm.                                                           |

## D8.4.6.1 Hierarchical control of Secure or Non-secure memory accesses

For a Secure translation regime, when a Table descriptor is accessed from a stage 1 translation table in Secure IPA or PA space, the NSTable field determines all of the following:

- If NSTable is 0, the next-level translation table address in the Table descriptor is in Secure IPA or PA space.
- If NSTable is 1, the next-level translation table address in the Table descriptor is in Non-secure IPA or PA space.

If the next-level translation table address in the Table descriptor is in Non-secure IPA or PA space, then the address specified by a descriptor in the next lookup-level translation table is in Non-secure IPA or PA space.

RWGTQD

RYPMZG

IXGNKR

RKRBNK

ITKPLZ

If stage 2 translation is enabled, the VSTCR\_EL2.SA, VTCR\_EL2.NSA, VSTCR\_EL2.SW, and VTCR\_EL2.NSW fields can map an IPA space to a PA space not matching the Security of the IPA space.

If all of the following apply, then a stage 1 translation is treated as non-global, meaning the Effective value of nG is 1, regardless of the actual value of the Block descriptor or Page descriptor nG bit:

- The stage 1 translation supports two privilege levels.
- The PE is in Secure state.
- NSTable is 1 at any level of the translation table walk.

For more information, see Global and process-specific translation table entries.

The descriptor NSTable field affects all subsequent lookup levels and the translation IPA or PA space. When an NSTable field is changed, software is required to use a break-before-make sequence, including TLB maintenance for all lookup levels for the V A range translated by the descriptor.

For more information, see TLB maintenance and Using break-before-make when updating translation table entries.