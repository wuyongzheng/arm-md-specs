## D21.8 PE-side Maximum-bandwidth limit injection control

- ICBQCG If FEAT\_MPAM\_PE\_BW\_CTRL is implemented, software can use MPAMBWn\_ELx registers to impose a maximum limit on the bandwidth that requests from the MPAM PE use.
- RVQNTY When MPAMBWn\_ELx.ENABLED is 1 and either of the following is true, MPAM PE requests to the memory system are stalled until the bandwidth the MPAM PE is using drops below the limit configured in MPAMBWn\_ELx.MAX:
- MPAMBWIDR\_EL1.MAX\_LIM is 0b00 or 0b10 and MPAMBWn\_ELx.HARDLIM is set.
- MPAMBWIDR\_EL1.MAX\_LIM is 0b00 or 0b01 , MPAMBWn\_ELx.HARDLIM is not set, and an IMPLEMENTATION DEFINED mechanism has determined the MPAM PE downstream resources to be saturated.

Otherwise, MPAM PE requests to the memory system are sent unregulated.

- RRGLDT MPAMBWSM\_EL1.MAXis used instead of MPAMBWn\_ELx.MAX when:
- The MPAM PE is in streaming mode, and:
- -Accessing from SVE load/store/prefetch.
- -Accessing from SIMD&amp;FP load/store.
- Accessing from SME load/store.
- IDPMDJ If MPAMIDR\_EL1.HAS\_HCR is 1, meaning that the MPAM virtualization option is implemented, and FEAT\_MPAM\_PE\_BW\_CTRL is implemented, EL2 software can use MPAMBWCAP\_EL2 to cap an EL1&amp;0-assigned maximum bandwidth limit.
- RCMMQR When MPAMBWCAP\_EL2.ENABLED is 1, EL1&amp;0 requests to the memory system are regulated based on the limit computed as MIN(MPAMBWCAP\_EL2.CAP, MPAMx\_BW\_CTRL\_EL.MAX) and MIN(MPAMBWCAP\_EL2.CAP, MPAMBWSM\_EL1.MAX).
- IVVYKT If {MPAMBWn\_ELx, MPAMBWSM\_EL1, MPAMBWCAP\_EL2}.HW\_SCALE\_ENABLE is 1, then hardware is permitted to scale down the maximum limit configured in {MPAMBWn\_ELx, MPAMBWSM\_EL1}.MAX or MPAMBWCAP\_EL2.CAP according to the number of PEs in a group that are all issuing the same specific PARTID\_D or PARTID\_I at the corresponding exception level.
- RCRGFM It is IMPLEMENTATION DEFINED how hardware determines the number of PEs that are all issuing the same specific PARTID\_D or PARTID\_I at any point in time.
- IFYXGY Memory bandwidth regulation relies on tracking bandwidth use by PARTIDs. Bandwidth measurements have a dependence on time, and that dependence is referred to as the accounting window . The accounting window tracks bandwidth use over a period of time.

RFZMPQ The PE-side maximum bandwidth limit accounting window scheme and its software-discoverability are IMPLEMENTATION DEFINED.