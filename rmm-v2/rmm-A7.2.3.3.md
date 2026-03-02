## A7.2.3.3 CCA platform claims

This section defines the format of the CCA platform token claim map. The format is described using a combination of Concise Data Definition Language (CDDL) and text description.

IFJKFY The CCA platform token claim map is defined as follows:

```
cca-platform-claims = (cca-platform-claim-map) cca-platform-claim-map = { cca-platform-profile cca-platform-challenge cca-platform-implementation-id cca-platform-instance-id cca-platform-config cca-platform-lifecycle cca-platform-sw-components ? cca-platform-verification-service cca-platform-hash-algo-id ? cca-platform-manufacturing-config cca-platform-client-id ? cca-platform-extension }
```

## See also:

- Concise Data Definition Language (CDDL) [12]
- A7.2.3.3.1 CCA platform profile claim
- A7.2.3.3.2 CCA platform challenge claim
- A7.2.3.3.3 CCA platform Implementation ID claim
- A7.2.3.3.4 CCA platform Instance ID claim
- A7.2.3.3.5 CCA platform config claim
- A7.2.3.3.6 CCA platform manufacturing config claim
- A7.2.3.3.7 CCA platform lifecycle claim
- A7.2.3.3.8 CCA platform software components claim
- A7.2.3.3.9 CCA platform verification service claim
- A7.2.3.3.10 CCA platform hash algorithm ID claim
- A7.2.3.3.11 CCA platform client ID claim

DRAFT

- A7.2.3.3.12 CCA platform extension
- A7.2.3.3.13 Collated CDDL for CCA platform claims
- A7.2.3.3.14 Example CCA platform claims

## A7.2.3.3.1 CCA platform profile claim

IFQYTP The CCA platform profile claim identifies the EAT profile to which the CCA platform token conforms. Note that because the platform token is expected to be issued when bound to a Realm token, the profile document should also include the relevant Realm profile or a reference to that profile.

IXMVFR

IGMKNR

The CCA platform profile claim is identified using the EAT profile label (265).

The CCA platform profile claim must be present in a CCA platform token.

IMHRTD The format of the CCA platform profile claim is defined as follows:

```
cca-platform-profile-label = 265 ; EAT profile cca-platform-profile-type = "tag:arm.com,2024:cca_platform#2.0.0" cca-platform-profile = ( cca-platform-profile-label => cca-platform-profile-type )
```

## A7.2.3.3.2 CCA platform challenge claim

ITKTWZ The CCA platform challenge claim contains a hash of the public key used to sign the Realm token.

ICLJKK The CCA platform challenge claim is identified using the EAT nonce label (10).

IXHLYJ The length of the CCA platform challenge is either 32, 48 or 64 bytes.

IGVHNX The CCA platform challenge claim must be present in a CCA platform token.

- ILRWHR The format of the CCA platform challenge claim is defined as follows:

```
cca-hash-type = bytes .size 32 / bytes .size 48 / bytes .size 64 cca-platform-challenge-label = 10 cca-platform-challenge = ( cca-platform-challenge-label => cca-hash-type )
```

## See also:

- A7.2.3.1.10 Realm public key claim

## A7.2.3.3.3 CCA platform Implementation ID claim

ISMWND The CCA platform Implementation ID claim uniquely identifies the implementation of the CCA platform.

```
cca-platform-implementation-id-label = 2396 ; PSA implementation ID cca-platform-implementation-id-type = bytes .size 32 cca-platform-implementation-id = ( cca-platform-implementation-id-label => cca-platform-implementation-id-type )
```

DRAFT INDVFB The value of the CCA platform Implementation ID claim can be used by a verification service to locate the details of the CCA platform implementation from an endorser or manufacturer. Such details are used by a verification service to determine the security properties or certification status of the CCA platform implementation. IRXPVW The semantics of the CCA platform Implementation ID value are defined by the manufacturer or a particular certification scheme. For example, the ID could take the form of a product serial number, database ID, or other appropriate identifier. ISRPZY The CCA platform Implementation ID claim does not identify a particular instance of the CCA implementation. INTCFY The CCA platform Implementation ID claim must be present in a CCA platform token. IDHYDG The format of the CCA platform Implementation ID claim is defined as follows:

## See also:

- Arm CCA Security model [4]
- A7.2.3.3.4 CCA platform Instance ID claim

## A7.2.3.3.4 CCA platform Instance ID claim

IZYRZB The CCA platform Instance ID claim represents the unique identifier of the CCA Platform Attestation Key (CPAK) for the CCA platform.

IXVLLN The CCA platform Instance ID claim is identified using the EAT ueid label (256).

RHVTNC The first byte of the CCA platform Instance ID value must be 0x01 .

IZNGDF The CCA platform Instance ID claim must be present in a CCA platform token.

IVPKJN

IWVQJT

UGPXWX

IMJHQJ

IRQKNX

ICJRBF

IFYFPJ

The format of the CCA platform Instance ID claim is defined as follows:

```
cca-platform-instance-id-type
```

```
cca-platform-instance-id-label = 256 ; EAT ueid ; EAT UEIDs need to be 7 -33 bytes cca-platform-instance-id-type = bytes .size 33 cca-platform-instance-id = ( cca-platform-instance-id-label => )
```

## See also:

- Arm CCA Security model [4]
- A7.2.3.3.3 CCA platform Implementation ID claim

## A7.2.3.3.5 CCA platform config claim

The CCA platform config claim describes the set of chosen implementation options of the CCA platform. As an example, these may include a description of the level of physical memory protection which is provided.

The CCA platform config byte string contains implementation information that is provided by the chip vendor and the device vendor. This is expected to include the following system properties:

- Per-PAS encryption (all RME systems will require this property)
- MEC
- MPE Level
- -L0 (none)
- -L1 (encryption only)
- -L2 (encryption and integrity)
- -L3 (anti-replay)
- RME-DA support
- RME-CDA support

The layout and encoding of this information is IMPLEMENTATION DEFINED.

An attestation verifier should use information from the relevant attestation profile document to understand the IMPLEMENTATION DEFINED choices made for this field.

DRAFT

## The CCA platform config claim must be present in a CCA platform token.

```
cca-platform-config-label = 2401 ; PSA platform range ; TBD: add to IANA registration cca-platform-config-type = bytes cca-platform-config = ( cca-platform-config-label => cca-platform-config-type )
```

## See also:

- RME system architecture spec [15]

## A7.2.3.3.6 CCA platform manufacturing config claim

The CCA platform manufacturing config claim represents a record of production phases and testing conducted during the manufacturing process for this instance.

The CCA platform manufacturing config claim is optional in a CCA platform token.

The format of the CCA platform manufacturing config claim is defined as follows:

```
cca-platform-manufacturing-config-label = 2403 cca-platform-manufacturing-config-type = bytes
```

ISYKFY

RNBFVV

IWFZHV

IQFYLF

```
cca-platform-manufacturing-config = ( cca-platform-manufacturing-config-label => cca-platform-manufacturing-config-type )
```

## A7.2.3.3.7 CCA platform lifecycle claim

The CCA platform lifecycle claim identifies the lifecycle state of the CCA platform.

The value of the CCA platform lifecycle claim is an integer which is divided as follows:

- value[15:8]: CCA platform lifecycle state
- value[7:0]: IMPLEMENTATION DEFINED

The CCA platform lifecycle claim must be present in a CCA platform token.

A non debugged CCA platform will be in psa-lifecycle-secured state. Realm Management Security Domain debug is always recoverable, and would therefore be represented by psa-lifecycle-non-psa-rot-debug state. Root world debug is recoverable on a HES system and would be represented by psa-lifecycle-recoverable-psa-rot state. On a non-HES system Root world debug is usually non-recoverable, and would be represented by psa-lifecycle-lifecycle-decommissioned state.

## IHMZLL The format of the CCA platform lifecycle claim is defined as follows:

```
DRAFT cca-platform-lifecycle-label = 2395 ; PSA lifecycle cca-platform-lifecycle-unknown-type = 0x0000..0x00ff cca-platform-lifecycle-assembly-and-test-type = 0x1000..0x10ff cca-platform-lifecycle-cca-platform-rot-provisioning-type = 0x2000..0x20ff cca-platform-lifecycle-secured-type = 0x3000..0x30ff cca-platform-lifecycle-non-cca-platform-rot-debug-type = 0x4000..0x40ff cca-platform-lifecycle-recoverable-cca-platform-rot-debug-type = 0x5000..0x50ff cca-platform-lifecycle-decommissioned-type = 0x6000..0x60ff cca-platform-lifecycle-type = cca-platform-lifecycle-unknown-type / cca-platform-lifecycle-assembly-and-test-type / cca-platform-lifecycle-cca-platform-rot-provisioning-type / cca-platform-lifecycle-secured-type / cca-platform-lifecycle-non-cca-platform-rot-debug-type / cca-platform-lifecycle-recoverable-cca-platform-rot-debug-type / cca-platform-lifecycle-decommissioned-type cca-platform-lifecycle = ( cca-platform-lifecycle-label => cca-platform-lifecycle-type )
```

## See also:

- Arm CCA Security model [4]

## A7.2.3.3.8 CCA platform software components claim

The CCA platform software components claim is a list of software components which can affect the behavior of the CCA platform. It is expected that an implementation will describe the expected software component values within the profile.

In some implementations, a software component may consist of a configuration data item.

The CCA platform software components claim must be present in a CCA platform token.

IPJCSC

UVDQYM

ITJTXG

A7.2. Realm attestation

IDPSKT

## The format of the CCA platform software components claim is defined as follows:

```
cca-platform-sw-components-label = 2399 ; PSA software components cca-platform-sw-component = { ? 1 => text, ; component type 2 => cca-hash-type, ; measurement value ? 4 => text, ; version 5 => cca-hash-type, ; signer id ? 6 => text, ; hash algorithm identifier ? 7 => bool, ; live firmware activation supported ? 8 => [ + cca-hash-type ], ; list of countersigner ids } cca-platform-sw-components = ( cca-platform-sw-components-label => [ + cca-platform-sw-component ] )
```

## CCA platform software component type

IPDNCF The CCA platform software component type is a string which represents the role of the software component.

ITPSYF The CCA platform software component type is intended for use as a hint to help the relying party understand how to evaluate the CCA platform software component measurement value.

If the CCA platform supports Live Firmware Activation, one entry in the platform software component table is reserved to act as a measurement register for the Firmware Activity Log. This entry is identified by having a software component type of 'FAL'.

The CCA platform software component measurement value represents a hash of the state of the software component in memory at the time it was initialized. The measurement values are implemented such that the values can only be extended rather than set. The values are initialised to 0, so the value reported in attestation will be H( 0 || H(software component)) . If the CCA platform supports Live Firmware Activation then the value reported in attestation may have been further extended by measurements of updates to the software component. In this case, the value of the measurement must be validated by reconstructing the reported value using information from the Firmware Activity Log.

## DRAFT RRSNBH The CCA platform software component type is optional in a CCA platform token. UJJLJT See also: · A3.14 Live Firmware Activation CCA platform software component measurement value IRWDKD

RTVXRZ The CCA platform software component measurement value must be a hash of 256 bits or stronger.

RLGBCM The CCA platform software component measurement value must be present in a CCA platform token.

## CCA platform software component version

IJVJFW The CCA platform software component version is a text string whose meaning is defined by the software component vendor.

RCZRXB The CCA platform software component version is optional in a CCA platform token.

## CCA platform software component signer ID

IDCDMR The CCA platform software component signer ID is the hash of a signing authority public key for the software component. It can be used by a verifier to ensure that the software component was signed by an expected trusted source.

- RPXRMC The CCA platform software component signer ID value must be a hash of 256 bits or stronger.

- RXPHQC

The CCA platform software signer ID must be present in a CCA platform token.

IMBBKC

- IFVDZF The CCA platform software component countersigner ID list is optional in a CCA platform token.

## CCA platform software component hash algorithm ID

- ITQWZX The CCA platform software component hash algorithm ID identifies the hash algorithm used to measure the CCA platform software component.

IHHBHG Arm recommends that the value of the CCA platform software component hash algorithm ID is an IANA Hash Function name IANA Named Information Hash Algorithm Registry [13].

INJYCM Arm recommends that the hash algorithm used to measure the CCA platform software component is one of the algorithms listed in the Arm CCA Security model [4].

IHPHCD The CCA platform software component hash algorithm ID is optional in a CCA platform token.

## CCA platform software component Live Firmware Activation support

- IYYTVP The CCA platform software component Live Firmware Activation support attribute declares whether an individual component is subject to Live Firmware Activation. If the attribute is False, the component will not be updated before the next CCA platform reset.
- ILWQHQ The CCA platform software component Live Firmware activation support attribute is optional in a CCA platform token.

See also:

- A3.14 Live Firmware Activation
- DRAFT CCA platform software component countersigner ID list The CCA platform software component countersigner ID list contains hashes of public keys which identify signing authorities that provides additional trustworthiness information for the software component. These signatures are provided in addition to the primary signature, which is identified by the CCA platform software component signer ID. UWXFDW Example use cases for CCA platform software component countersignatures include: · An indication of approval for the component, provided by the owner of the CCA platform · An indication of approval for the component, provided by a third party auditor UZCPJJ The order of multiple entries within the countersigner ID list may imply a hierarchy. The existence and meaning of any such hierarchy is IMPLEMENTATION DEFINED.

## A7.2.3.3.9 CCA platform verification service claim

- INSTDP The CCA platform verification service claim is a hint which can be used by a relying party to locate a verifier for the token.
- IRZJSQ The value of the CCA platform verification service claim is a text string which can be used to locate the service or a URL specifying the address of the service.

IMFYCX The CCA platform verification service claim may be ignored by a relying party in favor of other information.

- IMRSXY The CCA platform verification service claim is optional in a CCA platform token.
- IWRJSX The format of the CCA platform verification service claim is defined as follows:

```
cca-platform-verification-service-label = 2400 ; PSA verification service cca-platform-verification-service-type = text cca-platform-verification-service = ( cca-platform-verification-service-label => cca-platform-verification-service-type )
```

## A7.2.3.3.10 CCA platform hash algorithm ID claim

IVDZMF The CCA platform hash algorithm ID claim identifies the default algorithm used to calculate measurements in the CCA platform token.

IXHJFX The default hash algorithm may be overridden for an individual software component, by the CCA platform software component hash algorithm ID claim.

IYRPYY Arm recommends that the value of the CCA platform hash algorithm ID claim is an IANA Hash Function name IANA Named Information Hash Algorithm Registry [13].

- ITQSTK The CCA platform hash algorithm ID claim must be present in a CCA platform token.
- IRKZJT The format of the CCA platform hash algorithm ID claim is defined as follows:

```
cca-platform-hash-algo-id-label = 2402 ; PSA platform range ; TBD: add to IANA registration cca-platform-hash-algo-id = ( cca-platform-hash-algo-id-label => text )
```

## A7.2.3.3.11 CCA platform client ID claim

- IPTXFD The CCA platform client ID claim identifies the security domain from which the attestation token was requested.

```
DRAFT IKBVSR In this version of the specification, the only valid value for the CCA platform client ID claim is the Realm Management Security Domain (RMSD). IVYFPY The CCA platform client ID claim must be present in a CCA platform token. ILNXRB The format of the CCA platform client ID claim is defined as follows: cca-platform-client-id-label = 2394 ; PSA namespace cca-platform-client-id-rmsd = 1 ; Realm Management Security Domain cca-platform-client-id-type = cca-platform-client-id-rmsd cca-platform-client-id = ( cca-platform-client-id-label => cca-platform-client-id-type )
```

## A7.2.3.3.12 CCA platform extension

- I0009 The CCA platform extension claim identifies components which have been added to the CCA platform at runtime. An example of such a component is a coherent memory (CMEM) device.

I0010

The CCA platform extension claim is optional in a CCA platform token.

- I0011 The format of the CCA platform extension claim is defined as follows:

```
cca-platform-extension-label = 2404 ; protocols that support VCA $protocols-support-vca /= $protocols-support-vca /= $protocols-support-vca /= $protocols-support-vca /= $protocols-support-vca /= $protocols-support-vca /= $protocols-support-vca /= $protocols-support-vca /=
```

```
"spdm-1.2.0" "spdm-1.2.1" "spdm-1.2.2" "spdm-1.2.3" "spdm-1.3.0" "spdm-1.3.1" "spdm-1.3.2" "spdm-1.4.0"
```

```
cca-platform-extension-device-common = ( ? 1 => text, ; hash algorithm identifier 2 => cca-hash-type, ; device measurements exchange digest 3 => cca-hash-type, ; certificate chain digest 4 => bool, ; indicates whether this PDEV uses IDE ) cca-platform-extension-device = { cca-platform-extension-device-common ( ( ; ----VCA digest required ----5 => $protocols-support-vca, ; protocol, e.g. "spdm-1.2.3" 6 => cca-hash-type, ; SPDM VCA digest ) // ( ; ----no VCA needed ----5 => text ; protocol ) ) } cca-platform-extension = ( cca-platform-extension-label => [ + cca-platform-extension-device ] )
```

- I0016 The CCA platform extension device protocol is a string which represents the protocol used by the RMM to communicate with the device. An example of a protocol is 'spdm-1.2'. If the protocol is SPDM, then vca field is required.
- DRAFT I0012 The CCA platform extension device hash algorithm identifier is a string which identifies the algorithm used by the RMMto hash attestation evidence provided by the device. If this claim is absent then the algorithm is identified by the CCA platform hash algorithm ID claim. I0013 The CCA platform extension device measurement exchange digest is a cca-hash-type value which represents the digest of the device measurements, request and response, exchanged between the device and the RMM. I0014 The CCA platform extension device certificate chain digest is a cca-hash-type value which represents the digest of the device's certificate chain. I0015 The CCA platform extension device IDE indicator is a boolean value which specifies whether the device uses Integrity and Data Encryption (IDE) protection.
- I0017 The CCA platform extension device VCA digest is a cca-hash-type value which represents the digest of the SPDM VCA object. This field is present only when the protocol is SPDM.

## See also:

- A7.2.3.3.10 CCA platform hash algorithm ID claim
- A9.11 Coherent memory devices

## A7.2.3.3.13 Collated CDDL for CCA platform claims

## DDVMJZ The format of the CCA platform token claim map is defined as follows:

```
DRAFT cca-platform-claims = (cca-platform-claim-map) cca-platform-claim-map = { cca-platform-profile cca-platform-challenge cca-platform-implementation-id cca-platform-instance-id cca-platform-config cca-platform-lifecycle cca-platform-sw-components ? cca-platform-verification-service cca-platform-hash-algo-id ? cca-platform-manufacturing-config cca-platform-client-id ? cca-platform-extension } cca-platform-profile-label = 265 ; EAT profile cca-platform-profile-type = "tag:arm.com,2024:cca_platform#2.0.0" cca-platform-profile = ( cca-platform-profile-label => cca-platform-profile-type ) cca-hash-type = bytes .size 32 / bytes .size 48 / bytes .size 64 cca-platform-challenge-label = 10 cca-platform-challenge = ( cca-platform-challenge-label => cca-hash-type ) cca-platform-implementation-id-label = 2396 ; PSA implementation ID cca-platform-implementation-id-type = bytes .size 32 cca-platform-implementation-id = ( cca-platform-implementation-id-label => cca-platform-implementation-id-type ) cca-platform-instance-id-label = 256 ; EAT ueid ; EAT UEIDs need to be 7 -33 bytes cca-platform-instance-id-type = bytes .size 33 cca-platform-instance-id = ( cca-platform-instance-id-label => cca-platform-instance-id-type ) cca-platform-config-label = 2401 ; PSA platform range ; TBD: add to IANA registration cca-platform-config-type = bytes cca-platform-config = ( cca-platform-config-label => cca-platform-config-type ) cca-platform-lifecycle-label = 2395 ; PSA lifecycle cca-platform-lifecycle-unknown-type = 0x0000..0x00ff cca-platform-lifecycle-assembly-and-test-type = 0x1000..0x10ff cca-platform-lifecycle-cca-platform-rot-provisioning-type = 0x2000..0x20ff cca-platform-lifecycle-secured-type = 0x3000..0x30ff cca-platform-lifecycle-non-cca-platform-rot-debug-type = 0x4000..0x40ff
```

```
DRAFT cca-platform-lifecycle-recoverable-cca-platform-rot-debug-type = 0x5000..0x50ff cca-platform-lifecycle-decommissioned-type = 0x6000..0x60ff cca-platform-lifecycle-type = cca-platform-lifecycle-unknown-type / cca-platform-lifecycle-assembly-and-test-type / cca-platform-lifecycle-cca-platform-rot-provisioning-type / cca-platform-lifecycle-secured-type / cca-platform-lifecycle-non-cca-platform-rot-debug-type / cca-platform-lifecycle-recoverable-cca-platform-rot-debug-type / cca-platform-lifecycle-decommissioned-type cca-platform-lifecycle = ( cca-platform-lifecycle-label => cca-platform-lifecycle-type ) cca-platform-sw-components-label = 2399 ; PSA software components cca-platform-sw-component = { ? 1 => text, ; component type 2 => cca-hash-type, ; measurement value ? 4 => text, ; version 5 => cca-hash-type, ; signer id ? 6 => text, ; hash algorithm identifier ? 7 => bool, ; live firmware activation supported ? 8 => [ + cca-hash-type ], ; list of countersigner ids } cca-platform-sw-components = ( cca-platform-sw-components-label => [ + cca-platform-sw-component ] ) cca-platform-verification-service-label = 2400 ; PSA verification service cca-platform-verification-service-type = text cca-platform-verification-service = ( cca-platform-verification-service-label => cca-platform-verification-service-type ) cca-platform-hash-algo-id-label = 2402 ; PSA platform range ; TBD: add to IANA registration cca-platform-hash-algo-id = ( cca-platform-hash-algo-id-label => text ) cca-platform-client-id-label = 2394 ; PSA namespace cca-platform-client-id-rmsd = 1 ; Realm Management Security Domain cca-platform-client-id-type = cca-platform-client-id-rmsd cca-platform-client-id = ( cca-platform-client-id-label => cca-platform-client-id-type ) cca-platform-extension-label = 2404 ; protocols that support VCA $protocols-support-vca /= "spdm-1.2.0" $protocols-support-vca /= "spdm-1.2.1" $protocols-support-vca /= "spdm-1.2.2" $protocols-support-vca /= "spdm-1.2.3"
```

<!-- image -->

```
DRAFT $protocols-support-vca /= "spdm-1.3.0" $protocols-support-vca /= "spdm-1.3.1" $protocols-support-vca /= "spdm-1.3.2" $protocols-support-vca /= "spdm-1.4.0" cca-platform-extension-device-common = ( ? 1 => text, ; hash algorithm identifier 2 => cca-hash-type, ; device measurements exchange digest 3 => cca-hash-type, ; certificate chain digest 4 => bool, ; indicates whether this PDEV uses IDE ) cca-platform-extension-device = { cca-platform-extension-device-common ( ( ; ----VCA digest required ----5 => $protocols-support-vca, ; protocol, e.g. "spdm-1.2.3" 6 => cca-hash-type, ; SPDM VCA digest ) // ( ; ----no VCA needed ----5 => text ; protocol ) ) } cca-platform-extension = ( cca-platform-extension-label => [ + cca-platform-extension-device ] )
```

ITVHKL

## A7.2.3.3.14 Example CCA platform claims

An example CCA platform claim map is shown below in COSE-DIAG format:

```
DRAFT / CCA platform claim map / { / cca-platform-profile / 265: "tag:arm.com,2024:cca_platform#2.0.0", / cca-platform-challenge / 10: h'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', / cca-platform-implementation-id / 2396: h'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', / cca-platform-instance-id / 256: h'010BBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BB', / cca-platform-config / 2401: h'CFCFCFCF', / cca-platform-manufacturing-config / 2403: h'ABABABAB', / cca-platform-lifecycle / 2395: 12288, / cca-platform-sw-components / 2399: [ { / measurement value / 2: h'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', / signer id / 5: h'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', / version / 4: "1.0.0", / hash algorithm identifier / 6: "sha-256" }, { / measurement value / 2: h'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC',
```

```
DRAFT / signer id / 5: h'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD', / version / 4: "1.0.0", / hash algorithm identifier / 6: "sha-256" } ], / cca-platform-verification-service / 2400: "https://cca_verifier.org", / cca-platform-hash-algo-id / 2402: "sha-256", / cca-platform-client-id / 2394: 1, / cca-platform-extension / 2404: [ { / hash algorithm identifier / 1: "sha-256", / measurement exchange digest / 2: h'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', / certificate chain digest / 3: h'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', / device uses IDE / 4: true, / protocol / 5: "spdm-1.2.0", / VCA digest / 6: h'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB' } ] }
```