## 12.2 Error consumption visible through the SMMU programming interface

On consumption of an external error, an SMMU supporting RAS is expected to report a RAS event through the RAS register interface. Alternatively, consumption of an external error by an SMMU that does not support RAS presents it with an external abort. In both cases, the SMMU records the event through the Event queue (pertaining to the Security state of the transaction that caused the error to be consumed) or GERROR as appropriate:

- F\_WALK\_EABT where a translation table walk consumed an error.
- F\_STE\_FETCH where an STE fetch consumed an error.
- F\_CD\_FETCH where a CD fetch consumed an error.
- SMMU\_(*\_)GERROR errors:
- -GERROR.CMDQ\_ERR triggered and CERROR\_ABT reported in SMMU\_(*\_)CMDQ\_CONS.ERR, where a command fetch consumed an error.
- -GERROR.PRIQ\_ABT\_ERR triggered when a PRI queue access is aborted because of an external error.
- -GERROR.EVENTQ\_ABT\_ERR triggered when an Event queue access is aborted because of an external error.
- -GERROR.DPT\_ERR triggered DPT\_EABT reported in SMMU\_(R\_)DPT\_CFG\_FAR, where a DPT lookup consumed an error.