## 13.1 SMMU handling of attributes

## 13.1.1 Attribute definitions

A transaction has the attributes that are defined by the Arm architecture [2]:

| Attribute             | Shorthand   | Values                                                                                                                          |
|-----------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------|
| Memory Type           | MT          | Normal i{WB, WT, NC}-o{WB, WT, NC} - generally Normal, Device-{GRE, nGRE, nGnRE, nGnRnE} - generally any-Device.                |
| Shareability          | SH          | Non-shareable (NSH),Inner shareable (ISH), Outer shareable (OSH) Note: Device types and Normal iNC-oNC are considered to be OSH |
| Read Allocation hint  | RA          | Inner read allocate/no-allocate, Outer read allocate/no-allocate                                                                |
| Write Allocation hint | WA          | Inner write allocate/no-allocate, Outer write allocate/no-allocate                                                              |
| Transient hint        | TR          | Inner transient/non-transient, Outer transient/non-transient                                                                    |
| Read/Write            | R/W         | Read, Write                                                                                                                     |
| Inst/Data             | INST        | Instruction, Data                                                                                                               |
| Privilege             | PRIV        | Privileged/Unprivileged                                                                                                         |
| Non-secure            | NS          | Secure, Non-secure                                                                                                              |

## Key:

- i = Inner,
- o = Outer,
- WB=Write-Back cacheable,
- WT=Write-Through cacheable,
- NC = Non-Cacheable,

In this specification, a Normal memory type is expressed as:

- iNC-oNC, or
- i{ NC, {WB, WT}/[n]RA[n]WA[n]TR }-o{ NC, {WB, WT}/[n]RA[n]WA[n]TR }-{NSH,ISH,OSH}

(Syntax: {a,b} = Choose one of a or b, [x] = x is optional.)

## This means that:

- Normal-iWB/RAnWATR-oNC-ISH:
- -Is Inner writeback cacheable/Read-Allocate/no-Write-Allocate/transient, outer non-cacheable inner-shareable.
- -The (outer) NC type has no RA/WA or TR attributes.
- Normal-iWB/RAWAnTR-oWB/RAWAnTR-OSH:
- -Is inner/outer writeback read/write allocate non-transient, outer-shareable.
- Normal-iNC-oNC
- -Is architecturally non-cacheable, always OSH
- -NC has no RA/WA or TR attributes.

Note: System shareable is an AMBA interconnect term and is not used in this specification. Device memory is OSH according to the Arm architecture, but the AMBA interconnect Device type is System shareable. Similarly, a PE Normal-iNC-oNC attribute becomes Non-Cacheable System shareable in AMBA interconnect. Armv8-A memory attribute terminology is used in this specification.

While some interconnects might support an IMPLEMENTATION DEFINED subset of these attributes, R/W is mandatory.

The R/W, INST and PRIV attributes are used to check transaction permissions against the read/write and execute access permissions returned by the translation process. Some memory systems might also use INST, PRIV, RA, WAand TR attributes to influence cache allocation or prioritization policies but such usage is outside the scope of this specification.

Some interconnects support atomic transactions. These are treated as performing both a data read and a write for permission checking purposes independent of STE.INSTCFG. For Event records generated due to atomic accesses:

- In the event of a permission fault due to having write access but not read access, including the case where a descriptor is writable-clean, the value of the F\_PERMISSION event's RnW field is:
- -SMMUV3.0: IMPLEMENTATION DEFINED.
- -SMMUv3.1 and later: 1.
- Note: In the event of a permission fault in response to not having write access, or having no access, the F\_PERMISSION event is recorded with RnW == 0.
- For all other causes that trigger F\_PERMISSION, and for all other event types, RnW == 0.
- For the purposes of setting the RnW, DirtyBit and Overlay bits in an F\_PERMISSION record, the SMMU follows the permissions checks priority order where write permission is checked before read permission.

When the SMMU supports Secure state, the output NS attribute is used by the memory system to distinguish between Secure PA space and Non-secure PA space. At stage 1, distinction between Secure and Non-secure addresses is used to check against SMMU\_S\_CR0.SIF.

The access permission attributes of an incoming transaction are only used by the SMMU to enforce access permissions against the permissions determined by translation table descriptors and SMMU\_S\_CR0.SIF. They do not interact with the memory type in any way.

Note: In AArch32 state, a PE is permitted to raise a Permission fault when an instruction fetch is made to Device memory and execute-never is not set. The SMMU does not raise a Permission fault in this case, and the output attribute remains Device. An access is permitted if the permission checks succeed, regardless of the final memory type.

## 13.1.2 Attribute support

The SMMU defines behavior for all architected attributes. However, where an interconnect from the SMMU to the memory system supports only a subset of these attributes, the SMMU is not required to generate attributes that it does not use. With the exception of R/W, INST, and PRIV all configuration fields that affect unused attributes are IGNORED.

When SMMU\_S\_IDR1.SECURE\_IMPL == 1:

- Override fields that are associated with the input NS attribute might be supported.
- Any transaction that belongs to a Non-secure stream targets the Non-secure PA space.

When SMMU\_S\_IDR1.SECURE\_IMPL == 0:

- Override fields that are associated with the input NS attribute are not supported.
- Where supported by the memory system, all transactions target the Non-secure PA space.

If an interconnect supports attributes but does not differentiate inner and outer in the same way as the architecture, the mapping onto the architecturally-defined set of attributes is IMPLEMENTATION DEFINED.

In some implementations, a client device might request translation services from an SMMU and later perform transactions separately, based on the translations and attributes determined by the SMMU. The behavior of the client device transactions with respect to attributes presented to the system are outside the scope of the SMMU architecture. Where such a client device does not support certain memory types or attributes that are returned by the SMMUtranslation process, behavior on accesses with these memory types is defined by the device implementation. However, the page permission protection model of the SMMU translations must always be fully observed.

Note: For example, a client device must never use a read-only translation to issue a write transaction into the system. If a client device does not support a particular memory type, a valid behavior might be to alter the type in an architecturally-safe manner. This could be strengthening a Device-GRE access to a Device-nGnRnE access. If this is not possible, another valid behavior might be for the client device to abort the access in a client device-specific manner.

Note: A composite device that contains an SMMU, such as an intelligent accelerator, is conceptually identical to a client device making requests of an external SMMU.

The SMMU makes its own accesses to memory, for example to fetch configuration or perform translation table walks. Each access has a memory type and attributes that are configured using SMMU registers or structure fields. Where an SMMU and the memory system support only a subset of memory types, and where access to an unsupported type can be reported to the SMMU, the SMMU will record an external abort for the cause of the access in question in the architected manner. If such an access is instigated by an incoming transaction, the transaction will be terminated with an abort.

A fetch from unsupported memory types generates the following fault and errors:

| • STE:                      | F_STE_FETCH                                  |
|-----------------------------|----------------------------------------------|
| • CD:                       | F_CD_FETCH                                   |
| • Command queue read entry: | GERROR.CMDQ_ERR and Command queue CERROR_ABT |
| • Event queue access:       | GERROR.EVENTQ_ABT_ERR                        |
| • PRI queue access:         | GERROR.PRIQ_ABT_ERR                          |
| • MSIs:                     | GERROR.MSI_*_ABT_ERR                         |
| • Translation table walk:   | F_WALK_EABT                                  |

Arm strongly recommends that an SMMU supports all architected access types (for both its own structure accesses and for client transactions) so that it is compatible with generic driver software.

The SMMU considers all incoming writes to be Data, even if the client device marks the incoming write as Instruction. This is done on input, prior to any translation table permission checks. In addition, STE.INSTCFG and SMMU\_(S\_)GBPA.INSTCFG can only change the instruction/data marking of reads.

If an implementation provides INST and PRIV as output attributes to the memory system, then:

- SMMU-originated accesses are always represented as Data, Privileged. This includes:
- -All reads that originate from the SMMU, for example a structure fetch.
- -All SMMU writes of output queue data and MSIs.
- For client-originated transactions the following applies:
- -For SMMUv3.3 and earlier, the INST attribute reflects the output of the INSTCFG field for reads and is fixed as Data for writes. The PRIV attribute reflects the output of the PRIVCFG field.
- -For SMMUv3.4 and later the attributes are always Data, Privileged.

## 13.1.3 Default input attributes

Where the SMMU is not supplied with an attribute because the interconnect between the client device and SMMU does not have the ability to convey it, the SMMU constructs a default input value:

| Attribute   | Input generated as:   |
|-------------|-----------------------|
| MT          | Normal iWB-oWB        |
| SH          | NSH                   |
| RA          | Allocate              |
| WA          | Allocate              |
| TR          | Non-transient         |
| INST        | Data                  |
| PRIV        | Unprivileged          |
| NS          | Non-secure            |

These values are used when any configuration path is set to 'Use incoming' attribute, but the attribute is not supplied. For example, if the incoming attributes are Normal-iNC-oNC or any-Device and MTCFG/MemAttr override this to Normal-iWB-oWB, but ALLOCCFG is set to 'Use incoming', then because no allocation hints are supplied with these memory types, the default value of Read-Allocate, Write-Allocate, Non-transient is applied to both inner and outer allocation hints.

Note: The SMMU architecture only includes configuration of inner and outer properties for the Cacheability of a memory type. No separate inner or outer configuration is provided for RA, WA or TR in any location aside from the translation table descriptor. Attribute overrides for RA, WA and TR affect both inner and outer allocation and transient hints at the same time.

## 13.1.4 Replace

The Replace operation discards any input attribute, replacing a specific attribute with a configured value. For example, the SMMU\_GBPA.SHCFG field allows the input Shareability to be discarded and replaced by NSH/ISH/OSH values, or used directly without override, for the purposes of global bypass when the SMMU is disabled.

In this specification, the term Override refers to a configuration field that causes an attribute to be replaced with a specific value.

The STE fields INSTCFG, PRIVCFG, NSCFG, SHCFG, ALLOCCFG, MTCFG/MemAttr contain override fields that can cause individual input attributes to be replaced with values given in these fields. The effects of STE overrides depend on the transaction type issued to the SMMU. The effects of INSTCFG and PRIVCFG are summarised in Table 13.4. The effects of NSCFG, MTCFG/MemAttr, SHCFG, and ALLOCCFG are summarised in Table 13.5.

Table 13.4: STE.{PRIVCFG, INSTCFG} overrides.

| Transaction type                       | STE.PRIVCFG   | STE.INSTCFG   | Notes                                  |
|----------------------------------------|---------------|---------------|----------------------------------------|
| Ordinary untranslated read transaction | Applies       | Applies       | See STE.PRIVCFG and STE.INSTCFG.       |
| RCI                                    | Applies       | Applies       | See section 3.22.2 Permissions model . |
| DR                                     | Applies       | Applies       | See section 3.22.2 Permissions model . |
| Speculative transaction                | Applies       | Applies       |                                        |

| Transaction type                        | STE.PRIVCFG                                                                                                                  | STE.INSTCFG                                                                                                                  | Notes                                                                                                          |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Ordinary untranslated write transaction | Applies                                                                                                                      | Ignored, always Data                                                                                                         | See STE.PRIVCFG and STE.INSTCFG.                                                                               |
| Far Atomic operation                    | Applies                                                                                                                      | Ignored, always Data                                                                                                         | See section 16.7.6 Far Atomic operations .                                                                     |
| W-DCP                                   | Applies                                                                                                                      | Ignored, always Data                                                                                                         | See section 3.22.2 Permissions model .                                                                         |
| NW-DCP                                  | Applies                                                                                                                      | Ignored, always Data                                                                                                         | See section 3.22.2 Permissions model .                                                                         |
| ATS Translation Request                 | Applies                                                                                                                      | Applies                                                                                                                      | See sections 3.9.1.2 Responses to ATS Translation Requests and 13.7 PCIe permission attribute interpretation . |
| ATS Translated Transaction              | Applies if split-stage or if SMMU_IDR3.PASIDTT is 1 and transaction has a PASID TLP prefix, otherwise IMPLEMENTATION DEFINED | Applies if split-stage or if SMMU_IDR3.PASIDTT is 1 and transaction has a PASID TLP prefix, otherwise IMPLEMENTATION DEFINED | See sections 3.9.1.3 Handling of ATS Translated transactions 13.7 PCIe permission attribute interpretation .   |
| ATOS                                    | Ignored, PnU taken from ATOS_ADDR                                                                                            | Ignored, InD taken from ATOS_ADDR                                                                                            | See section Chapter 9 Address Translation Operations .                                                         |
| CMOs                                    | Applies                                                                                                                      | Applies                                                                                                                      | See section 16.7.2.2 Permissions model for Cache Maintenance Operations .                                      |

Table 13.5: STE.{NSCFG, MTCFG/MemAttr, SHCFG, ALLOCCFG} overrides.

| Transaction type             | STE.NSCFG   | STE.MTCFG/MemAttr STE.SHCFG                        | STE.MTCFG/MemAttr STE.SHCFG                        | STE.ALLOCCFG                                       | Notes                                                         |
|------------------------------|-------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|---------------------------------------------------------------|
| Untranslated transaction (1) | Applies     | For PCIe, IMPLEMENTATION DEFINED otherwise applies | For PCIe, IMPLEMENTATION DEFINED otherwise applies | For PCIe, IMPLEMENTATION DEFINED otherwise applies | See STE.MTCFG, STE.MemAttr, STE.SHCFG, STE.ALLOCCFG.          |
| ATS Translation Request      | Applies     | IMPLEMENTATION DEFINED                             | IMPLEMENTATION DEFINED                             | IMPLEMENTATION DEFINED                             | See section 3.9.1.2 Responses to ATS Translation Requests .   |
| ATS Translated Transaction   | Applies     | Ignored                                            | Ignored                                            | IMPLEMENTATION DEFINED                             | See section 3.9.1.3 Handling of ATS Translated transactions . |
| ATOS                         | Ignored     | Ignored                                            | Ignored                                            | Ignored                                            | See section Chapter 9 Address Translation Operations .        |

(1) This includes all Untranslated transactions that are issued by the client device including, ordinary reads/writes, RCI, DR, CMOs, W-DCP, NW-DCP, Far Atomics and speculative transactions.

Similar fields in SMMU\_(S\_)GBPA allow override of attributes when transactions globally bypass.

Whether overrides from STE or SMMU\_(S\_)GBPA fields take effect is indicated by SMMU\_IDR1.ATTR\_TYPES\_OVR and SMMU\_IDR1.ATTR\_PERMS\_OVR. See SMMU\_IDR1 and the field descriptions in Stream Table Entry for more information.

When stage 1 translation is used, memory type attributes that are provided by translation table entries replace the attributes provided by the input transaction and any input overrides, if appropriate.

This operation is represented by replace\_attrs() in pseudocode.

Global or STE input overrides are not permitted to make output attributes inconsistent. Because allocation and transient hints are only relevant to Normal cacheable memory types, their overrides in either SMMU\_(S\_)GBPA or in the STEs do not affect memory types that are not Normal-WB or Normal-WT. The override value is ignored. Similarly, an input type of Device or Normal-iNC-oNC, whether supplied by the client device or overridden in SMMU\_(S\_)GBPA or in the STE, will always be OSH regardless of any SHCFG override.

When an input transaction provides a memory type that is not cacheable and an STE or GBPA input override changes the inner or outer type to a cacheable type, the input RA, WA and TR attributes are taken to be 'RA, WA, nTR' (consistent with 13.1.3 Default input attributes ), unless these attributes are also overridden.

## 13.1.5 Combine

The result of combining one attribute value with another is governed by rules that are similar to those that apply to SMMUv2 [4] and the Arm Architecture's [2] combining of stage 1 and stage 2 attributes. The SMMUv3 behavior is the same as that of a PE in that stage 2 translation, when enabled, combines its attribute with those from stage 1, or with the incoming attributes when stage 1 is not enabled.

This operation is represented by combine\_attrs() in pseudocode.

Note: The SMMUv3 behavior with respect to Read-Allocate, Write-Allocate and transient hints with stage 2 differs from SMMUv2 in that SMMUv3 has no stage 2 overrides of RA/WA/TR. However, an order of precedence is defined here to make the pseudocode clearer.

The permission-related attributes (R/W, INST, PRIV, NS) are not subject to combine operations. These attributes are only used in the SMMU to check against each enabled stage of translation descriptor permissions. Only MT, SH, RA/WA and TR are combined.

Figure 13.1 shows the order of strength for each attribute. When combined, the operation takes the stronger of the values presented.

Figure 13.1: Attributes and their order of strength

<!-- image -->

The order for allocate and transient hints is chosen so that allocate and non-transient are the normal cases that are pulled down for no-allocate or transient special cases.

## 13.1.5.1 Combine examples

Normal-iWB/RAWAnTR-oNC-ISH + Device-nGnRE = Device-nGnRE

Device-nGnRE + Device-nGnRnE = Device-nGnRnE

Normal-iWB/RAWAnTR-oNC-ISH + Normal-iWT/RAWAnTR-oWT/RAnWATR-OSH

= Normal-iWT/RAWAnT-oNC-OSH

- (Note: outer non-transient even though onTR+oTR = oTR, as outer non-cacheable - see below.)

## 13.1.6 Stage 2 control of memory types and cacheability

Armv8.4 [2] adds the ability for a stage 2 translation to override a stage 1 memory type and Cacheability in order to force a virtual machine access to be a Normal-WB shareable type regardless of the stage 1 configuration.

This feature is supported if SMMU\_IDR3.FWB == 1.

This feature is enabled for a particular stream by setting STE.S2FWB == 1. When enabled, the behavior is as described for the FWB feature in Armv8.4 [2].

Note: The S2FWB bit is per-stream, but is cacheable in the TLB (see section 5.2 Stream Table Entry). In effect, the FWB property is specific to a particular VMID.

S2FWB affects the attribute of a translation that is returned using ATOS.

For PCI Express systems, transactions with the No\_snoop attribute are not affected by STE.S2FWB. See section 13.6.1.1 No\_snoop .

Note: To achieve the effect of all transactions relating to a PCIe function being forced to be coherent WB cacheable, then No\_snoop must be disabled in the configuration space of the function and the SMMU configured with STE.S2FWB == 1.

This operation is represented by the function combine\_attrs\_fwb() in the pseudocode.

The 2022 Memory Tagging extensions [2] introduced FEAT\_MTE\_PERM that affects the interpretation of the stage 2 MemAttr field when FWB is enabled or disabled. See section 3.23.1 SMMU support for FEAT\_MTE\_PERM .

## 13.1.7 Ensuring consistent output attributes

The SMMU does not allow the output of inconsistent attribute combinations. If overrides, translation table configuration or bad input results in inconsistent attributes, the SMMU ensures consistency:

- Any-Device and Normal iNC-oNC are output as Outer Shareable
- For Normal types, NC at either inner or outer cache level have no RA/WA or TR attributes at that level. A non-cached access is considered to be read-no-allocate, write-no-allocate, non-transient, regardless of programmed read/write allocate and transient configuration.
- For Normal types, a cacheable type that is read-no-allocate and write-no-allocate has no TR attribute. Such a type is considered to be non-transient, regardless of any input or programmed override configuration.

This also applies to the result of ATOS translation operations. See Chapter 9 Address Translation Operations .

Note: In addition to these architectural attribute consistency rules, an implementation might include interconnect-specific consistency rules. See section 16.7.5 SMMU and AMBA attribute differences .