## A7.2 Realm attestation

This section describes the primitives which are used to support remote Realm attestation.

## A7.2.1 Attestation token

A CCA attestation token is a collection of claims about the state of a Realm, the CCA platform on which the Realm is running, and the set of devices assigned to the Realm.

- A CCA attestation token consists of three parts:
- Realm token

Contains attributes of the Realm, including:

- -Realm Initial Measurement
- -Realm Extensible Measurements
- Device token

Contains a list of devices assigned to the Realm

- CCA platform token

Contains attributes of the CCA platform on which the Realm is running, including:

- -CCA platform identity
- -CCA platform lifecycle state
- -CCA platform software component measurements

The size of a CCA attestation token may be greater than the RSI Granule size.

See also:

- [A7.1.1 Realm Initial Measurement](rmm-A7.1.md#a711-realm-initial-measurement)
- [A7.1.2 Realm Extensible Measurement](rmm-A7.1.md#a712-realm-extensible-measurement)

## A7.2.2 Attestation token generation

- The process for a Realm to obtain an attestation token is:


- Call RSI\_ATTESTATION\_TOKEN\_INIT once
- Call RSI\_ATTESTATION\_TOKEN\_CONTINUE in a loop, until the result is not RSI\_INCOMPLETE

Each call to RSI\_ATTESTATION\_TOKEN\_CONTINUE retrieves up to one Granule of the attestation token.





The following pseudocode illustrates the process of a Realm obtaining an attestation token.

```
int get_attestation_token(...) { int ret; uint64_t size, max_size; uint64_t buf, granule; ret = RSI_ATTESTATION_TOKEN_INIT(challenge, &max_size); if (ret) { return ret; } buf = alloc(max_size); granule = buf; do { // Retrieve one Granule of data per loop iteration uint64_t offset = 0; do { // Retrieve sub-Granule chunk of data per loop iteration size = GRANULE_SIZE -offset; ret = RSI_ATTESTATION_TOKEN_CONTINUE(granule, offset, size, &len); offset += len; } while (ret == RSI_INCOMPLETE && offset < GRANULE_SIZE); // "offset" bytes of data are now ready for consumption from "granule" if (ret == RSI_INCOMPLETE) { granule += GRANULE_SIZE; } } while ((ret == RSI_INCOMPLETE) && (granule < buf + max_size)); return ret; } Up to one attestation token generation operation may be ongoing on a REC.
```

On execution of RSI\_ATTESTATION\_TOKEN\_INIT, if an attestation token generation operation is ongoing on the calling REC, it is terminated.

The challenge value provided to RSI\_ATTESTATION\_TOKEN\_INIT is included in the generated attestation token. This allows the relying party to establish freshness of the attestation token.

If the size of the challenge provided by the relying party is less than 64 bytes, it should be zero-padded prior to calling RSI\_ATTESTATION\_TOKEN\_INIT. Arm recommends that the challenge should contain at least 32 bytes of unique data.

- Generation of an attestation token can be a long-running operation, during which interrupts may need to be handled.


If a physical interrupt becomes pending during execution of RSI\_ATTESTATION\_TOKEN\_CONTINUE, a REC exit due to IRQ can occur.

On the next entry to the REC:

- If a virtual interrupt is pending on that REC, it is taken to the REC's exception handler
- RSI\_ATTESTATION\_TOKEN\_CONTINUE returns RSI\_INCOMPLETE
- The REC should call RSI\_ATTESTATION\_TOKEN\_CONTINUE again

## See also:

- [A4.3.5 REC exit due to IRQ](rmm-A4.3.md#a435-rec-exit-due-to-irq)
- [A6.1 Realm interrupts](rmm-A6.1.md)

- [A7.2.3.1.1 Realm challenge claim](rmm-A7.2.3.1.md#a72311-realm-challenge-claim)
- [B5.4.2 RSI\_ATTESTATION\_TOKEN\_CONTINUE command](rmm-B5.4.2.md)
- [B5.4.3 RSI\_ATTESTATION\_TOKEN\_INIT command](rmm-B5.4.3.md)
- [D1.7.1 Attestation token generation flow](rmm-D1.7.md#d171-attestation-token-generation-flow)
- [D1.7.2 Handling interrupts during attestation token generation flow](rmm-D1.7.md#d172-handling-interrupts-during-attestation-token-generation-flow)

## A7.2.3 Attestation token format

The CCA attestation token is a profiled IETF Entity Attestation Token (EAT).

The CCA attestation token is structured as a Conceptual Messages Wrapper (CMW) envelope RATS Conceptual Messages Wrapper (CMW) [7]. The CMW is a CBOR map that contains the CCA platform token and the Realm token, each encoded as an EAT CWT, and optionally contains a device token.

The Realm token contains structured data in CBOR, wrapped with a COSE\_Sign1 envelope according to the CBOR Object Signing and Encryption (COSE) standard.

The Realm token is signed by the Realm Attestation Key (RAK).

The CCA device token is an unsigned CBOR structure that represents the set of devices assigned to a Realm.

The CCA platform token contains structured data in CBOR, wrapped with a COSE\_Sign1 envelope according to the COSE standard.

Alternatively, the other certificates in the chain that endorses the CPAK certificate can be packaged in an additional entry within the RATS Conceptual Messages Wrapper (CMW) [7] token.

- The CCA platform token is signed by the CCA Platform Attestation Key (CPAK). ILMXMJ Where the CPAK is endorsed via an X.509 certificate chain, the endorsement artefacts can be included in the COSE\_Sign1 envelope of the CCA platform token using parameters from CBOR Object Signing and Encryption (COSE) Header Parameters for Carrying and Referencing X.509 Certificates [8]. It is recommended that this is done as follows: · The CPAK certificate is identified by including an x5t thumbprint parameter in the COSE\_Sign1 protected header. · The CPAK certificate itself is then packaged within an x5chain parameter in the COSE\_Sign1 unprotected header. · This x5chain parameter can also include other certificates that endorse the CPAK certificate.


The CCA platform token contains a hash of RAK\_pub. This establishes a cryptographic binding between the Realm token and the CCA platform token.

## The CCA attestation token is defined as follows:

```
;# import rfc9052 ; CBOR-tagged CMW Collection, see cca-token = #6.907(cca-token-CMW) EAT_CWT = ( bstr .cbor COSE_Sign1_Tagged ) CMW-CWT-element = ( [ eat-cwt-coap-label, EAT_CWT ] ) cca-device-token-bstr = (
```

```
draft-ietf-rats-msg-wrap
```


```
bstr .cbor cca-device-claims ) CMW-UCCS-device = ( [ eat-uccs-coap-label, cca-device-token-bstr ] ) cca-token-CMW = { cca-platform-token-label => CMW-CWT-element, cca-realm-delegated-token-label => CMW-CWT-element, ? cca-device-token-label => CMW-UCCS-device } cca-platform-token-label = 44234 cca-realm-delegated-token-label = 44241 cca-device-token-label = 44258 eat-cwt-coap-label = 263 ; application/eat+cwt ; the following labels are placeholders to be used where an implementation ; requires additional CMW entries cca-realm-direct-token-label = 44251 eat-uccs-coap-label = 601 ; application/uccs+cbor cca-platform-selective-device-evidence = 44252 cca-platform-comprehensive-device-evidence = 44253 ; device evidence is either uccs+cbor if hash locked or eat+cwt if signed cca-platform-cpak-cert-chain-label = 44254 ; cert-chain-coap-label = TBD ; application/pkix-pkipath cca-platform-cpak-cert-chain-with-evidence-label = 44255 ; cert-chain-with-evidence-coap-label = TBD ; application/dice-chain cca-platform-firmware-activity-log-label = 44256 ; activity-log-coap-label = TBD ; format IMPDEF
```

The composition of the CCA attestation token is summarised in the following figure.

## See also:

- Arm CCA Security model [4]
- Concise Binary Object Representation (CBOR) [9]
- CBOR Object Signing and Encryption (COSE) [10]
- Entity Attestation Token (EAT) [11]
- [A7.2.3.1 Realm claims](rmm-A7.2.3.1.md)
- [A7.2.3.2 CCA device claims](rmm-A7.2.3.2.md)
- [A7.2.3.3 CCA platform claims](rmm-A7.2.3.3.md)

Figure A7.1: Attestation token format

<!-- image -->

