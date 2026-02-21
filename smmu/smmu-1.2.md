## 1.2 Terms and abbreviations

This specification uses the following terms and abbreviations.

Address Space ID, distinguishing TLB entries for separate address spaces. For example, address spaces of PE processes are distinguished by ASID.

SMMU facility providing VA-to-IPA/PA translations using system-accessible registers. In addition, VATOS provides a second set of registers for direct use from a virtual machine, with the added constraint that only VA-to-IPA translations can be returned.

## ASID

## ATOS

## ATS

PCI Express [1] term for Address Translation Services provided for remote endpoint TLBs

## ATS Translated transaction

A memory transaction input to the SMMU, in which the supplied address has been translated. In PCIe this is indicated with the AT TLP field value 0b10 . For more information see 3.9 Support for PCI Express, PASIDs, PRI, and ATS .

## Bypass

## CD

## Completer

An agent in a computing system that responds to and completes a memory transaction that was initiated by a Requester.

## CONSTRAINED UNPREDICTABLE

Where an instruction can result in UNPREDICTABLE behavior, the architecture specifies a narrow range of permitted behaviors. This range is the range of CONSTRAINED UNPREDICTABLE behavior. All implementations that are compliant with the architecture must follow the CONSTRAINED UNPREDICTABLE behavior. In body text, the term CONSTRAINED UNPREDICTABLE is shown in SMALL CAPITALS.

## DVM

## E2H

## EI

A configuration that passes through a stage of translation without any addresses transformation is using bypass. If an SMMU does not implement a translation stage, that stage is considered equivalent to a bypass configuration.

Context Descriptor.

## Client device

A device whose incoming traffic to the system is controlled by an SMMU.

Distributed Virtual Memory, a protocol for interconnect messages to provide broadcast TLB maintenance operations (among other things).

EL2 Host Mode. The Virtualization Host Extensions in Armv8.1 [2] extend the EL2 translation regime providing ASID-tagged translations. In this specification, EL2-E2H mode is the abbreviation that is used.

Embedded Implementation. For more information see 3.16 Embedded Implementations .

## Endpoint (EP)

A PCI Express [1] function, used in the context of a device that is a client of the SMMU.

## GPC

## GPC fault

GPF

GPT

HTTU

## IGNORED

ILLEGAL

A set of conditions that make an STE or CD structure illegal. These conditions differ for the individual CDs and STEs, and are described in detail in the relevant CD and STE descriptions. A field in a structure can make the structure ILLEGAL, for example when it contains an incorrect value, only if the field was not IGNORED for other reasons. Attempts to use an ILLEGAL structure generate an error that is specific to the type of structure.

## IMPLEMENTATION DEFINED

Means that the behavior is not architecturally defined, but must be defined and documented by individual implementations. For more information, see [2]. In body text, the term IMPLEMENTATION DEFINED is shown in SMALL CAPITALS.

## IMPLEMENTATION SPECIFIC

Behavior that is not defined by the SMMU architecture, and might not be documented by individual implementations. Used where one of a number of implementation options might be chosen and the option chosen does not affect software compatibility. Software cannot rely on any IMPLEMENTATION SPECIFIC behavior.

IPA

L1CD

L1STD

LPAE

MBZ

Granule Protection Check

AGranule Protection Check fault, arising either because a Granule Protection Table lookup could not be completed, or because the lookup was successful and the access being checked failed the check.

Granule Protection Fault. The fault reported when a Granule Protection Table lookup is successful, but the access being checked fails the Granule Protection Check.

Granule Protection Table. An in-memory structure that describes the association of a Location and a PA space.

Hardware Translation Table Update. The act of updating the Access flag or dirty state of a page in a given descriptor which is automatically done in hardware, on an access or write to the corresponding page.

Indicates that the architecture guarantees that the bit or field is not interpreted or modified by hardware. In body text, the term IGNORED is shown in SMALL CAPITALS.

Intermediate Physical Address

Level-1 Context Descriptor. Used in a 2-level CD table.

Level-1 Stream Table Descriptor. Used in a 2-level Stream table.

Large Physical Address Extension. The ARMv7 'Long' translation table format, supporting 40-bit output addresses (and 40-bit IPAs) and having 64-bit descriptors - identical to the VMSAv8-32 translation table format.

Must Be Zero. Used in DPT descriptor formats. If a descriptor field described as MBZ is non-zero, the descriptor is Invalid. For more information, see 3.24.4 DPT lookup errors .

## MPAM

## Nested

## PASID

## PRI

PCI Express term for Page Request Interface, an extension to ATS allowing an endpoint to request an OS to make a paged virtual memory mapping present for DMA.

## Processing Element (PE)

The abstract machine defined in the Arm architecture, as documented in an Arm Architecture Reference Manual [2]. A PE implementation compliant with the Arm architecture must conform with the behaviors described in the corresponding Arm Architecture Reference Manual.

## RC

## Requester

## RES0

## RES1

## Reserved

## SEC\_SID

Memory System Resource Partitioning And Monitoring, part of the Armv8.4-A architecture [3].

A configuration that enables both stage 1 and stage 2 translation.

## NoStreamID device

An SMMU client device that is not associated with a StreamID.

## PA

Physical Address

## PARTID, PMG

MPAM partition and performance monitoring group identifiers.

PCI Express [1] term, a Process Address Space ID. Note: a PASID is an endpoint-local ID so there might be many distinct uses of a specific PASID value in a system. Despite the similarity in name, a PCIe PASID is not the same as a PE ASID, which is intended to be unique within the scope of an Operating System.

PCI Express Root Complex [1]

An agent in a computing system that is capable of initiating memory transactions.

A Reserved bit or field with Should-Be-Zero-or-Preserved (SBZP) behavior, or equivalent read-only or write-only behavior. Used for fields in register descriptions, and for fields in architecturally-defined data structures that are held in memory, for example in translation table descriptors. For a full description see [2].

A Reserved bit or field with Should-Be-One-or-Preserved (SBOP) behavior. Used for fields in register descriptions, and for fields in architecturally-defined data structures that are held in memory, for example in translation table descriptors. For a full description see [2].

Unless otherwise specified, a Reserved field behaves as RES0. For an identification, or otherwise read-only register field, a Reserved encoding is never given by the SMMU. For a field that is provided to the SMMU, Reserved values must not be used and their behavior must not be relied upon.

StreamID Security state. The identifer used to associate the StreamID in transactions from a client device with a specific Security state, and therefore determining which SMMU programming interface is responsible for configuration for the stream. See section 3.10.1 StreamID Security state (SEC\_SID) .

## SMMU

System MMU. Unless otherwise specified, this term is used to mean SMMUv3. Any reference to prior versions of the SMMU specifications is explicitly suffixed with the architecture version number, for example SMMUv1.

## Split-stage ATS

SMMU facility used with two-stage translation, providing a way to use ATS with stage 1 and use non-ATS translation for stage 2.

## Stage 1, Stage 2

One of the two stages of translation whereby the output of one set of translation tables can be fed into a second set of translation tables. In sequence, stage 1 is the first table indexed, stage 2 is the second. Each stage can be independently enabled. Stage 1 translates a V A to an IPA. Stage 2 translates an IPA to a PA.

## Stage N-only

A translation configuration for a stream of data in which one of two translation stages is configured to translate and the other is in bypass (whether by configuration or fixed by SMMU implementation).

## STE

## Terminate

## TR

## TT

## TTD

## TTW

## UNKNOWN

An UNKNOWN value does not contain valid data, and can vary from moment to moment and implementation to implementation. An UNKNOWN value must not return information that cannot be accessed at the current or a lower level of privilege of operating software using accesses that are not UNPREDICTABLE and do not return UNKNOWN values. An UNKNOWN value must not be documented or promoted as having a defined value or effect. In body text, the term UNKNOWN is shown in SMALL CAPITALS.

## UNPREDICTABLE

Means the behavior cannot be relied upon. UNPREDICTABLE behavior must not perform any function that cannot be performed at the current or a lower level of privilege using instructions that are not UNPREDICTABLE. UNPREDICTABLE behavior must not be documented or promoted as having a defined effect. In body text, the term UNPREDICTABLE is shown in SMALL CAPITALS.

## Untranslated transaction.

Stream Table Entry.

To complete a transaction with a negative status/abort response; the exact details depend on an implementation's interconnect behavior. When a client transaction is said to have been terminated by the SMMU, it has been prevented from progressing into the system and an abort response has been issued to the client (if appropriate for the interconnect in use).

Translation Request, used in the context of a PCIe ATS request to the SMMU, or another distributed implementation making translation requests to a central unit.

Translation table, synonymous with Page Table, as used by Arm architecture.

Translation table descriptor , synonymous with Page Table Entry, as used by the Arm architecture

Translation Table Walk. This is the act of performing a translation by traversing the in-memory tables.

## VA

VM

## VMID

## VMS

Virtual Machine Structure. Data structure containing per-VM information.

## 1.2.1 Inclusive Terminology Commitment

Arm values inclusive communities. Arm recognizes that we and our industry have used terms that can be offensive. Arm strives to lead the industry and create change.

Previous issues of this specification included terms that can be offensive. We have replaced these terms.

If you find offensive terms in this specification, please contact terms@arm.com.

A memory transaction input to the SMMU, in which the supplied address has not been translated. In PCIe this is indicated with the AT TLP field value 0b00 . For more information see 3.9 Support for PCI Express, PASIDs, PRI, and ATS .

Virtual Address

Virtual Machine. In this specification, VM never means Virtual Memory except when used as part of an existing acronym.

Virtual Machine ID, distinguishing TLB entries for addresses from separate virtual machines