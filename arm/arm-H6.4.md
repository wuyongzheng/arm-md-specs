## H6.4 Powerup request mechanism

If a powerup request mechanism is implemented, asserting the powerup request requests the power controller to power up the Core power domain, and to emulate any subsequent powerdown requests, until the powerup request mechanism is deasserted.

## H6.4.1 Powerup request mechanism if FEAT\_DoPD is implemented

If FEAT\_DoPD is implemented, the external debug component implements an OPTIONAL powerup request mechanism.

If the powerup request mechanism is implemented, Arm strongly recommends that the powerup request is a CoreSight Class 0x9 ROMtable block that contains both:

- Aparent entry for the debug registers of the PE.
- Aparent entry for the PMU registers of the PE, if the OPTIONAL PMU with an external debug interface is implemented.

Aparent entry of a component is an entry in a ROM table that either locates the component, or locates another ROM table that contains the parent entry for the component.

Note

The ROMtable and any descendants might describe other debug components, including debug components for other PEs. The ROM table might have a parent entry in a second ROM table and that parent entry might also have a powerup request mechanism in the second ROM table. This applies recursively.

The parent entries for the debug components have the following properties:

For the debug registers and Performance Monitors registers: These components are in the Core power domain.

The POWERIDVALID bit is 1.

All parent entries must have the same IMPLEMENTATION DEFINED POWERID value.

Note

The IMPLEMENTATION DEFINED POWERID value does not need to be unique for each PE.

For the CTI registers: This component is in the Debug power domain.

The POWERIDVALID bit is IMPLEMENTATION DEFINED.

If the POWERIDVALID bit is 1, the entries must have a valid POWERID value.

Note

If the Core power domain can be powered down independently of the Debug power domain, Arm recommends the system implements an external debug component with a powerup request mechanism which can request the Core power domain to be powered up.

For more information about Coresight Class 0x9 ROMTables, see ARM ® CoreSight™ Architecture Specification .

On a Cold reset, if FEAT\_DoPD is implemented, DBGPRCR.CORENPDRQ is set to an IMPLEMENTATION DEFINED choice between 0 and 1 if the powerup request is implemented and asserted, and 0 otherwise.

## H6.4.2 Powerup request mechanism if FEAT\_DoPD is not implemented

If FEAT\_DoPD is not implemented, the bit EDPRCR.COREPURQ is the powerup request mechanism.

The control registers DBGPRCR.CORENPDRQ and EDPRCR.COREPURQ provide an interface between the power controller and the PE. They typically map directly to signals in the recommended external debug interface.

On Cold reset, if FEAT\_DoPD is not implemented, DBGPRCR.CORENPDRQ is set to the value of EDPRCR.COREPURQ.