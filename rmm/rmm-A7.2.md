## A7.2 Realm attestation

This section describes the primitives which are used to support remote Realm attestation.

## A7.2.1 Attestation token

A CCA attestation token is a collection of claims about the state of a Realm and of the CCA platform on which the Realm is running.

- A CCA attestation token consists of two parts:
- Realm token

Contains attributes of the Realm, including:

- -Realm Initial Measurement
- -Realm Extensible Measurements
- CCA platform token

Contains attributes of the CCA platform on which the Realm is running, including:

- -CCA platform identity
- -CCA platform lifecycle state
- -CCA platform software component measurements

The size of a CCA attestation token may be greater than 4KB.

See also:

- A7.1.1 Realm Initial Measurement
- A7.1.2 Realm Extensible Measurement

## A7.2.2 Attestation token generation

- The process for a Realm to obtain an attestation token is:
- Call RSI\_ATTESTATION\_TOKEN\_INIT once
- Call RSI\_ATTESTATION\_TOKEN\_CONTINUE in a loop, until the result is not RSI\_INCOMPLETE

Each call to RSI\_ATTESTATION\_TOKEN\_CONTINUE retrieves up to one Granule of the attestation token.





The following pseudocode illustrates the process of a Realm obtaining an attestation token.

```
int get_attestation_token(...) { int ret; uint64_t size, max_size; uint64_t buf, granule; ret = RSI_ATTESTATION_TOKEN_INIT(challenge, &max_size); if (ret) { return ret; } buf = alloc(max_size); granule = buf; do { // Retrieve one Granule of data per loop iteration uint64_t offset = 0; do { // Retrieve sub-Granule chunk of data per loop iteration size = GRANULE_SIZE -offset; ret = RSI_ATTESTATION_TOKEN_CONTINUE(granule, offset, size, &len); offset += len; } while (ret == RSI_INCOMPLETE && offset < GRANULE_SIZE); // "offset" bytes of data are now ready for consumption from "granule" if (ret == RSI_INCOMPLETE) { granule += GRANULE_SIZE; } } while ((ret == RSI_INCOMPLETE) && (granule < buf + max_size)); return ret; }
```

Up to one attestation token generation operation may be ongoing on a REC.

On execution of RSI\_ATTESTATION\_TOKEN\_INIT, if an attestation token generation operation is ongoing on the calling REC, it is terminated.

- The challenge value provided to RSI\_ATTESTATION\_TOKEN\_INIT is included in the generated attestation token. This allows the relying party to establish freshness of the attestation token.

If the size of the challenge provided by the relying party is less than 64 bytes, it should be zero-padded prior to calling RSI\_ATTESTATION\_TOKEN\_INIT. Arm recommends that the challenge should contain at least 32 bytes of unique data.

- Generation of an attestation token can be a long-running operation, during which interrupts may need to be handled.


If a physical interrupt becomes pending during execution of RSI\_ATTESTATION\_TOKEN\_CONTINUE, a REC exit due to IRQ can occur.

On the next entry to the REC:

- If a virtual interrupt is pending on that REC, it is taken to the REC's exception handler
- RSI\_ATTESTATION\_TOKEN\_CONTINUE returns RSI\_INCOMPLETE
- The REC should call RSI\_ATTESTATION\_TOKEN\_CONTINUE again

## See also:

- A4.3.5 REC exit due to IRQ
- A6.1 Realm interrupts

- A7.2.3.1.1 Realm challenge claim
- B5.3.1 RSI\_ATTESTATION\_TOKEN\_CONTINUE command
- B5.3.2 RSI\_ATTESTATION\_TOKEN\_INIT command
- D1.7.1 Attestation token generation flow
- D1.7.2 Handling interrupts during attestation token generation flow

## A7.2.3 Attestation token format

- The CCA attestation token is a profiled IETF Entity Attestation Token (EAT).
- The CCA attestation token is a Concise Binary Object Representation (CBOR) map, in which the map values are the Realm token and the CCA platform token.
- The Realm token contains structured data in CBOR, wrapped with a COSE\_Sign1 envelope according to the CBOR Object Signing and Encryption (COSE) standard.
- The Realm token is signed by the Realm Attestation Key (RAK).
- The CCA platform token contains structured data in CBOR, wrapped with a COSE\_Sign1 envelope according to the COSE standard.
- The CCA platform token is signed by the Initial Attestation Key (IAK).
- The CCA platform token contains a hash of RAK\_pub. This establishes a cryptographic binding between the Realm token and the CCA platform token.
- The CCA attestation token is defined as follows:
- The composition of the CCA attestation token is summarised in the following figure.

```
cca-token = #6.399(cca-token-collection) ; CMW Collection ; (draft-ietf-rats-msg-wrap) cca-platform-token = bstr .cbor COSE_Sign1_Tagged cca-realm-delegated-token = bstr .cbor COSE_Sign1_Tagged cca-token-collection = { 44234 => cca-platform-token ; 44234 = 0xACCA 44241 => cca-realm-delegated-token } ; EAT standard definitions COSE_Sign1_Tagged = #6.18(COSE_Sign1) ; Deliberately shortcut these definitions until EAT is finalised and able to ; pull in the full set of definitions COSE_Sign1 = "COSE-Sign1 placeholder"
```

## See also:

- Arm CCA Security model [4]
- Concise Binary Object Representation (CBOR) [6]
- CBOR Object Signing and Encryption (COSE) [7]
- Entity Attestation Token (EAT) [8]
- A7.2.3.1 Realm claims
- A7.2.3.2 CCA platform claims

Figure A7.1: Attestation token format

<!-- image -->


## A7.2.3.1 Realm claims

This section defines the format of the Realm token claim map. The format is described using a combination of Concise Data Definition Language (CDDL) and text description.

The Realm token claim map is defined as follows:

```
cca-realm-claims = (cca-realm-claim-map) cca-realm-claim-map = { cca-realm-challenge ? cca-realm-profile cca-realm-personalization-value cca-realm-initial-measurement cca-realm-extensible-measurements cca-realm-hash-algo-id cca-realm-public-key cca-realm-public-key-hash-algo-id }
```

## See also:

- Concise Data Definition Language (CDDL) [9]
- A7.2.3.1.1 Realm challenge claim
- A7.2.3.1.2 Realm profile claim
- A7.2.3.1.3 Realm Personalization Value claim
- A7.2.3.1.4 Realm Initial Measurement claim
- A7.2.3.1.5 Realm Extensible Measurements claim
- A7.2.3.1.6 Realm hash algorithm ID claim
- A7.2.3.1.7 Realm public key claim
- A7.2.3.1.8 Realm public key hash algorithm identifier claim
- A7.2.3.1.9 Collated CDDL for Realm claims
- A7.2.3.1.10 Example Realm claims

## A7.2.3.1.1 Realm challenge claim

The Realm challenge claim is used to carry the challenge provided by the caller to demonstrate freshness of the generated token.


The Realm challenge claim is identified using the EAT nonce label (10).

- The length of the Realm challenge is 64 bytes.

The Realm challenge claim must be present in a Realm token.




The format of the Realm challenge claim is defined as follows:

```
cca-realm-challenge-label = 10 cca-realm-challenge-type = bytes .size 64 cca-realm-challenge = ( cca-realm-challenge-label => cca-realm-challenge-type )
```

## See also:

- A7.2.2 Attestation token generation
- B5.3.2 RSI\_ATTESTATION\_TOKEN\_INIT command

## A7.2.3.1.2 Realm profile claim

The Realm profile claim identifies the EAT profile to which the Realm token conforms.

The Realm profile claim is identified using the EAT profile label (265).

A7.2. Realm attestation




The Realm profile claim is optional in a CCA Realm token.

If the Realm profile is not included in a CCA Realm token then the profile value used in the CCA Platform token should refer to a profile that describes both Platform and Realm claims.

The format of the Realm profile claim is defined as follows:

```
cca-realm-profile-label = 265 ; EAT profile cca-realm-profile-type = "tag:arm.com,2023:realm#1.0.0" cca-realm-profile = ( cca-realm-profile-label => cca-realm-profile-type )
```

## A7.2.3.1.3 Realm Personalization Value claim

The Realm Personalization Value claim contains the RPV which was provided at Realm creation.

The Realm Personalization Value claim must be present in a Realm token.

- The format of the Realm Personalization Value claim is defined as follows:

```
cca-realm-personalization-value-label = 44235 cca-realm-personalization-value-type = bytes .size 64 cca-realm-personalization-value = ( cca-realm-personalization-value-label => cca-realm-personalization-value-type )
```

## See also:

- A2.1.3 Realm attributes

## A7.2.3.1.4 Realm Initial Measurement claim


The Realm Initial Measurement claim contains the values of the Realm Initial Measurement.


The Realm Initial Measurement claim must be present in a Realm token.

- The format of the Realm Initial Measurement claim is defined as follows:

```
cca-realm-measurement-type = bytes .size 32 / bytes .size 48 / bytes .size 64 cca-realm-initial-measurement-label = 44238 cca-realm-initial-measurement = ( cca-realm-initial-measurement-label => cca-realm-measurement-type )
```

## See also:

- A7.1 Realm measurements
- A7.2.3.1.5 Realm Extensible Measurements claim

## A7.2.3.1.5 Realm Extensible Measurements claim


The Realm Extensible Measurements claim contains the values of the Realm Extensible Measurements.


The Realm Extensible Measurements claim must be present in a Realm token.

- The format of the Realm measurements claim is defined as follows:

```
cca-realm-measurement-type = bytes .size 32 / bytes .size 48 / bytes .size 64 cca-realm-extensible-measurements-label = 44239 cca-realm-extensible-measurements = ( cca-realm-extensible-measurements-label => [ 4*4 cca-realm-measurement-type ]
```


)

## See also:

- A7.1 Realm measurements
- A7.2.3.1.4 Realm Initial Measurement claim

## A7.2.3.1.6 Realm hash algorithm ID claim

The Realm hash algorithm ID claim identifies the algorithm used to calculate all hash values which are present in the Realm token.


Arm recommends that the value of the Realm hash algorithm ID claim is an IANA Hash Function name IANA Named Information Hash Algorithm Registry [10].


- The Realm hash algorithm ID claim must be present in a Realm token.
- The format of the Realm hash algorithm ID claim is defined as follows:

```
cca-realm-hash-algo-id-label = 44236 cca-realm-hash-algo-id = ( cca-realm-hash-algo-id-label => text )
```

## A7.2.3.1.7 Realm public key claim

The Realm public key claim identifies the key which is used to sign the Realm token.

The value of the Realm public key claim is a CBOR bstr of a COSE\_Key structure. The parameters used for the COSE\_Key are profile-specific.

- The Realm public key claim must be present in a Realm token.
- The format of the Realm public key claim is defined as follows:

```
cca-realm-public-key-type
```

```
cca-realm-public-key-label = 44237 cca-realm-public-key-type = bstr .cbor COSE_Key cca-realm-public-key = ( cca-realm-public-key-label => ) COSE_Key-label = int / tstr COSE_Key-values = any ; See RFC8152 for full definition of COSE_Key COSE_Key = { 1 => tstr / int, ; kty ? 2 => bstr, ; kid ? 3 => tstr / int, ; alg ? 4 => [+ (tstr / int) ], ; key_ops ? 5 => bstr, ; Base IV * COSE_Key-label => COSE_Key-values }
```

## See also:

- SEC 1: Elliptic Curve Cryptography, version 2.0 [11]
- A7.2.3.1.8 Realm public key hash algorithm identifier claim
- A7.2.3.2.2 CCA platform challenge claim

## A7.2.3.1.8 Realm public key hash algorithm identifier claim

- The Realm public key hash algorithm identifier claim identifies the algorithm used to calculate H(RAK\_pub).


The Realm public key hash algorithm identifier claim must be present in a Realm token.


The format of the Realm public key hash algorithm identifier claim is defined as follows:

```
cca-realm-public-key-hash-algo-id-label = 44240 cca-realm-public-key-hash-algo-id = ( cca-realm-public-key-hash-algo-id-label => )
```

## See also:

- SEC 1: Elliptic Curve Cryptography, version 2.0 [11]
- A7.2.3.1.7 Realm public key claim
- A7.2.3.2.2 CCA platform challenge claim

```
text
```


## A7.2.3.1.9 Collated CDDL for Realm claims

The format of the Realm token claim map is defined as follows:

```
cca-realm-claims = (cca-realm-claim-map) cca-realm-claim-map = { cca-realm-challenge ? cca-realm-profile cca-realm-personalization-value cca-realm-initial-measurement cca-realm-extensible-measurements cca-realm-hash-algo-id cca-realm-public-key cca-realm-public-key-hash-algo-id } cca-realm-challenge-label = 10 cca-realm-challenge-type = bytes .size 64 cca-realm-challenge = ( cca-realm-challenge-label => cca-realm-challenge-type ) cca-realm-profile-label = 265 ; EAT profile cca-realm-profile-type = "tag:arm.com,2023:realm#1.0.0" cca-realm-profile = ( cca-realm-profile-label => cca-realm-profile-type ) cca-realm-personalization-value-label = 44235 cca-realm-personalization-value-type = bytes .size 64 cca-realm-personalization-value = ( cca-realm-personalization-value-label => cca-realm-personalization-value-type ) cca-realm-measurement-type = bytes .size 32 / bytes .size 48 / bytes .size 64 cca-realm-initial-measurement-label = 44238 cca-realm-initial-measurement = ( cca-realm-initial-measurement-label => cca-realm-measurement-type ) cca-realm-extensible-measurements-label = 44239 cca-realm-extensible-measurements = ( cca-realm-extensible-measurements-label => [ 4*4 cca-realm-measurement-type ] ) cca-realm-hash-algo-id-label = 44236 cca-realm-hash-algo-id = ( cca-realm-hash-algo-id-label => text ) cca-realm-public-key-label = 44237 cca-realm-public-key-type = bstr .cbor COSE_Key cca-realm-public-key = ( cca-realm-public-key-label => cca-realm-public-key-type ) COSE_Key-label = int / tstr COSE_Key-values = any
```

```
; See RFC8152 for full definition of COSE_Key COSE_Key = { 1 => tstr / int, ; kty ? 2 => bstr, ; kid ? 3 => tstr / int, ; alg ? 4 => [+ (tstr / int) ], ; key_ops ? 5 => bstr, ; Base IV * COSE_Key-label => COSE_Key-values } cca-realm-public-key-hash-algo-id-label = 44240 cca-realm-public-key-hash-algo-id = ( cca-realm-public-key-hash-algo-id-label => text )
```


## A7.2.3.1.10 Example Realm claims

An example Realm claim map is shown below in COSE-DIAG format:

```
/ Realm claim map / { / cca-realm-profile / 265: "tag:arm.com,2023:realm#1.0.0", / cca-realm-challenge / 10: h'ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB', / cca-realm-personalization-value / 44235: h'ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB', / cca-realm-initial-measurement / 44238: h'0000000000000000000000000000000000000000000000000000000000000000', / cca-realm-extensible-measurements / 44239: [ h'0000000000000000000000000000000000000000000000000000000000000000', h'0000000000000000000000000000000000000000000000000000000000000000', h'0000000000000000000000000000000000000000000000000000000000000000', h'0000000000000000000000000000000000000000000000000000000000000000' ], / cca-realm-hash-algo-id / 44236: "sha-256", / cca-realm-public-key / 44237: h'A50102033823200221582066EEA6A22678C3A9F83148EF349800B20ABB486F2C C6D7ED017EC49798C8D4372258202F25DE86812374E6E8D48DEE8E230AD29CCD 839BE6E0DB8C7AB9DEDE0805D29D', / cca-realm-public-key-hash-algo-id / 44240: "sha-256" }
```

## A7.2.3.2 CCA platform claims

This section defines the format of the CCA platform token claim map. The format is described using a combination of Concise Data Definition Language (CDDL) and text description.

## The CCA platform token claim map is defined as follows:

```
(cca-platform-claim-map)
```

```
cca-platform-claims = cca-platform-claim-map = { cca-platform-profile cca-platform-challenge cca-platform-implementation-id cca-platform-instance-id cca-platform-config cca-platform-lifecycle cca-platform-sw-components ? cca-platform-verification-service cca-platform-hash-algo-id }
```

## See also:

- Concise Data Definition Language (CDDL) [9]
- A7.2.3.2.1 CCA platform profile claim
- A7.2.3.2.2 CCA platform challenge claim
- A7.2.3.2.3 CCA platform Implementation ID claim
- A7.2.3.2.4 CCA platform Instance ID claim
- A7.2.3.2.5 CCA platform config claim
- A7.2.3.2.6 CCA platform lifecycle claim
- A7.2.3.2.7 CCA platform software components claim
- A7.2.3.2.8 CCA platform verification service claim
- A7.2.3.2.9 CCA platform hash algorithm ID claim
- A7.2.3.2.10 Collated CDDL for CCA platform claims
- A7.2.3.2.11 Example CCA platform claims

## A7.2.3.2.1 CCA platform profile claim

The CCA platform profile claim identifies the EAT profile to which the CCA platform token conforms. Note that because the platform token is expected to be issued when bound to a Realm token, the profile document should also include the relevant Realm profile or a reference to that profile.

The CCA platform profile claim is identified using the EAT profile label (265).

The CCA platform profile claim must be present in a CCA platform token.

- The format of the CCA platform profile claim is defined as follows:

```
cca-platform-profile-label = 265 ; EAT profile cca-platform-profile-type = "tag:arm.com,2023:cca_platform#1.0.0" cca-platform-profile = ( cca-platform-profile-label => cca-platform-profile-type )
```

## A7.2.3.2.2 CCA platform challenge claim

The CCA platform challenge claim contains a hash of the public key used to sign the Realm token.


The CCA platform challenge claim is identified using the EAT nonce label (10).

- The length of the CCA platform challenge is either 32, 48 or 64 bytes.


The CCA platform challenge claim must be present in a CCA platform token.

- The format of the CCA platform challenge claim is defined as follows:

```
cca-hash-type = bytes .size 32 / bytes .size 48 / bytes .size 64 cca-platform-challenge-label = 10 cca-platform-challenge = ( cca-platform-challenge-label => cca-hash-type )
```

## See also:

- A7.2.3.1.7 Realm public key claim

## A7.2.3.2.3 CCA platform Implementation ID claim

The CCA platform Implementation ID claim uniquely identifies the implementation of the CCA platform.

The value of the CCA platform Implementation ID claim can be used by a verification service to locate the details of the CCA platform implementation from an endorser or manufacturer. Such details are used by a verification service to determine the security properties or certification status of the CCA platform implementation.

The semantics of the CCA platform Implementation ID value are defined by the manufacturer or a particular certification scheme. For example, the ID could take the form of a product serial number, database ID, or other appropriate identifier.

The CCA platform Implementation ID claim does not identify a particular instance of the CCA implementation.

The CCA platform Implementation ID claim must be present in a CCA platform token.

- The format of the CCA platform Implementation ID claim is defined as follows:

```
cca-platform-implementation-id-label = 2396 ; PSA implementation ID cca-platform-implementation-id-type = bytes .size 32 cca-platform-implementation-id = ( cca-platform-implementation-id-label => cca-platform-implementation-id-type )
```

## See also:

- Arm CCA Security model [4]
- A7.2.3.2.4 CCA platform Instance ID claim

## A7.2.3.2.4 CCA platform Instance ID claim

The CCA platform Instance ID claim represents the unique identifier of the Initial Attestation Key (IAK) for the CCA platform.

The CCA platform Instance ID claim is identified using the EAT ueid label (256).

The first byte of the CCA platform Instance ID value must be 0x01 .

The CCA platform Instance ID claim must be present in a CCA platform token.

- The format of the CCA platform Instance ID claim is defined as follows:

```
cca-platform-instance-id-label = 256 ; EAT ueid ; TODO: require that the first byte of cca-platform-instance-id-type is 0x01 ; EAT UEIDs need to be 7 -33 bytes cca-platform-instance-id-type = bytes .size 33 cca-platform-instance-id = ( cca-platform-instance-id-label => cca-platform-instance-id-type )
```

## See also:

- Arm CCA Security model [4]
- A7.2.3.2.3 CCA platform Implementation ID claim

## A7.2.3.2.5 CCA platform config claim

The CCA platform config claim describes the set of chosen implementation options of the CCA platform. As an example, these may include a description of the level of physical memory protection which is provided.

The CCA platform config claim is expected to contain the System Properties field which is present in the Root Non-volatile Storage (RNVS) public parameters.

- The CCA platform config claim must be present in a CCA platform token.

```
cca-platform-config-label = 2401 ; PSA platform range ; TBD: add to IANA registration cca-platform-config-type = bytes cca-platform-config = ( cca-platform-config-label => cca-platform-config-type )
```

## See also:

- RME system architecture spec [12]

## A7.2.3.2.6 CCA platform lifecycle claim

- The CCA platform lifecycle claim identifies the lifecycle state of the CCA platform.


- The value of the CCA platform lifecycle claim is an integer which is divided as follows:
- value[15:8]: CCA platform lifecycle state
- value[7:0]: IMPLEMENTATION DEFINED

The CCA platform lifecycle claim must be present in a CCA platform token.


A non debugged CCA platform will be in psa-lifecycle-secured state. Realm Management Security Domain debug is always recoverable, and would therefore be represented by psa-lifecycle-non-psa-rot-debug state. Root world debug is recoverable on a HES system and would be represented by psa-lifecycle-recoverable-psa-rot state. On a non-HES system Root world debug is usually non-recoverable, and would be represented by psa-lifecycle-lifecycle-decommissioned state.

## The format of the CCA platform lifecycle claim is defined as follows:

```
cca-platform-lifecycle-label = 2395 ; PSA lifecycle cca-platform-lifecycle-unknown-type = 0x0000..0x00ff cca-platform-lifecycle-assembly-and-test-type = 0x1000..0x10ff cca-platform-lifecycle-cca-platform-rot-provisioning-type = 0x2000..0x20ff cca-platform-lifecycle-secured-type = 0x3000..0x30ff cca-platform-lifecycle-non-cca-platform-rot-debug-type = 0x4000..0x40ff cca-platform-lifecycle-recoverable-cca-platform-rot-debug-type = 0x5000..0x50ff cca-platform-lifecycle-decommissioned-type = 0x6000..0x60ff cca-platform-lifecycle-type = cca-platform-lifecycle-unknown-type / cca-platform-lifecycle-assembly-and-test-type / cca-platform-lifecycle-cca-platform-rot-provisioning-type / cca-platform-lifecycle-secured-type / cca-platform-lifecycle-non-cca-platform-rot-debug-type / cca-platform-lifecycle-recoverable-cca-platform-rot-debug-type /
```

A7.2. Realm attestation

```
cca-platform-lifecycle-decommissioned-type cca-platform-lifecycle = ( cca-platform-lifecycle-label => cca-platform-lifecycle-type )
```

## See also:

- Arm CCA Security model [4]

## A7.2.3.2.7 CCA platform software components claim

The CCA platform software components claim is a list of software components which can affect the behavior of the CCA platform. It is expected that an implementation will describe the expected software component values within the profile.


- The CCA platform software components claim must be present in a CCA platform token.




- The format of the CCA platform software components claim is defined as follows:

```
cca-platform-sw-components-label = 2399 ; PSA software components cca-platform-sw-component = { ? 1 => text, ; component type 2 => cca-hash-type, ; measurement value ? 4 => text, ; version 5 => cca-hash-type, ; signer id ? 6 => text, ; hash algorithm identifier } cca-platform-sw-components = ( cca-platform-sw-components-label => [ + cca-platform-sw-component ] )
```

## CCA platform software component type

The CCA platform software component type is a string which represents the role of the software component.

The CCA platform software component type is intended for use as a hint to help the relying party understand how to evaluate the CCA platform software component measurement value.

The CCA platform software component type is optional in a CCA platform token.

## CCA platform software component measurement value

The CCA platform software component measurement value represents a hash of the state of the software component in memory at the time it was initialized.

The CCA platform software component measurement value must be a hash of 256 bits or stronger.


The CCA platform software component measurement value must be present in a CCA platform token.

## CCA platform software component version

The CCA platform software component version is a text string whose meaning is defined by the software component vendor.

The CCA platform software component version is optional in a CCA platform token.

## CCA platform software component signer ID

The CCA platform software component signer ID is the hash of a signing authority public key for the software component. It can be used by a verifier to ensure that the software component was signed by an expected trusted source.

The CCA platform software component signer ID value must be a hash of 256 bits or stronger.

The CCA platform software signer ID must be present in a CCA platform token.




## CCA platform software component hash algorithm ID

The CCA platform software component hash algorithm ID identifies the way in which the hash algorithm used to measure the CCA platform software component.

- Arm recommends that the value of the CCA platform software component hash algorithm ID is an IANA Hash Function name IANA Named Information Hash Algorithm Registry [10].

Arm recommends that the hash algorithm used to measure the CCA platform software component is one of the algorithms listed in the Arm CCA Security model [4].

- The CCA platform software component hash algorithm ID is optional in a CCA platform token.

## A7.2.3.2.8 CCA platform verification service claim

The CCA platform verification service claim is a hint which can be used by a relying party to locate a verifier for the token.

- The value of the CCA platform verification service claim is a text string which can be used to locate the service or a URL specifying the address of the service.
- The CCA platform verification service claim may be ignored by a relying party in favor of other information.
- The CCA platform verification service claim is optional in a CCA platform token.
- The format of the CCA platform verification service claim is defined as follows:

```
cca-platform-verification-service-label = 2400 ; PSA verification service cca-platform-verification-service-type = text cca-platform-verification-service = ( cca-platform-verification-service-label => cca-platform-verification-service-type )
```

## A7.2.3.2.9 CCA platform hash algorithm ID claim

- The CCA platform hash algorithm ID claim identifies the default algorithm used to calculate measurements in the CCA platform token.
- The default hash algorithm may be overridden for an individual software component, by the CCA platform software component hash algorithm ID claim.
- Arm recommends that the value of the CCA platform hash algorithm ID claim is an IANA Hash Function name IANA Named Information Hash Algorithm Registry [10].
- The CCA platform hash algorithm ID claim must be present in a CCA platform token.

## The format of the CCA platform hash algorithm ID claim is defined as follows:

```
cca-platform-hash-algo-id-label = 2402 ; PSA platform range ; TBD: add to IANA registration cca-platform-hash-algo-id = ( cca-platform-hash-algo-id-label => text )
```

## A7.2.3.2.10 Collated CDDL for CCA platform claims

## The format of the CCA platform token claim map is defined as follows:

```
cca-platform-claims = (cca-platform-claim-map) cca-platform-claim-map = { cca-platform-profile cca-platform-challenge cca-platform-implementation-id cca-platform-instance-id cca-platform-config cca-platform-lifecycle cca-platform-sw-components ? cca-platform-verification-service cca-platform-hash-algo-id } cca-platform-profile-label = 265 ; EAT profile cca-platform-profile-type = "tag:arm.com,2023:cca_platform#1.0.0" cca-platform-profile = ( cca-platform-profile-label => cca-platform-profile-type ) cca-hash-type = bytes .size 32 / bytes .size 48 / bytes .size 64 cca-platform-challenge-label = 10 cca-platform-challenge = ( cca-platform-challenge-label => cca-hash-type ) cca-platform-implementation-id-label = 2396 ; PSA implementation ID cca-platform-implementation-id-type = bytes .size 32 cca-platform-implementation-id = ( cca-platform-implementation-id-label => cca-platform-implementation-id-type ) cca-platform-instance-id-label = 256 ; EAT ueid ; TODO: require that the first byte of cca-platform-instance-id-type is 0x01 ; EAT UEIDs need to be 7 -33 bytes cca-platform-instance-id-type = bytes .size 33 cca-platform-instance-id = ( cca-platform-instance-id-label => cca-platform-instance-id-type ) cca-platform-config-label = 2401 ; PSA platform range ; TBD: add to IANA registration cca-platform-config-type = bytes cca-platform-config = ( cca-platform-config-label => cca-platform-config-type ) cca-platform-lifecycle-label = 2395 ; PSA lifecycle cca-platform-lifecycle-unknown-type = 0x0000..0x00ff cca-platform-lifecycle-assembly-and-test-type = 0x1000..0x10ff cca-platform-lifecycle-cca-platform-rot-provisioning-type = 0x2000..0x20ff cca-platform-lifecycle-secured-type = 0x3000..0x30ff cca-platform-lifecycle-non-cca-platform-rot-debug-type = 0x4000..0x40ff cca-platform-lifecycle-recoverable-cca-platform-rot-debug-type = 0x5000..0x50ff cca-platform-lifecycle-decommissioned-type = 0x6000..0x60ff
```

```
cca-platform-lifecycle-type = cca-platform-lifecycle-unknown-type / cca-platform-lifecycle-assembly-and-test-type / cca-platform-lifecycle-cca-platform-rot-provisioning-type / cca-platform-lifecycle-secured-type / cca-platform-lifecycle-non-cca-platform-rot-debug-type / cca-platform-lifecycle-recoverable-cca-platform-rot-debug-type / cca-platform-lifecycle-decommissioned-type cca-platform-lifecycle = ( cca-platform-lifecycle-label => cca-platform-lifecycle-type ) cca-platform-sw-components-label = 2399 ; PSA software components cca-platform-sw-component = { ? 1 => text, ; component type 2 => cca-hash-type, ; measurement value ? 4 => text, ; version 5 => cca-hash-type, ; signer id ? 6 => text, ; hash algorithm identifier } cca-platform-sw-components = ( cca-platform-sw-components-label => [ + cca-platform-sw-component ] ) cca-platform-verification-service-label = 2400 ; PSA verification service cca-platform-verification-service-type = text cca-platform-verification-service = ( cca-platform-verification-service-label => cca-platform-verification-service-type ) cca-platform-hash-algo-id-label = 2402 ; PSA platform range ; TBD: add to IANA registration cca-platform-hash-algo-id = ( cca-platform-hash-algo-id-label => text )
```


## A7.2.3.2.11 Example CCA platform claims

An example CCA platform claim map is shown below in COSE-DIAG format:

```
/ CCA platform claim map / { / cca-platform-profile / 265: "tag:arm.com,2023:cca_platform#1.0.0", / cca-platform-challenge / 10: h'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', / cca-platform-implementation-id / 2396: h'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', / cca-platform-instance-id / 256: h'010BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BB', / cca-platform-config / 2401: h'CFCFCFCF', / cca-platform-lifecycle / 2395: 12288, / cca-platform-sw-components / 2399: [ { / measurement value / 2: h'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', / signer id / 5: h'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', / version / 4: "1.0.0", / hash algorithm identifier / 6: "sha-256" }, { / measurement value / 2: h'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC', / signer id / 5: h'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD', / version / 4: "1.0.0", / hash algorithm identifier / 6: "sha-256" } ], / cca-platform-verification-service /
```

```
Chapter A7. Realm measurement and attestation A7.2. Realm attestation 2400: "https://cca_verifier.org", / cca-platform-hash-algo-id / 2402: "sha-256" }
```