## Glossary

ASL

Arm Specification Language

Language used to express pseudocode implementations. Formal language definition can be found in Arm Specifica- tion Language Reference Manual [14].

CBOR

Concise Binary Object Representation

CCA

Confidential Compute Architecture

CCA platform

All hardware and firmware components which are involved in delivering the CCA security guarantee. See Arm CCA Security model [4].

CDDL

Concise Data Definition Language

COSE

CBOR Object Signing and Encryption

EAT

Entity Attestation Token

FID

Function Identifier

GIC

Generic Interrupt Controller

See Arm Generic Interrupt Controller (GIC) Architecture Specification version 3 and version 4 [5]

GPF

Granule Protection Fault

GPT

Granule Protection Table Table which determines the Physical Address Space of each Granule.

HIPAS

Host IPA state

Host

Software executing in Non-secure Security state which manages resources used by Realms

IAK

Initial Attestation Key Key used to sign the CCA platform attestation token.

IPA

Intermediate Physical Address Address space visible to software executing at EL1 in the Realm.

IPI

Inter-processor interrupt

IRI

Interrupt Routing Infrastructure A subset of the components which make up the GIC.

ITS

Interrupt Translation Service A service provided by the GIC.

MBZ

Must Be Zero

MMIO

Memory-mapped I/O

MPIDR

Multiprocessor Affinity Register

NS

Non-secure

PAS

Physical Address Space

PE

Processing Element

PMU

Performance Monitor Unit

PSCI

Power State Control Interface See Arm Power State Coordination Interface (PSCI) [16]

RAK

Realm Attestation Key Key used to sign the Realm attestation token.

RD

Realm Descriptor Object which stores attributes of a Realm.

Realm

A protected execution environment

REC

Realm Execution Context Object which stores PE state associated with a thread of execution within a Realm.

REM

Realm Extensible Measurement Measurement value which can be extended during the lifetime of a Realm.

## Glossary

| RHA      | Realm Hash Algorithm                                                                     |    |
|----------|------------------------------------------------------------------------------------------|----|
| RIM      |                                                                                          |    |
| RIPAS    | Realm Initial Measurement Measurement of the state of a Realm at the time of activation. |    |
|          | Realm IPA state                                                                          |    |
| RMM      | Realm Management Interface The ABI exposed by the RMMfor use by the Host.                |    |
| RNVS RPV | Realm Management Monitor                                                                 |    |
|          | Root Non-volatile Storage                                                                |    |
| RSI      | Realm Personalization Value                                                              |    |
| RTT      | Realm Services Interface The ABI exposed by the RMMfor use by the Realm.                 |    |
|          | Realm Translation Table Object which describes the IPA space of a Realm.                 |    |
| RTTE     | Realm Translation Table Entry                                                            |    |
| SBZ      | Should Be Zero                                                                           |    |
| SEA      | Synchronous External Abort                                                               |    |
| SGI      | Software Generated Interrupt                                                             |    |
| SMCCC    | SMC Calling Convention See Arm SMC Calling Convention [13]                               |    |
| SPM      |                                                                                          |    |
|          | Secure Partition Manager                                                                 |    |
| TOS      |                                                                                          |    |
|          | Trusted OS                                                                               |    |
| VMM      |                                                                                          |    |
|          | Trusted Application                                                                      |    |
|          |                                                                                          | TA |

Glossary

Virtual Machine Monitor

VMSA

Virtual Memory System Architecture

VPE

Virtual Processing Element

Wiping

An operation which changes the value of a memory location from X to Y , such that the value X cannot be determined from the value Y