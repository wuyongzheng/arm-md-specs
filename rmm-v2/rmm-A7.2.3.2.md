IFZMBB

IQHWQB

## A7.2.3.2 CCA device claims

This section defines the format of the CCA device token claim map. The format is described using a combination of Concise Data Definition Language (CDDL) and text description.

## IBPBTP The CCA device token claim map is defined as follows:

```
; CCA device token cca-device-claims = (cca-device-claim-map) cca-device-claim-map = { cca-device-profile cca-devices }
```

## See also:

- Concise Data Definition Language (CDDL) [12]
- A7.2.3.2.1 CCA device profile claim
- A7.2.3.2.2 CCA devices claim
- A7.2.3.2.3 Collated CDDL for CCA device claims
- A7.2.3.2.4 Example Device claims

## A7.2.3.2.1 CCA device profile claim

```
DRAFT IZFFXM The CCA device profile claim identifies the EAT profile to which the CCA device token conforms. INFJMF The CCA device profile claim is identified using the EAT profile label (265). ICQVZC The CCA device profile claim must be present in a CCA device token. IPVJTS The format of the CCA device profile claim is defined as follows: cca-device-profile-label = 265 ; EAT profile cca-device-profile-type = "tag:arm.com,2025:cca_device#2.0.0" cca-device-profile = ( cca-device-profile-label => cca-device-profile-type )
```

## A7.2.3.2.2 CCA devices claim

The CCA device identity digest is a cca-hash-type value which represents the digest of the device's identity.

The CCA device measurement digest is a cca-hash-type value representing a digest of the device's measurement evidence. If communication between the RMM and the device uses SPDM, the digest of the device measurements are the SPDM measurements exchange, request and response, between the device and the RMM. If communication between the RMM and the device uses an IMPLEMENTATION DEFINED channel, the digest of the device measurements contains a digest of the received measurements from the device.

IGSVNY The CCA device protocol negotiation data digest is a cca-hash-type value which represents the digest of the communication protocol negotiation data. If communication between the RMM and the device uses SPDM, this field corresponds to the VCA digest.

IWRLZT The CCA devices claim must be present in a CCA device token.

IPPKQK The CCA device coherent traffic IDE protection is a boolean value which specifies whether coherent traffic between the host and the device is protected by IDE.

ICDMFD The CCA device coherent traffic IDE protection field must be present in a CCA device claim.

IYXYYR The CCA device non-coherent traffic IDE protection is a boolean value which specifies whether non-coherent traffic between the host and the device is protected by IDE.

## A7.2. Realm attestation

IHJSXQ The CCA device non-coherent traffic IDE protection field must be present in a CCA device claim.

IZFPLT Devices are listed in the CCA devices claim in the order with which the corresponding VDEVs were created.

## ICBLCX The format of the CCA devices claim is defined as follows:

```
cca-devices-label = 44259 cca-device = { 1 => cca-hash-type, ; device identity digest 2 => cca-hash-type, ; device measurements exchange digest ? 3 => cca-hash-type, ; protocol negotiation data digest 4 => bool, ; coherent traffic IDE protection 5 => bool, ; non-coherent traffic IDE protection } cca-devices = ( cca-devices-label => [ + cca-device ] )
```

<!-- image -->

DCZRNS

## A7.2.3.2.3 Collated CDDL for CCA device claims

The format of the CCA device token claim map is defined as follows:

<!-- image -->

```
DRAFT ; CCA device token cca-device-claims = (cca-device-claim-map) cca-device-claim-map = { cca-device-profile cca-devices } cca-device-profile-label = 265 ; EAT profile cca-device-profile-type = "tag:arm.com,2025:cca_device#2.0.0" cca-device-profile = ( cca-device-profile-label => cca-device-profile-type ) cca-hash-type = bytes .size 32 / bytes .size 48 / bytes .size 64 cca-devices-label = 44259 cca-device = { 1 => cca-hash-type, ; device identity digest 2 => cca-hash-type, ; device measurements exchange digest ? 3 => cca-hash-type, ; protocol negotiation data digest 4 => bool, ; coherent traffic IDE protection 5 => bool, ; non-coherent traffic IDE protection } cca-devices = ( cca-devices-label => [ + cca-device ] )
```

IMNMGY

## A7.2.3.2.4 Example Device claims

An example device claim map is shown below in DIAG format:

```
/ Device claim map / { / cca-device-profile / 265: "tag:arm.com,2025:cca_device#2.0.0", / cca-devices / 44259: [ { / device identity digest / 1: h'000102030405060708090A0B0C0D0E0F / device measurements digest / 2: h'202122232425262728292A2B2C2D2E2F / protocol negotiation data digest / 3: h'404142434445464748494A4B4C4D4E4F / coherent traffic IDE protection / 4: false, / non-coherent traffic IDE protection 5: true } ]
```

<!-- image -->

```
DRAFT 101112131415161718191A1B1C1D1E1F', 303132333435363738393A3B3C3D3E3F', 505152535455565758595A5B5C5D5E5F', / }
```