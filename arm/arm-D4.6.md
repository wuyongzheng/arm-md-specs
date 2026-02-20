## D4.6 Resource operation

IPKCDG

FEAT\_ETE has a number of resources that can be used to provide advanced filtering functionality.

RPWBZK

The resources operate in one of the following states:

Running

All the resources are active.

Pausing

The resources are progressing to the Paused state.

Paused

All the resources are static and inactive except for External Input Selectors.

Figure D4-16 Resources operation

<!-- image -->

IHWYYK

As described in System behaviors, the trace unit can be disabled by either:

- Setting TRCPRGCTLR.EN to 0.

- Locking the OS Lock, by setting OSLAR\_EL1.OSLK to 1.

RJLLVN

While the resources are in the Running state, and when any of the following occur, the resources enter the Pausing state:

- The trace unit becomes disabled.

- The trace unit enters the low-power state.

- The PE begins executing in a Trace Prohibited region.

RYWDVJ

While the resources are in the Pausing state, the resources enter the Paused state in finite time.

RLYFDT

While the trace unit is in the Paused state, when all of the following are true, the resources enter the Running state:

- The trace unit is enabled.

- The trace unit is not in the low-power state.

- The PE is not executing in a Trace Prohibited region.

RTMPZZ

Atrace unit buffer overflow has no impact on the behavior of the resources.

## D4.6.1 Behavior of the resources while in the Running state

SJVYQP

The time taken for the resources to operate might vary between different trace unit implementations.

## D4.6.2 Behavior of the resources while in the Pausing state

| R RDCGC   | When the resources enter the Pausing state, the resources perform the following procedure: 1. All resources, except for the Sequencer and any Counters, are driven low as inputs to the Resource Selector logic.                                                                                                                                                                               |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I LGWRK   | The procedure that the resources perform when the resources are in the Pausing state has the result that, for resource events that are activated by a resource that is not a Counter or a Sequencer, no activity is lost, because all those resource events are updated.                                                                                                                       |
| I CQNGN   | When Counter and Sequencer states are propagated back as resources, so that a loop is created, then the following are true:                                                                                                                                                                                                                                                                    |
| I BRZXY   | When the trace unit becomes disabled, the behavior of the resources in the Pausing state ensures that the programmers' model provides a consistent view of the state of the trace unit resources. That is, regarding the Counters and the Sequencer, the following are true: • If the state of the Sequencer propagated back as a resource, then the view of the Sequencer as a resource event |

## D4.6.3 Behavior of the resources while in the Paused state

| I YXKSQ   | The behavior of the resources when the PE enters the low-power state or a Trace Prohibited region differs from other trace architectures defined by Arm.                                                                                                                                                                                                                              |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R FHYQW   | While the resources are in the Paused state and the trace unit is not disabled, the resources do not lose resource events that are in transition, except those permitted when moving through the Pausing state of the resources. See Behavior of the resources while in the Pausing state for details on the resource events that are permitted to be lost when in the Pausing state. |
| I HZRSS   | While the resources are in the Paused state, the resources might not observe resource events that are in transition until after the resources leave the Paused state.                                                                                                                                                                                                                 |
| R YWQNQ   | While the resources are in the Paused state, the resources remain in the state they are in.                                                                                                                                                                                                                                                                                           |
| R BQSMN   | While the resources are in the Paused state, the trace unit drives all External Outputs low.                                                                                                                                                                                                                                                                                          |
| R MVZYP   | When the trace unit becomes disabled and the resources enter the Paused state, and not before, the trace unit might set TRCSTATR.PMSTABLE to 1.                                                                                                                                                                                                                                       |
| R RWNTS   | While TRCSTATR.PMSTABLE is set to 1, all resources and resource events remain in a quiescent state.                                                                                                                                                                                                                                                                                   |
| I ZSHWT   | The behavior of the External Input Selectors is detailed in Operation while in Paused state.                                                                                                                                                                                                                                                                                          |

## D4.6.4 Behavior of resources on a Trace synchronization event

RRFSRY

When the following resources have finished calculations for all instructions prior to the previous Context synchronization event, a Trace synchronization event completes:

- Address Comparators.
- Context Identifier Comparators.
- Virtual Context Identifier Comparators.
- Single-shot Comparator Controls.

## D4.6.5 Resource organization

INJLRF There are 2 types of resources:

- Precise resources.
- Imprecise resources.

Each resource has a current state, which is output as a Resource state Selectors, and then used by various trace unit functions as a Resource event , see Figure D4-17.

IJCKLL

. The Resource state is selected by Resource

Figure D4-17 Resources organization

<!-- image -->

## D4.6.5.1 Precise resources

IQSPKY

The precise resources are used in the evaluation of the ViewInst include/exclude function and the ViewInst start/stop function.

RWNGDH

The trace unit evaluates the precise resources for each instruction block. See Instruction block for more details.

RNFDCZ

The trace unit maintains execution order of the precise resources.

Figure D4-18 Precise resource path

<!-- image -->

INNHSY

## D4.6.5.2 Imprecise resources

If a Resource is not a precise resource, it is an imprecise resource.

Figure D4-19 Imprecise resource path

<!-- image -->

## D4.6.5.3 Selecting a resource or a pair of resources

| I BRQFW   | Aresource is selected by using a Resource Selector.                                                                                                                                                                   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R QDJVV   | Each Resource Selector uses one of the 30 TRCRSCTLR<n> registers. The trace unit implements Resource Selectors in pairs, so that a maximum of 15 programmable pairs can be implemented.                               |
| R NRSGN   | Resource Selector 0 always provides a FALSE result.                                                                                                                                                                   |
| R SXSQT   | While the resources are in the Running state, Resource Selector 1 provides a TRUE result.                                                                                                                             |
| I TQVKS   | TRCIDR4.NUMRSPAIR indicates how many pairs of Resource Selectors are implemented.                                                                                                                                     |
| I MSHWC   | Resource Selectors can be used in pairs or used individually. When a pair of Resource Selectors is used, a Boolean function can be applied to the outputs of the combination of selected resources. See Figure D4-21. |
| R WZVDQ   | While TRCRSCTLR<n>.SELECT[m] is 1, the Resource Selector selects the Resource Number mof the group selected by TRCRSCTLR<n>.GROUP as described in Table D4-26.                                                        |

## Table D4-26 Resource grouping

| Group   | Resource Number   | Resource                                  |
|---------|-------------------|-------------------------------------------|
| 0b0000  | 0-3               | External Input Selectors 0-3              |
| 0b0000  | 4-15              | Reserved                                  |
| 0b0001  | 0-7               | PE Comparator Inputs 0-7                  |
| 0b0001  | 8-15              | Reserved                                  |
| 0b0010  | 0                 | Counter 0 at zero                         |
| 0b0010  | 1                 | Counter 1 at zero                         |
| 0b0010  | 2                 | Counter 2 at zero                         |
| 0b0010  | 3                 | Counter 3 at zero                         |
| 0b0010  | 4                 | Sequencer state 0                         |
| 0b0010  | 5                 | Sequencer state 1                         |
| 0b0010  | 6                 | Sequencer state 2                         |
| 0b0010  | 7                 | Sequencer state 3                         |
| 0b0010  | 8-15              | Reserved                                  |
| 0b0011  | 0-7               | Single-shot Comparator Control 0-7        |
| 0b0011  | 8-15              | Reserved                                  |
| 0b0100  | 0-15              | Single Address Comparator 0-15            |
| 0b0101  | 0-7               | Address Range Comparator 0-7              |
| 0b0101  | 8-15              | Reserved                                  |
| 0b0110  | 0-7               | Context Identifier Comparator 0-7         |
| 0b0110  | 8-15              | Reserved                                  |
| 0b0111  | 0-7               | Virtual Context Identifier Comparator 0-7 |
| 0b0111  | 8-15              | Reserved                                  |
| 0b1xxx  | 0-15              | Reserved                                  |

RHVNQG

While TRCRSCTLR&lt;n&gt;.INV is set to 0 and one or more resources in a group are selected, when any of the outputs of the selected resources are high, the Resource Selector fires.

RWFGMY

While TRCRSCTLR&lt;n&gt;.INV is set to 1, when none of the outputs of the selected resources are high, the Resource Selector fires.

ISZZMP

Figure D4-20 summarizes the process of resource selection.

IDLRMJ

RKTNJM

IQKTSJ

## D4.6.5.4 A Resource Selector pair

The Resource Selectors are arranged in pairs, and the result of each of a pair of Resource Selectors can be combined using a Boolean function and used to drive other resources and events in the trace unit.

For each TRCRSCTLR&lt;n&gt; register which is the lower register for a pair of Resource Selectors, the TRCRSCTLR&lt;n&gt; register has the TRCRSCTLR&lt;n&gt;.PAIRINV field.

## For example:

- TRCRSCTLR2 and TRCRSCTLR3 constitute a Resource Selector pair. In this case:
- -TRCRSCTLR2 is the lower register.
- -TRCRSCTLR2.PAIRINV optionally inverts the result of the Boolean function that is applied to the outputs of the combination of selected resources.
- -TRCRSCTLR3 is the upper register.
- -TRCRSCTLR3.PAIRINV is RES0.

This means that, when a Resource Selector pair is used, the following scenario is possible:

- One TRCRSCTLR&lt;n&gt; might select only one resource within the group.
- The other TRCRSCTLR&lt;n&gt; might select more than one resource from the group, so that the result is a logical ORof the selected resources.
- ABoolean function, for example a logical AND, might be applied to the outputs of the combination of selected resources.
- The result of that Boolean function might be inverted by using PAIRINV .

ILPJXK In Figure D4-21, the Boolean function is selected by using the INV field for each Resource Selector, with the PAIRINV field for each Resource Selector pair, see Table D4-27.

Figure D4-20 A Resource Selector

<!-- image -->

Figure D4-21 A Resource Selector pair

<!-- image -->

## Table D4-27 Selecting a Boolean function

| Function         | PAIRINV   | Resource A INV   | Resource B INV   |
|------------------|-----------|------------------|------------------|
| AANDB            | 0b0       | 0b0              | 0b0              |
| NOT(AANDB)       | 0b1       | 0b0              | 0b0              |
| Reserved         | 0b0       | 0b0              | 0b1              |
| NOT(A)ORB        | 0b1       | 0b0              | 0b1              |
| NOT(A)ANDB       | 0b0       | 0b1              | 0b0              |
| Reserved         | 0b1       | 0b1              | 0b0              |
| NOT(A) ANDNOT(B) | 0b0       | 0b1              | 0b1              |
| AORB             | 0b1       | 0b1              | 0b1              |

## D4.6.6 Address comparators

| I LGGVG   | An ETE trace unit provides between 0 and 16 Single Address Comparators (SACs), each of which compares the instruction address with a user-programmed value.   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R YCRNP   | The trace unit implements SACs in pairs, so that a trace unit implementation contains an even number of SACs.                                                 |
| I MNTCY   | TRCIDR4.NUMACPAIRS indicates how many pairs of SACs are implemented.                                                                                          |

| R YMVDZ   | When the PE executes instructions in Debug state, Address Comparators do not match.               |
|-----------|---------------------------------------------------------------------------------------------------|
| R YPWLR   | When the PE executes instructions in a Trace Prohibited region, Address Comparators do not match. |
| I RFTWJ   | Address Comparators might match in failed transactions.                                           |
| I WDJPG   | Address Comparators might match on Speculative execution.                                         |

## D4.6.6.1 Single Address Comparators

ISSHHT ASACcan be used in the following ways:

- As inputs to the ViewInst start/stop function in the ViewInst function. For more information, see ViewInst start/stop function filtering.
- As an individual resource.
- The comparator can be programmed so that, whenever the PE is in a specific Security state, the comparator only matches in certain Exception levels.

RDKCFF An SAC only matches on Exception levels and Security states as indicated by TRCACATR&lt;n&gt;.

|                  |   ¬ TRCACATRn.EXLEVEL S EL0                                               | Secure EL0     |
|------------------|-----------------------------------------------------------------------------|----------------|
|                  |      ¬ TRCACATRn.EXLEVEL S EL1                                         | Secure EL1     |
|                  |      ¬ TRCACATRn.EXLEVEL S EL2                                         | Secure EL2     |
|                  |     ¬ TRCACATRn.EXLEVEL S EL3                                           | EL3            |
|                  |       ¬ TRCACATRn.EXLEVEL NS EL0                                      | Non-secure EL0 |
|                  |     ¬ TRCACATRn.EXLEVEL NS EL1                                          | Non-secure EL1 |
| SAC EL i [ n ] = |  ¬ TRCACATRn.EXLEVEL NS EL2                                                | Non-secure EL2 |
|                  |         ¬ (TRCACATRn.EXLEVEL RL EL0 ⊕ TRCACATRn.EXLEVEL NS EL0)     | Realm EL0      |
|                  |           ¬ (TRCACATRn.EXLEVEL RL EL1 ⊕ TRCACATRn.EXLEVEL NS EL1) | Realm EL1      |
|                  |         ¬ (TRCACATRn.EXLEVEL RL EL2 ⊕ TRCACATRn.EXLEVEL NS EL2)     | Realm EL2      |

RQFNSK

An SAC only matches on the context indicated by TRCACATR&lt;n&gt;.CONTEXT and TRCACATR&lt;n&gt;.CONTEXTTYPE.

m = TRCACATRn.CONTEXT type = TRCACATRn.CONTEXTTYPE

RPYMZV

<!-- formula-not-decoded -->

When an instruction is executed, and the address of the lowest byte of the instruction exactly matches the programmed address of an SAC, the SAC matches.

<!-- formula-not-decoded -->

| I SPFXX   | For example, for a 4-byte instruction at address 0x1000 :                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I JZXFJ   | It is IMPLEMENTATION DEFINED whether an SAC matches when its programmed address matches any byte of an instruction which is not the lowest byte of the instruction.                                                                                                                                                                                                                                                                                                                                  |
| I VSFSS   | The Arm architecture supports disabling IT instructions on more than one subsequent instruction, using the ITD bits in the SCTLR, HSCTLR, and SCTLR_EL1 System registers. If any of the ITD bits are set to 1 and are affecting IT operation, and a SAC is programmed to match on the address of the instruction that is immediately after an IT instruction, when the instruction immediately after the IT instruction is executed it is CONSTRAINED UNPREDICTABLE whether that comparator matches. |
| S TFYFT   | If any of the ITD bits are set to 1, Arm recommends that a SAC is programmed to match on the address of the IT instruction, instead of the instruction immediately after the IT instruction.                                                                                                                                                                                                                                                                                                         |
| S MLDYK   | To avoid unexpected behavior from an SAC, Arm recommends that the SAC is always programmed with an address that is for the lowest byte of an instruction.                                                                                                                                                                                                                                                                                                                                            |
| I MCKFH   | When the instruction immediately after a MOVPRFX instruction executes, if a SAC is programmed to match on the address of this instruction, then it is CONSTRAINED UNPREDICTABLE whether that comparator matches.                                                                                                                                                                                                                                                                                     |
| S FPTHL   | Arm recommends that a SAC is programmed to match on the address of the MOVPRFX instruction, instead of the instruction immediately after the MOVPRFX instruction.                                                                                                                                                                                                                                                                                                                                    |
| I TBNTJ   | The operation of a SAC is as follows:                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

<!-- image -->

## D4.6.6.2 Address Range Comparators

Pairs of SACs are arranged to form one Address Range Comparator (ARC). An ARC is programmed with an address range, so that whenever any address in that range is accessed, the ARC matches. A trace unit contains between zero and eight ARCs. ARCs can be used in the following ways:

- Selected for the ViewInst include/exclude function in the ViewInst function. See ViewInst include/exclude function filtering.
- As individual resources.

An ARC is programmed by programming the SACs as follows:

- The first SAC is programmed with the start address of the instruction range.
- The second SAC is programmed with the end address of the instruction range.

The address that the second SAC is programmed with must be greater than or equal to the address that the first SAC is programmed with, that is, the end address must be greater than or equal to the start address.

While the start address of an ARC is greater than the end address, the behavior of the ARC is CONSTRAINED UNPREDICTABLE, that is, at any time the ARC might do one of the following:

- Match.
- Not match.

While the TRCACATR&lt;n&gt; registers for the SACs in an ARC are programmed to different values, the behavior of the

ARCis CONSTRAINED UNPREDICTABLE.

RLLQPL While an ARC is programmed with an instruction address range, when the PE executes an instruction at an address in the following range, the ARC matches:

start \_ address = TRCACVRn.ADDRESS end \_ address = TRCACVR ( n +1) .ADDRESS ARC \_ ADDR i [ n/ 2] = ( ThisInstrAddr () i ≥ start \_ address ) ∧ ( ThisInstrAddr () i ≤ end \_ address )

RYYXSQ

IRPFWZ

IRZFPT

SHSFTQ

When an instruction is executed, and the address of the lowest byte of the instruction is within the programmed address range of an ARC, the ARC matches.

When an instruction is executed and the programmed address range of an ARC contains addresses for one or more bytes of the instruction, but does not contain the address for the lowest byte of the instruction, it is IMPLEMENTATION SPECIFIC whether the ARC matches.

For example, for a 4-byte instruction at address 0x1000 :

- The lowest byte of the instruction is at 0x1000 .
- The second byte of the instruction is at 0x1001 .
- The third byte of the instruction is at 0x1002 .
- The highest byte of the instruction is at 0x1003 .

If the programmed address range contains 0x1000 , then the ARC always matches. However, if the programmed address range starts at either 0x1001 , 0x1002 , or 0x1003 , then it is IMPLEMENTATION SPECIFIC whether the ARC matches.

To avoid unexpected behavior from an ARC, Arm recommends that the ARC is always programmed with an address range that starts with an address for the lowest byte of an instruction.

IHDFQM

SWFSPV

RMXCGD

RXYJLC

| I VRRHS   | The Arm architecture supports disabling IT instructions on more than one subsequent instruction, using the ITD bits in the SCTLR, HSCTLR, and SCTLR_EL1 System registers. If any of the ITD bits are set to 1 and are affecting IT operation, and an ARCis programmed to include the address of the instruction that is immediately after an IT instruction but not include the IT instruction, when the instruction immediately after the IT instruction is executed then it is CONSTRAINED UNPREDICTABLE whether that comparator matches.   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| S DMHQH   | If any of the ITD bits are set to 1, Arm recommends that an ARCis programmed to include both the IT instruction and the instruction immediately after the IT instruction.                                                                                                                                                                                                                                                                                                                                                                     |
| I PBKPJ   | When the instruction immediately after a MOVPRFX instruction is executed, if an ARCis programmed to include the address of the instruction that is after the MOVPRFX instruction but not the MOVPRFX instruction, then it is CONSTRAINED UNPREDICTABLE whether that comparator matches.                                                                                                                                                                                                                                                       |
| S HVTHL   | Arm recommends that an ARCis programmed to include both the MOVPRFX instruction and the instruction immediately after the MOVPRFX instruction.                                                                                                                                                                                                                                                                                                                                                                                                |
| I HTXLT   | It might be possible for multiple matches to occur simultaneously. The definition of when matches occur simultaneously is IMPLEMENTATION SPECIFIC, and might vary because of runtime conditions. However, an example of when multiple matches might occur simultaneously is when multiple instructions are observed in the same processor clock cycle, so that multiple comparisons take place with each address in the programmed range. In this case, any of the following might occur:                                                     |
| R HMYMX   | When multiple ARCmatches occur simultaneously for one ARC, both of the following are true: • The ARCsignals a match at least once. • The ARCdoes not signal more matches than the number of instructions that are executed with an address that matches an address in the programmed range.                                                                                                                                                                                                                                                   |
| I CTBDN   | Each ARCcan be used with one, or a combination of, the following: • AContext Identifier Comparator. • AVirtual Context Identifier Comparator.                                                                                                                                                                                                                                                                                                                                                                                                 |
| R         | An ARConly matches on Exception levels and Security states as indicated by TRCACATR<2n>.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

<!-- image -->

RVSBJF

RRTXJN

An ARC only matches on the context indicated by TRCACATR&lt;2n&gt;.CONTEXT and TRCACATR&lt;2n&gt;.CONTEXTTYPE.

<!-- image -->

<!-- formula-not-decoded -->

The operation of an ARC is as follows:

<!-- formula-not-decoded -->

## D4.6.7 Context Identifier Comparator

IKDSNY

RDCCBY

RBKQKQ

IPBXRH

An ETE trace unit provides between zero and eight Context Identifier Comparators. Each Context Identifier Comparator can be used in any of the following ways:

- Associated with a SAC.
- Associated with an ARC.
- As an individual resource.

While a Context Identifier Comparator is associated with either an SAC or an ARC, only while the PE is executing with the Context identifier that the Context Identifier Comparator is programmed with and when an address is accessed which the SAC or ARC is programmed to match on, the SAC or ARC signals a match.

While a Context Identifier Comparator is used as an individual resource, when an instruction block is executed with the Context identifier that the Context Identifier Comparator is programmed with, the Context Identifier Comparator matches.

When using a Context Identifier Comparator as an independent resource to activate a resource event, the time that the resource event is activated relative to the time that the Context Identifier Comparator becomes active might be imprecise.

IRBLYL

RMPJBW

It might be possible for multiple matches of a Context Identifier Comparator to occur simultaneously. The definition of when matches occur simultaneously is IMPLEMENTATION SPECIFIC, and might vary because of runtime conditions. However, an example of when multiple matches might occur simultaneously is when multiple instructions are observed in the same processor clock cycle, so that multiple comparisons take place.

When multiple Context Identifier Comparator matches occur simultaneously for one Context Identifier Comparator, all of the following are true:

- The Context Identifier Comparator signals a match at least once.
- The Context Identifier Comparator does not signal more matches than the number of instructions that are executed with the Context identifier that the Context Identifier Comparator is programmed with.

IHDCJK AContext Identifier Comparator might match on Speculative execution, that is, a Context Identifier Comparator might match if the PE speculatively changes the Context identifier.

RMCYYC

When the PE executes instructions in Debug state, Context Identifier Comparators do not match.

RSRZGJ When the PE executes instructions in a Trace Prohibited region, Context Identifier Comparators do not match.

IGKDRL

The Context identifier might change at points that are not Context synchronization events, for example when a System instruction is used to write to the current Context identifier register. In these scenarios, the Context Identifier Comparator might compare against the old or new Context identifier value for any instruction after the P0 element before the System instruction, up to the Context synchronization event after the System instruction.

<!-- formula-not-decoded -->

## D4.6.8 Virtual Context Identifier Comparators

IBXVPG

An ETE trace unit provides between zero and eight Virtual Context Identifier Comparators. Each Virtual Context Identifier Comparator can be used in any of the following ways:

- Associated with a SAC.
- Associated with an ARC.

- As an individual resource.

| R RTRBM   | While a Virtual Context Identifier Comparator is associated with either an SAC or an ARC, only while the PE is executing with the Virtual context identifier that the Virtual Context Identifier Comparator is programmed with and when an address is accessed which the SAC or ARCis programmed to match on, the SAC or ARCsignals a match.                                                                                                                    |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R VWYMY   | While a Virtual Context Identifier Comparator is used as an individual resource, when an instruction block is executed with the Virtual context identifier that matches the Virtual Context Identifier Comparator value, the Virtual Context Identifier Comparator matches.                                                                                                                                                                                     |
| R FLXQL   | While TRFCR_EL2.CX indicates that Virtual Context Identifier Comparators cannot match, Virtual Context Identifier Comparators do not match.                                                                                                                                                                                                                                                                                                                     |
| R LPKBR   | When the PE executes instructions in Debug state, Virtual Context Identifier Comparators do not match.                                                                                                                                                                                                                                                                                                                                                          |
| R WZWLT   | When the PE executes instructions in a Trace Prohibited region, Virtual Context Identifier Comparators do not match.                                                                                                                                                                                                                                                                                                                                            |
| I SCPJP   | When using a Virtual Context Identifier Comparator as an independent resource to activate a resource event, the time at which the resource event is activated relative to the time at which the Virtual Context Identifier Comparator becomes active might be imprecise.                                                                                                                                                                                        |
| R LJRPW   | AVirtual Context Identifier Comparator is associated with an SAC by programming TRCACATR<n>.CONTEXT for the SAC.                                                                                                                                                                                                                                                                                                                                                |
| I GJCRG   | It might be possible for multiple matches of a Virtual context identifier to occur simultaneously. The definition of when matches occur simultaneously is IMPLEMENTATION SPECIFIC, and might vary because of runtime conditions. However, an example of when multiple matches might occur simultaneously is when multiple instructions are observed in the same processor clock cycle, so that multiple comparisons take place.                                 |
| R JNNDL   | When multiple Virtual Context Identifier Comparator matches occur simultaneously for one Virtual Context Identifier Comparator, both of the following are true: • The Virtual Context Identifier Comparator signals a match at least once.                                                                                                                                                                                                                      |
| I NPPCF   | AVirtual Context Identifier Comparator might signal a match on Speculative execution, that is, a Virtual Context Identifier Comparator might signal a match when the PE speculatively changes the Virtual context identifier.                                                                                                                                                                                                                                   |
| I PPWXT   | The Virtual context identifier might change at points which are not Context synchronization events, for example when a System instruction is used to write to CONTEXTIDR_EL2. In these scenarios, the Virtual Context Identifier Comparator might compare against the old or new Virtual context identifier value for any instruction after the P0 element before the System instruction, up to the Context synchronization event after the System instruction. |

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## D4.6.9 Counters

INCCBM

The Counters that are employed by the ETE architecture are all decrement counters.

The ETE architecture enables a trace unit to connect Counter outputs to resource events, so that a Counter at zero state can be used as a resource to activate a resource event. For example, a Counter at zero state might be used to assert an External Output or to make ViewInst active.

An ETE trace unit provides up to four 16-bit Counters. TRCIDR5.NUMCNTR indicates how many Counters are implemented. For each Counter, the following can be specified:

- The initial counter value. This can be programmed using TRCCNTVR&lt;n&gt;.
- The reload value. This can be programmed using TRCCNTRLDVR&lt;n&gt;.
- The resource event that causes the Counter to reload with the reload value. This resource event is called RLDEVENT. In addition, if required, the Counter can be programmed so that it automatically reloads whenever it reaches zero.
- The resource event that enables the Counter to decrement. This resource event is called CNTEVENT. The Counter decrements whenever CNTEVENT is active.

RRBMQM

The processor clock clocks the Counters in the trace unit.

RPZQGV

While the PE is stalled, the Counters continue to count.

RFHFMP

While the resources are in the Paused state, the Counters do not count.

RLFVYH

When a Counter value is changed by anything other than a direct write to TRCCNTVR&lt;n&gt;, the trace unit considers the change to be an indirect write to TRCCNTVR&lt;n&gt;.VALUE.

IMLDXC

Each Counter operates in one of the two following possible modes:

- Normal mode.

- Self-reload mode.

RSBQPN

While the Counter is in Normal mode, when the Counter reaches zero, the Counter remains at zero until the reload resource event, RLDEVENT, occurs.

RHYLGG

While the Counter is in Normal mode, the Counter-at-zero resource is active for the whole of the time that the Counter is at zero.

RYLYPH

While the Counter is in Self-reload mode, when the Counter reaches zero, when the decrement resource event is next active, the trace unit reloads the Counter with the reload value.

RVGJNL

While the Counter is in Self-reload mode, when the Counter value is zero, the decrement resource event is active and the reload resource event is not active, the Counter-at-zero resource is active for one cycle.

IKTRXV

The following examples show various operating scenarios for a single Counter. Each Counter is programmed with a reload value of 0x3 .

Figure D4-22 Counter Example 1, Normal mode

<!-- image -->

Figure D4-23 Counter Example 2, Normal mode

<!-- image -->

<!-- image -->

Figure D4-24 Counter Example 3, Self-reload mode

Figure D4-25 Counter Example 4, Self-reload mode

<!-- image -->

Figure D4-26 Counter Example 5, Self-reload mode

<!-- image -->

RKXLKC

While the decrement resource event is inactive, the Counters do not decrement.

RDDCDK

The trace unit prioritizes the reload resource event over the count decrement resource event.

ISHWBT

## D4.6.9.1 Counter Operation in Normal mode

IBRLYH

This table describes the counter operation in Normal mode.

| RLDEVENT   | dec_action   | Counter value   | Action    | Resource Active   | Notes                                                           |
|------------|--------------|-----------------|-----------|-------------------|-----------------------------------------------------------------|
| Inactive   | x            | 0               | Stable    | Yes               | Resource is active while Counter is at zero and remains at zero |
| Inactive   | 0            | > 0             | Stable    | No                | No activity                                                     |
| Inactive   | 1            | > 0             | Decrement | No                | Decrement when not zero                                         |
| Active     | x            | 0               | Reload    | Yes               | Reload, but resource is active because Counter is at zero       |
| Active     | x            | > 0             | Reload    | No                | Reload                                                          |

## D4.6.9.2 Counter Operation in Self-reload mode

This table describes the counter operation in Self-reload mode:

| RLDEVENT   | dec_action   | Counter value   | Action    | Resource Active   | Notes                                                                                                 |
|------------|--------------|-----------------|-----------|-------------------|-------------------------------------------------------------------------------------------------------|
| Inactive   | 0            | x               | Stable    | No                | No activity, resource is not active even if the Counter is at zero                                    |
| Inactive   | 1            | 0               | Reload    | Yes               | Reload because dec_action is active and the Counter is at zero, resource is active only in this cycle |
| Inactive   | 1            | > 0             | Decrement | No                | Decrement when not zero                                                                               |
| Active     | x            | x               | Reload    | No                | Reload regardless of decrement action and the value of the Counter, resource is never active          |

## D4.6.9.3 Forming a larger Counter from two separate Counters

ITYLSH

Some Counters can be chained together to form a larger counter, so that every time one Counter reloads, another Counter decrements.

IMMDRW

The following example shows an operating scenario for 2 Counters chained together. Counter 0 is programmed with a reload value of 0x2 .

Figure D4-27 Chained Counter Example 1

<!-- image -->

RWPWQD

Only certain Counters can be programmed to be chained together, as follows:

- Counter 1 can be programmed to decrement when Counter 0 reloads.

- Counter 3 can be programmed to decrement when Counter 2 reloads.

RQHZFW

The decrement resource event for the higher Counter n is active when either of the following occurs:

- The lower Counter reloads due to one of the following:

- The reload resource event that is selected by TRCCNTCTLR&lt;n-1&gt;.RLDEVENT.

- The Self-reload mechanism that is controlled by TRCCNTCTLR&lt;n-1&gt;.RLDSELF.

- The decrement resource event that is selected by TRCCNTCTLR&lt;n&gt;.CNTEVENT is active.

RBDPDN While two Counters are chained together to form a larger counter, the larger counter appears as a 32-bit counter without any tearing of the values between the two Counters.

IFTDHL

For example, if Counter 0 is in Self-reload mode and has a value of 0x0000 and a reload value of 0xFFFF , and Counter 1 is in Normal mode and has a value of 0x1234 , then when a decrement resource event occurs on Counter 0, Counter 0 reloads to 0xFFFF . The reload of Counter 0 causes Counter 1 to decrement, resulting in a value of 0x1233 . Therefore the sequence on the Counters on consecutive cycles is 0x1234\_0000 and 0x1233\_FFFF .

IBCMGM

For Counters 1 and 3, TRCCNTCTLR&lt;n&gt;.CNTCHAIN is an RW field that determines whether the Counter is chained. For Counters 0 and 2, TRCCNTCTLR&lt;n&gt;.CNTCHAIN is RES0.

Note

The CounterAtZero resource might not be asserted at the same time that the Counter is at zero. For example, this could happen if the trace unit implementation pipelines some logic.

IKJSDV

The CounterAtZero resource might not be asserted at the same time that the Counter is at zero. For example, this could happen if the trace unit implementation pipelines some logic.

D4.6.9.4

Pseudocode

D4.6.9.4.1

EvalAllCounters()

```
// The counter-at-zero resources array boolean CounterAtZero[0..3]; // // EvalAllCounters() is called each clock cycle // EvalAllCounters() array boolean reload[0..3]; reload[0] = EvalCounter(0, FALSE); reload[1] = EvalCounter(1, reload[0]); reload[2] = EvalCounter(2, FALSE); reload[3] = EvalCounter(3, reload[2]); // // EvalCounter() is called for each counter // boolean EvalCounter(integer index, boolean lower_reloads) boolean dec_action; boolean resource_active; bits(16) next_value; boolean reload; boolean decrement; // A dec_action signal is constructed which indicates whether the counter // decrements. This is based on TRCCNTCTLR[n].CNTEVENT and, for counters // which support chaining, on TRCCNTCTLR[n].CNTCHAIN and on whether or not // the lower counter is reloading. dec_action = IsEventActive(TRCCNTCTLR[index].CNTEVENT) || (TRCCNTCTLR[index].CNTCHAIN && lower_reloads); // The counter-at-zero resource is active if the counter is // currently at zero and is either in Normal mode or in // Self-Reload mode and dec_action is active and the reload // event is not active. resource_active = (TRCCNTVR[index] == 0) && (!TRCCNTCTLR[index].RLDSELF || (dec_action && !IsEventActive(TRCCNTCTLR[index].RLDEVENT) ) ); // The counter reloads if the reload event is active or the self-reload // mechanism causes a reload. reload = IsEventActive(TRCCNTCTLR[index].RLDEVENT) || (TRCCNTCTLR[index].RLDSELF && dec_action && TRCCNTVR[index] == 0); // The counter only decrements if it is nonzero and does not reload and // dec_action is active. decrement = !reload && (TRCCNTVR[index] != 0) && dec_action; // Determine the next value of the counter if reload then TRCCNTVR[index] = TRCCNTRLDVR[index].VALUE; else if decrement then TRCCNTVR[index] = TRCCNTVR[index] 1; else TRCCNTVR[index] = TRCCNTVR[index]; CounterAtZero[index] = resource_active; return reload;
```

## D4.6.10 Sequencer

IBGGRG

An ETE trace unit can contain a Sequencer state machine that has four states.

<!-- image -->

Figure D4-28 Sequencer state machine

| I PTVBH   | TRCIDR5.NUMSEQSTATE indicates whether the state machine is implemented.                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R QYNJH   | If the Sequencer state machine is implemented, it has four states, numbered 0 to 3.                                                                                                                                                                                                                                                                                                                                                                                                     |
| R TQWHX   | When the trace unit leaves the Disabled state, the Sequencer state machine starts in the state programmed in TRCSEQSTR.STATE.                                                                                                                                                                                                                                                                                                                                                           |
| I SYCBV   | The Sequencer can be connected to resource events, so that the Sequencer transitions from one state to another when certain resource events occur. The TRCSEQEVR<n> registers can be used to specify which resource events cause the state machine to transition. Each register can be used to specify the following:                                                                                                                                                                   |
|           | • Aresource event that causes the state machine to progress to the next state.                                                                                                                                                                                                                                                                                                                                                                                                          |
|           | • Aresource event that causes the state machine to transition backwards to the previous state.                                                                                                                                                                                                                                                                                                                                                                                          |
|           | Different resource events can be chosen to cause the Sequencer to transition between different states. For example, a particular resource event might cause an F0 transition from state 0 to state 1 on one processor clock cycle, whereas a different resource event might cause an F1 transition from state 1 to state 2 on the next processor clock cycle. Athird independent resource event might cause a B1 transition backwards from state 2 to state 1 on the third clock cycle. |
| R NPVRQ   | The trace unit prioritizes forward transitions over backward transitions in the Sequencer state machine. That is, when two resource events occur that result in a forward transition conflicting with a backward transition in the same processor clock cycle, the trace unit gives priority to the forward transition and ignores the backward transition.                                                                                                                             |
| I QNFJZ   | The Sequencer can progress through multiple states in a single processor clock cycle. For example, if the Sequencer is in state 0 and the resource events that cause an F0 and F1 transition to take place both become active in one clock cycle, then the Sequencer progresses from state 0 to state 2.                                                                                                                                                                                |
| I DMZGJ   | The Sequencer can be reset to state 0 from any other state. TRCSEQRSTEVR can be used to specify a resource event to reset the Sequencer.                                                                                                                                                                                                                                                                                                                                                |
| R HQBBF   | When a resource event that causes an RST transition occurs, the Sequencer finishes the clock cycle in state 0 and does not progress to another state until the next clock cycle.                                                                                                                                                                                                                                                                                                        |
| R KVSXC   | The trace unit prioritizes RST transitions over all other transitions. That is, when a resource event that causes an RST transition is active in the same clock cycle as resource events that cause other transitions, the trace unit gives priority to the RST transition and ignores all other transitions.                                                                                                                                                                           |
| R JDPYL   | The following table defines all of the possible state transitions.                                                                                                                                                                                                                                                                                                                                                                                                                      |

|      | To                              |                               |                      |          |
|------|---------------------------------|-------------------------------|----------------------|----------|
| From | 0                               | 1                             | 2                    | 3        |
| 0    | RST &#124; !F0                  | F0 &!F1                       | F0&F1&!F2            | F0&F1&F2 |
| 1    | RST &#124; (B0 &!F1 &!F0)       | (!B0 &#124; F0) &!F1          | F1 &!F2              | F1&F2    |
| 2    | RST &#124; (B0 &B1&!F2&!F1&!F0) | B1 &(!B0 &#124; F0) &!F1 &!F2 | (!B1 &#124; F1) &!F2 | F2       |

|    | To                               |             |          |                 |               |
|----|----------------------------------|-------------|----------|-----------------|---------------|
|  3 | RST&#124;(B0&B1&B2&!F2&!F1& !F0) | B2 &B1&(!B0 | B2 &(!B1 | &#124; F1) &!F2 | !B2 &#124; F2 |

IYQZGV

- RVDTDP

If multiple resource events that cause transitions become active in one processor clock cycle, there is no guarantee that

- the order of these resource events becoming active is observed. For example, you might program:
- F0 to be active on an instruction Address Comparator at address 0x1000 .
- F1 to be active on an instruction Address Comparator at address 0x1004 .

If the instruction at 0x1000 and the instruction at 0x1004 are executed in the same processor clock cycle, then the transition from state 0 to state 2 occurs regardless of the program order of the two instructions.

When the Sequencer state is changed by anything other than a direct write to TRCSEQSTR, the trace unit considers the change to be an indirect write to TRCSEQSTR.STATE.

- IWYFZH The ETE architecture provides each Sequencer state as a resource, so that states can be used to trigger other resource events in the trace unit.

<!-- image -->

Figure D4-29 Sequencer operation

| R HQHFT   | When the Sequencer progresses through multiple states in a single processor clock cycle, for each state that it passes through, the resource state that the Sequencer triggers is active for that cycle.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I DCFMF   | For example, if the Sequencer is in state 0, and in one processor clock cycle it moves to state 3, then the resource events that state 1 and state 2 are connected to must be active for that clock cycle. The same rule applies if the Sequencer is transitioning backwards, so that if it is in state 3, and in one processor clock cycle B2 and B1 cause it move to state 1, then the resource event that state 2 is connected to must be active for that clock cycle. The exception to this is when an RST transition causes the Sequencer to return to state 0. For example, if the is in state 3, and in one processor clock cycle it moves to state 0, then the resource events that state 2 and stage 1 are connected to must not become active. |
|           | Sequencer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

Figure D4-30 Example of State Transitions

<!-- image -->

## D4.6.10.1 Pseudocode

## D4.6.10.1.1 EvalSequencer()

```
// The sequencer state resources array boolean SequencerState[0..3]; // EvalSequencer() // =============== EvalSequencer() (rst, txn0, txn1, txn2, txn3) = // Sequencer State resources SequencerState[0] = FALSE; SequencerState[1] = FALSE; SequencerState[2] = FALSE; SequencerState[3] = FALSE; SequencerResource(rst, txn0, txn1, txn2, txn3); SequencerNextState(rst, txn0, txn1, txn2, txn3);
```

D4.6.10.1.2 SequencerTransitions()

```
SequencerTransitions();
```

```
// SequencerTransitions() // ====================== ( boolean rst, array boolean txn0[0..3], array boolean txn1[0..3], array boolean txn2[0..3], array boolean txn3[0..3]) SequencerTransitions() boolean F0 = IsEventActive(TRCSEQEVR0.F); boolean B0 = IsEventActive(TRCSEQEVR0.B); boolean F1 = IsEventActive(TRCSEQEVR1.F); boolean B1 = IsEventActive(TRCSEQEVR1.B); boolean F2 = IsEventActive(TRCSEQEVR2.F); boolean B2 = IsEventActive(TRCSEQEVR2.B); boolean rst = IsEventActive(TRCSEQRSTEVR); array boolean txn0[0..3]; array boolean txn1[0..3]; array boolean txn2[0..3]; array boolean txn3[0..3]; txn0[1] = F0 && !F1; txn0[2] = F0 && F1 && !F2; txn0[3] = F0 && F1 && F2; txn1[0] = B0 && !F0 && !F1; txn1[1] = (!B0 || F0) && !F1; txn1[2] = F1 && !F2; txn1[3] = F1 && F2; txn2[0] = B0 && !F0 && B1 && !F1 && !F2; txn2[1] = (!B0 || F0) && B1 && !F1 && !F2; txn2[2] = (!B1 || F1) && !F2; txn2[3] = F2; txn3[0] = B0 && !F0 && B1 && !F1 && B2 && !F2; txn3[1] = (!B0 || F0) && B1 && !F1 && B2 && !F2; txn3[2] = (!B1 || F1) && B2 && !F2; txn3[3] = (!B2 || return (rst, txn0, txn1, txn2, txn3)
```

## D4.6.10.1.3

```
// SequencerResource() // =================== SequencerResource(boolean rst, array boolean txn0[0..3], array boolean txn1[0..3], array boolean txn2[0..3], array boolean txn3[0..3]) case TRCSEQSTR.STATE of 0 then SequencerState[0] = TRUE; 1 then SequencerState[1] = TRUE; 2 then SequencerState[2] = TRUE; 3 then SequencerState[3] = TRUE; // If the statemachine passes through // several states in one iteration then // set the SequencerState
```

```
F2); SequencerResource() as appropriate.
```

```
if !rst then case TRCSEQSTR.STATE of 0 then if txn0[2] then SequencerState[1] = TRUE; if txn0[3] then SequencerState[1] = TRUE; SequencerState[2] = TRUE; 1 then if txn1[3] then SequencerState[1] = TRUE; SequencerState[2] = TRUE; 2 then if txn2[0] then SequencerState[1] = TRUE; 3 then if txn3[0] then SequencerState[1] = TRUE; SequencerState[2] = TRUE; if txn3[1] then SequencerState[2] = TRUE;
```

## D4.6.10.1.4 SequencerNextState()

```
// SequencerNextState() // ==================== SequencerNextState(boolean rst, array boolean txn0[0..3], array boolean txn1[0..3], array boolean txn2[0..3], array boolean txn3[0..3]) if rst then TRCSEQSTR.STATE = 0; else case TRCSEQSTR.STATE of 0 then if txn0[1] then TRCSEQSTR.STATE = 1; if txn0[2] then TRCSEQSTR.STATE = 2; if txn0[3] then TRCSEQSTR.STATE = 3; 1 then if txn1[0] then TRCSEQSTR.STATE = 0; if txn1[1] then TRCSEQSTR.STATE = 1; if txn1[2] then TRCSEQSTR.STATE = 2; if txn1[3] then TRCSEQSTR.STATE = 3; 2 then if txn2[0] then TRCSEQSTR.STATE = 0; if txn2[1] then TRCSEQSTR.STATE = 1; if txn2[2] then TRCSEQSTR.STATE = 2; if txn2[3] then TRCSEQSTR.STATE = 3; 3 then if txn3[0] then TRCSEQSTR.STATE = 0; if txn3[1] then
```

- RXVVYX

RXFJGB

RSWNFV

RGBDCK

```
TRCSEQSTR.STATE = 1; if txn3[2] then TRCSEQSTR.STATE = 2; if txn3[3] then TRCSEQSTR.STATE = 3;
```

## D4.6.11 Single-shot Comparator Controls

IQSKXC

ITLFLF

IRBMXW

If a trace unit is exposed to speculative execution or execution in Transactional state, when Address Comparators are used to activate resource events in the trace unit, then those resource events might be activated when speculative execution occurs:

- ASingle Address Comparator might signal a match on speculative execution or within a transaction.
- An Address Range Comparator might signal a match on speculative execution or within a transaction.

For example, this means that if an Address Comparator is used to activate a Counter or assert an External Output, then that Counter might decrement, or that External Output might become asserted, as a result of speculative execution. The Single-shot Comparator Controls for Address Comparators make it possible for resource events in the trace unit to be activated based only on non-speculative execution, that is, only on architectural execution.

Atrace unit can provide up to eight Single-shot Comparator Controls. Each Single-shot Comparator Control can be used with one or more Address Comparators.

Single-shot Comparator Controls can be used as a trace unit resource, to activate trace unit resource events. For example, a Single-shot Comparator Control can be selected to:

- Enable or reload a trace unit Counter.
- Initiate a transition in the trace unit Sequencer state machine.
- Assert an External Output.

ASingle-shot Comparator Control can therefore, if programmed to assert an External Output, be used to indicate to a trace analyzer that a particular instruction has been resolved for execution. This means that a trace analyzer can start or stop trace capture that is based on the architectural execution of that instruction.

If a trace unit contains one or more Address Comparators, Arm recommends that at least one Single-shot Comparator Control is implemented.

- IVNBPG ASingle-shot Comparator Control works in the following way:
1. One or more Address Comparators are selected by using the TRCSSCCR&lt;n&gt; for the Single-shot Comparator Control. The selected Address Comparators can be all Single Address Comparators, all Address Range Comparators, or a combination of both.
2. When one of the selected Address Comparators matches, then when the instruction is confirmed to have architecturally executed, the Single-shot Comparator Control fires.

When a selected Address Comparator matches, but the instruction is confirmed to have not architecturally executed, the Single-shot Comparator Control does not fire.

When an instruction which matches an Address Comparator is confirmed to have architecturally executed, and the Address Comparator is selected by TRCSSCCR&lt;n&gt;, and TRCSSCSR&lt;n&gt;.STATUS is 0 or TRCSSCCR&lt;n&gt;.RST is 1, the Single-shot Comparator Control &lt;n&gt; fires.

When a TSB CSYNC instruction is executed while a Single-shot Comparator Control is programmed to fire due to the TSB CSYNC instruction, only when the related Trace synchronization event has completed, the Single-shot Comparator fires.

When a Single-shot Comparator Control fires, the trace unit considers this an indirect write to set TRCSSCSR&lt;n&gt;.STATUS to 1.

While the resources are in the Paused state, when the conditions for a Single-shot Comparator Control to fire are met:

- If TRCSSCCR&lt;n&gt;.RST is 1 or TRCSSCSR&lt;n&gt;.STATUS is 0 then TRCSSCSR&lt;n&gt;.PENDING is indirectly written to 1.
- If TRCSSCCR&lt;n&gt;.RST is 0 and TRCSSCSR&lt;n&gt;.STATUS is 1 then TRCSSCSR&lt;n&gt;.PENDING is either indirectly written to 1 or is unchanged.

| R SDDWY   | When one of the Address Comparators selected for a Single-shot Comparator Control matches, when the instruction that it matches on is in a Transaction which fails or is canceled, the Single-shot Comparator Control does not fire.                                                                                                                                                                                                                                                                         |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R NKKSN   | When the trace unit becomes disabled and an Address Comparator selected by a Single-shot Comparator Control has matched on an instruction that is still speculative, the Single-shot Comparator Control does not fire.                                                                                                                                                                                                                                                                                       |
| R KFMKS   | While the PE is executing in Transactional state, when the trace unit becomes disabled and an Address Comparator selected by a Single-shot Comparator Control has matched on an instruction in Transactional state, the Single-shot Comparator Control does not fire.                                                                                                                                                                                                                                        |
| R DQZSD   | When tracing becomes prohibited and an Address Comparator selected by a Single-shot Comparator Control has matched on an instruction that is still speculative, the Single-shot Comparator Control waits until the instruction speculation is resolved and fires if the instruction is architecturally executed.                                                                                                                                                                                             |
| R XRSYH   | While the PE is executing in Transactional state, when tracing becomes prohibited and an Address Comparator selected by a Single-shot Comparator Control has matched on an instruction in Transactional state, the behavior of the Single-shot Comparator Control is IMPLEMENTATION DEFINED and is one of the following: • The Single-shot Comparator Control does not fire. • The Single-shot Comparator Control waits for the transaction to be resolved and fires if the transaction completes            |
| R VTWXJ   | While a Single-shot Comparator Control is used for instruction address comparisons, when the conditions for the Single-shot Comparator Control to fire are met, the Single-shot Comparator Control fires, regardless of whether either the following are true:                                                                                                                                                                                                                                               |
| I XZKFW   | When a Single-shot Comparator Control is used to activate a resource event, the resource event might not become activated until some time after the trace unit has traced the instruction. This is because although the trace unit traces the instruction it is executed, the PE might not confirm whether the instruction was architecturally executed or canceled because of mis-speculation until some time later, and therefore the Single-shot Comparator Control might not fire until some time later. |
| I XZJSV   | Each Single-shot Comparator Control operates in one of the following modes: • Single-shot mode: The Single-shot Comparator Control only fires once. That is, after it has fired, it never fires again. • Multi-shot mode: The Single-shot Comparator Control resets after each time it fires. That is, it can fire again                                                                                                                                                                                     |
| R KJBCH   | While a Single-shot Comparator Control is in multi-shot mode, when the Single-shot Comparator Control fires, it fires for a maximum of one processor clock cycle.                                                                                                                                                                                                                                                                                                                                            |
| R SNDBZ   | While a Single-shot Comparator Control is in multi-shot mode, when multiple of the comparators selected for the Single-shot Comparator Control match in close succession, only the first match is guaranteed to cause the Single-shot Comparator Control to fire.                                                                                                                                                                                                                                            |
| I HSGTY   | Examples of multiple comparator matches in close succession include: • More than one of the Address Comparators that are selected signal an address match simultaneously.                                                                                                                                                                                                                                                                                                                                    |
| I SPQLS   | D4.6.11.2 Operation while in Paused state The resolution of a speculative instruction might occur after the PE has entered a Trace Prohibited region and the resources have entered the Paused state. If the conditions for the Single-shot Comparator Control to fire are met while the resources are in the Paused state, then the Single-shot Comparator Control resource event is delayed to ensure that the Single-shot Comparator Control resource event is seen.                                      |

RTQHNK

While the resources are in the Paused state, the Single-shot Comparator Controls do not fire.

- RPVRGR

When the resources enter the Running state while TRCSSCSR&lt;n&gt;.PENDING is 1, the following occur:

- If TRCSSCCR&lt;n&gt;.RST is 1 or TRCSSCSR&lt;n&gt;.STATUS is 0, the Single-shot Comparator Control fires.

- TRCSSCSR&lt;n&gt;.PENDING is indirectly written to 0.

IDMGDY Some implementations might have no scenarios where TRCSSCSR&lt;n&gt;.PENDING can be set to 1 by an indirect write by the trace unit, in particular if the trace unit is not exposed to any speculative execution. However all implementations support software setting TRCSSCSR&lt;n&gt;.PENDING to 1, and the Single-shot Comparator fires when the trace unit enters the Running state. This behavior ensures the state from one trace unit can be migrated to a different trace unit.

## D4.6.12 External Outputs

| I BZHDF   | The ETE architecture supports between zero and four External Outputs. The number of outputs that a trace unit has is IMPLEMENTATION DEFINED, and Arm recommends that at least one output is implemented.                                                                                                                             |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I QPQFJ   | External Outputs are used to indicate ETEEvents to a trace analyzer. ETEEvents are controlled by resources events. For example, an instruction Address Comparator can be used to drive one of the resource events. If an External Output is programmed to be asserted based on program execution, such as an Address Comparator, the |
| I PNVWQ   | Typically, the generated trace might be buffered in a trace unit which means that the External Output would be asserted before the trace is output.                                                                                                                                                                                  |
| S MFTNW   | To program an External Output, use TRCEVENTCTL0R to select a resource.                                                                                                                                                                                                                                                               |
| S RBKWB   | The TRCIDR0.NUMEVENT field shows how many ETEEvents are supported for the particular implementation.                                                                                                                                                                                                                                 |
| I RFLGF   | The External Outputs are connected to the Cross Trigger Interface (CTI) for the PE. See The Embedded Cross-Trigger Interface.                                                                                                                                                                                                        |
| R RFGJD   | In a PE where the Trace Unit reset is independent of the PE Warm reset and the CTI reset is independent of the PE Warm reset, transmission of External Outputs to the CTI is unaffected by a PE Warm reset.                                                                                                                          |
|           | D4.6.12.1 Operation while in Paused state                                                                                                                                                                                                                                                                                            |
| I NXCSB   | While the resources are in the Paused state an ETEEvent might occur, but any associated trace packets might not be generated. TRCRSR.EVENT provides a mechanism for recording this occurrence so that the trace unit state can be saved and restored.                                                                                |
| R BCMYM   | While the resources are in the Paused state, the ETEEvent selector retains that one or more ETEEvents have been generated but not traced.                                                                                                                                                                                            |
| R SNKFL   | When an ETEEvent has been generated and the associated External Output has been asserted, any associated Event packets are generated.                                                                                                                                                                                                |
| R FVCMB   | When an ETEEvent has been generated but the associated External Output has not been asserted, any associated Event packets are not generated.                                                                                                                                                                                        |
| R GYWLS   | When an ETEEvent occurs while the resources are in the Paused state and the Event packet is not output, the trace unit sets the associated TRCRSR.EVENT[n] to 1.                                                                                                                                                                     |
| R DCLHJ   | When an ETEEvent occurs while the resources are in the Paused state, this is considered an indirect write to TRCRSR.                                                                                                                                                                                                                 |
| R SWBRL   | When the trace unit enters the Running state while TRCRSR.EVENT[n] is 1, the associated ETEEvent resource is active for a single PE clock cycle, and the trace unit clears TRCRSR.EVENT[n] to 0 and considers the action an indirect write to TRCRSR.                                                                                |

IKZYKM

When the trace unit enters the Running state while TRCRSR.EVENT[n] is 1, the resource event selected by TRCEVENTCTL0R.EVENT&lt;n&gt; might also be active on the same PE clock cycle. If this happens, the associated ETEEvent resource is active for the single PE clock cycle and might not generate 2 separate ETEEvents for these 2 causes of the ETEEvent .

## D4.6.13 External inputs

| I TPPSC   | The trace unit uses the PMUevents as External Inputs.                                                                                                                                                                                                                                                                                                                                                            |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R MTGKB   | If a PMUevent number that is selected is not implemented, then the External Input resource event is inactive.                                                                                                                                                                                                                                                                                                    |
| R YCNCR   | Unless otherwise specified by the PMUevent, the following events are selectable by the trace unit: • If FEAT_PMUv3 is implemented, all Common architectural and microarchitectural events implemented by the PMU. • If FEAT_PMUv3 is not implemented, all PMUevents required by the Performance Monitors Extension. See Required events. Note This includes all events required by other implemented extensions. |
| I XJBHV   | Additional ASIC-specific events can be selected by using a number in the IMPLEMENTATION DEFINED region.                                                                                                                                                                                                                                                                                                          |
| I VWHTZ   | There is no requirement that all IMPLEMENTATION DEFINED events are visible by the trace unit, PMUcounters, and the PMUEVENT bus .                                                                                                                                                                                                                                                                                |
| R PHDQT   | For ETE, export of PMUevents to the trace unit is not affected by PMCR.X or PMCR_EL0.X.                                                                                                                                                                                                                                                                                                                          |
| R RFWZB   | When self-hosted trace is enabled and tracing is prohibited, only the PMUevents defined by rulesR VBCBZ andR KRSMY are exported to the trace unit.                                                                                                                                                                                                                                                               |
| R WSXTC   | When self-hosted trace is disabled and counting in the current Security state of the PE is prohibited, only the PMUevents defined by rulesR VBCBZ andR KRSMY are exported to the trace unit.                                                                                                                                                                                                                     |
| R VBCBZ   | The following PMUevents are always exported to the trace unit: • CTI_TRIGOUT4. • CTI_TRIGOUT5. • CTI_TRIGOUT6. • CTI_TRIGOUT7. • PMU_OVFS. • TRB_TRIG.                                                                                                                                                                                                                                                           |
| R KRSMY   | The following PMUevents are always exported to the trace unit, unless self-hosted trace is enabled and TRFCR_EL2.E2TRE is 0: • PMU_HOVFS.                                                                                                                                                                                                                                                                        |
| R QPDHK   | When multiple occurrences of the same PMUevent occur during the same cycle, the trace unit only observes a single occurrence of the PMUevent.                                                                                                                                                                                                                                                                    |
| I MHHNV   | The operation of the PMUevents and the generation of trace within the trace unit are not tightly coupled, and there is no guarantee that enabling ViewInst due to a PMUevent will cause the instruction that caused the PMUevent to be traced.                                                                                                                                                                   |
| R XGMPN   | When the PMUevent SW_INCR is selected as an External Input and PMSWINC_EL0 is written from EL2 or EL3, the External Input is asserted if any bit [n] written has the value 1 and the relevant PMUcounter <n> is implemented.                                                                                                                                                                                     |

RBXPZK

RKVFVS

When the PMU event SW\_INCR is selected as an External Input and PMSWINC\_EL0 is written from EL1 or EL0, the External Input is asserted if any bit [n] written has the value 1 and the relevant PMU counter &lt;n&gt; is implemented and any of the following are true:

- EL2 is implemented and enabled in the current Security state and &lt;n&gt; is less than MDCR\_EL2.HPMN.
- EL2 is implemented and disabled in the current Security state.
- EL2 is not implemented.

RTTPPY

In a PE where the trace unit reset is independent of the PE Warm reset and the CTI reset is independent of the PE Warm reset, transmission of the CTI\_TRIGOUTn events from the CTI to the trace unit is unaffected by a PE Warm reset.

## D4.6.13.1 Operation while in Paused state

IHZLDV

The External Input Selectors are guaranteed to be active while in the Paused state. This is so that while the resources are

Paused any cross trigger event is not lost but will occur when the resources resume running.

TRCRSR.EXTIN provides a mechanism to capture the sticky state of the External Input Selectors while in the Paused state so that the ETE state can be saved and restored.

IZQFND When one or more selected External Inputs have been asserted, while the resources are in the Paused state, the trace unit retains the knowledge that one or more selected External Inputs have been asserted.

RKCXLF While the resources are in the Pausing or Paused states and the trace unit is not disabled and is not in the low-power state, when an External Input Selector n detects the selected External Input is asserted, the trace unit performs an indirect write to set TRCRSR.EXTIN[n] to 1.

RQWYSK

When the resources enter the Running state while TRCRSR.EXTIN[n] is 1, the External Input Selector resource is active for a single PE clock cycle, and the trace unit clears TRCRSR.EXTIN[n] and considers the action an indirect write to TRCRSR.

## D4.6.13.2 Operation while in low-power state

While the trace unit is in the low-power state, the External Input Selectors are inactive.

## D4.6.14 PE Comparator Inputs

ICXBPR

The ETE architecture provides up to eight PE Comparator Inputs, that is, inputs that can be driven from comparators within the PE. For example, a PE might contain IMPLEMENTATION DEFINED comparators.

RCNVSS The number of PE Comparator Inputs is indicated by TRCIDR4.NUMPC.

RBDWHM

While the PE is executing in a Trace Prohibited region, the PE Comparator Inputs are inactive.

IDDXFB

Each PE Comparator Input can be used in any of the following ways:

- To control the ViewInst start/stop function.

- To control the Single-shot Comparator Controls.

- As an independent resource.

ISKDCW

The timing of the effects of the PE Comparator Inputs on the resources and the filtering of the trace unit is IMPLEMENTATION DEFINED.

## Chapter D5 ETE Protocol Descriptions

This chapter describes the ETE packets. It contains the following sections:

- About the ETE protocol.
- Summary list of ETE packets.
- Alphabetical list of ETE packets.