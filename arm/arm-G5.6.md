## G5.6 Memory access control

In addition to an output address, a translation table entry that refers to page or region of memory includes fields that define properties of the target memory region. Information returned by a translation table lookup describes the classification of those fields as address map control, access control, and memory attribute fields. The access control fields, described in this section, determine whether the PE, in its current state, is permitted to perform the required access to the output address given in the Translation Table descriptor. If a translation stage does not permit the access, then an MMUfault is generated for that translation stage, and no memory access is performed.

The following sections describe the memory access controls:

- About access permissions.
- About the PAN bit.
- Access permissions for instruction execution.
- Domains, Short-descriptor format only.
- The Access flag.
- Hyp mode control of Non-secure access permissions.

## G5.6.1 About access permissions

The Translation Table descriptors include fields that define access permissions for data accesses and for instruction fetches. This section introduces those fields. In addition:

- System register controls can prevent execution from writable locations, see Preventing execution from writable locations.
- In Armv8.1, the PSTATE.PAN can affect the access permissions for privileged data accesses, see About the PAN bit.

Note

This section gives a general description of memory access permissions. Software executing at PL1 in Non-secure state can see only the access permissions defined by the Non-secure PL1&amp;0 stage 1 translations. However, software executing at EL2 can modify these permissions, as described in Hyp mode control of Non-secure access permissions. This modification is invisible to Non-secure software executing at EL1 or EL0.

Access permission bits in a Translation Table descriptor control access to the corresponding memory region. The details of this control depend on the translation table format, as follows:

## Short-descriptor format

This format supports two options for defining the access permissions:

- Three bits, AP[2:0], define the access permissions.
- Two bits, AP[2:1], define the access permissions, and AP[0] can be used as an Access flag.

SCTLR.AFE selects the access permissions option. Setting this bit to 1, to enable the Access flag, also selects use of AP[2:1] to define access permissions.

Arm deprecates any use of the AP[2:0] scheme for defining access permissions.

## Long-descriptor format

AP[2:1] to control the access permissions, and the descriptors provide an AF bit for use as an Access flag. This means VMSAv8-32 behaves as if the value of SCTLR.AFE is 1, regardless of the value that software has written to this bit.

Note

When use of the Long-descriptor format is enabled, SCTLR.AFE is UNK/SBOP.

The Access flag describes the Access flag, for both translation table formats.

The XN and PXN bits provide additional access controls for instruction fetches, see Access permissions for instruction execution.

An attempt to perform a memory access that the translation table access permission bits do not permit generates a Permission fault, for the corresponding stage of translation. However, when using the Short-descriptor translation table format, it generates the fault only if the access is to memory in the Client domain, see Domains, Short-descriptor format only.

Note

For the Non-secure PL1&amp;0 translation regime, memory accesses are subject to two stages of translation. Each stage of translation has its own, independent, fault checking. Fault handling is different for the two stages, see Exception reporting in a VMSAv8-32 implementation.

The following sections describe the two access permissions models:

- AP[2:1] access permissions model.
- AP[2:0] access permissions control, Short-descriptor format only. This section includes some information on access permission control in earlier versions of the Arm VMSA.

## G5.6.1.1 AP[2:1] access permissions model

Note

Arm recommends that this model is always used, even where the AP[2:0] model is permitted. Some documentation describes the AP[2:1] model as the simplified access permissions model.

This access permissions model is used if the translation is either:

- Using the Long-descriptor translation table format.
- Using Short-descriptor translation table format, and the SCTLR.AFE bit is set to 1.

## In this model:

- One bit, AP[2], selects between read-only and read/write access.
- Asecond bit, AP[1], selects between Application level (EL0) and System level (PL1) control. For the Non-secure EL2 stage 1 translations, AP[1] is SBO.

This provides four access combinations:

- Read-only at all privilege levels.
- Read/write at all privilege levels.
- Read-only at PL1, no access by software executing at EL0.
- Read/write at PL1, no access by software executing at EL0.

Table G5-7 shows this access control model.

## Table G5-7 VMSAv8-32 AP[2:1] access permissions model

|   AP[2], disable write access | AP[1], enable unprivileged access   | Access                             |
|-------------------------------|-------------------------------------|------------------------------------|
|                             0 | 0 a                                 | Read/write, only at PL1            |
|                             0 | 1                                   | Read/write, at any privilege level |

|   AP[2], disable write access | AP[1], enable unprivileged access   | Access                            |
|-------------------------------|-------------------------------------|-----------------------------------|
|                             1 | 0 a                                 | Read-only, only at PL1            |
|                             1 | 1                                   | Read-only, at any privilege level |

## G5.6.1.1.1 Hierarchical control of access permissions, Long-descriptor format

The Long-descriptor translation table format introduces a mechanism that entries at one level of translation table lookup can use to set limits on the permitted entries at subsequent levels of lookup. This applies to the access permissions, and also to the restrictions on instruction fetching described in Hierarchical control of instruction fetching, Long-descriptor format.

The restrictions apply only to subsequent levels of lookup at the same stage of translation. The APTable[1:0] field restricts the access permissions, as Table G5-8 shows.

However, in an implementation that includes FEAT\_AA32HPD, when hierarchical control of data access permissions is disabled for a translation regime, the information in this subsection does not apply. See Attribute fields in VMSAv8-32 Long-descriptor translation table format descriptors.

As stated in the table footnote, for the Non-secure EL2 stage 1 translation tables, APTable[0] is reserved, SBZ.

## Table G5-8 Effect of APTable[1:0] on subsequent levels of lookup

| APTable[1:0]   | Effect                                                                                                        |
|----------------|---------------------------------------------------------------------------------------------------------------|
| 00             | No effect on permissions in subsequent levels of lookup.                                                      |
| 01 a           | Access at EL0 not permitted, regardless of permissions in subsequent levels of lookup.                        |
| 10             | Write access not permitted, at any Exception level, regardless of permissions in subsequent levels of lookup. |
| 11 a           | Regardless of permissions in subsequent levels of lookup:                                                     |

- Write access not permitted, at any Exception level.
- Read access not permitted at EL0.

a. Not valid for the Non-secure EL2 stage 1 translation tables. In those tables, APTable[0] is SBZ.

Note

The APTable[1:0] settings are combined with the translation table access permissions in the Translation Tables descriptors accessed in subsequent levels of lookup. They do not restrict or change the values entered in those descriptors.

The Long-descriptor format provides APTable[1:0] control only for the stage 1 translations. The corresponding bits are SBZ in the stage 2 Translation Table descriptors.

The effect of APTable applies to later entries in the translation table walk, and so its effects can be held in one or more TLB entries. Therefore, a change to APTable requires coarse-grained invalidation of the TLB to ensure that the effect of the change is visible to subsequent memory transactions.

## G5.6.1.2 AP[2:0] access permissions control, Short-descriptor format only

This access permissions model applies when using the Short-descriptor translation tables format, and the SCTLR.AFE bit is set to 0. Arm deprecates any use of this access permissions model.

When SCTLR.AFE is set to 0, ensuring that the AP[0] bit is always set to 1 effectively changes the access model to the simpler model described in AP[2:1] access permissions model.

Table G5-9 shows the full AP[2:0] access permissions model:

## Table G5-9 VMSAv8-32 MMU access permissions

| AP[2]   |   AP[1:0] | PL1 access   | Unprivileged access   | Description                                    |
|---------|-----------|--------------|-----------------------|------------------------------------------------|
| 0       |        00 | No access    | No access             | All accesses generate Permission faults        |
|         |        01 | Read/write   | No access             | Access only at PL1                             |
|         |        10 | Read/write   | Read-only             | Writes at EL0 generate Permission faults       |
|         |        11 | Read/write   | Read/write            | Full access                                    |
| 1       |        00 | -            | -                     | Reserved                                       |
|         |        01 | Read-only    | No access             | Read-only, only at PL1                         |
|         |        10 | Read-only    | Read-only             | Read-only at any Exception level, deprecated a |
|         |        11 | Read-only    | Read-only             | Read-only at any Exception level b             |

## Note

- VMSAv8-32 supports the full set of access permissions shown in Table G5-9 only when SCTLR.AFE is set to 0. When SCTLR.AFE is set to 1, the only supported access permissions are those described in AP[2:1] access permissions model.
- Some old documentation describes the AP[2] bit in the translation table entries as the APX bit.

## G5.6.2 About the PAN bit

When the value of PSTATE.PAN is 1, any privileged data access from PL1 or EL2 to a virtual memory address that is accessible at EL0 generates a Permission fault.

When the value of PSTATE.PAN is 0, the translation system is the same as in Armv8.0.

Acorresponding PAN bit is added to CPSR and SPSR for exception returns, and DSPSR for entry to and exit from Debug state.

Anew SPAN bit is added to SCTLR that controls whether the PAN state bit is set on taking an exception to EL1 from either Secure or Non-secure state, or to EL3 from Secure state when EL3 is using AArch32.

CPSR.PAN bit can be written using an MSR instruction at PL1 or higher. Data writes to CPSR.PAN using an MSR instruction at EL0 are ignored. The value that is returned for an MRS instruction of CPSR from EL0 is UNKNOWN. In keeping with all other writes to the CPSR, other than for instruction fetches, the effect of the PAN state bit does not need to be explicitly synchronized.

The PAN state bit has no effect on:

- Data Cache instructions.
- Address translation instructions, other than ATS1CPRP and ATS1CPWP when FEAT\_PAN2 is implemented.
- Unprivileged instructions, LDRBT , LDRHT , LDRT , LDRSBT , LDRSHT , STRBT , STRHT , STRT , STRSBT , and STRSHT , unless the Effective value of HCR\_EL2.{E2H, TGE} is {1, 0}.
- Instruction accesses.
- Manager domains.

The PAN bit has no effect when the first stage of translation is disabled for the current translation regime or when the first stage of translation for the current translation regime does not describe the permissions for access at EL0.

If access is disabled, then the access will give rise to a stage 1 Permission fault.

On an exception taken from AArch32:

- CPSR.PAN is copied to SPSR\_ELx.PAN, when the target Exception level is AArch64.

- CPSR.PAN is copied to SPSR.PAN, when the target Exception level is AArch32.

On an exception return from AArch32 to AArch32, SPSR.PAN is copied to CPSR.PAN.

On entry to Debug state, CPSR.PAN is copied to DSPSR.PAN.

On exit from Debug state, DSPSR.PAN is copied to CPSR.PAN.

The CPSR.PAN bit is not an Execution state bit.

## Note

- In Non-debug state, in AArch32 state, software can use the SETPAN #imm instruction to modify PSTATE.PAN.
- In Debug state, in AArch32 state, a debugger can use the ERET instruction to perform a DRPS operation to modify PSTATE.PAN.

## G5.6.3 Access permissions for instruction execution

Execute-never controls provide an additional level of control on memory accesses permitted by the access permissions settings. These controls are:

## XN, Execute-never

Descriptor bit[54], defined as XN for:

- Stage 1 of any translation regime.
- Stage 2 translations when FEAT\_XNX is not implemented.

Note

XN[1:0], Execute-never, stage 2 only describes the stage 2 control when FEAT\_XNX is implemented.

This field applies to execution at any Exception level to which the stage of translation applies. A value of 0 indicates that this control permits execution.

## PXN, Privileged execute-never, stage 1 only

Descriptor bit[53], used only for stage 1 of any translation regime for which the stage 1 translation can support two VA ranges:

- For stage 1 of a translation regime for which the stage 1 translation supports only a single V A range the stage 1 descriptors define a PXN field that is RES0, meaning it is ignored by hardware.

This field applies only to execution at an Exception level higher than EL0. A value of 0 indicates that this control permits execution.

## XN[1:0], Execute-never, stage 2 only

Descriptor bits[54:53], defined as XN[1:0] for:

- Stage 2 translations when FEAT\_XNX is implemented.

Table G5-10 shows the operation of this control.

## Table G5-10 XN[1:0] stage 2 access permissions model

|   XN[1] |   XN[0] | Access                                                                                                          |
|---------|---------|-----------------------------------------------------------------------------------------------------------------|
|       0 |       0 | The stage 2 control permits execution at EL1 and EL0 if read access is permitted.                               |
|       0 |       1 | The stage 2 control does not permit execution at EL1, but permits execution at EL0 if read access is permitted. |

|   XN[1] |   XN[0] | Access                                                                                                          |
|---------|---------|-----------------------------------------------------------------------------------------------------------------|
|       1 |       0 | The stage 2 control does not permit execution at EL1 or at EL0.                                                 |
|       1 |       1 | The stage 2 control permits execution at EL1 if read access is permitted, but does not permit execution at EL0. |

Note

For stage 2 translations when FEAT\_XNX is not implemented, descriptor bit[53] is RES0, meaning it is ignored by hardware, and bit[54] is the XN control, see XN, Execute-never.

Executing an instruction at ELx in a particular Security state generates a Permission fault unless all of the following are true for the instruction address:

- Any stage 1 execute-never control that applies to execution at ELx in the current Security state permits execution.
- If the translation regime that applies to ELx in the current Security state has two stages of translations, the stage 2 execute-never control that applies to execution at ELx permits execution.
- Read access is permitted.

However, if a stage 1 translation is using the Short-descriptor translation table format and the address is in a Managers domain the stage 1 access permissions are not checked, and therefore the access cannot cause a stage 1 Permission fault, see Domains, Short-descriptor format only.

See also Hyp mode control of Non-secure access permissions.

In addition, System register controls can enforce execute-never restrictions, regardless of the settings in the translation table XN and PXN fields, see:

- Restriction on Secure instruction fetch.
- Preventing execution from writable locations.

The execute-never controls apply also to speculative instruction fetching. This means a speculative instruction fetch from a memory region that is execute-never at the current level of privilege is prohibited.

The execute-never controls means that, when the stage of address translation is enabled, the PE can fetch, or speculatively fetch, an instruction from a memory location only if all of the following apply:

- If using the Short-descriptor translation table format, the Translation Table descriptor for the location does not indicate that it is in a No access domain.
- If using the Long-descriptor translation table format, or using the Short descriptor format and the descriptor indicates that the location is in a Client domain, in the descriptor for the location the following apply:
- -The stage 1 execute-never control for the Exception level at which the instruction is executed permits execution.
- -For a translation regime with two stages of address translation, the stage 2 execute-never control that applies to the Exception level at which the instruction is executed permits execution.
- -The access permissions permit a read access from the current PE mode.
- No other Prefetch Abort condition exists.

Note

- The PXN control applies to the PE privilege when it attempts to execute the instruction. In an implementation that fetches instructions speculatively, this might not be the privilege when the instruction was prefetched. Therefore, the architecture does not require the PXN control to prevent instruction fetching.
- Although the XN control applies to speculative fetching, on a speculative instruction fetch from an XN location, no Permission fault is generated unless the PE attempts to execute the instruction that would have been fetched from that location. This means that, if a speculative fetch from an XN location is attempted, but there is no attempt to execute the corresponding instruction, a Permission fault is not generated.
- The software that defines a translation table must mark any region of memory that is read-sensitive as XN, to avoid the possibility of a speculative fetch accessing the memory region. This means it must mark any memory region that corresponds to a read-sensitive peripheral as XN. Hardware does not prevent speculative accesses to a region of any Device memory type unless that region is also marked as execute-never for all Exception levels from which it can be accessed.
- When using the Short-descriptor translation table format, the XN attribute is not checked for domains marked as Manager. Therefore, the system must not include read-sensitive memory in domains marked as Manager, because the XN field does not prevent speculative fetches from a Manager domain.

When no stage of address translation for the translation regime is enabled, memory regions cannot have XN or PXN attributes assigned. Behavior of instruction fetches when all associated address translations are disabled describes how disabling all MMUs affects instruction fetching.

## G5.6.3.1 Hierarchical control of instruction fetching, Long-descriptor format

The Long-descriptor translation table format introduces a mechanism that means entries at one level of translation tables lookup can set limits on the permitted entries at subsequent levels of lookup. This applies to the restrictions on instruction fetching, and also to the access permissions described in Hierarchical control of access permissions, Long-descriptor format.

## Note

Similar hierarchical controls apply to data accesses, see Hierarchical control of access permissions, Long-descriptor format.

However, in an implementation that includes FEAT\_AA32HPD, when hierarchical control of instruction fetching is disabled for a translation regime, the information in this subsection does not apply. See Attribute fields in VMSAv8-32 Long-descriptor translation table format descriptors.

The restrictions apply only to subsequent levels of lookup at the same stage of translation, and:

- XNTable restricts the XN control:
- -When XNTable is set to 1, the XN field is treated as 1 in all subsequent levels of lookup, regardless of the actual value of the field.
- -When XNTable is set to 0 it has no effect.
- PXNTable restricts the PXN control:
- -When PXNTable is set to 1, the PXN field is treated as 1 in all subsequent levels of lookup, regardless of the actual value of the field.
- -When PXNTable is set to 0 it has no effect.

Note

The XNTable and PXNTable settings are combined with the XN and PXN fields in the Translation Table descriptors accessed at subsequent levels of lookup. They do not restrict or change the values entered in those descriptors.

The XNTable and PXNTable controls are provided only in the Long-descriptor translation table format, and only for stage 1 translations. The corresponding bits are SBZ in the stage 2 Translation Table descriptors.

The effect of XNTable or PXNTable applies to later entries in the translation table walk, and so its effects can be held in one or more TLB entries. Therefore, a change to XNTable or PXNTable requires coarse-grained invalidation of the TLB to ensure that the effect of the change is visible to subsequent memory transactions.

## G5.6.3.2 Preventing execution from writable locations

The architecture provides control bits that, when the corresponding stage 1 address translation is enabled, force writable memory to be treated as XN or PXN, regardless of the value of the XN or PXN field. When the translation stages are controlled by an Exception level that is using AArch32:

- For PL1&amp;0 stage 1 translations, when SCTLR.WXN is set to 1, all regions that are writable at stage 1 of the address translation are treated as XN.
- For PL1&amp;0 stage 1 translations, when SCTLR.UWXN is set to 1, an instruction fetch is treated as accessing a PXNregion if it accesses a region that software executing at EL0 can write to.
- For Non-secure EL2 stage 1 translations, when HSCTLR.WXN is set to 1, all regions that are writable at stage 1 of the address translation are treated as XN.

Note

- The SCTLR.WXN controls are intended to be used in systems with very high security requirements.
- Setting a WXN or UWXN bit to 1 changes the interpretation of the translation table entry, overriding a zero value of an XN or PXN field. It does not cause any change to the translation table entry.

For any given virtual machine, Arm expects WXN and UWXN to remain static in normal operation. In particular, it is IMPLEMENTATION DEFINED whether TLB entries associated with a particular VMID reflect the effect of the values of these fields. A generic sequence to ensure synchronization of a change to these fields, when that change is made without a corresponding change of VMID, is:

```
Change the WXN or UWXN bit ISB ; This ensures synchronization of the change Invalidate entire TLB of associated entries DSB ; This completes the TLB Invalidation ISB ; This ensures instruction synchronization
```

As with all Permission fault checking, if the stage 1 translation is using the Short-descriptor translation table format, the permission checks are performed only for Client domains. For more information, see About access permissions.

For more information about address translation, see About address translation for VMSAv8-32.

## G5.6.3.3 Restriction on Secure instruction fetch

EL3 provides a Secure instruction fetch bit, SCR.SIF. When this bit is 1, any attempt in Secure state to execute an instruction fetched from Non-secure physical memory causes a Permission fault. As with all Permission fault checking, when using the Short-descriptor format translation tables the check applies only to Client domains, see About access permissions.

Arm expects SCR.SIF to be static during normal operation. In particular, whether the TLB holds the effect of the SIF bit is IMPLEMENTATION DEFINED. The generic sequence to ensure visibility of a change to the SIF bit is:

```
Change the SCR.SIF bit ISB ; This ensures synchronization of the change Invalidate entire TLB DSB ; This completes the TLB Invalidation ISB ; This ensures instruction synchronization
```

## G5.6.4 Domains, Short-descriptor format only

Adomain is a collection of memory regions. The Short-descriptor translation table format supports 16 domains, and requires the software that defines a translation table to assign each VMSAv8-32 memory region to a domain. When using the Short-descriptor format:

- Level 1 translation table entries for translation tables and Sections include a domain field.
- Translation table entries for Supersections do not include a domain field. The Short-descriptor format defines Supersections as being in domain 0.

- Level 2 translation table entries inherit a domain setting from the parent level 1 Translation Table descriptor.
- Each TLB entry includes a domain field.

The domain field specifies which of the 16 domains the entry is in, and a two-bit field in the DACR defines the permitted access for each domain. The possible settings for each domain are:

| No access   | Any access using the Translation Table descriptor generates a Domain fault.                                                                                      |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Clients     | On an access using the Translation Table descriptor, the access permission attributes are checked. Therefore, the access might generate a Permission fault.      |
| Managers    | On an access using the Translation Table descriptor, the access permission attributes are not checked. Therefore, the access cannot generate a Permission fault. |

See The MMU fault-checking sequence for more information about how, when using the Short-descriptor translation table format, the Domain attribute affects the checking of the other attributes in the Translation Table descriptor.

Note

Asingle program might:

- Be a Client of some domains.
- Be a Manager of some other domains.
- Have no access to the remaining domains.

The Long-descriptor translation table format does not support domains. When a stage of translation is using this format, all memory is treated as being in a Client domain, and the settings in the DACR are ignored.

## G5.6.5 The Access flag

The Access flag indicates when a page or section of memory is accessed for the first time since the Access flag in the corresponding Translation Table descriptor was set to 0:

- If address translation is using the Short-descriptor translation table format, it must set SCTLR.AFE to 1 to enable use of the Access flag. Setting this bit to 1 redefines the AP[0] bit in the Translation Table descriptors as an Access flag, and limits the access permissions information in the Translation Table descriptors to AP[2:1], as described in AP[2:1] access permissions model.
- The Long-descriptor format always supports an Access flag bit in the Translation Table descriptors, and address translation using this format behaves as if SCTLR.AFE is set to 1, regardless of the value of that bit.

In Armv8.0, the Access flag is managed by software as described in Software management of the Access flag.

Note

Previous versions of the Arm architecture optionally supported hardware management of the Access flag. Armv8.0 obsolete this option. However, FEAT\_HAFDBS provides a new mechanism for hardware management of the Access flag, that is supported only for the VMSAv8-64 translation regimes.

## G5.6.5.1 Software management of the Access flag

Armv8.0 requires that software manages the Access flag. This means an Access flag fault is generated whenever an attempt is made to read into the TLB a Translation Table descriptor entry for which the value of the Access flag is 0.

Note

When using the Short-descriptor translation table format, Access flag faults are generated only if SCTLR.AFE is set to 1, to enable use of a Translation Table descriptor bit as an Access flag.

The Access flag mechanism expects that, when an Access flag fault occurs, software resets the Access flag to 1 in the translation table entry that caused the fault. This prevents the fault occurring the next time that memory location is accessed. Entries with the Access flag set to 0 are never held in the TLB, meaning software does not have to flush the entry from the TLB after setting the flag.

Note

If a system incorporates components that can autonomously update translation table entries that are shared with the Arm PE, then the software must be aware of the possibility that such components can update the access flag autonomously. In such a system, system software should perform any changes of translation table entries with an Access flag of 0, other than changes to the Access flag value, by using an Load-Exclusive/Store-Exclusive loop, to allow for the possibility of simultaneous updates.

## G5.6.6 Hyp mode control of Non-secure access permissions

When EL2 is using AArch32, Non-secure software executing in Hyp mode controls two sets of translation tables, both of which use the Long-descriptor translation table format:

- The translation tables that control the Non-secure EL2 stage 1 translations. These map V As to PAs, for memory accesses made when executing in Non-secure state in Hyp mode, and are indicated and controlled by the HTTBR and HTCR.

These translations have similar access controls to other Non-secure stage 1 translations using the Long-descriptor translation table format, as described in:

- -AP[2:1] access permissions model.
- -Access permissions for instruction execution.

The differences from the Non-secure stage 1 translations are that:

- -The APTable[0], PXNTable, and PXN bits are reserved, SBZ.
- -AP[1] is reserved, SBO.
- The translation tables that control the Non-secure PL1&amp;0 stage 2 translations. These map the IPAs from the stage 1 translation onto PAs, for memory accesses made when executing in Non-secure state at PL1 or EL0, and are indicated and controlled by the VTTBR and VTCR.

The descriptors in the virtualization translation tables define stage 2 access permissions, that are combined with the permissions defined in the stage 1 translation. This section describes this combining of access permissions.

## Note

The level 2 access permissions mean a hypervisor can define additional access restrictions to those defined by a Guest OS in the stage 1 translation tables. For a particular access, the actual access permission is the more restrictive of the permissions defined by:

- The Guest OS, in the stage 1 translation tables.
- The hypervisor, in the stage 2 translation tables.

The stage 2 access controls defined from Hyp mode:

- Affect only the Non-secure stage 1 access permissions settings.
- Take no account of whether the accesses are from a Non-secure PL1 mode or a Non-secure EL0 mode.
- Permit software executing in Hyp mode to assign a write-only attribute to a memory region.

The S2AP field in the stage 2 descriptors define the stage 2 access permissions, as Table G5-11 shows:

## Table G5-11 Stage 2 control of access permissions

|   S2AP | Access permission                                                                           |
|--------|---------------------------------------------------------------------------------------------|
|     00 | No access permitted.                                                                        |
|     01 | Read-only. Writes to the region are not permitted, regardless of the stage 1 permissions.   |
|     10 | Write-only. Reads from the region are not permitted, regardless of the stage 1 permissions. |

|   S2AP | Access permission                                                                    |
|--------|--------------------------------------------------------------------------------------|
|     11 | Read/write. The stage 1 permissions determine the access permissions for the region. |

For more information about the S2AP field, see Attribute fields in VMSAv8-32 Long-descriptor stage 2 Block and Page descriptors.

If the stage 2 permissions cause a Permission fault, this is a stage 2 MMU fault. Stage 2 MMU faults are taken to Hyp mode, and reported in the HSR using an EC code of 0x20 or 0x24 . For more information, see Use of the HSR.

Note

In the HSR, the combination of the EC code and the DFSC or IFSC value in the ISS indicate that the fault is a stage 2 MMUfault.

The stage 2 permissions include an XN attribute. If this identifies the region as execute-never, execution from the region is not permitted, regardless of the value of the XN or UXN attribute in the stage 1 translation. If a Permission fault is generated because the stage 2 XN field identifies the region as execute-never, this is reported as a stage 2 MMU fault.

Note

The stage 2 XN attribute:

- Is a single bit if FEAT\_XNX is not implemented, see XN, Execute-never.
- Is a 2-bit field if FEAT\_XNX is implemented, see XN[1:0], Execute-never, stage 2 only.

AArch32 state prioritization of synchronous aborts from a single stage of address translation describes the abort prioritization if both stages of a translation generate a fault.