## D9.2 GPC bypass windows

RZNCFP

All statements in this section require implementation of FEAT\_RME\_GPC3.

IJJLRM

Granule Protection Table (GPT) lookups can be skipped in portions of the memory map by using GPCbypass windows . All GPC bypass windows are the same size and have a base address that is aligned to a common stride value.

IXJPJF

The GPCBW\_EL3 system register describes the base, size, and stride properties of the GPC bypass windows. The following diagram illustrates how GPC bypass windows are described using GPCBW\_EL3 fields.

<!-- image -->

Figure D9-1 GPC bypass windows

| R SRQWF   | If GPCCR_EL3.GPCBW is set to 1 and a PA falls within a GPC bypass window range, then the GPC behaves as if the GPI encoding for the PA is All accesses permitted .                     |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R VKXCB   | GPC bypass windows are always located within the protected PA space that is configured using GPCCR_EL3.PPS.                                                                            |
| I XNHTX   | The GPC bypass window check does not modify the GPC fault reporting priority shown in Table D9-2, and is performed immediately after priority 3, Granule protection fault at Level 0 . |