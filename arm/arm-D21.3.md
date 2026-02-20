## D21.3 Partition Identifiers (PARTIDs)

| I NHJZF   | A Partition Identifier (PARTID) is a number that has no inherent meaning and does not imply any ordering. The number solely references a particular partition in a PARTID space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R CZHSY   | Each PARTID can exist once in each PARTID space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| R RBWRS   | The scope of a PARTID is bound by its PARTID space. If a PARTID is used in multiple PARTID spaces, then a reference to that PARTID in one PARTID space does not also reference that PARTID in the other PARTID spaces.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| I NFCZF   | Each MPAM-compliant component in an SoC is permitted to implement a maximum PARTID width that is less than or equal to the architecturally defined maximum width of 16-bits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| I NPBWK   | In an MPAMPE, MPAMIDR_EL1.PARTID_MAX reports the maximum PARTID implemented.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| R PJTCQ   | In an MPAMPE, MPAMn_ELx.{PARTID_D, PARTID_I} are permitted to hold PARTIDs in the range 0 to MPAMIDR_EL1.PARTID_MAX, inclusive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| R NYXVG   | The PARTID that an MPAMPERequester sends as part of an MPAMinformation bundle is one of: • If any of the conditions for the Default PARTID are met, the Default physical PARTID. • If the PARTID held is treated as virtual and a valid mapping exists, the mapped physical PARTID. Also see both: - Behavior when a valid mapping does not exist for a PARTID that is treated as virtual. - Behavior when a PARTID is out-of-range. • If the PARTID held is not treated as virtual, it is determined as follows: - For an instruction fetch, MPAMn_ELx.PARTID_I is used. - For a data access, MPAMn_ELx.PARTID_D is used. However, if a data access is due to the execution of |
| I QKRPD   | Software can set MPAMn_ELx.{PARTID_D, PARTID_I} to the same or different PARTID values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| I QDFWX   | Arm recommends that all MPAM-compliant components in an SoC implement the same maximum PARTID, though this is not required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| I TLVJP   | See also: • About MPAM, for the definitions of MPAM-compliant and PE Requester .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## D21.3.1 PARTID virtualization

RDNZFT

IPKKWM

ITSKGT

ITXFDH

The behaviors in this section apply if all the following are true:

- EL2 is implemented and enabled in the current Security state.
- Any FEAT\_MPAM version is implemented.
- MPAMIDR\_EL1.HAS\_HCR is 1, meaning that the MPAM virtualization option is implemented.
- If a version other than v1p0 is implemented and execution is in Secure state, then in addition:
- -MPAM3\_EL3.SDEFLT is 0, preventing generation of the Default physical PARTID in Secure state. See Effect of the MPAM3\_EL3.{SDEFLT, FORCE\_NS} controls on MPAM PE Secure state execution.

EL2 hypervisor software continuously updates MPAMvirtual PARTID mapping registers , MPAMVPM0\_EL2 to MPAMVPM7\_EL2, that map virtual PARTIDs to physical PARTIDs.

Each MPAMVPMn\_EL2 register contains four mapping fields , and the maximum implemented MPAMVPMn\_EL2 is MPAMIDR\_EL1.VPMR\_MAX. Therefore, the maximum implemented mapping field is (4 x VPMR\_MAX) + 3, and virtualized guests are limited to mapping fields in the range 0 to (4 x VPMR\_MAX) + 3.

IXGFNP

## RXSJVY

IBSWTR

RQTSFN

## If MPAMIDR\_EL1.VPMR\_MAX reports:

- 0b000 , the maximum implemented register is MPAMVPM0\_EL2, and the maximum implemented mapping field is (4 x 0) + 3 = 3. There are therefore four virtual PARTIDs available for virtualized guests, numbered 0 to 3, that can be mapped to physical PARTIDs.
- 0b111 , the maximum implemented register is MPAMVPM7\_EL2, and the maximum implemented mapping field is (4 x 7) + 3 = 31. There are therefore 32 virtual PARTIDs available for virtualized guests, numbered 0 to 31, that can be mapped to physical PARTIDs.

## RQMSMK When:

- MPAMHCR\_EL2.EL0\_VPMEN is 1, the PARTIDs in MPAM0\_EL1.{PARTID\_D, PARTID\_I} are treated as virtual , and EL0 produces requests with virtual PARTID spaces.
- MPAMHCR\_EL2.EL1\_VPMEN is 1, the PARTIDs in MPAM1\_EL1.{PARTID\_D, PARTID\_I} are treated as virtual, and EL1 produces requests with virtual PARTID spaces.

When a PARTID is treated as virtual, the MPAM PE attempts to map the PARTID to a physical PARTID using a MPAM virtual PARTID mapping register MPAMVPMn\_EL2. The PARTID that is treated as virtual is used as an index into both:

- The vector of physical PARTIDs that the mapping registers hold.
- The array of valid flags that MPAMVPMV\_EL2 holds.

## Example D21-2 Example of an MPAM PE mapping a virtual PARTID to a physical PARTID

Assume all the following are true:

- EL2 is implemented and enabled in the current Security state.
- Version v1p1 of FEAT\_MPAM is implemented, MPAMIDR\_EL1.HAS\_HCR is 1, meaning that the MPAM virtualization option is implemented, and MPAMIDR\_EL1.HAS\_SDEFLT is 0, meaning that MPAM3\_EL3.SDEFLT is not implemented.
- MPAMHCR\_EL2.EL1\_VPMEN is 1, meaning that PARTIDs in MPAM1\_EL1.{PARTID\_D, PARTID\_I} are treated as virtual.
- MPAMIDR\_EL1.VPMR\_MAX is 0b010 , meaning that the maximum implemented mapping field is (4 x 2) + 3 = 11.
- The value of MPAM1\_EL1.PARTID\_D is 6.

In this example, 6 is treated as virtual and is the index into the array of valid flags and vector of physical PARTIDs. Behavior is:

1. Valid flag MPAMVPMV\_EL2.VPM\_V&lt;6&gt; is checked:
1. Aresult of 1 means a valid mapping exists for virtual PARTID 6. MPAMVPM1\_EL2.PhysPARTID6 contains the physical PARTID that the MPAM PE Requester sends.
2. Aresult of 0 means invalid .
2. If the result is invalid, the mapping for the Default virtual PARTID, 0, is used. If a valid mapping does not exist for virtual PARTID 0, the MPAM PE Requester sends the Default physical PARTID.

## The virtual PARTID spaces are:

- If Secure state is implemented, Secure virtual PARTID space. This translates to the Secure physical PARTID space.
- Non-secure virtual PARTID space. This translates to the Non-secure physical PARTID space.
- If FEAT\_RME is implemented, Realm virtual PARTID space. This translates to the Realm physical PARTID space.

If a virtual PARTID is greater than (4 x MPAMIDR\_EL1.VPMR\_MAX) + 3, it is an out-of-range virtual P ARTID .

When a PARTID is an out-of-range virtual PARTID, the behavior is a CONSTRAINED UNPREDICTABLE choice of:

- The out-of-range virtual PARTID is replaced by any in-range virtual PARTID in the same PARTID space.
- The out-of-range virtual PARTID is replaced by the Default physical PARTID in the same PARTID space.

Example D21-1

IHWFQY

In each MPAMVPMn\_EL2.PhyPARTID&lt;n&gt; mapping field, the architecture requires implementation of sufficient low-order bits to represent MPAMIDR\_EL1.PARTID\_MAX. It is permitted to implement the bits that are higher-order than MPAMIDR\_EL1.PARTID\_MAX as RAZ/WI.

## D21.3.2 The Default PARTID

RQKQCF

RCQXMC

IXCZMJ

The Default PARTID number, in each PARTID space, is 0.

In the following scenario, the MPAM PE attempts to map the Default virtual P ARTID :

- When no valid mapping exists for a PARTID that is treated as virtual . See PARTID virtualization.

In each of the following scenarios, the MPAM PE Requester sends the Default physical P ARTID as part of the MPAM information bundle:

- When the MPAM enable control is 0, meaning MPAM is disabled.
- When the MPAM version implemented is any other than v1p0, the request is from Secure state, and MPAM3\_EL3.SDEFLT is implemented and is set to 1. See Effect of the MPAM3\_EL3.{SDEFLT, FORCE\_NS} controls on MPAM PE Secure state execution.
- When a PARTID is an out-of-range virtual P ARTID and the choice of CONSTRAINED UNPREDICTABLE behavior is to replace it with the Default physical PARTID. See Behavior when a PARTID is out-of-range.
- When no valid mapping exists for the Default virtual PARTID. See Behavior when a valid mapping does not exist for a PARTID that is treated as virtual.

Note

The MPAMarchitecture permits SoC designers to make non-MPAM Requesters label every request to the memory system with the Default physical PARTID.