## A9.1 Realm device assignment overview

- IDKBCY The RMM allows a device to be assigned to a Realm in a trustworthy manner, allowing the Realm to attest the identity and configuration of the device before it is permitted to access the Realm's memory.

## A9.1.1 Device objects

- IWQVRH From the Host point of view, devices are managed using the following RMM objects:
- Physical Device (PDEV)

Represents a communication channel between the RMM and a physical device, for example a PCIe device.

- Virtual Device (VDEV)

Represents the binding between a device function and a Realm. For example, a VDEV can represent a physical function of a PCIe device or a virtual function of a multi-function PCIe device. Every VDEV is associated with one PDEV.

- Physical SMMU (PSMMU)

Allows the RMM to apply the same stage 2 translations to Realm-assigned devices as for Realm VPEs.

- Virtual SMMU (VSMMU)

Stores the state of an Arm Virtual System Memory Management Unit (VSMMU) which is emulated by the RMM, allowing the Realm to apply stage 1 translation to transactions inititated by assigned device functions.

Interaction between the Host and a PDEV, VDEV and VSMMU objects is performed via RMI commands.

See also:

- A9.2 Physical device object
- A9.4 Virtual device object
- A9.7 Physical SMMU
- A9.8 Virtual SMMU

## A9.1.2 Device properties

DRAFT

- DPTXBK The trust model of a PDEV determines the actions which are necessary for the whole device, or one of its interfaces, to be admitted into the TCB of a Realm. A device trust model is one of the following:
- Selective trust : a Realm makes a decision whether to trust a given VDEV which has been assigned to it. Until and unless the Realm informs the RMM that it trusts the VDEV, the device is not granted access to the Realm's memory.
- Comprehensive trust : all Realms implicitly trust the entire device.

In this version of the specification, the only supported type of comprehensive trust device is a coherent memory device.

- DGRWDX The communication model of a PDEV determines how the RMM communicates management requests to the device. The communication model also constrains the form of device identity evidence used during device assignment. A device communication model is one of the following:
- SPDM communication : communication consists of Security Protocol and Data Model (SPDM) messages, transported via Non-secure memory.
- -Device identity evidence : the device certificate chain.
- Platform communication : communication is performed via a secure IMPLEMENTATION DEFINED channel.
- -Device identity evidence : IMPLEMENTATION DEFINED.

DBKVYM The traffic protection model of a PDEV determines how the confidentiality and integrity of traffic between the SoC and the device is protected. A device traffic protection model is one of the following:

- IDE protection : traffic is protected using the Integrity and Data Encryption (IDE) standard.
- Platform protection : traffic is protected via system construction, for example by restricting physical access to the transport.

Coherent and non-coherent traffic to a given device may be subject to different traffic protection models.

See also:

- PCI Express 6.0 specification [16]
- Secured Messages using SPDM Specification version 1.1.0 [17]
- A9.5 Communication between RMM and a device
- A9.11 Coherent memory devices

## A9.1.3 Device assignment flow

## A9.1.3.1 Assignment of a selective-trust device

- ISZYSK Assignment of a selective-trust device to a Realm involves the following steps:
1. The Host creates and initializes a PDEV object, associated with the target physical device. This causes the following to happen:
- A secure communication channel is established between the RMM and the device. Details depend on the device communication model .
- Protection is configured for traffic between the SoC and the device. Details depend on the device traffic protection model .
- The device identity evidence is provided to the Host. The Host is expected to store this information, and to later present it to the Realm.
- A digest of the device identity evidence is stored by the RMM. This is used later to check integrity of the attestation evidence provided by the Host to the Realm.
2. If communication between the RMM and the device uses SPDM, the Host extracts the public key from the device certificate chain and provides it to the RMM. The RMM verifies that the device to which it has a secure communication channel holds the corresponding private key. The RMM stores a digest of the public key.

DRAFT

3. The Host creates a VDEV object, which represents a binding between a function of the target device, and a Realm. At this stage, the target device is not granted access to the Realm-owned memory.
4. Optionally, the Host maps memory regions of the target device function into the Protected IPA space of the Realm. At this stage, the mappings are invalid, so the Realm cannot yet access the device's memory regions.

Alternatively, the Host can create these mappings later, in response to a request from the guest.

5. The Host requests the RMM to retrieve device attestation evidence (device interface report and device measurements.) The RMM provides the attestation evidence to the Host for caching, and the RMM stores digests of the attestation evidence.

The Realm later requests device attestation evidence from the Host, and verifies that this matches the corresponding digests stored by the RMM.

6. If communication between the RMM and the device uses SPDM, the Realm verifies that the digest of the public key held by the RMM matches the public key in the device certificate chain.
7. The Realm verifies that the negotiation data, device identity evidence, and device measurements are acceptable.

Chapter A9. Realm device assignment A9.1. Realm device assignment overview

8. The Realm requests the RMM to verify that device memory mappings created by the Host match those described in the device interface report. Once each mapping has been verified, it is made valid by the RMM, so the Realm can access the device's memory regions.
9. The Realm instructs the RMM to grant the device access to Realm-owned memory.
3. XRSSXY Requiring the Host to store device attestation evidence means that storage for this information, whose size may not be known ahead of time, does not need to be allocated in RMM memory. The RMM therefore only needs to store a digest of the Host-cached data, which can be used by the Realm to check integrity of data retrieved from the Host.
4. IRBJHR Assignment of a selective-trust device to a Realm is illustrated in the following sequence diagram.

<!-- image -->

Chapter A9. Realm device assignment A9.1. Realm device assignment overview

<!-- image -->

RPYHYC

For a selective-trust device which uses SPDM communication, all of the following are true:

- The device certificate chain digest computed by the RMM is computed over the concatenation of individual X.509 certificates in the chain, without SPDM header and root certificate hash.
- The device certificate chain must meet SPDM requirements.
- The leaf certificate must meet CMA-SPDM requirements.

## A9.1.3.2 Initialization of a comprehensive-trust device

IKLRYY Initialization of a comprehensive-trust device is illustrated in the following sequence diagram.

Figure A9.2: Initialization of a comprehensive-trust device

<!-- image -->