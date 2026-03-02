
## A7.2.3.1 Realm claims

This section defines the format of the Realm token claim map. The format is described using a combination of Concise Data Definition Language (CDDL) and text description.

The Realm token claim map is defined as follows:

```
cca-realm-claims = (cca-realm-claim-map) cca-realm-claim-map = { cca-realm-challenge ? cca-realm-profile cca-realm-instance-id cca-realm-personalization-value cca-realm-initial-measurement cca-realm-extensible-measurements cca-realm-hash-algo-id cca-realm-public-key cca-realm-public-key-hash-algo-id cca-realm-mec-policy ? cca-realm-lfa-policy ? cca-realm-devices-token-hash }
```

## See also:

- Concise Data Definition Language (CDDL) [12]
- A7.2.3.1.1 Realm challenge claim
- A7.2.3.1.2 Realm profile claim
- A7.2.3.1.3 Realm Instance ID claim
- A7.2.3.1.4 Realm Personalization Value claim
- A7.2.3.1.5 Realm Initial Measurement claim
- A7.2.3.1.6 Realm Extensible Measurements claim
- A7.2.3.1.7 Realm hash algorithm ID claim
- A7.2.3.1.8 Realm MEC policy claim
- A7.2.3.1.9 Realm LFA policy claim
- A7.2.3.1.10 Realm public key claim
- A7.2.3.1.11 Realm public key hash algorithm identifier claim


- A7.2.3.1.12 Realm devices token hash claim
- A7.2.3.1.13 Collated CDDL for Realm claims
- A7.2.3.1.14 Example Realm claims

## A7.2.3.1.1 Realm challenge claim

The Realm challenge claim is used to carry the challenge provided by the caller to demonstrate freshness of the generated token.





The Realm challenge claim is identified using the EAT nonce label (10).

The length of the Realm challenge is 64 bytes.

The Realm challenge claim must be present in a Realm token.

The format of the Realm challenge claim is defined as follows:

```
cca-realm-challenge-type
```

```
cca-realm-challenge-label = 10 cca-realm-challenge-type = bytes .size 64 cca-realm-challenge = ( cca-realm-challenge-label => )
```

## See also:

A7.2. Realm attestation

- A7.2.2 Attestation token generation
- B5.4.3 RSI\_ATTESTATION\_TOKEN\_INIT command

## A7.2.3.1.2 Realm profile claim

- The Realm profile claim identifies the EAT profile to which the Realm token conforms.

The Realm profile claim is identified using the EAT profile label (265).

The Realm profile claim is optional in a CCA Realm token.

- If the Realm profile is not included in a CCA Realm token then the profile value used in the CCA Platform token should refer to a profile that describes both Platform and Realm claims.
- The format of the Realm profile claim is defined as follows:

```
cca-realm-profile-label = 265 ; EAT profile cca-realm-profile-type = "tag:arm.com,2024:realm#2.0.0" cca-realm-profile = ( cca-realm-profile-label => cca-realm-profile-type )
```

## A7.2.3.1.3 Realm Instance ID claim

```
The Realm Instance ID claim is a random value generated using a cryptographic-quality entropy source. IYHLZK The Realm Instance ID claim is identified using the EAT ueid label (256). RBVCXM The first byte of the Realm Instance ID value must be 0x01 . ITFZYD The Realm Instance ID claim must be present in a Realm token. ILTZVS The format of the CCA Realm Instance ID claim is defined as follows: cca-realm-instance-id-label = 256 ; EAT ueid ; EAT UEIDs need to be 7 -33 bytes cca-realm-instance-id-type = bytes .size 33 cca-realm-instance-id = ( cca-realm-instance-id-label => cca-realm-instance-id-type )
```

## See also:

- Arm CCA Security model [4]

## A7.2.3.1.4 Realm Personalization Value claim

- The Realm Personalization Value claim contains the RPV which was provided at Realm creation.


The Realm Personalization Value claim must be present in a Realm token.

- The format of the Realm Personalization Value claim is defined as follows:

```
cca-realm-personalization-value-label = 44235 cca-realm-personalization-value-type = bytes .size 64 cca-realm-personalization-value = ( cca-realm-personalization-value-label => cca-realm-personalization-value-type )
```

## See also:

- A2.2.3 Realm attributes

## A7.2.3.1.5 Realm Initial Measurement claim

- The Realm Initial Measurement claim contains the values of the Realm Initial Measurement.

The Realm Initial Measurement claim must be present in a Realm token.

- The format of the Realm Initial Measurement claim is defined as follows:

```
cca-realm-measurement-type = bytes .size 32 / bytes .size 48 / bytes .size 64 cca-realm-initial-measurement-label = 44238 cca-realm-initial-measurement = ( cca-realm-initial-measurement-label => cca-realm-measurement-type )
```

## See also:

- A7.1 Realm measurements
- A7.2.3.1.6 Realm Extensible Measurements claim

## A7.2.3.1.6 Realm Extensible Measurements claim

The Realm Extensible Measurements claim contains the values of the Realm Extensible Measurements.


```
The format of the Realm measurements claim is defined as follows: cca-realm-measurement-type = bytes .size 32 / bytes .size 48 / bytes .size 64 cca-realm-extensible-measurements-label = 44239 cca-realm-extensible-measurements = ( cca-realm-extensible-measurements-label => [ 4*4 cca-realm-measurement-type ] ) See also: · A7.1 Realm measurements · A7.2.3.1.5 Realm Initial Measurement claim A7.2.3.1.7 Realm hash algorithm ID claim
```

The Realm Extensible Measurements claim must be present in a Realm token.

The Realm hash algorithm ID claim identifies the algorithm used to calculate all hash values which are present in the Realm token.

Arm recommends that the value of the Realm hash algorithm ID claim is an IANA Hash Function name IANA Named Information Hash Algorithm Registry [13].



The Realm hash algorithm ID claim must be present in a Realm token.

The format of the Realm hash algorithm ID claim is defined as follows:

```
cca-realm-hash-algo-id-label = 44236 cca-realm-hash-algo-id = ( cca-realm-hash-algo-id-label => text )
```

## A7.2.3.1.8 Realm MEC policy claim


The Realm MEC policy identifies the MEC policy of the Realm.


The Realm MEC policy claim must be present in a Realm token.


On a platform which does not implement FEAT\_MEC, the value of the Realm MEC policy claim is cca-realm-mec-policy-shared.

A7.2. Realm attestation


The format of the Realm MEC policy claim is defined as follows:

```
cca-realm-mec-policy-label = 44243 cca-realm-mec-policy-shared = 0 cca-realm-mec-policy-private = 1 cca-realm-mec-policy = ( cca-realm-mec-policy-label => cca-realm-mec-policy-shared cca-realm-mec-policy-private )
```

## See also:

- Chapter A11 Realm memory encryption

## A7.2.3.1.9 Realm LFA policy claim


The Realm LFA policy identifies the Live Firmware Activation policy of the Realm.


The Realm LFA policy claim is optional in a Realm token.


The format of the Realm LFA policy claim is defined as follows:

```
cca-realm-lfa-policy-label = 44244 cca-realm-lfa-policy-disallow = 0 cca-realm-lfa-policy-allow = 1 cca-realm-lfa-policy = ( cca-realm-lfa-policy-label => cca-realm-lfa-policy-disallow cca-realm-lfa-policy-allow )
```

## See also:

- A3.14 Live Firmware Activation

## A7.2.3.1.10 Realm public key claim

```
/
```

The Realm public key claim identifies the key which is used to sign the Realm token.

The value of the Realm public key claim is a CBOR bstr of a COSE\_Key structure. The parameters used for the COSE\_Key are profile-specific.

- The Realm public key claim must be present in a Realm token.




- The format of the Realm public key claim is defined as follows:

```
;# import rfc9052 cca-realm-public-key-label = 44237 cca-realm-public-key-type = bstr .cbor COSE_Key cca-realm-public-key = ( cca-realm-public-key-label => cca-realm-public-key-type )
```

## See also:

- SEC 1: Elliptic Curve Cryptography, version 2.0 [14]
- A7.2.3.1.11 Realm public key hash algorithm identifier claim

```
/
```

- A7.2.3.3.2 CCA platform challenge claim

## A7.2.3.1.11 Realm public key hash algorithm identifier claim

The Realm public key hash algorithm identifier claim identifies the algorithm used to calculate H(RAK\_pub).


The Realm public key hash algorithm identifier claim must be present in a Realm token.

- The format of the Realm public key hash algorithm identifier claim is defined as follows:

```
cca-realm-public-key-hash-algo-id-label = 44240 cca-realm-public-key-hash-algo-id = ( cca-realm-public-key-hash-algo-id-label => )
```

## See also:

- SEC 1: Elliptic Curve Cryptography, version 2.0 [14]
- A7.2.3.1.10 Realm public key claim
- A7.2.3.3.2 CCA platform challenge claim

## A7.2.3.1.12 Realm devices token hash claim

The Realm devices token hash claim contains a hash of the CBOR encoding of cca-realm-devices-token that represents the set of devices assigned to the Realm.

The Realm devices token hash claim must be present in a Realm token whenever one or more devices are assigned to the Realm. If no devices are assigned, the claim must not be present.

- The format of the Realm devices token hash claim is defined as follows:

```
cca-realm-devices-token-hash-label = 44257 cca-realm-devices-token-hash = ( cca-realm-devices-token-hash-label => )
```

## See also:

- A7.2.3.2 CCA device claims

```
cca-hash-type
```

```
text
```


## A7.2.3.1.13 Collated CDDL for Realm claims

The format of the Realm token claim map is defined as follows:

```
cca-realm-claims = (cca-realm-claim-map) cca-realm-claim-map = { cca-realm-challenge ? cca-realm-profile cca-realm-instance-id cca-realm-personalization-value cca-realm-initial-measurement cca-realm-extensible-measurements cca-realm-hash-algo-id cca-realm-public-key cca-realm-public-key-hash-algo-id cca-realm-mec-policy ? cca-realm-lfa-policy ? cca-realm-devices-token-hash } cca-realm-challenge-label = 10 cca-realm-challenge-type = bytes .size 64 cca-realm-challenge = ( cca-realm-challenge-label => cca-realm-challenge-type ) cca-realm-profile-label = 265 ; EAT profile cca-realm-profile-type = "tag:arm.com,2024:realm#2.0.0" cca-realm-profile = ( cca-realm-profile-label => cca-realm-profile-type ) cca-realm-personalization-value-label = 44235 cca-realm-personalization-value-type = bytes .size 64 cca-realm-personalization-value = ( cca-realm-personalization-value-label => cca-realm-personalization-value-type ) cca-realm-measurement-type = bytes .size 32 / bytes .size 48 / bytes .size 64 cca-realm-initial-measurement-label = 44238 cca-realm-initial-measurement = ( cca-realm-initial-measurement-label => cca-realm-measurement-type ) cca-realm-extensible-measurements-label = 44239 cca-realm-extensible-measurements = ( cca-realm-extensible-measurements-label => [ 4*4 cca-realm-measurement-type ] ) cca-realm-hash-algo-id-label = 44236 cca-realm-hash-algo-id = ( cca-realm-hash-algo-id-label => text ) ;# import rfc9052 cca-realm-public-key-label = 44237 cca-realm-public-key-type = bstr .cbor COSE_Key
```

```
cca-realm-public-key = ( cca-realm-public-key-label => cca-realm-public-key-type ) cca-realm-public-key-hash-algo-id-label = 44240 cca-realm-public-key-hash-algo-id = ( cca-realm-public-key-hash-algo-id-label => text ) cca-realm-mec-policy-label = 44243 cca-realm-mec-policy-shared = 0 cca-realm-mec-policy-private = 1 cca-realm-mec-policy = ( cca-realm-mec-policy-label => cca-realm-mec-policy-shared / cca-realm-mec-policy-private ) cca-realm-lfa-policy-label = 44244 cca-realm-lfa-policy-disallow = 0 cca-realm-lfa-policy-allow = 1 cca-realm-lfa-policy = ( cca-realm-lfa-policy-label => cca-realm-lfa-policy-disallow / cca-realm-lfa-policy-allow ) cca-hash-type = bytes .size 32 / bytes .size 48 / bytes .size 64 cca-realm-devices-token-hash-label = 44257 cca-realm-devices-token-hash = ( cca-realm-devices-token-hash-label => cca-hash-type )
```


## A7.2.3.1.14 Example Realm claims

An example Realm claim map is shown below in COSE-DIAG format:

```
/ Realm claim map / { / cca-realm-profile / 265: "tag:arm.com,2024:realm#2.0.0", / cca-realm-challenge / 10: h'ABABABABABABABABABABABABABABABAB ABABABABABABABABABABABABABABABAB ABABABABABABABABABABABABABABABAB ABABABABABABABABABABABABABABABAB', / cca-realm-instance-id / 256: h'010BBBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB BB', / cca-realm-personalization-value / 44235: h'ABABABABABABABABABABABABABABABAB ABABABABABABABABABABABABABABABAB ABABABABABABABABABABABABABABABAB ABABABABABABABABABABABABABABABAB', / cca-realm-initial-measurement / 44238: h'00000000000000000000000000000000 00000000000000000000000000000000', / cca-realm-extensible-measurements / 44239: [ h'00000000000000000000000000000000 00000000000000000000000000000000', h'00000000000000000000000000000000 00000000000000000000000000000000', h'00000000000000000000000000000000 00000000000000000000000000000000', h'00000000000000000000000000000000 00000000000000000000000000000000' ], / cca-realm-hash-algo-id / 44236: "sha-256", / cca-realm-public-key / 44237: h'A50102033823200221582066EEA6A226 78C3A9F83148EF349800B20ABB486F2C C6D7ED017EC49798C8D4372258202F25 DE86812374E6E8D48DEE8E230AD29CCD 839BE6E0DB8C7AB9DEDE0805D29D', / cca-realm-public-key-hash-algo-id / 44240: "sha-256", / cca-realm-mec-policy / 44243: 0, / cca-realm-lfa-policy / 44244: 1,
```

```
Chapter A7. Realm measurement and attestation A7.2. Realm attestation / cca-realm-devices-token-hash / 44257: h'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' }
```

<!-- image -->