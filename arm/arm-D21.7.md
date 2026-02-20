## D21.7 Virtualization support

IHRVFB

See the following subsections:

- Single PARTID for an EL1 guest OS and all its EL0 applications.
- Trap controls to virtualize MPAMIDR\_EL1.
- Trap controls to trap accesses to MPAM System registers.
- Trap controls priorities.
- Virtualization of PARTIDs.
- Interaction with FEAT\_VHE.
- Support for nested virtualization.

## D21.7.1 Single PARTID for an EL1 guest OS and all its EL0 applications

RFNKGZ

Setting MPAMHCR\_EL2.GSTAPP\_PLK to 1 causes MPAM1\_EL1 to supply PARTIDs and PMGs for both EL1 and EL0, and causes MPAM0\_EL1 to be unused, meaning that an EL1 guest OS and all its EL0 applications are in the same partition.

RJNWLV

IRMPJJ

When MPAMHCR\_EL2.{GSTAPP\_PLK, EL1\_VPMEN} is {1, 1}, the PARTID that results from the mapping process is the PARTID that the MPAM PE Requester sends for requests originating from EL0, as well as for those originating from EL1. See PARTID virtualization.

Note

EL1 software cannot determine the state of MPAMHCR\_EL2.GSTAPP\_PLK. MPAMHCR\_EL2.GSTAPP\_PLK==1 does not affect EL1 accesses to MPAM0\_EL1.

## D21.7.2 Trap controls to virtualize MPAMIDR\_EL1

ILDNNY

An EL2 hypervisor is able to provide a virtual view of MPAMIDR\_EL1 to an EL1 guest OS by using MPAMHCR\_EL2.TRAP\_MPAMIDR\_EL1, or MPAM2\_EL2.TIDR if MPAMIDR\_EL1.HAS\_TIDR is 1, to trap EL1 accesses to MPAMIDR\_EL1. The virtual view shows MPAMIDR\_EL1.PARTID\_MAX as the largest virtual P ARTID that the EL2 hypervisor is providing for the EL1 guest OS to use.

See also:

- Partition identifiers (PARTIDs).
- PARTID virtualization.

## D21.7.3 Trap controls to trap accesses to MPAM System registers

ITKRWM

ISQQYN

The MPAM architecture provides trap controls for all the following:

- EL1 accesses to MPAM0\_EL1, MPAM1\_EL1, and MPAMSM\_EL1, to trap these to EL2. See the trap controls MPAM2\_EL2.{TRAPMPAM0EL1, TRAPMPAM1EL1, EnMPAMSM} respectively.
- EL1 accesses to MPAMBW0\_EL1, MPAMBW1\_EL1, and MPAMBWSM\_EL1, to trap these to EL2. See the trap controls MPAMBW2\_EL2.{nTRAP\_MPAMBW0\_EL1, nTRAP\_MPAMBW1\_EL1, nTRAP\_MPAMBWSM\_EL1} respectively.
- EL2 and EL1 accesses to MPAM System registers, to trap these to EL3. See MPAM3\_EL3.TRAPLOWER and MPAMBW3\_EL3.nTRAPLOWER.

Accesses to all the following are not subject to any traps:

- MPAM1\_EL12.
- MPAM1\_EL1 when the Effective value of HCR\_EL2.E2H is 1.

See Interaction with FEAT\_VHE.

## D21.7.4 Trap controls priorities

RCFZGR

MPAM3\_EL3.TRAPLOWER and MPAMBW3\_EL3.nTRAPLOWER traps have priority over all traps controlled by MPAMregisters with names ending in \_EL2.

## D21.7.5 Virtualization of PARTIDs

IJNSFB

See PARTID virtualization.

## D21.7.6 Interaction with FEAT\_VHE

IQQPKC

ILVGCR

IFCMPY

RXCQTJ

When the Effective value of HCR\_EL2.E2H is 1, the following are alias registers for accesses from EL2:

- MPAM1\_EL12 is an alias for MPAM1\_EL1. See RPHHPL in System and Special-purpose register aliasing.
- MPAM1\_EL1 is an alias for MPAM2\_EL2. See RJGGMV in System and Special-purpose register redirection.
- MPAMBW1\_EL12 is an alias for MPAMBW1\_EL1. See RPHHPL in System and Special-purpose register aliasing.
- MPAMBW1\_EL1 is an alias for MPAMBW2\_EL2. See RJGGMV in System and Special-purpose register redirection.

If the Effective value of HCR\_EL2.E2H is 1, software executing at EL2 can use all of:

- MPAM1\_EL12, to control PARTIDs and PMGs for execution at EL1.
- MPAM1\_EL1, to configure the MPAM controls that apply to execution at EL2.
- MPAMBW1\_EL12, to configure a maximum limit on the bandwidth that EL1 requests use.
- MPAMBW1\_EL1, to configure a maximum limit on the bandwidth that EL2 requests use.

The Effective value of HCR\_EL2.E2H does not affect:

- Use of the following registers by EL2 software:
- -MPAM0\_EL1, to control PARTIDs and PMGs used by applications running at EL0, or MPAMBW0\_EL1, to configure a maximum limit on the bandwidth that EL0 requests use. When running applications at EL0, EL2 software also sets HCR\_EL2.TGE to 1 to route exceptions from EL0 to EL2.
- -MPAMHCR\_EL2.
- -MPAMVPMV\_EL2.
- -MPAMVPMn\_ELx.
- -MPAMBWCAP\_EL2.
- Use of the following registers by EL1 software:
- -MPAM0\_EL1, to control PARTIDs and PMGs used by applications running at EL0, and MPAM1\_EL1, to control PARTIDs and PMGs used by EL1 software.
- -MPAMBW0\_EL1 and MPAMBW1\_EL1, to configure maximum limits on the bandwidth that EL0 requests and EL1 requests use, respectively.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the alternative PARTID space in EL0 is selected only if the alternative PARTID space is selected in EL2. When the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the alternative PARTID space in EL0 is selected only if the alternative PARTID space is selected in EL1.

## D21.7.7 Support for nested virtualization

RWDPPT

In an MPAM PE with FEAT\_NV, when the Effective value of HCR\_EL2.{NV, NV2} is {1, 0}, EL1 accesses to the following System registers are trapped to a higher Exception level:

- MPAM1\_EL12.
- MPAM2\_EL2.
- MPAMHCR\_EL2.
- MPAMVPMV\_EL2.
- The MPAMvirtual PARTID mapping registers , MPAMVPM0\_EL2 to MPAMVPM7\_EL2.
- The MPAMbandwidth control registers MPAMBW2\_EL2, MPAMBWCAP\_EL2, and MPAMBW1\_EL12.

IXXYXW

RJPQVQ

IRXGXW

For the MPAM bandwidth control registers MPAMBW2\_EL2, MPAMBWCAP\_EL2, and MPAMBW1\_EL12, the controls that determine which Exception level EL1 accesses are trapped to are MPAM3\_EL3.TRAPLOWER and MPAMBW3\_EL3.nTRAPLOWER:

Table D21-15 MPAM Bandwidth control register traps

|   MPAM3_EL3.TRAPLOWER |   MPAMBW3_EL3.nTRAPLOWER | Behaviour when HCR_EL2.{NV, NV2} is {1, 0}   |
|-----------------------|--------------------------|----------------------------------------------|
|                     0 |                        0 | EL1 access trapped to EL3                    |
|                     0 |                        1 | EL1 access trapped to EL2                    |
|                     1 |                        0 | EL1 access trapped to EL3                    |
|                     1 |                        1 | EL1 access trapped to EL3                    |

Otherwise, for the other registers, the value of MPAM3\_EL3.TRAPLOWER determines which higher Exception level EL1 accesses are trapped to:

- When 0, the EL1 accesses are trapped to EL2.
- When 1, the EL1 accesses are trapped to EL3.

In an MPAM PE with FEAT\_NV2, Loads and stores generated by transforming register accesses describes the behavior when the Effective value of HCR\_EL2.{NV, NV1, NV2} is {1, 0, 1} and {1, 1, 1}, and Table D8-120 includes the MPAMSystem registers for which that behavior applies.

In an MPAM PE with FEAT\_NV2, when the Effective value of HCR\_EL2.{NV, NV2} is {1, 1}, setting MPAM3\_EL3.TRAPLOWER to 1 does not cause EL1 accesses to the MPAM System registers in Table D8-120 to be trapped to EL3.

When the Effective value of HCR\_EL2.{NV, NV2} is {1, 1}, EL1 accesses to the MPAM System registers are transformed to memory accesses. See Loads and stores generated by transforming register accesses.