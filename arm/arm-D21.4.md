## D21.4 Performance Monitoring Groups (PMGs)

INQQHK

RBVQFD

IJYNXW

An MPAM resource monitor measures how much of a shared partitionable resource a software execution environment is using. See Memory system resource usage monitoring. A Performance Monitoring Group (PMG) is an identifier used in the filter register of a monitor, MSMON\_CFG\_MBWU\_FLT or MSMON\_CFG\_CSU\_FLT.

Filtering by PMG provides a way to group measurements, and a way to subdivide measurements. For example:

- Multiple monitors, each measuring usage of a different shared resource, can be made sensitive to a single PMG and no PARTIDs, so that they create a group of measurements for usage of the different shared resources by one PMGvalue.
- Monitors can be made sensitive to both a PARTID and a PMG, so that the PMG provides a subdivision of what is measured for the PARTID.

The PMG that an MPAM PE Requester sends as part of an MPAM information bundle is one of:

- If any of the conditions for the the Default PMG are met, the Default PMG.
- Otherwise, the PMG is determined as follows:
- -For an instruction fetch, MPAMn\_ELx.PMG\_I is used.
- -For a data access, MPAMn\_ELx.PMG\_D is used. However, if a data access is due to the execution of an SMEload or store instruction, or of a Streaming SVE mode load or store instruction, MPAMSM\_EL1.PMG\_D is used instead.

Also see Behavior when a PMG is out-of-range.

Software can set MPAMn\_ELx.{PMG\_D, PMG\_I} to the same or different PMG values.

## D21.4.1 PMG virtualization

IJNHSB

Performance Monitoring Group (PMG) values are not virtualized. PMGs modify PARTIDs and do not require any further virtualization support.

## D21.4.2 The Default PMG

RCZSZX

RPQSLB

ITJBXP

The Default PMG number is 0.

In each of the following scenarios, the MPAM PE Requester sends the Default PMG as part of the MPAM information bundle:

- When the MPAM enable control is 0, meaning that MPAM is disabled.
- When a PMG is an out-of-range PMGand the choice of CONSTRAINED UNPREDICTABLE behavior is to replace it with the Default PMG. See Behavior when a PMG is out-of-range.
- When a Default PARTID is generated due to a PARTID generation error, and the choice of CONSTRAINED UNPREDICTABLE behavior is to send the Default PMG. See PMG value when a Default PARTID is generated due to an MPAM error.

Note

The MPAMarchitecture permits SoC designers to make non-MPAM Requesters label every request to the memory system with the Default PMG.