## 6.3.61 SMMU\_S\_S2PII

The SMMU\_S\_S2PII characteristics are:

## Purpose

Configuration of stage 2 permission indirection interpretation in Secure state for Secure and Non-secure IPA spaces.

## Configuration

This register is present only when SMMU\_IDR3.S2PI == 1. Otherwise, direct accesses to SMMU\_S\_S2PII are RES0.

## Attributes

SMMU\_S\_S2PII is a 64-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

| 63      | 60 59   | 56 55   | 52 51   | 48 47   | 44 43   | 40 39   | 36 35   |        | 32   |
|---------|---------|---------|---------|---------|---------|---------|---------|--------|------|
| S2PII15 | S2PII14 | S2PII13 | S2PII12 | S2PII11 | S2PII10 | S2PII9  |         | S2PII8 |      |
| 31      | 28 27   | 24 23   | 20 19   | 16 15   | 12 11   | 8 7     | 4       | 3      | 0    |
| S2PII7  | S2PII6  | S2PII5  | S2PII4  | S2PII3  | S2PII2  |         | S2PII1  | S2PII0 |      |

## S2PII&lt;p&gt; , bits [4p+3:4p], for p = 15 to 0

The set of 16 stage 2 base permission interpretations.

This field is indexed by the PIIndex value derived from a stage 2 Block or Page descriptor, as S2PII[PIIndex*4+3 : PIIndex*4], to give a permission interpretation.

| S2PII<p>   | Meaning                        |
|------------|--------------------------------|
| 0b0000     | No Access                      |
| 0b0001     | Reserved, treated as No Access |
| 0b0010     | MRO                            |
| 0b0011     | MRO-TL1                        |
| 0b0100     | WO                             |
| 0b0101     | Reserved, treated as No Access |
| 0b0110     | MRO-TL0                        |
| 0b0111     | MRO-TL01                       |
| 0b1000     | RO                             |
| 0b1001     | RO+uX                          |
| 0b1010     | RO+pX                          |
| 0b1011     | RO+puX                         |
| 0b1100     | RW                             |
| 0b1101     | RW+uX                          |

| S2PII<p>   | Meaning   |
|------------|-----------|
| 0b1110     | RW+pX     |
| 0b1111     | RW+puX    |

This field is permitted to be cached in a TLB.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_S\_S2PII

Arm strongly recommends that this register is not written if SMMUEN is 1 and there are any STEs for which STE.S2PIE is 1.

Accesses to this register use the following encodings:

Accessible at offset 0x8030 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.