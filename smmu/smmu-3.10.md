## 3.10 Security states support

The Arm architecture provides support for two Security states, each with an associated physical address space (PA space):

| Security state   | PA space             |
|------------------|----------------------|
| Secure state     | Secure (NS == 0)     |
| Non-secure state | Non-secure (NS == 1) |

The SMMU always supports the Non-secure state and programming interface.

The Realm Management Extension, FEAT\_RME, introduces two new security states, each with an associated physical address space:

| Security state   | PA space   |
|------------------|------------|
| Secure state     | Secure     |
| Non-secure state | Non-secure |
| Realm state      | Realm      |
| Root state       | Root       |

## 3.10.1 StreamID Security state (SEC\_SID)

StreamID Security state (SEC\_SID) determines the Security state of the programming interface that controls a given transaction.

The association between a device and the Security state of the programming interface is a system-defined property.

If SMMU\_S\_IDR1.SECURE\_IMPL == 0, then incoming transactions have a StreamID, and either:

- A SEC\_SID identifier with a value of 0.
- No SEC\_SID identifer, and SEC\_SID is implicitly treated as 0.

If SMMU\_S\_IDR1.SECURE\_IMPL == 1, incoming transactions have a StreamID, and a SEC\_SID identifier.

|   SEC_SID | Meaning                                                                            |
|-----------|------------------------------------------------------------------------------------|
|         0 | The StreamID is a Non-secure stream, and indexes into the Non-secure Stream table. |
|         1 | The StreamID is a Secure stream, and indexes into the Secure Stream table.         |

In this specification, the terms Secure StreamID and Secure stream refer to a stream that is associated with the Secure programming interface, as determined by SEC\_SID.

The terms Non-secure StreamID and Non-secure stream refer to a stream that is associated with the Non-secure programming interface, which might be determined by SEC\_SID or the absence of the SEC\_SID identifier.

Note: Whether a stream is under Secure control or not is a different property to the target PA space of a transaction. If a stream is Secure, it means that it is controlled by Secure software through the Secure Stream table. Whether a transaction on that stream results in a transaction targeting Secure PA space depends on the translation table attributes of the configured translation, or, for bypass, the incoming NS attribute.

For an SMMU with RME DA, the encoding of SEC\_SID is extended to 2 bits, and has the following encoding:

| SEC_SID   | Meaning    |
|-----------|------------|
| 0b00      | Non-secure |
| 0b01      | Secure     |
| 0b10      | Realm      |
| 0b11      | Reserved   |

Transactions with a SEC\_SID value of Realm are associated with the Realm programming interface.

## 3.10.2 Support for Secure state

SMMU\_S\_IDR1.SECURE\_IMPL indicates whether an SMMU implementation supports the Secure state.

When SMMU\_S\_IDR1.SECURE\_IMPL == 0:

- The SMMU does not support the Secure state.
- SMMU\_S\_* registers are RAZ/WI to all accesses.
- Support for stage 1 translation is OPTIONAL.

When SMMU\_S\_IDR1.SECURE\_IMPL == 1:

- The SMMU supports the Secure state.
- SMMU\_S\_* registers configure Secure state, including a Secure Command queue, Secure Event queue and a Secure Stream table.
- The SMMU supports stage 1 translation and might support stage 2 translation.
- The SMMU can generate transactions to the memory system, to Secure PA space (NS == 0) and Non-secure PA space (NS == 1) where permitted by SMMU configuration.

The Non-secure StreamID namespace and the Secure StreamID namespace are separate namespaces. The assignment of a client device to either a Secure StreamID or a Non-secure StreamID, and reassignment between StreamID namespaces, is system-defined.

With the exception of SMMU\_S\_INIT, SMMU\_S\_* registers are Secure access only, and RAZ/WI to Non-secure accesses.

Note: Arm does not expect a single software driver to be responsible for programming both the Secure and Non-secure interface. However, the two programming interfaces are intentionally similar.

When a stream is identified as being under Secure control according to SEC\_SID, see 3.10.1 StreamID Security state (SEC\_SID) , its configuration is taken from the Secure Stream table or from the global bypass attributes that are determined by SMMU\_S\_GBPA.

Otherwise, its configuration is taken from the Non-secure Stream table or from the global bypass attributes that are determined by SMMU\_GBPA.

The Secure programming interface and Non-secure programming interface have separate global SMMUEN translation-enable controls that determine whether bypass occurs.

A transaction that belongs to a Stream that is under Secure control can generate transactions to the memory system that target Secure (NS == 0) and Non-secure (NS == 1) PA spaces. A transaction that belongs to a Stream that is under Non-secure control can only generate transactions to the memory system that target Non-secure (NS == 1) PA space.

| Security state   | Permitted target PA spaces   |
|------------------|------------------------------|
| Secure           | Secure, Non-secure           |
| Non-secure       | Non-secure                   |

## 3.10.2.1 Secure commands, events and configuration

In this specification, the term Event queue and the term Command queue refer to the queue that is appropriate to the Security state of the relevant stream. Similarly, the term Stream table and Stream Table Entry (STE) refer to the table or table entry that is appropriate to the Security state of the stream as indicated by SEC\_SID.

For instance:

- An event that originates from a Secure StreamID is written to the Secure Event queue.
- An event that originates from a Non-secure StreamID is written to the Non-secure Event queue.
- Commands that are issued on the Non-secure Command queue only affect streams that are configured as Non-secure.
- Some commands that are issued on the Secure Command queue can affect any stream or data in the system.
- The stream configuration for a Non-secure StreamID X is taken from the X th entry in the Non-secure Stream table.
- Stream configuration for a Secure StreamID Y is taken from the Y th entry in the Secure Stream table.

The Non-secure programming interface of an SMMU with SMMU\_S\_IDR1.SECURE\_IMPL == 1 is identical to the interface of an SMMU with SMMU\_S\_IDR1.SECURE\_IMPL == 0.

Note: To simplify descriptions of commands and programming, this specification refers to the Non-secure programming interface registers, Stream table, Command queue and Event queue even when SMMU\_S\_IDR1.SECURE\_IMPL == 0.

The register names associated with the Non-secure programming interface are of the form SMMU\_x . The register names associated with the Secure programming interface are of the form SMMU\_S\_x . In this specification, where reference is made to a register but the description applies equally to the Secure or Non-secure version, the register name is given as SMMU\_(S\_)x . Where an association exists between multiple Non-secure, or multiple Secure registers and reference is made using the SMMU\_(S\_)x syntax, the registers all relate to the same Security state unless otherwise specified.

The two programming interfaces operate independently as though two logical and separate SMMUs are present, with the exception that some commands issued on the Secure Command queue and some Secure registers might affect Non-secure state, as indicated in this specification. This independence means that:

- The Command and Event queues that are associated with a programming interface operate independently of the Command and Event queues that are associated with the other programming interface. The operation of one does not affect the other programming interface, for example when:
- -The queues are full.
- -The queues overflow.
- -The queues experience an error condition, for example a Command queue that stops processing because of a command error, or an abort on queue access.
- Translation through each programming interface can be separately enabled and disabled using the SMMUEN field that is associated with the particular programming interface. This means that one interface might bypass transactions in which case the behavior is governed by the respective SMMU\_(*\_)GBPA and the other programming interface might translate transactions.
- Error conditions in SMMU\_(*\_)GERROR apply only to the programming interface with which the register is associated.
- Each interface has its own ATOS interface, where ATOS is implemented.

- Interrupts are configured and enabled separately for the Secure and Non-secure programming interface interrupt sources.

When SMMU\_S\_IDR1.SECURE\_IMPL == 1, Arm expects that the SMMU will be controlled by a PE that also implements Secure state. The host PE might:

- Implement Armv7-A.
- Implement Armv8-A, with EL3 using AArch64 state.
- Implement Armv8-A, with EL3 using AArch32 state.

StreamWorld differentiates the Secure EL1 translation regime from the EL3 translation regime, allowing TLB entries to be maintained separately for each of these two translation regimes. Secure EL1 TLB entries might be tagged with an ASID, whereas EL3 TLB entries are not. In this case, Arm expects that the Secure SMMU interface is either:

- Managed by Secure EL1, with no SMMU usage by EL3.
- Managed by EL3 with any EL1 usage brokered to EL3 using a software interface, which is outside the scope of this specification.

Arm recommends that Secure EL1 and EL3 do not attempt to both access the Secure Command queue. Arm further recommends that Secure EL1 does not configure streams to cause TLB entries to be marked as EL3.

For a PE that implements Armv8-A and uses AArch32 state in EL3 or a PE that implements Armv7-A, there is only one privileged Secure translation regime. No separation is made between TLB entries inserted for Secure OS and Secure monitor software. When a client device is associated with this type of Secure system, Arm recommends that the StreamWorld is configured as Secure so that resulting TLB entries that are associated with this Secure translation regime are ASID-tagged. In this case, Arm recommends that StreamWorld is not configured to insert EL3 TLB entries, because broadcast TLB invalidation from the PE would not be able to affect these TLB entries. For more information, see section 3.17 TLB tagging, VMIDs, ASIDs and participation in broadcast TLB maintenance .

A client device with a Secure StreamID provides an input attribute called NS that indicates whether an access is intended to be to a Secure or Non-secure address. A Secure STE might override the input NS attribute of a Secure stream.

In bypass configurations of a Secure stream, overriding the input NS attribute allows a client device to issue Secure accesses even if the device is not able to control the input NS attribute. If the input NS attribute is not overridden, the client device can control whether it makes accesses to the Secure or Non-secure PA spaces. In the case where Secure stage 1 is disabled and Secure stage 2 translation is enabled, the input NS attribute distinguishes between Secure and Non-secure IPA spaces.

When a Secure STE is configured for stage 1 only translation, the stage 1 translation table descriptor (in conjunction with intermediate NSTable bits) determines the output NS attribute if the translation table descriptor is fetched from Secure memory, in the same way as in a PE and in the SMMUv2 architecture [4]. See Chapter 13 Attribute Transformation . A Secure STE can also be configured for stage 2 translation, if supported. See section 3.10.2.2 Secure EL2 and support for Secure stage 2 translation ,

A Non-secure STE does not override the input NS attribute, which is treated as Non-secure for all transactions belonging to a Non-secure stream.

Access to the Secure Stream table, the Secure Event queue and the Secure Command queue are always made to the Secure PA space.

For access to L1CDs and CDs, then the use of Secure IPA or PA space applies at the appropriate stage:

- If Secure stage 2 is not in use, L1CD and CD addresses are treated as Secure physical addresses.
- If Secure stage 2 is enabled, L1CD and CD addresses are translated through the Secure IPA space. See section 3.10.2.2 Secure EL2 and support for Secure stage 2 translation .

Some SMMU commands take a StreamID parameter. When issued to the Secure Command queue, an additional parameter, SSec, indicates whether the SMMU interprets the command as applying to a Secure or a Non-secure StreamID.

The SMMU\_S\_CR0.SIF flag provides a mechanism to terminate instruction fetches from Secure streams that target Non-secure PAs or Non-secure IPAs in some configurations. See section 6.3.57.2 SIF for details.

## 3.10.2.2 Secure EL2 and support for Secure stage 2 translation

SMMUv3.2 introduces support for a Secure EL2 translation regime, corresponding with that in an Armv8.4 PE.

A Secure STE can be configured with Config[1] set to 1 to enable stage 2 translation if Secure stage 2 is implemented.

Support for Secure EL2 and Secure stage 2 is optional for implementations supporting SMMUv3.2 or later. An implementation might support Secure EL2 and Secure stage 2, if the implementation also supports both stage 1 and stage 2. The following implementation options are supported:

|   SMMU_S_IDR1.SECURE_IMPL | SMMU_S_IDR1.SEL2   | Result                                                                        |
|---------------------------|--------------------|-------------------------------------------------------------------------------|
|                         0 | X                  | Secure programming interface absent. Secure state is not supported.           |
|                         1 | 0                  | Secure EL2 is not supported. Secure stage 2 is not supported.                 |
|                         1 | 1                  | Secure EL2 is supported. Secure stage 2 is supported for use by a Secure STE. |

In the same way as described in Armv8.4, the result of a Secure stage 1 translation is an address in one of two address spaces, for Secure IPA and a Secure stream Non-secure IPA. The Secure stream Secure IPA space corresponds to a stage 1 output targeting Secure IPA space. The Secure stream Non-secure IPA space corresponds to a stage 1 output of a Secure stream targeting Non-secure IPA space. A Secure stream Non-secure IPA space is translated differently to a Non-secure stream IPA space. A Secure stage 2 supports two translation tables, corresponding to input from each of the two IPA spaces.

For a Secure stream with stage 2 translation enabled, the final transaction PA space is determined at stage 2 from the S2SW, S2SA, S2NSW and S2NSA configuration of the selected Secure stream IPA spaces as follows:

- If the input into stage 2 is a Secure IPA, the Secure stream Secure IPA space is used for translation. The translation table configured in STE.S\_S2TTB is used. The translation table accesses are made to the Secure or Non-secure PA space configured in STE.S2SW. If STE.S2SW == 0, then the final output PA space is determined by by STE.S2SA, otherwise the final output PA space is Non-secure.
- If the input into stage 2 is a Non-secure IPA, the Secure stream Non-secure IPA space is used for translation. The translation table configured in STE.S2TTB is used. The translation table accesses are made to the Secure or Non-secure PA space configured in STE.S2NSW. If STE.S2SW == 0 and STE.S2SA == 0 and STE.S2NSW == 0, then the final output PA space is determined by STE.S2NSA. Otherwise the final output PA space is Non-secure.

For a Non-secure stream, translation table accesses and final output PA space is always Non-secure.

A Secure translation regime with stage 1 and stage 2 configured fetches the L1CD and CD using a Secure IPA.

For a Secure stage 2-only translation (resulting from STE.Config == 0b110 or from STE.S1DSS causing stage 1 to be skipped), the choice of whether the IPA is in Non-secure or Secure IPA space after stage 1 bypass is determined from the result of the STE.NSCFG field.

For a Secure EL2 translation table walk, the target PA space of the initial level of walk is given by CD.NSCFG{0,1}, depending on the translation table used.

Note: An S-EL2 StreamWorld uses one translation table, CD.TTB0 and an S-EL2-E2H StreamWorld might use two translation tables, CD.TTB0 and CD.TTB1.

The S-EL2 and S-EL2-E2H translation regimes are only used in CD.AA64 == 1 configuration. A Secure STE with stage 2 translation enabled is not permitted to have STE.S2AA64 select VMSAv8-32 LPAE.

When stage 2 translation is disabled, all Secure IPA accesses become Secure PA accesses, and all Secure stream Non-secure IPA accesses become Non-secure PA accesses.

A Secure translation regime that supports Secure stage 2 configuration uses a VMID tag for TLB entries. This is a Secure VMID and is a distinct namespace from the Non-secure VMID namespace. When Secure stage 2 is implemented then TLB entries inserted from StreamWorld == Secure configurations are:

- Tagged with the VMID from STE.S2VMID when stage 2 is enabled.
- Tagged with VMID 0 when stage 2 is not enabled.
- -Note: These entries are affected by corresponding TLB invalidation operations that target VMID 0. See section 3.17 TLB tagging, VMIDs, ASIDs and participation in broadcast TLB maintenance .
- -Note: This behavior differs from that of the Non-secure S2VMID field because the STE.S2VMID field was IGNORED in Secure STEs before SMMUv3.2.

Consistent with Armv8.4, a translation table entry fetched for a Secure stream is treated as non-global if it is read from the Non-secure IPA space. That is, these entries are treated as if nG == 1, regardless of the value of the nG bit in the descriptor. See section 3.17.1 The Global flag in the translation table descriptor .

## 3.10.3 Support for Realm state

The Realm translation regimes are:

- The same as the Realm translation regimes in the Armv9-A architecture.
- Supported only when VMSAv8-64 or VMSAv9-128 translation tables are used.

The SMMU also supports Stream disabled and Stream bypass configuration for Realm state.

The size of a StreamID parameter for Realm state is the same as for Non-secure state, as advertised in SMMU\_IDR1.SIDSIZE.

Consistent with the Realm translation regimes in FEAT\_RME [2], the output physical address space of a transaction on a Realm stream is as follows:

| Configuration                               | Output address space determination                 |
|---------------------------------------------|----------------------------------------------------|
| Stream bypass, and bypass due to STE.S1DSS. | See 3.10.3.3 Realm stream bypass .                 |
| EL1 stage 1 only                            | Output PA space is always Realm.                   |
| EL1 stage 1 and 2                           | Output PA space determined by stage 2 translation. |
| EL1 stage 2 only                            | Output PA space determined by stage 2 translation. |
| EL2 or EL2-E2H stage 1                      | Output PA space determined by stage 1 translation. |

A Realm L1STD has the same format and meaning as a Non-secure L1STD, except that L1STD.L2Ptr is a Realm physical address.

Unless otherwise specified, a Realm STE has the same format and meaning as a Non-secure STE, except that all pointers from a Realm STE are Realm addresses.

Realm L1CD has the same format and meaning as a Non-secure L1CD, except that L1CD.L2Ptr for a Realm L1CD is a Realm address.

Realm CD has the same format and meaning as a Non-secure CD, except that CD.TTB0 and CD.TTB1 for a Realm CD are Realm addresses.

Note: This means CD.NSCFG0 and CD.NSCFG1 are IGNORED for a Realm stream.

For all commands issued to a Realm Command queue, then:

- The command applies to Realm SEC\_SID only.
- Any command with a StreamID is interpreted as a Realm StreamID.
- SSec == 1 gives CERROR\_ILL.

For more details, see 16.4.1 System integration for an SMMU with RME DA .

## 3.10.3.1 Input NS attribute

For a Realm stream, the input NS attribute distinguishes between Non-secure and Realm.

This applies for untranslated transactions, translated transactions, and translation requests.

If the client device does not provide an input NS attribute, the input NS attribute takes a default value of Realm.

For example, in AMBA the distinction between Realm and Non-secure address spaces is made with the NSE signal.

For PCIe-related behaviors, see 3.9.4 SMMU interactions with the PCIe fields T, TE and XT .

## 3.10.3.2 Realm stream disabled

Note: If SMMU\_R\_CR0.SMMUEN is 1 and a Realm STE is configured with STE.Config == 0b000 , that stream is disabled.

Realm stream disabled is consistent with the stream disabled behavior of Non-secure state.

Note: This means that if a Realm stream is disabled then transactions are terminated with an abort.

## 3.10.3.3 Realm stream bypass

Note: If SMMU\_R\_CR0.SMMUEN is 1, and a Realm STE is configured with STE.Config == 0b100 , that stream is in stream bypass mode.

The requirements in this subsection also apply when translation is bypassed as a result of STE.S1DSS configuration.

Realm stream bypass is consistent with the behavior of stream bypass for Non-secure state, except that the output physical address space for a transaction is derived by applying the STE.NSCFG configuration to the the input NS attribute.

Note: Transactions for a Realm StreamID that is configured for stream bypass can still result in:

- F\_ADDR\_SIZE.
- F\_PERMISSION, if an instruction access targets Non-secure PA space.
- F\_BAD\_ATS\_TREQ for ATS translation requests.
- F\_TRANSL\_FORBIDDEN for ATS Translated transactions.
- Granule protection check faults.

Note: In Realm stream bypass mode, client-originated transactions are still associated with the MECID configured in STE.MECID.