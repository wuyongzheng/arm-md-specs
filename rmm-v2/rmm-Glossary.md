## Glossary

ASL


Arm Specification Language Language used to express pseudocode implementations. Formal language definition can be found in tion Language Reference Manual [24].

Arm Specifica-

ATC

Address Translation Cache

ATS

Address Translation Service

CBOR

Concise Binary Object Representation

CCA

Confidential Compute Architecture

CCA platform

All hardware and firmware components which are involved in delivering the CCA security guarantee. See Arm CCA Security model [4].

CDDL

Concise Data Definition Language

CMEM device

Coherent memory device

COSE

CBOR Object Signing and Encryption

CPAK

CCA Platform Attestation Key Key used to sign the CCA platform attestation token.

CXL

Compute eXpress Link

CXL TSP

CXL Trusted Execution Environment Security Protocol

DOE

Data Object Exchange See PCI Express 6.0 specification [16]

DPT

Device Permission Table

DSM

Device Security Manager See PCI Express 6.0 specification [16]

EAT

|            | Entity Attestation Token                                                                                                                                                                 |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ECAM       |                                                                                                                                                                                          |
|            | Enhanced Configuration Access Mechanism See PCI Express 6.0 specification [16]                                                                                                           |
| FAL        |                                                                                                                                                                                          |
|            | Firmware Activity Log                                                                                                                                                                    |
| FID        |                                                                                                                                                                                          |
|            | Function Identifier                                                                                                                                                                      |
| GIC        |                                                                                                                                                                                          |
|            | Generic Interrupt Controller See Arm Generic Interrupt Controller (GIC) Architecture Specification version 3 and                                                                         |
| GPF        |                                                                                                                                                                                          |
|            | Granule Protection Fault                                                                                                                                                                 |
| GPT        |                                                                                                                                                                                          |
| HIPAS Host  Granule Protection Table Table which determines the Physical Address Space of each Granule. Software executing in Non-secure Security state which manages resources used by Realms |
| HDM        |                                                                                                                                                                                          |
|            | Host-managed Device memory                                                                                                                                                               |
| HDM-H      |                                                                                                                                                                                          |
|            | Host-managed Device memory (Host-coherent)                                                                                                                                               |
|            | Host IPA state                                                                                                                                                                           |
| IDE        |                                                                                                                                                                                          |
|            | Integrity and Data Encryption See PCI Express 6.0 specification [16]                                                                                                                     |
| IPA        |                                                                                                                                                                                          |
|            | Intermediate Physical Address Address space visible to software executing at EL1 in the Realm.                                                                                           |
| IPI        |                                                                                                                                                                                          |
|            | Inter-processor interrupt                                                                                                                                                                |
| IRI        |                                                                                                                                                                                          |
|            | Interrupt Routing Infrastructure                                                                                                                                                         |
| ITS        |                                                                                                                                                                                          |
|            | A subset of the components which make up the GIC.                                                                                                                                        |
|            | Interrupt Translation Service A service provided by the GIC.                                                                                                                             |
| LFA        |                                                                                                                                                                                          |

Non-secure Peer-to-peer (device communication) Physical Address Space Physical Device Object which represents a communication channel between the RMM and a physical device, for example a PCIe device.

LOR

Limited Order Region See Arm Architecture Reference Manual for A-Profile architecture [3]

MBZ

Must Be Zero

MEC

Memory Encryption Context

MECID

Memory Encryption Context Identifier

MMIO

Memory-mapped I/O

MPIDR

Multiprocessor Affinity Register

NS

P2P

PAS

PDEV

PE

Processing Element

PMU

Performance Monitor Unit

PPR

PRI Page Request

PRG

Page Request Group

PRI

Page Request Interface

PSCI

Power State Control Interface

See Arm Power State Coordination Interface (PSCI) [28]

PSMMU

|                 | Physical System Memory Management Unit See Arm System Memory Management Unit Architecture Specification [22]   |
|-----------------|----------------------------------------------------------------------------------------------------------------|
| RAK             | Realm Attestation Key Key used to sign the Realm attestation token.                                            |
| RD              | Realm Descriptor Object which stores attributes of a Realm.                                                    |
| Realm           | A protected execution environment                                                                              |
| REM             | Realm Execution Context Object which stores PE state associated with a thread of execution within a Realm.     |
|                 | Realm Extensible Measurement Measurement value which can be extended during the lifetime of a Realm.           |
| RHA RHI RIM RME  Realm Hash Algorithm Realm Host Interface Realm Management Extension                                     |
|                 | Realm Initial Measurement Measurement of the state of a Realm at the time of activation.                       |
| RIPAS           |                                                                                                                |
|                 | Realm IPA state                                                                                                |
| RMI             | Realm Management Interface The ABI exposed by the RMMfor use by the Host. Realm Management Monitor             |
| RMM             | Realm Management Security Domain                                                                               |
| RMSD RNVS       | Root Non-volatile Storage                                                                                      |
| RPV             | Realm Personalization Value                                                                                    |
| RSI             | Realm Services Interface The ABI exposed by the RMMfor use by the                                              |
| RTT             | Realm.                                                                                                         |

| Glossary   |                                                                                                                                             |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------|
|            | Realm Translation Table Object which describes the IPA space of a Realm.                                                                    |
| RTTE       |                                                                                                                                             |
|            | Realm Translation Table Entry                                                                                                               |
| SBZ        |                                                                                                                                             |
|            | Should Be Zero                                                                                                                              |
| SEA        |                                                                                                                                             |
|            | Synchronous External Abort                                                                                                                  |
| SGI        |                                                                                                                                             |
|            | Software Generated Interrupt                                                                                                                |
| SMCCC      |                                                                                                                                             |
|            | SMC Calling Convention                                                                                                                      |
|            | See Arm SMC Calling Convention [23]                                                                                                         |
| SMMU       |                                                                                                                                             |
|            | System Memory Management Unit See Arm System Memory Management                                                                              |
|            | Unit Architecture Specification [22]                                                                                                        |
| SPDM       |                                                                                                                                             |
|             Security Protocol and Data Model See Security Protocol and Data Model (SPDM) [21] and Secured Messages 1.1.0 [17] Trusted Application |
| SPM        |                                                                                                                                             |
|            | Secure Partition Manager                                                                                                                    |
| TA         |                                                                                                                                             |
| TOS        |                                                                                                                                             |
|            | Trusted OS                                                                                                                                  |
| TSE        |                                                                                                                                             |
|            | Target-Side Encryption                                                                                                                      |
| TSM        | Trusted Security Manager                                                                                                                    |
|            | See Chapter A9 Realm device assignment                                                                                                      |
| VDEV       |                                                                                                                                             |
|            | Virtual Device Object which represents the binding between a device function and a Realm.                                                   |
| VMM        |                                                                                                                                             |
|            | Virtual Machine Monitor                                                                                                                     |
| VMSA       |                                                                                                                                             |
|            | Virtual Memory System Architecture                                                                                                          |

VPE

## VSMMU

## Wiping

Virtual Processing Element

Virtual System Memory Management Unit See Arm System Memory Management Unit Architecture Specification [22]

An operation which changes the value of a memory location from X to Y , such that the value X cannot be determined from the value Y

<!-- image -->