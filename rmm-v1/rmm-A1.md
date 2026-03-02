## Chapter A1 Overview

The RMM is a software component which forms part of a system which implements the Arm Confidential Compute Architecture (Arm CCA). Arm CCA is an architecture which provides protected execution environments called Realms .

The threat model which Arm CCA is designed to address is described in Introducing Arm CCA [1].

The hardware architecture of Arm CCA is called the Realm Management Extension (RME), and is described in Arm Architecture Reference Manual Supplement, The Realm Management Extension (RME), for Armv9-A [2].

## A1.1 Confidential computing

The Armv8-A architecture ( Arm Architecture Reference Manual for A-Profile architecture [3]) includes mechanisms that establish a privilege hierarchy. Software operating at higher privilege levels is responsible for managing the resources (principally memory and processor cycles) that are used by entities at lower privilege levels.

Prior to Arm CCA, resource management was coupled with a right of access. That is, a resource that is managed by a higher-privileged entity is also accessible by it. A Realm is a protected execution environment for which this coupling is broken, so that the right to manage resources is separated from the right to access those resources.

The purpose of a Realm is to provide to the Realm owner an environment for confidential computing, without requiring the Realm owner to trust the software components that manage the resources used by the Realm.

Construction of a Realm, and allocation of resources to a Realm at runtime, are the responsibility of the Virtual Machine Monitor (VMM). In this specification, the term Host is used to refer to the VMM.

See also:

- A2.1 Realm

## A1.2 System software components

The system software architecture of Arm CCA is summarised in the following figure.

Figure A1.1: System software architecture

<!-- image -->

The components shown in the diagram are listed below.

| Component                      | Description                                                                                                                             |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Monitor                        | The most privileged software component, which is responsible for switching between the Security states used at EL2, EL1 and EL0.        |
| Realm                          | A protected execution environment.                                                                                                      |
| Realm Management Monitor (RMM) | The software component which is responsible for the management of Realms.                                                               |
| Virtual Machine (VM)           | An execution environment within which an operating system can run. Note that a Realm is a VMwhich executes in the Realm security state. |
| Hypervisor                     | The software component which is responsible for the management of VMs.                                                                  |
| Secure Partition Manager (SPM) | The software component which is responsible for the management of Secure Partitions.                                                    |
| Trusted OS (TOS)               | An operating system which runs in a Secure Partition.                                                                                   |
| Trusted Application (TA)       | An application hosted by a TOS.                                                                                                         |

## A1.3 Realm Management Monitor

The Realm Management Monitor (RMM) is the system component that is responsible for the management of Realms.

The responsibilities of the RMM are to:

- Provide services that allow the Host to create, populate, execute and destroy Realms.
- Provide services that allow the initial configuration and contents of a Realm to be attested.
- Protect the confidentiality and integrity of Realm state during the lifetime of the Realm.
- Protect the confidentiality of Realm state during and following destruction of the Realm.

The RMM exposes the following interfaces, which are accessed via SMC instructions, to the Host:

- The Realm Management Interface (RMI), which provides services for the creation, population, execution and destruction of Realms.

The RMM exposes the following interfaces, which are accessed via SMC instructions, to Realms:

- The Realm Services Interface (RSI), which provides services used to manage resources allocated to the Realm, and to request an attestation report.
- The Power State Coordination Interface (PSCI), which provides services used to control power states of VPEs within a Realm. Note that the HVC conduit for PSCI is not supported for Realms.

The RMM operates by manipulating data structures which are stored in memory accessible only to the RMM.

See also:

- Chapter B4 Realm Management Interface
- Chapter B5 Realm Services Interface
- Chapter B6 Power State Control Interface